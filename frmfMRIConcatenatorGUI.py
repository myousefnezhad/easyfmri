# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmfMRIConcatenatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmfMRIConcatenator(object):
    def setupUi(self, frmfMRIConcatenator):
        frmfMRIConcatenator.setObjectName("frmfMRIConcatenator")
        frmfMRIConcatenator.resize(623, 212)
        self.label = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label_3.setGeometry(QtCore.QRect(20, 165, 141, 17))
        self.label_3.setObjectName("label_3")
        self.btnFFile = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnFFile.setGeometry(QtCore.QRect(560, 10, 51, 32))
        self.btnFFile.setObjectName("btnFFile")
        self.txtFFile = QtWidgets.QLineEdit(frmfMRIConcatenator)
        self.txtFFile.setGeometry(QtCore.QRect(119, 15, 431, 21))
        self.txtFFile.setStatusTip("")
        self.txtFFile.setText("")
        self.txtFFile.setObjectName("txtFFile")
        self.btnSFile = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnSFile.setGeometry(QtCore.QRect(561, 55, 51, 32))
        self.btnSFile.setObjectName("btnSFile")
        self.txtSFile = QtWidgets.QLineEdit(frmfMRIConcatenator)
        self.txtSFile.setGeometry(QtCore.QRect(120, 60, 431, 21))
        self.txtSFile.setStatusTip("")
        self.txtSFile.setText("")
        self.txtSFile.setObjectName("txtSFile")
        self.txtDim = QtWidgets.QSpinBox(frmfMRIConcatenator)
        self.txtDim.setGeometry(QtCore.QRect(180, 159, 111, 29))
        self.txtDim.setMinimum(1)
        self.txtDim.setMaximum(6)
        self.txtDim.setProperty("value", 4)
        self.txtDim.setObjectName("txtDim")
        self.btnClose = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnClose.setGeometry(QtCore.QRect(330, 160, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.btnConcatenate = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnConcatenate.setGeometry(QtCore.QRect(480, 160, 131, 29))
        self.btnConcatenate.setObjectName("btnConcatenate")
        self.btnOFile = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnOFile.setGeometry(QtCore.QRect(561, 101, 51, 32))
        self.btnOFile.setObjectName("btnOFile")
        self.txtOFile = QtWidgets.QLineEdit(frmfMRIConcatenator)
        self.txtOFile.setGeometry(QtCore.QRect(120, 106, 431, 21))
        self.txtOFile.setStatusTip("")
        self.txtOFile.setText("")
        self.txtOFile.setObjectName("txtOFile")
        self.label_4 = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label_4.setGeometry(QtCore.QRect(20, 106, 101, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(frmfMRIConcatenator)
        QtCore.QMetaObject.connectSlotsByName(frmfMRIConcatenator)

    def retranslateUi(self, frmfMRIConcatenator):
        _translate = QtCore.QCoreApplication.translate
        frmfMRIConcatenator.setWindowTitle(_translate("frmfMRIConcatenator", "fMRI Concatenator"))
        self.label.setText(_translate("frmfMRIConcatenator", "First File:"))
        self.label_2.setText(_translate("frmfMRIConcatenator", "Second File:"))
        self.label_3.setText(_translate("frmfMRIConcatenator", "Combine from dim:"))
        self.btnFFile.setText(_translate("frmfMRIConcatenator", "..."))
        self.txtFFile.setToolTip(_translate("frmfMRIConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.btnSFile.setText(_translate("frmfMRIConcatenator", "..."))
        self.txtSFile.setToolTip(_translate("frmfMRIConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.btnClose.setText(_translate("frmfMRIConcatenator", "Close"))
        self.btnConcatenate.setText(_translate("frmfMRIConcatenator", "Concatenate"))
        self.btnOFile.setText(_translate("frmfMRIConcatenator", "..."))
        self.txtOFile.setToolTip(_translate("frmfMRIConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_4.setText(_translate("frmfMRIConcatenator", "Output:"))

