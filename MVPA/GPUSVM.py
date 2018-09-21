# Copyright (c) 2014--2018 Muhammad Yousefnezhad
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

import time
import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
from scipy.sparse.linalg.eigen.arpack import eigsh
import scipy.io as io
from sklearn.preprocessing import label_binarize
from sklearn.metrics import accuracy_score

class LinearSVM(nn.Module):
    def __init__(self, NumDim=None, NumClass=None):
        super(LinearSVM, self).__init__()
        self.fc = nn.Linear(NumDim, NumClass)

    def forward(self, x):
        return self.fc(x)

class GPUSVM:
    def __init__(self, epoch=10, batchsize=10, learningrate=0.1, C=0.1, normalization=True, optim='adam', kernel='linear', gamma=None, degree=3, n_component=None):
        self.C = C
        self.W = None
        self.b = None
        self.model = None
        self.epoch = epoch
        self.kernel = str.lower(kernel)
        self.n_component = n_component
        self.gamma = gamma
        self.degree = int(degree)
        self.optim = str.lower(optim)
        self.NumDim = None
        self.NumClass = None
        self.batchsize = batchsize
        self.learningrate = learningrate
        self.normalization = normalization
        self.TrainError = None
        self.TrainPredict = None
        self.TrainDataShape = None
        self.TrainRuntime = None
        self.TestError = None
        self.TestPredict = None
        self.TestDataShape = None
        self.TestRuntime = None


    def rbf(self, X):
        Xk = None
        nfeature    = X.shape[1]
        Degree      = self.degree
        Gamma       = self.gamma
        NComp       = self.n_component
        if Gamma is None:
            Gamma = 1 / nfeature
        if NComp is None:
            NComp = nfeature
        K = Gamma*(torch.mm(X, X.t()) + 1)**Degree
        ninstance = K.shape[0]
        eigvals, eigvecs = torch.eig(K, eigenvectors=True)
        for i in range(1, NComp + 1):
           Xk = torch.reshape(eigvecs[:, -i], (1, ninstance)) if Xk is None else torch.cat((Xk, torch.reshape(eigvecs[:, -i], (1, ninstance))))
        return Xk.t()


    def train(self, X, Y, verbose=True, penalty=True, per_iteration=0.5):
        # tic
        tme = time.time()

        # Change Shape
        dataOK = None
        try:
            np.shape(Y)[1]
        except:
            dataOK = True

        if dataOK is None:
            X = np.transpose(X)
            Y = Y[0]
        # Normalization
        if self.normalization:
            X = (X - X.mean()) / X.std()
            if verbose:
                print("Training set is normalized.")

        # Shape data
        self.TrainDataShape = np.shape(X)
        SampleSize = len(Y)

        # Data shape error
        if not self.TrainDataShape[0] == SampleSize:
            raise  Exception("Data samples and class labels must be the same size!")

        # Generate Model
        NClass = np.shape(np.unique(Y))[0]
        if NClass <= 2:
            NClass = 1
        self.model = LinearSVM(self.TrainDataShape[1], NClass)
        self.NumDim, self.NumClass = self.TrainDataShape[1], NClass
        if torch.cuda.is_available():
            self.model.cuda()

        # Convert data to Tensor
        X = torch.Tensor(X)
        Y = torch.Tensor(label_binarize(Y, np.unique(Y)))

        if torch.cuda.is_available():
            X = X.cuda()
            Y = Y.cuda()

        # Apply Kernel
        if self.kernel == 'rbf':
            print("Applying RBF kernel ...")
            X = self.rbf(X)
            print("RBF kernel is applied.")

        # Optimization approach
        if   self.optim == 'adam':
            optimizer = optim.Adam(self.model.parameters(), lr=self.learningrate)
        elif self.optim == 'sgd':
            optimizer = optim.SGD(self.model.parameters(), lr=self.learningrate)
        else:
            raise Exception("Optimization algorithm is wrong!")
        criterion = torch.nn.MultiLabelSoftMarginLoss()
        self.model.train()

        for epoch in range(self.epoch):
            perm = torch.randperm(SampleSize)
            sum_loss = 0

            for i in range(0, SampleSize, self.batchsize):
                x = X[perm[i: i + self.batchsize]]
                y = Y[perm[i: i + self.batchsize]]

                optimizer.zero_grad()
                output = self.model(x)
                if penalty:
                    loss = self.C *  criterion(output, y) + self.C * torch.mean(self.model.fc.weight ** 2)
                else:
                    loss = self.C * criterion(output, y)
                loss.backward()
                optimizer.step()
                sum_loss += loss.data.cpu().numpy()

                if per_iteration is not None:
                    if per_iteration != 1:
                        if per_iteration <= i / SampleSize:
                            break

            if verbose:
                print("Epoch: {:6d}\tLoss: {}".format(epoch, sum_loss / SampleSize))


        self.TrainPredict = self.model(X)
        self.TrainPredict = np.argmax(self.TrainPredict.data.cpu().numpy(),axis=1)+1
        Y = np.argmax(Y.data.cpu().numpy(),axis=1)+1
        self.TrainError = 1 - accuracy_score(Y, self.TrainPredict)
        self.W = self.model.fc.weight
        self.W = self.W.data.cpu().numpy()
        self.b = self.model.fc.bias
        self.b = self.b.data.cpu().numpy()
        self.model.eval()
        self.TrainRuntime = time.time() - tme
        if verbose:
            print("Training phase is done.")

        return self.TrainPredict


    def test(self, X, Y=None, verbose=True):
        # tic
        tme = time.time()

        if self.model is None:
            raise Exception("You must train a model first!")

        # Change Shape
        if Y is not None:
            dataOK = None
            try:
                np.shape(Y)[1]
            except:
                dataOK = True

            if dataOK is None:
                X = np.transpose(X)
                Y = Y[0]

        # Normalizing Data
        if self.normalization:
            X = (X - X.mean()) / X.std()
            if verbose:
                print("Testing set is normalized.")

        # Convert data to Tensor
        self.TestDataShape = np.shape(X)
        X = torch.Tensor(X)
        Y = torch.Tensor(label_binarize(Y, np.unique(Y)))

        # Send data to GPU
        if torch.cuda.is_available():
            X = X.cuda()
            if Y is not None:
                Y = Y.cuda()

        # Predicting testing set
        self.TestPredict = self.model(X)
        self.TestPredict = np.argmax(self.TestPredict.data.cpu().numpy(),axis=1)+1

        if Y is None:
            self.TestError = None
        else:
            Y = np.argmax(Y.data.cpu().numpy(),axis=1)+1
            self.TestError = 1 - accuracy_score(Y, self.TestPredict)

        if verbose:
            print("Testing phase is done.")

        self.TestRuntime = time.time() - tme

        return self.TestPredict

    def save(self, filename):
        if self.model is None:
            print("There is no trained model!")
            return None
        torch.save(self.model.state_dict(), filename)

    def load(self, filename):
        state = torch.load(filename)
        cls, dim = state['fc.weight'].shape
        self.model = LinearSVM(dim, cls)
        if torch.cuda.is_available():
            self.model.cuda()
        self.model.load_state_dict(state)

    def parameters(self):
        if self.model is None:
            print("There is no trained model!")
            return None
        return {"W": self.W, "b": self.b}


