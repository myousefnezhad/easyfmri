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

from PyQt5.QtWidgets import *
import numpy as np

class frmSelectRange(QDialog):
    def __init__(self, parent=None,Mode=None, D1From=0, D1To =0, D2From=0, D2To=0):
        super(frmSelectRange, self).__init__(parent)

        if Mode is None:
            print("Please select mode, i.e. \'d1\' or \'d2\'")
            return

        # inputs
        self.D1From = D1From
        self.D1To   = D1To
        self.D2From = D2From
        self.D2To   = D2To
        self.Mode = Mode
        self.PASS = False
        layout = QFormLayout()
        self.lblD1From = QLabel("Row -> From:")
        self.txtD1From = QLineEdit(str(D1From))
        layout.addRow(self.lblD1From, self.txtD1From)
        self.lblD1To = QLabel("Row -> To:")
        self.txtD1To = QLineEdit(str(D1To))
        layout.addRow(self.lblD1To, self.txtD1To)

        if Mode == "d2":
            self.lblD2From = QLabel("Column -> From:")
            self.txtD2From = QLineEdit(str(D2From))
            layout.addRow(self.lblD2From, self.txtD2From)
            self.lblD2To = QLabel("Column -> To:")
            self.txtD2To = QLineEdit(str(D2To))
            layout.addRow(self.lblD2To, self.txtD2To)



        self.btnOK = QPushButton("OK")
        self.btnOK.clicked.connect(self.btnOK_onclick)

        self.btnCan = QPushButton("Cancel")
        self.btnCan.clicked.connect(self.btnCan_onclick)
        layout.addRow(self.btnCan,self.btnOK)


        self.setLayout(layout)
        self.setWindowTitle("Session Selector")
        self.exec_()


    def btnOK_onclick(self):
        try:
            self.D1From = np.int32(self.txtD1From.text())
        except:
            msgBox = QMessageBox()
            msgBox.setText("Row -> From is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        try:
            self.D1To = np.int32(self.txtD1To.text())
        except:
            msgBox = QMessageBox()
            msgBox.setText("Row -> To is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if self.D1To < self.D1From:
            msgBox = QMessageBox()
            msgBox.setText("Row -> To is smaller then Row -> From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if self.Mode == "d2":
            try:
                self.D2From = np.int32(self.txtD2From.text())
            except:
                msgBox = QMessageBox()
                msgBox.setText("Column -> From is wrong!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            try:
                self.D2To = np.int32(self.txtD2To.text())
            except:
                msgBox = QMessageBox()
                msgBox.setText("Column -> To is wrong!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            if self.D2To < self.D2From:
                msgBox = QMessageBox()
                msgBox.setText("Column -> To is smaller then Column -> From!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

        self.PASS = True
        self.close()

    def btnCan_onclick(self):
        self.PASS = False
        self.close()
        pass
