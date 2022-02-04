# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEzEzxGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmEzEzx(object):
    def setupUi(self, frmEzEzx):
        frmEzEzx.setObjectName("frmEzEzx")
        frmEzEzx.resize(887, 167)
        self.label = QtWidgets.QLabel(frmEzEzx)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmEzEzx)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 211, 20))
        self.label_2.setObjectName("label_2")
        self.txtInFile = QtWidgets.QLineEdit(frmEzEzx)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 631, 29))
        self.txtInFile.setObjectName("txtInFile")
        self.txtOutFile = QtWidgets.QLineEdit(frmEzEzx)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 60, 631, 29))
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnInFile = QtWidgets.QPushButton(frmEzEzx)
        self.btnInFile.setGeometry(QtCore.QRect(830, 20, 41, 29))
        self.btnInFile.setObjectName("btnInFile")
        self.btnOutFile = QtWidgets.QPushButton(frmEzEzx)
        self.btnOutFile.setGeometry(QtCore.QRect(830, 60, 41, 29))
        self.btnOutFile.setObjectName("btnOutFile")
        self.btnConvert = QtWidgets.QPushButton(frmEzEzx)
        self.btnConvert.setGeometry(QtCore.QRect(740, 120, 131, 29))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmEzEzx)
        self.btnClose.setGeometry(QtCore.QRect(20, 120, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.label_3 = QtWidgets.QLabel(frmEzEzx)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 561, 61))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(frmEzEzx)
        QtCore.QMetaObject.connectSlotsByName(frmEzEzx)

    def retranslateUi(self, frmEzEzx):
        _translate = QtCore.QCoreApplication.translate
        frmEzEzx.setWindowTitle(_translate("frmEzEzx", "Easy fMRI to Matlab"))
        self.label.setText(_translate("frmEzEzx", "Easy Data: Header File:"))
        self.label_2.setText(_translate("frmEzEzx", "easyX File:"))
        self.btnInFile.setText(_translate("frmEzEzx", "..."))
        self.btnOutFile.setText(_translate("frmEzEzx", "..."))
        self.btnConvert.setText(_translate("frmEzEzx", "Covert"))
        self.btnClose.setText(_translate("frmEzEzx", "Close"))
        self.label_3.setText(_translate("frmEzEzx", "WARNING: Free memory (RAM) must be more than 2.5x data size!"))