if __name__ == "__main__":
    i = 0 # 0: create, 1: load
    model = GPUSVM(kernel='rbf')
    if i == 0:
        from sklearn.datasets.samples_generator import make_blobs
        X, y = make_blobs(n_samples=100, centers=20, random_state=0, cluster_std=1)
        y = y + 1
        Xtr = X[:80,:]
        ytr = y[:80]
        Xte = X[81:, :]
        yte = y[81:]
        io.savemat("/home/tony/data.mat", {"test_data": Xte, "test_label": yte, "train_data": Xtr, "train_label": ytr, "FoldID": 1})
        model.train(Xtr, ytr, verbose=True)
        #print(model.parameters())
        model.test(Xte, yte, verbose=True)
        print("GSVM, train: {:6f}, runtime: {}".format(model.TrainError, model.TrainRuntime))
        print("GSVM,  test: {:6f}, runtime: {}".format(model.TestError, model.TestRuntime))
        model.save("/home/tony/mod.model")
        from sklearn import svm
        clf = svm.SVC(decision_function_shape='ova',kernel='linear')
        tme = time.time()
        clf.fit(Xtr, ytr)
        error = 1 - accuracy_score(ytr, clf.predict(Xtr))
        print("Normal SVM, train: {:6f}, runtime: {}".format(error, time.time() - tme))
        tme = time.time()
        p = clf.predict(Xte)
        error = 1 - accuracy_score(yte, p)
        print("Normal SVM,  test: {:6f}, runtime: {}".format(error, time.time() - tme))

    else:
        data = io.loadmat("/home/tony/data.mat")
        Xte = data["test_data"]
        yte = data["test_label"][0]
        model.load("/home/tony/mod.model")
        model.test(Xte, yte)
        print(model.TestError, model.TestPredict)