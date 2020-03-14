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
