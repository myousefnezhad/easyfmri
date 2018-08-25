'''
Implementation of Regularized Hyperalignment based on Xu et al. 2012
Objective Function: ||G - XiQi||_F^2
Input: views = {X1, X2, ..., Xn} \in R^{Subject x Time x Voxel} for training/testing phase
'''

import numpy as np
import time

class rHA:
    def __init__(self, alpha=0.5):
        self.G              = None # Shared Space
        self.TrainXp        = None # Projected Training Set
        self.TrainQt        = None
        self.TrainError     = None
        self.TrainXt        = None
        self.TestXp         = None # Projected Training Set
        self.TestQt         = None
        self.TestError      = None
        self.TestXt         = None
        self.alpha          = alpha

    def train(self, views, iter=10, verbose=True):
        tme = time.time()
        # Data Shape
        N = np.shape(views)[0]
        T = np.shape(views)[1]
        V = np.shape(views)[2]

        # Generating Shared Space
        G = np.random.randn(T, V)

        # Generating X tilde
        if verbose:
            print("Generating X tilda ...")
        Xt = list()
        for viewID, view in enumerate(views):
            Ui, Si, Vi = np.linalg.svd(view, full_matrices=False)
            Xt.append(np.dot(np.dot(Ui,self.f(Si,self.alpha)),Vi))
            if verbose:
                print("Subject ", viewID + 1, " is done.")
            del Ui, Si, Vi

        # Main Iteration
        for it in range(iter):
            # For fixed G, calculating Qi
            Qt      = list()
            errors  = list()
            for xiID, xi in enumerate(Xt):
                Uk, Sk, Vk = np.linalg.svd(np.dot(np.transpose(xi), G), full_matrices=False)
                Qt.append(np.dot(Uk, np.transpose(Vk)))
                if verbose:
                    print("Iteration: ", it + 1, ", Calculating Mapping: ", xiID + 1)

            # For fixed Qi, calculating G
            if verbose:
                print("Updating shared space ...")
            G = np.zeros((T, V))
            for qi, xi in zip(Qt, Xt):
                G = G + np.dot(xi, qi)
            G = G / N
            if verbose:
                print("Iteration ", it + 1, " is done.")

        if verbose:
            print("Projecting data ...")
        Xp = None
        error = 0
        i = 1
        for qi, xi in zip(Qt, Xt):
            prj = np.dot(xi, qi)
            error = error + np.linalg.norm(prj - G)**2
            Xp = prj if Xp is None else np.concatenate((Xp,prj),axis=0)
            if verbose:
                print("Subject ", i, " is projected.")
            i = i + 1
        error = error / N
        self.G = G
        self.TrainXp        = Xp
        self.TrainXt        = Xt
        self.TrainQt        = Qt
        self.TrainError     = error
        return Xp, G, error, time.time() - tme


    def test(self, views, Gtrain=None, verbose=True):
        tme = time.time()
        # Data Shape
        N = np.shape(views)[0]
        # Set shared space G
        if Gtrain == None:
            G = self.G
        else:
            G = Gtrain
        # Generating X tilde
        if verbose:
            print("Generating X tilda ...")
        Xt = list()
        for viewID, view in enumerate(views):
            Ui, Si, Vi = np.linalg.svd(view, full_matrices=False)
            Xt.append(np.dot(np.dot(Ui,self.f(Si,self.alpha)),Vi))
            if verbose:
                print("Subject ", viewID + 1, " is done.")
            del Ui, Si, Vi
        Qt      = list()
        Xp      = None
        error = 0
        for xiID, xi in enumerate(Xt):
            Uk, Sk, Vk = np.linalg.svd(np.dot(np.transpose(xi), G), full_matrices=False)
            qi = np.dot(Uk, np.transpose(Vk))
            Qt.append(qi)
            prj = np.dot(xi, qi)
            Xp = prj if Xp is None else np.concatenate((Xp,prj),axis=0)
            error = error + np.linalg.norm(prj - G) ** 2
            if verbose:
                print("Subject ", xiID + 1, " is done.")
        error = error / N
        self.TestQt     = Qt
        self.TestError  = error
        self.TestXp     = Xp
        self.TestXt     = Xt
        return Xp, error, time.time() - tme


    def f(self, x, alpha):
        vec = None
        out = np.zeros(np.shape(x)[0])
        try:
            if np.shape(x)[1] > 0:
                pass
            vec = np.diag(x)
        except:
            vec = x.copy()
        for elementID, element in enumerate(vec):
            out[elementID] = element / np.sqrt( ((1 - alpha) * element**2) + alpha)
        return np.diag(out)


# Auto Run
if __name__ == "__main__":
    trsubs = np.random.rand(5, 10, 100)
    tesubs = np.random.rand(5, 10, 100)
    model = rHA(alpha=0.4)
    Xp, G, e, _, t  = model.train(trsubs, verbose=False)
    error = 0
    for sub in trsubs:
        error = error + np.linalg.norm(sub - G) ** 2
    print("Train set: ", error, " aligned train shape: ", np.shape(Xp), " err: ", e, " time: ", t, " Shared space shape: ", np.shape(G))

    Xp, e, t        = model.test(tesubs, verbose=False)
    for sub in tesubs:
        error = error + np.linalg.norm(sub - G) ** 2
    print("Test set: ", error, " aligned test  shape: ", np.shape(Xp), " err: ", e, " time: ", t)
