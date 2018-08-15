# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmImageInfoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmImageInfo(object):
    def setupUi(self, frmImageInfo):
        frmImageInfo.setObjectName("frmImageInfo")
        frmImageInfo.resize(714, 613)
        self.label = QtWidgets.QLabel(frmImageInfo)
        self.label.setGeometry(QtCore.QRect(22, 20, 111, 16))
        self.label.setToolTip("")
        self.label.setToolTipDuration(-1)
        self.label.setStatusTip("")
        self.label.setObjectName("label")
        self.btnImage = QtWidgets.QPushButton(frmImageInfo)
        self.btnImage.setGeometry(QtCore.QRect(640, 15, 51, 32))
        self.btnImage.setObjectName("btnImage")
        self.txtImage = QtWidgets.QLineEdit(frmImageInfo)
        self.txtImage.setGeometry(QtCore.QRect(130, 20, 501, 21))
        self.txtImage.setStatusTip("")
        self.txtImage.setText("")
        self.txtImage.setObjectName("txtImage")
        self.txtImageInfo = QtWidgets.QTextEdit(frmImageInfo)
        self.txtImageInfo.setGeometry(QtCore.QRect(10, 60, 691, 501))
        self.txtImageInfo.setObjectName("txtImageInfo")
        self.btnClose = QtWidgets.QPushButton(frmImageInfo)
        self.btnClose.setGeometry(QtCore.QRect(580, 570, 113, 32))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(frmImageInfo)
        QtCore.QMetaObject.connectSlotsByName(frmImageInfo)

    def retranslateUi(self, frmImageInfo):
        _translate = QtCore.QCoreApplication.translate
        frmImageInfo.setWindowTitle(_translate("frmImageInfo", "Dialog"))
        self.label.setText(_translate("frmImageInfo", "Image File"))
        self.label.setProperty("setToolTip", _translate("frmImageInfo", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.btnImage.setText(_translate("frmImageInfo", "..."))
        self.txtImage.setToolTip(_translate("frmImageInfo", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.btnClose.setText(_translate("frmImageInfo", "Close"))

