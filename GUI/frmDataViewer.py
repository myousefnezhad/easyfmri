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
import PyQt5.QtCore as QtCore

import numpy as np

class frmDataViewer(QDialog):
    def __init__(self, Data = None, VarName = "", VarType = None, D1From=0, D1To =0, D2From=0, D2To=0):
        super().__init__()
        # if not len(VarName):
        #     return
        self.title = 'Data Viewer (Variable: ' + VarName + ')'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Variable Name:")
        self.txtRowStart = QLineEdit()
        self.txtRowStart.setReadOnly(True)
        self.txtRowStart.setText(str(VarName))
        self.txtData = QTableWidget()
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.txtData.clear()
        self.txtData.setSortingEnabled(True)
        self.txtData.doubleClicked.connect(self.View_onclick)

        #self.txtData.setReadOnly(True)

        if Data is None or VarType is None:
            return
        if VarType == "str":
            self.txtData.setRowCount(1)
            self.txtData.setColumnCount(1)
            self.txtData.setColumnWidth(0,500)
            self.txtData.setHorizontalHeaderLabels(['string'])
            item = QTableWidgetItem(Data)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.txtData.setItem(0, 0, item)
            self.txtData.move(0, 0)
        elif VarType == "str_arr":
            self.txtData.setRowCount(np.shape(Data)[0])
            self.txtData.setColumnCount(1)
            self.txtData.setColumnWidth(0,500)
            self.txtData.setHorizontalHeaderLabels(['string'])
            for le in range(0, np.shape(Data)[0]):
                item = QTableWidgetItem(Data[le])
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.txtData.setItem(le, 0, item)
            self.txtData.move(0, 0)
        elif VarType == "num":
            self.txtData.setRowCount(1)
            self.txtData.setColumnCount(1)
            self.txtData.setColumnWidth(0,500)
            self.txtData.setHorizontalHeaderLabels(['value'])
            item = QTableWidgetItem(Data)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.txtData.setItem(0, 0, item)
            self.txtData.move(0, 0)
        elif VarType == "d1":
            self.txtData.setRowCount(D1To - D1From)
            self.txtData.setColumnCount(1)
            self.txtData.setHorizontalHeaderLabels(['value'])
            for inxDD, inx in enumerate(range(D1From, D1To)):
                item = QTableWidgetItem(str(Data[inx]))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.txtData.setItem(inxDD, 0, item)
            self.txtData.move(0, 0)
        elif VarType == "d2":
            self.txtData.setRowCount(D1To - D1From)
            self.txtData.setColumnCount(D2To - D2From)
            for inxD1DD, inxD1 in enumerate(range(D1From, D1To)):
                for inxD2DD, inxD2 in enumerate(range(D2From, D2To)):
                    item = QTableWidgetItem(str(Data[inxD1][inxD2]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.txtData.setItem(inxD1DD, inxD2DD, item)
            self.txtData.move(0, 0)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.txtRowStart)
        self.layout.addWidget(self.txtData)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.setWindowFlags(self.windowFlags() & QtCore.Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        self.exec_()
        pass

    def btnExit_onclick(self):
        self.close()

    def View_onclick(self):
        msgBox = QMessageBox()
        rowID = self.txtData.currentIndex().row()
        colID = self.txtData.currentIndex().column()
        value = self.txtData.item(rowID,colID).text()
        print("current value: " + value)
        msgBox.setText("current value: " + value)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
