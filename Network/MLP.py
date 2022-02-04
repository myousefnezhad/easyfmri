# This file is part of the easy fMRI distribution 
#
# Copyright (c) 2014—2021 Tony Muhammad Yousefnezhad.
#
# Website: https://easyfmri.learningbymachine.com
# GitLab:  https://gitlab.com/easyfmri/easyfmri
# GitHub:  https://github.com/easyfmri/easyfmri
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#

import torch.nn as nn

class MLP(nn.Module):
    import torch
    def __init__(self, model, activation, gpu_enable=torch.cuda.is_available()):
        super(MLP, self).__init__()
        # Save GPU status
        self.gpu_enable = gpu_enable
        # Create temp variables
        self.x = None
        self.weight = None
        self.bias = None
        # Generate network features
        self.model = model
        modelLen = len(self.model)
        self.activation = list()
        if len(activation) == 1:
            for _ in range(modelLen - 1):
                self.activation.append(activation[0])
        elif modelLen != len(activation) + 1:
            raise Exception("Length of the model and the list of activation functions are not matched!")
        else:
            self.activation = activation
        # Create network layers
        self.layer_list = list()
        for i in range(modelLen - 1):
            self.layer_list.append(["_layer" + str(i + 1), model[i], model[i + 1]])
            exec("self._layer%s =  nn.Linear(%s, %s)" % (i + 1, model[i], model[i + 1]))

    def forward(self, x):
        import torch.nn.functional as fun
        import torch
        self.x = x
        del x
        # GPU Enable
        if self.gpu_enable:
            self.x = self.x.cuda()
        # Forward layers
        for l, a in zip(self.layer_list, self.activation):
            # GPU Enable
            if self.gpu_enable:
                exec("self.%s = self.%s.cuda()" % (l[0], l[0]))
            # Apply Layers
            if a is None:
                exec("self.x = self.%s(self.x)" % (l[0]))
            elif str.lower(a) == "sigmoid":
                exec("self.x = torch.sigmoid(self.%s(self.x))" % (l[0]))
            else:
                exec("self.x = fun.%s(self.%s(self.x))" % (a, l[0]))
        return self.x

    def get_weights(self):
        self.weights = list()
        for l in self.layer_list:
            exec("self.weights.append([\'%s.weight\', self.%s.weight])"  % (l[0], l[0]))
        return self.weights

    def get_bias(self):
        self.bias = list()
        for l in self.layer_list:
            exec("self.bias.append([\'%s.bias\', self.%s.bias])"  % (l[0], l[0]))
        return self.bias


if __name__ == "__main__":
    import torch
    #mlp = MLP([5, 4, 4, 3], ['relu', 'sigmoid', None])
    mlp = MLP([5, 4, 4, 3], ['relu'])
    print(mlp)
    x = torch.Tensor([1, 2, 3, 4, 5])
    print(mlp(x))
    print(mlp.get_bias())
