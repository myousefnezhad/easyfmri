'''
Implementation of Regularized Hyperalignment by using MVLSA optimization approach (without trans. mat.)
Objective Function: ||G - XiUi||_F^2
Input: views = {X1, X2, ..., Xn} \in R^{Subject x Time x Voxel} for training phase
    or views_tilde = {X1_tilde, X2_tilde, ..., Xn_tilde} \in R^{Subject x Time x Voxel} for testing phase
Optional Input: K for managing missed values for training phase
                W as weight of each view for training phase
                G_tilde: for testing phase
Output: G \in R^{Time x Feature} for training
        X_new = {X1, X2, ..., Xn} R^{Subject x Time x Feature} for training
Functions:
fit(Xs) for training phase
project(Xs_bar) for testing phase
get_G: return G
get_Us: return Us for training phase
get_Us_tilde return Us_tilde for testing phase
'''

import numpy as np
import scipy
import scipy.sparse
import scipy.linalg
import scipy.io as io

class RHA:
    def __init__(self,Dim=None,regularization=10**-4):
        self.G = None # Shared Space
        self.EigVal = None # Eigenvalues (Lambda) of Shared Space
        self.Xtrain = None # Transformed trained data
        self.Xtest  = None # Transformed test data
        self.Dim = Dim # Number of Dimension
        self.regularization=regularization

    def train(self, views, verbose=True):
        # Show Message or not
        self.verbose = verbose
        # Number of Subjects
        self.V = np.shape(views)[0]

        try:
            if len(self.regularization) == self.V:
                self.eps = [np.float32(e) for e in self.regularization]
            else:
                self.eps = [np.float32(self.regularization) for i in range(self.V)]  # Assume eps is same for each view
        except:
            self.eps = [np.float32(self.regularization) for i in range(self.V)]  # Assume eps is same for each view


        self.F = [np.int(np.shape(views)[2]) for i in range(self.V)]  # Assume eps is same for each view

        if self.Dim is None:
            self.k = np.shape(views)[2]  # Dimensionality of embedding we want to learn
        else:
            try:
                self.k = np.int32(self.Dim)
            except:
                self.k = np.shape(views)[2]  # Dimensionality of embedding we want to learn

        N = views[0].shape[0]

        _Stilde = np.float32(np.zeros(self.k))
        _Gprime = np.float32(np.zeros((N, self.k)))

        ProjectMats = list()

        # Take SVD of each view, to calculate A_i and T_i
        for i, (eps, view) in enumerate(zip(self.eps, views)):
            if self.verbose:
                print('TRAIN DATA -> View %d -> Run SVD ...' % (i + 1))
            A, S_thin, B = scipy.linalg.svd(view, full_matrices=False)
            if self.verbose:
                print('TRAIN DATA -> View %d -> Calculate Sigma inverse ...' % (i + 1))
            S2_inv = 1. / (np.multiply(S_thin, S_thin) + eps)
            T = np.diag(np.sqrt(np.multiply(np.multiply(S_thin, S2_inv), S_thin)))
            if self.verbose:
                print('TRAIN: Calculate dot product AT for View %d' % (i + 1))
            ajtj =  A.dot(T)
            ProjectMats.append(ajtj)
            if self.verbose:
                print('TRAIN DATA -> View %d -> Calculate Incremental PCA ...' % (i + 1))
            _Gprime, _Stilde = self._batch_incremental_pca(ajtj,_Gprime,_Stilde, i, self.verbose)
            if self.verbose:
                print('TRAIN DATA -> View %d -> Decomposing data matrix ...' % (i + 1))
        self.G = _Gprime
        self.EigVal = _Stilde
        self.Xtrain = list()

        print('TRAIN DATA -> Mapping to shared space ...')
              # Get mapping to shared space
        for pid, project in enumerate(ProjectMats):
            self.Xtrain.append(np.dot(np.dot(project, np.transpose(project)),self.G))
            print('TRAIN DATA -> View %d is projected ...' % (pid + 1))

        return self.Xtrain, self.G

    def test(self, views, G=None, verbose=True):
        if G is not None:
            self.G = G
        else:
            if self.G is None:
                if verbose:
                    print("There is no G")
                return None

        # Show Message or not
        self.verbose = verbose
        # Number of Subjects
        self.V_test = np.shape(views)[0]

        try:
            if len(self.regularization) == self.V_test:
                self.eps_test = [np.float32(e) for e in self.regularization]
            else:
                self.eps_test = [np.float32(self.regularization) for i in range(self.V_test)]  # Assume eps is same for each view
        except:
            self.eps_test = [np.float32(self.regularization) for i in range(self.V_test)]  # Assume eps is same for each view

        self.F_test = [np.int(np.shape(views)[2]) for i in range(self.V_test)]  # Assume eps is same for each view

        if self.Dim is None:
            self.k = np.shape(views)[2]  # Dimensionality of embedding we want to learn
        else:
            try:
                self.k = np.int32(self.Dim)
            except:
                self.k = np.shape(views)[2]  # Dimensionality of embedding we want to learn

        self.Xtest = list()

        # Take SVD of each view, to calculate A_i and T_i
        for i, (eps, view) in enumerate(zip(self.eps, views)):
            if self.verbose:
                print('TEST DATA -> View %d -> Run SVD ...' % (i + 1))
            A, S_thin, B = scipy.linalg.svd(view, full_matrices=False)
            if self.verbose:
                print('TEST DATA -> View %d -> Calculate Sigma inverse ...' % (i + 1))
            S2_inv = 1. / (np.multiply(S_thin, S_thin) + eps)
            T = np.diag(np.sqrt(np.multiply(np.multiply(S_thin, S2_inv), S_thin)))
            if self.verbose:
                print('TEST: Calculate dot product AT for View %d' % (i + 1))
            ajtj = A.dot(T)
            self.Xtest.append(np.dot(np.dot(ajtj,np.transpose(ajtj)), self.G))
            print('TEST DATA -> View %d is projected ...' % (i + 1))

        return self.Xtest


    def get_G(self):
        return self.G

    def get_Xtrain(self):
        return self.Xtrain

    def get_Xtest(self):
        return self.Xtest


    @staticmethod
    def _batch_incremental_pca(x, G, S, i, verbose):
        r = G.shape[1]
        b = x.shape[0]
        xh = G.T.dot(x)
        H = x - G.dot(xh)
        if verbose:
            print('TRAIN DATA -> View %d -> IPCA -> Run QR decomposition ...' % (i + 1))
        J, W = scipy.linalg.qr(H, overwrite_a=True, mode='full', check_finite=False)
        if verbose:
            print('TRAIN DATA -> View %d -> IPCA -> Run bmat ...' % (i + 1))
        Q = np.bmat([[np.diag(S), xh], [np.zeros((b, r), dtype=np.float32), W]])
        if verbose:
            print('TRAIN DATA -> View %d -> IPCA -> Run SVD decomposition on Q ...' % (i + 1))
            print('TRAIN DATA -> View %d -> IPCA -> Q size: ' % (i + 1), np.shape(Q))
        try:
            G_new, St_new, Vtoss = scipy.linalg.svd(Q, full_matrices=False, check_finite=False)
        except:
            print("WARNING: SVD for View %d is not coverage!" % (i + 1))
            return  G, S
        St_new = St_new[:r]
        if verbose:
            print('TRAIN DATA -> View %d -> IPCA -> Run dot product ...' % (i + 1))
        G_new = np.asarray(np.bmat([G, J]).dot(G_new[:, :r]))
        return G_new, St_new
