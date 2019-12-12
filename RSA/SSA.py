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
import torch
import time

class SSA:
    def __init__(self, gamma=1.0, gpu=torch.cuda.is_available()):
        self.NumView        = None
        self.NumTime        = None
        self.NumVoxel       = None
        self.NumCat         = None
        self.Dim            = None
        self.Runtime        = None
        self.Iteration      = None
        self.gpu            = gpu
        self.gamma          = gamma
        self.Signatures     = None
        self.TransformMats  = None
        self.SubjectSpace   = None
        self.LostVec        = None
        self.Loss           = None


    def run(self, X, Y, Dim=None, verbose=True, Iteration=5, ShowError=False):
        tic = time.time()
        assert np.shape(X).__len__() == 3, "Data must have 3D shape, i.e. Views (Subjects) x Time Points x Voxels"
        assert np.shape(Y).__len__() == 3, "Design Matrix must have 3D shape, i.e. Views (Subjects) x Time Points x Categories"
        assert np.shape(X)[0] == np.shape(Y)[0], "Number of views must be the same in data and design"
        self.NumView, self.NumTime, self.NumVoxel = np.shape(X)
        self.NumCat  = np.shape(Y)[2]
        self.Iteration = Iteration
        if np.shape(Y)[2] == 1:
            NewY = list()
            for yi in Y:
                NewY.append(np.concatenate((yi, 1 - yi), axis=1))
            Y = NewY
            if verbose:
                print("SSA::Format of binary labels are fixed!")
        if Dim is None:
            self.Dim = np.min((np.shape(X)[1], np.shape(X)[2]))
        elif Dim == 0:
            self.Dim = None
            for Xi in X:
                self.Dim = np.shape(Xi)[0] if self.Dim is None else np.min((self.Dim, np.shape(Xi)[0]))
        else:
            self.Dim = Dim
        if verbose:
            print("SSA::Data Properties -> Number of views: {0}, Number of Categories: {1}, Number of Dimensions: {2}".format(self.NumView, self.NumCat, self.Dim))

        # Initiate Values
        SubjectSpace    = np.zeros((self.NumView, self.NumVoxel, self.NumCat))
        TransformMat    = np.random.rand(self.NumView, self.NumVoxel, self.Dim)
        SharedSpace     = self._calculateSharedSpace(X, Y, SubjectSpace, TransformMat)
        if ShowError:
            self.LostVec = list()
        # Update Parameters
        for it in range(self.Iteration):
            if verbose:
                print("SSA::Iteration %4d of %4d -> Calculating Transform Matrix ..." % (it + 1, self.Iteration))
            TransformMat = self._calculateTransformMatrix(X, Y, SubjectSpace, SharedSpace)
            if verbose:
                print("SSA::Iteration %4d of %4d ->  Calculating Subject Space ..." % (it + 1, self.Iteration))
            SubjectSpace = self._calculateSubjectSpace(X, Y, SharedSpace, TransformMat)
            if verbose:
                print("SSA::Iteration %4d of %4d ->  Calculating Shared Space ..." % (it + 1, self.Iteration))
            SharedSpace = self._calculateSharedSpace(X, Y, SubjectSpace, TransformMat)
            if verbose:
                if ShowError:
                    loss = self._calculateObjective(X, Y, SubjectSpace, SharedSpace, TransformMat)
                    print("SSA::Iteration %4d of %4d is done. Objective error: %20.2f" % (it + 1, self.Iteration, loss))
                    self.LostVec.append([it, loss])
                else:
                    print("SSA::Iteration %4d of %4d is done." % (it + 1, self.Iteration))
        if ShowError:
            self.Loss = loss
        self.SubjectSpace   = SubjectSpace
        self.TransformMats   = TransformMat
        self.Signatures     = np.transpose(SharedSpace)
        self.Runtime        = time.time() - tic
        return self.Signatures


    def _calculateSharedSpace(self, Data, Labels, SubjectSpace, TransformMat):
        ShareSpace = None
        for Xi, Yi, Si, Ri in zip(Data, Labels, SubjectSpace, TransformMat):
            TenXi = torch.Tensor(np.transpose(Xi))
            TenYi = torch.Tensor(Yi)
            TenSi = torch.Tensor(Si)
            TenRi = torch.Tensor(Ri)
            if self.gpu:
                TenRi = TenRi.cuda()
                TenSi = TenSi.cuda()
                TenXi = TenXi.cuda()
                TenYi = TenYi.cuda()
            Ti = TenYi.shape[0]
            Hi = torch.eye(Ti) - torch.ones(Ti, Ti) / Ti
            if self.gpu:
                Hi = Hi.cuda()
            Ki = torch.mm(TenYi.t(), Hi)
            ShareSpace = torch.mm(TenRi.t(), torch.mm(TenXi, Ki.t()) - TenSi) if ShareSpace is None else ShareSpace + torch.mm(TenRi.t(), torch.mm(TenXi, Ki.t()) - TenSi)
        return ShareSpace.cpu().numpy() / self.NumView


    def _calculateTransformMatrix(self, Data, Labels, SubjectSpace, SharedSpace):
        TranformMatrix = list()
        G = torch.Tensor(np.transpose(SharedSpace))
        if self.gpu:
            G = G.cuda()
        for Xi, Yi, Si in zip(Data, Labels, SubjectSpace):
            TenXi = torch.Tensor(np.transpose(Xi))
            TenYi = torch.Tensor(Yi)
            TenSi = torch.Tensor(Si)
            if self.gpu:
                TenSi = TenSi.cuda()
                TenXi = TenXi.cuda()
                TenYi = TenYi.cuda()
            Ti = TenYi.shape[0]
            Hi = torch.eye(Ti) - torch.ones(Ti, Ti) / Ti
            if self.gpu:
                Hi = Hi.cuda()
            Ki = torch.mm(TenYi.t(), Hi)
            Ai =  torch.mm(torch.mm(TenXi, Ki.t()), G)
            Ai -= torch.mm(TenSi, G)
            Ui, _, Vi = torch.svd(Ai, some=True)
            TranformMatrix.append(torch.mm(Ui, Vi).cpu().numpy())
        return TranformMatrix


    def _sign(self, x):
        if x >= 0:
            return 1
        return -1


    def _calculateSubjectSpace(self, Data, Labels, SharedSpace, TransformMat):
        SubjectSpace = list()
        G = torch.Tensor(SharedSpace)
        if self.gpu:
            G = G.cuda()
        for Xi, Yi, Ri in zip(Data, Labels, TransformMat):
            TenXi = torch.Tensor(np.transpose(Xi))
            TenYi = torch.Tensor(Yi)
            TenRi = torch.Tensor(Ri)
            if self.gpu:
                TenXi = TenXi.cuda()
                TenYi = TenYi.cuda()
                TenRi = TenRi.cuda()
            Ti = TenYi.shape[0]
            Hi = torch.eye(Ti) - torch.ones(Ti, Ti) / Ti
            if self.gpu:
                Hi = Hi.cuda()
            Ki = torch.mm(TenYi.t(), Hi)
            Ci = torch.mm(TenXi, Ki.t()) - torch.mm(TenRi, G)
            Ci = Ci.cpu().numpy()
            pos = Ci > self.gamma
            neg = Ci < -1 * self.gamma
            Ci[pos] -= self.gamma
            Ci[neg] += self.gamma
            Ci[np.logical_and(~pos, ~neg)] = .0
            SubjectSpace.append(Ci)
        return SubjectSpace

    def _calculateObjective(self, X, Y, S, cpuG, R):
        error = 0
        G = torch.Tensor(cpuG)
        if self.gpu:
            G = G.cuda()
        for Xi, Yi, Ri, Si in zip(X, Y, R, S):
            TenXi = torch.Tensor(np.transpose(Xi))
            TenYi = torch.Tensor(Yi)
            TenRi = torch.Tensor(Ri)
            TenSi = torch.Tensor(Si)
            if self.gpu:
                TenXi = TenXi.cuda()
                TenYi = TenYi.cuda()
                TenRi = TenRi.cuda()
                TenSi = TenSi.cuda()
            Ti = TenYi.shape[0]
            Hi = torch.eye(Ti) - torch.ones(Ti, Ti) / Ti
            if self.gpu:
                Hi = Hi.cuda()
            Ki = torch.mm(TenYi.t(), Hi)
            e = torch.norm(torch.mm(TenXi, Ki.t()) - torch.mm(TenRi, G) - TenSi) ** 2 + torch.norm(TenSi, p=1)
            error += e.cpu().numpy()
        return error / self.NumView

    def getSubjectSpace(self):
        return self.SubjectSpace


    def getTransformMats(self):
        return self.TransformMats


    def getSharedSpace(self):
        return self.Signatures


    def getSharedVoxelSpace(self):
        assert self.TransformMats is not None, "You must create the model first!"
        assert self.Signatures is not None, "You must create the model first!"
        MeanTransMat = None
        for mat in self.TransformMats:
            MeanTransMat = mat if MeanTransMat is None else MeanTransMat + mat
        MeanTransMat = MeanTransMat / self.NumView
        return np.transpose(np.dot(MeanTransMat, np.transpose(self.Signatures)))