# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmfMRIConcatenatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmfMRIConcatenator(object):
    def setupUi(self, frmfMRIConcatenator):
        frmfMRIConcatenator.setObjectName("frmfMRIConcatenator")
        frmfMRIConcatenator.resize(623, 503)
        self.label_3 = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label_3.setGeometry(QtCore.QRect(20, 56, 141, 17))
        self.label_3.setObjectName("label_3")
        self.btnAdd = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnAdd.setGeometry(QtCore.QRect(480, 50, 131, 32))
        self.btnAdd.setObjectName("btnAdd")
        self.txtDim = QtWidgets.QSpinBox(frmfMRIConcatenator)
        self.txtDim.setGeometry(QtCore.QRect(160, 50, 111, 29))
        self.txtDim.setMinimum(1)
        self.txtDim.setMaximum(6)
        self.txtDim.setProperty("value", 4)
        self.txtDim.setObjectName("txtDim")
        self.btnClose = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnClose.setGeometry(QtCore.QRect(20, 460, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.btnConcatenate = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnConcatenate.setGeometry(QtCore.QRect(480, 460, 131, 29))
        self.btnConcatenate.setObjectName("btnConcatenate")
        self.btnOFile = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnOFile.setGeometry(QtCore.QRect(561, 10, 51, 32))
        self.btnOFile.setObjectName("btnOFile")
        self.txtOFile = QtWidgets.QLineEdit(frmfMRIConcatenator)
        self.txtOFile.setGeometry(QtCore.QRect(90, 15, 461, 21))
        self.txtOFile.setStatusTip("")
        self.txtOFile.setText("")
        self.txtOFile.setObjectName("txtOFile")
        self.label_4 = QtWidgets.QLabel(frmfMRIConcatenator)
        self.label_4.setGeometry(QtCore.QRect(20, 15, 101, 17))
        self.label_4.setObjectName("label_4")
        self.lwFiles = QtWidgets.QListWidget(frmfMRIConcatenator)
        self.lwFiles.setGeometry(QtCore.QRect(10, 90, 601, 361))
        self.lwFiles.setObjectName("lwFiles")
        self.btnRemove = QtWidgets.QPushButton(frmfMRIConcatenator)
        self.btnRemove.setGeometry(QtCore.QRect(340, 50, 131, 32))
        self.btnRemove.setObjectName("btnRemove")

        self.retranslateUi(frmfMRIConcatenator)
        QtCore.QMetaObject.connectSlotsByName(frmfMRIConcatenator)
        frmfMRIConcatenator.setTabOrder(self.txtOFile, self.btnOFile)
        frmfMRIConcatenator.setTabOrder(self.btnOFile, self.txtDim)
        frmfMRIConcatenator.setTabOrder(self.txtDim, self.btnRemove)
        frmfMRIConcatenator.setTabOrder(self.btnRemove, self.btnAdd)
        frmfMRIConcatenator.setTabOrder(self.btnAdd, self.btnConcatenate)
        frmfMRIConcatenator.setTabOrder(self.btnConcatenate, self.btnClose)
        frmfMRIConcatenator.setTabOrder(self.btnClose, self.lwFiles)

    def retranslateUi(self, frmfMRIConcatenator):
        _translate = QtCore.QCoreApplication.translate
        frmfMRIConcatenator.setWindowTitle(_translate("frmfMRIConcatenator", "fMRI Concatenator"))
        self.label_3.setText(_translate("frmfMRIConcatenator", "Combine from dim:"))
        self.btnAdd.setText(_translate("frmfMRIConcatenator", "Add"))
        self.btnClose.setText(_translate("frmfMRIConcatenator", "Close"))
        self.btnConcatenate.setText(_translate("frmfMRIConcatenator", "Concatenate"))
        self.btnOFile.setText(_translate("frmfMRIConcatenator", "..."))
        self.txtOFile.setToolTip(_translate("frmfMRIConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_4.setText(_translate("frmfMRIConcatenator", "Output:"))
        self.btnRemove.setText(_translate("frmfMRIConcatenator", "Remove"))

