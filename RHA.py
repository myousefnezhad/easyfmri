'''
Implementation of Regularized Hyperalignment by using MVLSA optimization approach
Objective Function: ||G - XiUi||_F^2
Input: views = {X1, X2, ..., Xn} \in R^{Subject x Time x Voxel} for training phase
    or views_tilde = {X1_tilde, X2_tilde, ..., Xn_tilde} \in R^{Subject x Time x Voxel} for testing phase        
Optional Input: K for managing missed values for training phase
                W as weight of each view for training phase
                G_tilde: for testing phase
Output: G \in R^{Time x Voxel} for training
        U = {U1, U2, ..., Un} R^{Subject x Time x Voxel} for training
        U_tilde = {U1, U2, ..., Un} R^{Subject x Time x Voxel} for training
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

class RHA:
    def __init__(self,regularization=10**-4,Dim=None):
        self.G = None
        self.U_tilde = None
        self.U = None
        self.Dim = Dim
        self.regularization=regularization

    def fit(self, views, verbose=True):
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

        # Take SVD of each view, to calculate A_i and T_i
        for i, (eps, view) in enumerate(zip(self.eps, views)):
            A, S_thin, B = scipy.linalg.svd(view, full_matrices=False)
            S2_inv = 1. / (np.multiply(S_thin, S_thin) + eps)
            T = np.diag(np.sqrt(np.multiply(np.multiply(S_thin, S2_inv), S_thin)))
            ajtj =  A.dot(T)
            #ajtj = A.dot(T)
            _Gprime, _Stilde = self._batch_incremental_pca(ajtj,_Gprime,_Stilde)
            if self.verbose:
                print('TRAIN: decomposing data matrix for View %d' % (i + 1))

        self.G = _Gprime
        self.lbda = _Stilde
        self.U = []  # Mapping from views to latent space

        # Get mapping to shared space
        for idx, (eps, f, view) in enumerate(zip(self.eps, self.F, views)):
            R = scipy.linalg.qr(view, mode='r')[0]
            Cjj_inv = np.linalg.inv((R.transpose().dot(R) + eps * np.eye(f)))
            pinv = Cjj_inv.dot(view.transpose())
            self.U.append(pinv.dot(self.G))
            if self.verbose:
                print('TRAIN: solving mapping for View %d' % (idx + 1))

        return self.G, self.U

    def project(self, views_tilde,verbose=True, G=None):
        self.V_tilde = np.shape(views_tilde)[0]

        self.eps_tilde = [np.float32(self.regularization) for i in range(self.V_tilde)]  # Assume eps is same for each view

        self.F_tilde = [np.int(np.shape(views_tilde)[2]) for i in range(self.V_tilde)]  # Assume eps is same for each view
        if G is not None:
            self.G = G
        else:
            if self.G is None:
                if verbose:
                    print("There is no G")
                return None

        self.U_tilde = []
       # Get mapping to shared space
        for idx, (eps, f, view) in enumerate(zip(self.eps_tilde, self.F_tilde, views_tilde)):
            R = scipy.linalg.qr(view, mode='r')[0]
            Cjj_inv = np.linalg.inv((R.transpose().dot(R) + eps * np.eye(f)))
            pinv = Cjj_inv.dot(view.transpose())
            self.U_tilde.append(pinv.dot(self.G))
            if self.verbose:
                print('TEST: solving mapping for View %d' % (idx + 1))
        return self.U_tilde

    def get_G(self):
        return self.G

    def get_U(self):
        return self.U

    def get_U_tilde(self):
        return self.U_tilde

    @staticmethod
    def _batch_incremental_pca(x, G, S):
        r = G.shape[1]
        b = x.shape[0]
        xh = G.T.dot(x)
        H = x - G.dot(xh)
        J, W = scipy.linalg.qr(H, overwrite_a=True, mode='full', check_finite=False)
        Q = np.bmat([[np.diag(S), xh], [np.zeros((b, r), dtype=np.float32), W]])
        G_new, St_new, Vtoss = scipy.linalg.svd(Q, full_matrices=False, check_finite=False)
        St_new = St_new[:r]
        G_new = np.asarray(np.bmat([G, J]).dot(G_new[:, :r]))
        return G_new, St_new