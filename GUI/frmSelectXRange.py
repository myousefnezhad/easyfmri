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

from PyQt5.QtWidgets import *
import numpy as np
import sys

class frmSelectXRange(QDialog):
    def __init__(self, RangeTo, RangeFrom=None):
        super(frmSelectXRange, self).__init__(None)
        self.From = None
        self.To   = None
        self.PASS = False
        self.objects = dict()
        if RangeFrom is None:
            RangeFrom = np.zeros((len(RangeTo), 1))
        else:
            if len(RangeFrom) != len(RangeTo):
                print("Ranges are not matched!")
                return
        self.Len = len(RangeTo)
        layout = QFormLayout()
        for i, (rf, rt) in enumerate(zip(RangeFrom, RangeTo)):
            self.objects["labelfrom" + str(i)]  = QLabel("Dimension " + str(i) + ", From: ")
            self.objects["sbfrom" + str(i)]     = QSpinBox()
            self.objects["sbfrom" + str(i)].setMinimum(rf)
            self.objects["sbfrom" + str(i)].setMaximum(rt - 1)
            self.objects["sbfrom" + str(i)].setValue(rf)
            layout.addRow(self.objects["labelfrom" + str(i)], self.objects["sbfrom" + str(i)])
            self.objects["labelto" + str(i)]    = QLabel("Dimension " + str(i) + ", To: ")
            self.objects["sbto" + str(i)]       = QSpinBox()
            self.objects["sbto" + str(i)].setMinimum(rf + 1)
            self.objects["sbto" + str(i)].setMaximum(rt)
            self.objects["sbto" + str(i)].setValue(rt)
            layout.addRow(self.objects["labelto" + str(i)], self.objects["sbto" + str(i)])


        self.btnOK = QPushButton("OK")
        self.btnOK.clicked.connect(self.btnOK_onclick)

        self.btnCan = QPushButton("Cancel")
        self.btnCan.clicked.connect(self.btnCan_onclick)
        layout.addRow(self.btnCan,self.btnOK)


        self.setLayout(layout)
        self.setWindowTitle("Session Selector")
        self.exec_()


    def btnOK_onclick(self):
        self.From = list()
        self.To   = list()
        for i in range(self.Len):
            self.From.append(self.objects["sbfrom" + str(i)].value())
            self.To.append(self.objects["sbto" + str(i)].value())
        self.PASS = True
        self.close()

    def btnCan_onclick(self):
        self.PASS = False
        self.close()
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = frmSelectXRange((4, 5, 7))
    if frm.PASS:
        print(frm.From, frm.To)
    sys.exit(app.exec_())