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

import threading
import numpy as np
from sklearn.metrics import accuracy_score

class MultiThreadingVectorClassification(threading.Thread):
    def __init__(self, TrX, Try, TeX, Tey, startIndex, model, metric=accuracy_score, processID=""):
        super(MultiThreadingVectorClassification, self).__init__()
        self.processID = processID
        # Training set
        self.TrX = TrX
        self.Try = Try
        # Testing set
        self.TeX = TeX
        self.Tey = Tey
        # Corresponding Coordinates
        self.startIndex = startIndex
        # Classification model and metric
        self.model = model
        self.metric = metric
        # Analysis results
        self.Results = list()

    def run(self):
        self.Results = list()
        _, Xy = np.shape(self.TrX)
        index = self.startIndex
        for idx, (Trx, Tex) in enumerate(zip(np.transpose(self.TrX), np.transpose(self.TeX))):
            self.model.fit(np.transpose([Trx]), self.Try)
            Prediction = self.model.predict(np.transpose([Tex]))
            self.Results.append([index, self.metric(self.Tey, Prediction)])
            index += 1
            print('Thread {:5d}: Model {:15d} of {:15d} is done.\n'.format(self.processID, idx+1, Xy))
