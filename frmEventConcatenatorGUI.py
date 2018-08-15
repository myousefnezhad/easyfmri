# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmEventConcatenatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmEventConcatenator(object):
    def setupUi(self, frmEventConcatenator):
        frmEventConcatenator.setObjectName("frmEventConcatenator")
        frmEventConcatenator.resize(623, 503)
        self.btnAdd = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnAdd.setGeometry(QtCore.QRect(480, 84, 131, 32))
        self.btnAdd.setObjectName("btnAdd")
        self.txtOffset = QtWidgets.QSpinBox(frmEventConcatenator)
        self.txtOffset.setGeometry(QtCore.QRect(140, 84, 111, 29))
        self.txtOffset.setMinimum(1)
        self.txtOffset.setMaximum(10000000)
        self.txtOffset.setProperty("value", 2)
        self.txtOffset.setObjectName("txtOffset")
        self.btnClose = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnClose.setGeometry(QtCore.QRect(20, 460, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.btnConcatenate = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnConcatenate.setGeometry(QtCore.QRect(480, 460, 131, 29))
        self.btnConcatenate.setObjectName("btnConcatenate")
        self.btnOFile = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnOFile.setGeometry(QtCore.QRect(561, 10, 51, 32))
        self.btnOFile.setObjectName("btnOFile")
        self.txtOFile = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtOFile.setGeometry(QtCore.QRect(90, 15, 461, 21))
        self.txtOFile.setStatusTip("")
        self.txtOFile.setText("")
        self.txtOFile.setObjectName("txtOFile")
        self.label_4 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_4.setGeometry(QtCore.QRect(20, 15, 101, 17))
        self.label_4.setObjectName("label_4")
        self.btnRemove = QtWidgets.QPushButton(frmEventConcatenator)
        self.btnRemove.setGeometry(QtCore.QRect(340, 84, 131, 32))
        self.btnRemove.setObjectName("btnRemove")
        self.label_3 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 17))
        self.label_3.setObjectName("label_3")
        self.lwFiles = QtWidgets.QTreeWidget(frmEventConcatenator)
        self.lwFiles.setGeometry(QtCore.QRect(10, 130, 601, 321))
        self.lwFiles.setObjectName("lwFiles")
        self.lwFiles.headerItem().setText(0, "1")
        self.txtHDR = QtWidgets.QLineEdit(frmEventConcatenator)
        self.txtHDR.setGeometry(QtCore.QRect(90, 50, 511, 21))
        self.txtHDR.setStatusTip("")
        self.txtHDR.setText("")
        self.txtHDR.setObjectName("txtHDR")
        self.label_5 = QtWidgets.QLabel(frmEventConcatenator)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(frmEventConcatenator)
        QtCore.QMetaObject.connectSlotsByName(frmEventConcatenator)
        frmEventConcatenator.setTabOrder(self.txtOFile, self.btnOFile)
        frmEventConcatenator.setTabOrder(self.btnOFile, self.txtOffset)
        frmEventConcatenator.setTabOrder(self.txtOffset, self.btnRemove)
        frmEventConcatenator.setTabOrder(self.btnRemove, self.btnAdd)
        frmEventConcatenator.setTabOrder(self.btnAdd, self.btnConcatenate)
        frmEventConcatenator.setTabOrder(self.btnConcatenate, self.btnClose)

    def retranslateUi(self, frmEventConcatenator):
        _translate = QtCore.QCoreApplication.translate
        frmEventConcatenator.setWindowTitle(_translate("frmEventConcatenator", "Event Concatenator"))
        self.btnAdd.setText(_translate("frmEventConcatenator", "Add"))
        self.btnClose.setText(_translate("frmEventConcatenator", "Close"))
        self.btnConcatenate.setText(_translate("frmEventConcatenator", "Concatenate"))
        self.btnOFile.setText(_translate("frmEventConcatenator", "..."))
        self.txtOFile.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_4.setText(_translate("frmEventConcatenator", "Output:"))
        self.btnRemove.setText(_translate("frmEventConcatenator", "Remove"))
        self.label_3.setText(_translate("frmEventConcatenator", "Offset from Line:"))
        self.txtHDR.setToolTip(_translate("frmEventConcatenator", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_5.setText(_translate("frmEventConcatenator", "Header:"))

