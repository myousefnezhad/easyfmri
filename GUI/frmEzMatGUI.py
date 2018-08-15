# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEzMatGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmEzMat(object):
    def setupUi(self, frmEzMat):
        frmEzMat.setObjectName("frmEzMat")
        frmEzMat.resize(887, 167)
        self.label = QtWidgets.QLabel(frmEzMat)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmEzMat)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 211, 20))
        self.label_2.setObjectName("label_2")
        self.txtInFile = QtWidgets.QLineEdit(frmEzMat)
        self.txtInFile.setGeometry(QtCore.QRect(140, 20, 671, 29))
        self.txtInFile.setObjectName("txtInFile")
        self.txtOutFile = QtWidgets.QLineEdit(frmEzMat)
        self.txtOutFile.setGeometry(QtCore.QRect(140, 60, 671, 29))
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnInFile = QtWidgets.QPushButton(frmEzMat)
        self.btnInFile.setGeometry(QtCore.QRect(830, 20, 41, 29))
        self.btnInFile.setObjectName("btnInFile")
        self.btnOutFile = QtWidgets.QPushButton(frmEzMat)
        self.btnOutFile.setGeometry(QtCore.QRect(830, 60, 41, 29))
        self.btnOutFile.setObjectName("btnOutFile")
        self.btnConvert = QtWidgets.QPushButton(frmEzMat)
        self.btnConvert.setGeometry(QtCore.QRect(740, 120, 131, 29))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmEzMat)
        self.btnClose.setGeometry(QtCore.QRect(20, 120, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.label_3 = QtWidgets.QLabel(frmEzMat)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 561, 61))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(frmEzMat)
        QtCore.QMetaObject.connectSlotsByName(frmEzMat)

    def retranslateUi(self, frmEzMat):
        _translate = QtCore.QCoreApplication.translate
        frmEzMat.setWindowTitle(_translate("frmEzMat", "Easy fMRI to Matlab"))
        self.label.setText(_translate("frmEzMat", "Header File:"))
        self.label_2.setText(_translate("frmEzMat", "Matlab File:"))
        self.btnInFile.setText(_translate("frmEzMat", "..."))
        self.btnOutFile.setText(_translate("frmEzMat", "..."))
        self.btnConvert.setText(_translate("frmEzMat", "Covert"))
        self.btnClose.setText(_translate("frmEzMat", "Close"))
        self.label_3.setText(_translate("frmEzMat", "WARNING: Free memory (RAM) must be more than 2.5x data size!\n"
"WARNING: Data size > 3GB is not supported!"))

