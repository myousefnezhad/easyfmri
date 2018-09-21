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

import torch
import torch.nn as nn
import torch.nn.functional as fun
import numpy as np
import scipy.io as io

class CNN(nn.Module):
    def __init__(self, model, in_channel=1, gpu_enable=torch.cuda.is_available()):
        super(CNN, self).__init__()
        if type(model) == type(''):
            file = io.loadmat(model, appendmat=False)
            NLayer = 0
            for key in file.keys():
                if str(key).lower().find("layer") != -1:
                    NLayer += 1
            self.model = list()
            for l in range(NLayer):
                module = file["layer" + str(l)][0][0]
                element = list()
                for el in module:
                    if type(el[0]) == np.str_:
                        element.append(el[0])
                    else:
                        if np.shape(el[0])[0] == 1:
                            element.append(el[0][0])
                        else:
                            element.append(tuple(el[0]))
                self.model.append(element)
        else:
            self.model = model

        self.gpu_enable = gpu_enable
        self.convs = list()
        self.in_channel = in_channel
        in_channels = in_channel
        for module in self.model:
            if   str.lower(module[0]) == 'conv1':
                convfun = nn.Conv1d
            elif str.lower(module[0]) == 'conv2':
                convfun = nn.Conv2d
            elif str.lower(module[0]) == 'conv3':
                convfun = nn.Conv3d

            if   str.lower(module[0]) == 'conv1' or str.lower(module[0]) == 'conv2' or str.lower(module[0]) == 'conv3':
                if   len(module) < 3:
                    raise Exception("Conv parametets are wrong!")

                out_channels = module[1]
                kernel_size  = module[2]
                stride       = 1
                padding      = 0
                dilation     = 1
                groups       = 1
                bias         = True

                if len(module) >= 4:
                        stride = module[3] if module[3] is not None else 1

                if len(module) >= 5:
                    padding = module[4] if module[4] is not None else 0

                if len(module) >= 6:
                    dilation = module[5] if module[5] is not None else 1

                if len(module) >= 7:
                    groups = module[6] if module[6] is not None else 1

                if len(module) >= 8:
                    bias = module[7] if module[7] is not None else True

                self.convs.append(convfun(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, \
                                          stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias))
                in_channels = module[1] # for the next Conv net
            else:
                self.convs.append(None)

    def forward(self, x):
        if self.gpu_enable:
            x = x.cuda()
        for conv, module in zip(self.convs, self.model):
            if   str.lower(module[0]) == 'conv1' or str.lower(module[0]) == 'conv2' or str.lower(module[0]) == 'conv3':
                if self.gpu_enable:
                    conv = conv.cuda()
                x = conv(x)
            elif str.lower(module[0]) == 'max1':
                x = fun.max_pool1d(x, int(module[1]))
            elif str.lower(module[0]) == 'max2':
                x = fun.max_pool2d(x,module[1])
            elif str.lower(module[0]) == 'max3':
                x = fun.max_pool3d(x, int(module[1]))
            elif str.lower(module[0]) == 'avg1':
                x = fun.avg_pool1d(x, int(module[1]))
            elif str.lower(module[0]) == 'avg2':
                x = fun.avg_pool2d(x, int(module[1]))
            elif str.lower(module[0]) == 'avg3':
                x = fun.avg_pool3d(x, int(module[1]))
            elif str.lower(module[0]) == 'afun':
                if   str.lower(module[1]) == 'relu':
                    x = fun.relu(x)
                elif str.lower(module[1]) == 'softmax':
                    x = fun.softmax(x)
                elif str.lower(module[1]) == 'softmin':
                    x = fun.softmin(x)
                elif str.lower(module[1]) == 'sigmoid':
                    x = fun.sigmoid(x)
                elif str.lower(module[1]) == 'tanh':
                    x = fun.tanh(x)
                else:
                    raise Exception("Unknown activation function!")
            else:
                raise Exception("Unknown module!")
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

    def save(self, filename):
        mod = dict()
        for mID, m in enumerate(self.model):
            module = dict()
            for elementID, element  in enumerate(m):
                module["param" + str(elementID)] = element
            mod["layer" + str(mID)] = module
        mod["in_channel"] = self.in_channel
        io.savemat(filename, mdict=mod, appendmat=False)

    def vectorize(self, x):
        return x.view(-1, self.num_flat_features(x))

    def tonumpy(self, x):
        return x.data.cpu().numpy()


if __name__ == "__main__":
    i = 0 # 0: create network, 1: load network
    # Create a data
    X = np.random.rand(10, 5, 128, 128, 128)
    X = torch.Tensor(X)
    if i == 0:
        # Create a CNN model
        model = list()
        model.append(['conv3', 5, 2, 2])
        model.append(['afun', 'relu'])
        model.append(['max3', 2])
        model.append(['conv3', 12, (2, 3, 3), 2])
        model.append(['afun', 'relu'])
        model.append(['max3', 2])
        # Create a network
        net = CNN(model, X.shape[1])
        # Applying network to data X ---> Y
        Y = net(X)
        # Data shape
        print(Y.shape, Y[0, 0, 2, 2, 2])
        # Save model
        net.save("/home/tony/cnn.model")
    else:
        # Load a network
        net = CNN("/home/tony/cnn.model", X.shape[1])
        # Applying network to data X ---> Y
        Y = net(X)
        print(Y.shape, Y[0, 0, 2, 2, 2])