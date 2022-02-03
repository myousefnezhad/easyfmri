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

from PyQt6.QtWidgets import *
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