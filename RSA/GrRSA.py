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
import torch.optim as optim
from sklearn.metrics import mean_squared_error
import numpy as np
from Network.MLP import MLP

class GrRSA:
    def __init__(self, method='ridge', loss_type='norm', optim='adam', learning_rate = 0.1, epoch = 10, batch_size = 50, report_step = 1, ridge_param = 1, elstnet_l1_ratio = 0.5, elstnet_alpha = 1, lasso_alpha = 1.0, verbose=True, gpu_enable=torch.cuda.is_available(), normalization=False):
        # Loss Options
        self.method             = str.lower(method)  # 'linear', 'lasso', 'elastic', 'ridge', 'ln1', 'ln2', 'ln12'
        self.loss_type          = str.lower(loss_type) # 'norm', 'mse', 'soft', 'mean'
        self.optim              = str.lower(optim) # 'adam', 'sgd'
        self.normalization      = normalization
        # Learning Options
        self.epoch              = epoch
        self.batch_size         = batch_size
        self.learning_rate      = float(learning_rate)
        self.gpu_enable         = gpu_enable
        # Regularization Options
        self.ridge_param        = float(ridge_param)
        self.elstnet_l1_ratio   = float(elstnet_l1_ratio)
        self.elstnet_alpha      = float(elstnet_alpha)
        self.lasso_alpha        = float(lasso_alpha)
        # Report Options
        self.verbose            = verbose
        self.report_step        = report_step
        self.loss_vec           = None
        self.Beta               = None
        self.Eps                = None


    # This function solve ||AX - B|| where A is the design matrix and B is the fMRI data
    def fit(self, data_vals, design_vals):
        tic = time.time()

        SampleSize, FeatureSize = np.shape(data_vals)
        Sam, RegressorSize = np.shape(design_vals)
        assert SampleSize == Sam, "Data and Design Matrix must have the same size samples, data shape: " + \
                                  str(np.shape(data_vals)) + ", design shape: " + str(np.shape(design_vals))
        del Sam
        A = torch.Tensor(design_vals)
        B = torch.Tensor(data_vals)
        if self.normalization:
            A = A - A.mean() / A.std()
            B = B - B.mean() / B.std()

        model = MLP([RegressorSize, FeatureSize], [None], gpu_enable=self.gpu_enable)


        if   self.optim == "adam":
            optimizer = optim.Adam(model.parameters(), lr=self.learning_rate)
        elif self.optim == "sgd":
            optimizer = optim.SGD(model.parameters(), lr=self.learning_rate)
        else:
            raise Exception("Optimization algorithm is wrong! Options: \'adam\' or \'sgd\'")


        if   self.loss_type == 'mse':
            criterion = torch.nn.MSELoss()
        elif self.loss_type == 'soft':
            criterion = torch.nn.MultiLabelSoftMarginLoss()
        elif self.loss_type == 'mean':
            criterion = torch.mean
        elif self.loss_type == 'norm':
            criterion = torch.norm
        else:
            raise Exception("Loss function type is wrong! Options: \'mse\', \'soft\', \'mean\', or \'norm\'")

        ModelIsWrong = True
        for mod in ['linear', 'lasso', 'elastic', 'ridge', 'ln1', 'ln2', 'ln12']:
            if self.method == mod:
                ModelIsWrong = False
                break

        if ModelIsWrong:
            raise Exception("Method option is wrong! Options: \'linear\', \'lasso\', \'elastic\', \'ridge\', \'ln1\', \'ln2\', \'ln12\'")

        model.train()

        self.loss_vec = list()

        for epoch in range(self.epoch):
            perm = torch.randperm(SampleSize)
            sum_loss = 0

            for i in range(0, SampleSize, self.batch_size):
                a = A[perm[i: i + self.batch_size]]
                b = B[perm[i: i + self.batch_size]]

                # Send data to GPU
                if self.gpu_enable:
                    a = a.cuda()
                    b = b.cuda()

                optimizer.zero_grad()

                output = model(a)
                W = model.get_weights()[0][1]

                if   self.method == 'linear':
                    # ||y - Xw||
                    if self.loss_type == 'mse' or self.loss_type == 'soft':
                        loss = criterion(output, b)
                    else:
                        loss = criterion(output - b)

                elif self.method == 'lasso':
                    # (1 / (2 * n_samples)) * ||y - Xw|| + alpha * ||w||_1
                    if self.loss_type == 'mse' or self.loss_type == 'soft':
                        loss = criterion(output, b) / (SampleSize * 2) + self.lasso_alpha * torch.norm(W, p=1)
                    else:
                        loss = criterion(output - b) / (SampleSize * 2) + self.lasso_alpha * torch.norm(W, p=1)

                elif self.method == 'elastic':
                    # 1 / (2 * n_samples) * ||y - Xw|| +
                    # alpha * l1_ratio * ||w||_1 +
                    # 0.5 * alpha * (1 - l1_ratio) * ||w||^2_2
                    if self.loss_type == 'mse' or self.loss_type == 'soft':
                        loss = criterion(output, b) / (SampleSize * 2) + \
                               self.elstnet_alpha * self.elstnet_l1_ratio * torch.norm(W, p=1) +\
                               0.5 * self.elstnet_alpha * (1 - self.elstnet_l1_ratio) * torch.norm(W, p=2) ** 2
                    else:
                        loss = criterion(output - b) / (SampleSize * 2) + \
                               self.elstnet_alpha * self.elstnet_l1_ratio * torch.norm(W, p=1) +\
                               0.5 * self.elstnet_alpha * (1 - self.elstnet_l1_ratio) * torch.norm(W, p=2) ** 2

                elif self.method == 'ridge':
                    # || y - Xw|| + ||w||^2_2
                    if self.loss_type == 'mse' or self.loss_type == 'soft':
                        loss = criterion(output, b) + self.ridge_param * torch.norm(W, p=2) ** 2
                    else:
                        loss = criterion(output - b) + self.ridge_param * torch.norm(W, p=2) ** 2

                elif self.method == 'ln1':
                    # ||w||_1
                    loss = torch.norm(W, p=1)
                elif self.method == 'ln2':
                    # ||w||_2^2
                    loss = torch.norm(W, p=2) ** 2
                elif self.method == 'ln12':
                    # ||w||_2^2 + ||w||_1
                    loss = torch.norm(W, p=2) ** 2 + torch.norm(W, p=1)
                else:
                    raise Exception("Method option is wrong! Options: \'linear\', \'lasso\', \'elastic\', \'ridge\', \'ln1\', \'ln2\', \'ln12\'")

                loss.backward()
                optimizer.step()
                sum_loss += loss.data.cpu().numpy()
                self.loss_vec.append(loss.data.cpu().numpy())


            if self.verbose:
                if (epoch+1)%self.report_step == 0:
                    print("Epoch: {:4d}  Error: {}".format(epoch + 1, sum_loss))

        self.Beta = np.transpose(model.get_weights()[0][1].data.cpu().numpy())
        self.Eps  = model.get_bias()[0][1].data.cpu().numpy()

        if self.gpu_enable:
            A = A.cuda()
            B = B.cuda()

        Performance = torch.mean((B - model(A)) ** 2) / SampleSize
        Performance = Performance.data.cpu().numpy()
        MSE = mean_squared_error(data_vals, np.dot(design_vals, self.Beta))
        return self.Beta, self.Eps, self.loss_vec, MSE, Performance, time.time() - tic




if __name__ == "__main__":
    rsa = GrRSA(normalization=True, method='ridge', report_step=2)

    data = np.random.rand(10, 20)
    design = np.random.rand(10, 4)
    beta, eps, loss, mse, per, time = rsa.fit(data, design)
    print("Beta shape: ", beta.shape)
    print("Epsilon shape: ", eps.shape)
    print("MSE", mse)
    print("Performance: ", per)
    print("Runtime: ", time)

