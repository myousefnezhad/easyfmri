# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import scipy.sparse
import scipy.linalg
import time

# Supervised Hyperalignment
class SHA:
    def __init__(self, reg = 10**-4, lamb=-1):
        self.NumView        = None
        self.NumCat         = None
        self.NumVoxel       = None
        self.Dim            = None
        self.Runtime        = None
        self.reg            = reg
        self.lamb           = lamb

        self.Sig            = None
        self.G              = None # Shared Space
        self.EigVal         = None # Eigenvalues (Lambda) of Shared Space
        self.Xtrain         = None # Transformed trained data
        self.Etrain         = None # Training Error
        self.Xtest          = None # Transformed test data
        self.ETest          = None # Testing Error

    def train(self, X, Y, verbose=True, Dim=None):
        tic = time.time()
        assert np.shape(X).__len__() == 3, "Data must have 3D shape, i.e. Views (Subjects) x Time Points x Voxels"
        assert np.shape(Y).__len__() == 3, "Label must have 3D shape, i.e. Views (Subjects) x Time Points x Categories"
        assert np.shape(X)[0] == np.shape(Y)[0], "Number of views must be the same in data and label"
        self.NumView = np.shape(X)[0]
        self.NumCat  = np.shape(Y)[2]
        if Dim is None:
            self.Dim = np.shape(X)[1]
        elif Dim == 0:
            self.Dim = None
            for Xi in X:
                self.Dim = np.shape(Xi)[0] if self.Dim is None else np.min((self.Dim, np.shape(Xi)[0]))
        else:
            self.Dim = Dim
        if verbose:
            print("Data Properties -> Number of views: {0}, Number of Categories: {1}, Number of Dimensions: {2}".format(self.NumView, self.NumCat, self.Dim))
        SigmaTilde = np.float32(np.zeros(self.Dim))
        SharedTilde = np.float32(np.zeros((self.NumCat, self.Dim)))
        UTs = list()
        Ks  = list()
        for i, (Xi, Yi) in enumerate(zip(X, Y)):
            if verbose:
                print('DATA -> View %d -> Run SVD ...' % (i + 1))
            Ti = np.shape(Xi)[0]
            if self.lamb == -1:
                self.lamb = 1 / (2 * Ti)

            if self.lamb > 1 / Ti:
                print("WARNING: Lambda must be smaller than 1 / Ti")

            Hi = np.eye(Ti) - self.lamb * np.ones((Ti, Ti))

            Ki = np.dot(Yi.T, Hi)
            Ks.append(Ki)
            # Decompose KiXi for calculating W
            Ui, Si, Vi          = scipy.linalg.svd(np.dot(Ki, Xi), full_matrices=False)
            # Decompose Xi for calculating Ri based on G (and W)
            Un_Ui, Un_Si, Un_Vi = scipy.linalg.svd(Xi, full_matrices=False)

            if verbose:
                print('DATA -> View %d -> Calculate Sigma inverse ...' % (i + 1))

            # For KiXi => Pi = Sigma * (Sigma * Sigma + \epsilon  * I) * Sigma
            SIi = 1. / (np.multiply(Si, Si) + self.reg)
            Phi = np.diag(np.sqrt(np.multiply(np.multiply(Si, SIi), Si)))

            # For Xi => Pi = Sigma * (Sigma * Sigma + \epsilon  * I) * Sigma
            Un_SIi = 1. / (np.multiply(Un_Si, Un_Si) + self.reg)
            Un_Phi = np.diag(np.sqrt(np.multiply(np.multiply(Un_Si, Un_SIi), Un_Si)))


            # For KiXi => I - Ai*Di
            if verbose:
                print('DATA -> Calculate dot product AT for View %d' % (i + 1))
            UPhi = np.eye(np.shape(Ui)[0]) - np.dot(Ui, Phi)
            Un_UPhi = np.dot(Un_Ui, Un_Phi)


            UTs.append(Un_UPhi)
            if verbose:
                print('DATA -> View %d -> Calculate Incremental PCA ...' % (i + 1))

            SharedTilde, SigmaTilde = self._batch_incremental_pca(UPhi, SharedTilde, SigmaTilde, i, verbose)

            if verbose:
                print('DATA -> View %d -> Decomposing data matrix ...' % (i + 1))
            self.G = np.dot(np.transpose(Ki), SharedTilde) if self.G is None else self.G + np.dot(np.transpose(Ki), SharedTilde)


        self.Sig = SharedTilde
        self.G   = self.G / self.NumView

        self.Xtrain = list()

        self.Etrain = list()

        if verbose:
            print('TRAIN DATA -> Mapping to shared space ...')
              # Get mapping to shared space
        for pid, UTi in enumerate(UTs):
            xtrprokject = np.dot(np.dot(UTi, np.transpose(UTi)), self.G)
            # Save features
            self.Xtrain.append(xtrprokject)
            # Save errors
            self.Etrain.append(np.linalg.norm(xtrprokject - self.G)**2)
            if verbose:
                print('TRAIN DATA -> View %d is projected ...' % (pid + 1))

        self.Runtime = time.time() - tic

        return self.Xtrain, self.G, self.Sig, self.Runtime, np.mean(self.Etrain), self.Etrain

    def test(self, views, G=None, verbose=True):
        tme = time.time()

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


        if self.Dim is None:
            self.k = np.shape(views)[1]  # Dimensionality of embedding we want to learn
        else:
            try:
                self.k = np.int32(self.Dim)
            except:
                self.k = np.shape(views)[2]  # Dimensionality of embedding we want to learn

        self.Xtest = list()
        self.ETest = list()

        # Take SVD of each view, to calculate A_i and T_i
        for i, view in enumerate(views):
            if self.verbose:
                print('TEST DATA -> View %d -> Run SVD ...' % (i + 1))
            A, S_thin, B = scipy.linalg.svd(view, full_matrices=False)
            if self.verbose:
                print('TEST DATA -> View %d -> Calculate Sigma inverse ...' % (i + 1))
            S2_inv = 1. / (np.multiply(S_thin, S_thin) + self.reg)
            T = np.diag(np.sqrt(np.multiply(np.multiply(S_thin, S2_inv), S_thin)))
            if self.verbose:
                print('TEST: Calculate dot product AT for View %d' % (i + 1))
            ajtj = A.dot(T)
            xteprokject = np.dot(np.dot(ajtj,np.transpose(ajtj)), self.G)
            self.Xtest.append(xteprokject)
            self.ETest.append(np.linalg.norm(xteprokject - self.G)**2)

            print('TEST DATA -> View %d is projected ...' % (i + 1))

        return self.Xtest, time.time() - tme, np.mean(self.ETest), self.ETest

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