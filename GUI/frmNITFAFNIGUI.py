# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmNITFAFNIGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmNITFAFNI(object):
    def setupUi(self, frmNITFAFNI):
        frmNITFAFNI.setObjectName("frmNITFAFNI")
        frmNITFAFNI.resize(841, 247)
        self.btnInFile = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnInFile.setGeometry(QtCore.QRect(770, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.btnConvert = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnConvert.setGeometry(QtCore.QRect(680, 200, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmNITFAFNI)
        self.label_35.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_35.setObjectName("label_35")
        self.txtInFile = QtWidgets.QLineEdit(frmNITFAFNI)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 601, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnClose = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnClose.setGeometry(QtCore.QRect(20, 200, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.txtAFNI = QtWidgets.QLineEdit(frmNITFAFNI)
        self.txtAFNI.setGeometry(QtCore.QRect(160, 60, 601, 21))
        self.txtAFNI.setText("")
        self.txtAFNI.setObjectName("txtAFNI")
        self.btnAFNI = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnAFNI.setGeometry(QtCore.QRect(770, 60, 51, 32))
        self.btnAFNI.setObjectName("btnAFNI")
        self.label_36 = QtWidgets.QLabel(frmNITFAFNI)
        self.label_36.setGeometry(QtCore.QRect(20, 60, 211, 16))
        self.label_36.setObjectName("label_36")
        self.btnFAFNI = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnFAFNI.setGeometry(QtCore.QRect(770, 100, 51, 32))
        self.btnFAFNI.setObjectName("btnFAFNI")
        self.txtFSUMA = QtWidgets.QLineEdit(frmNITFAFNI)
        self.txtFSUMA.setGeometry(QtCore.QRect(155, 140, 601, 21))
        self.txtFSUMA.setObjectName("txtFSUMA")
        self.label_3 = QtWidgets.QLabel(frmNITFAFNI)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_3.setObjectName("label_3")
        self.btnFSUMA = QtWidgets.QPushButton(frmNITFAFNI)
        self.btnFSUMA.setGeometry(QtCore.QRect(770, 140, 51, 32))
        self.btnFSUMA.setObjectName("btnFSUMA")
        self.txtFAFNI = QtWidgets.QLineEdit(frmNITFAFNI)
        self.txtFAFNI.setGeometry(QtCore.QRect(155, 100, 601, 21))
        self.txtFAFNI.setObjectName("txtFAFNI")
        self.label = QtWidgets.QLabel(frmNITFAFNI)
        self.label.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.label.setObjectName("label")

        self.retranslateUi(frmNITFAFNI)
        QtCore.QMetaObject.connectSlotsByName(frmNITFAFNI)

    def retranslateUi(self, frmNITFAFNI):
        _translate = QtCore.QCoreApplication.translate
        frmNITFAFNI.setWindowTitle(_translate("frmNITFAFNI", "NITF to AFNI"))
        self.btnInFile.setText(_translate("frmNITFAFNI", "..."))
        self.btnConvert.setText(_translate("frmNITFAFNI", "Convert"))
        self.label_35.setText(_translate("frmNITFAFNI", "Nifti1 Input"))
        self.btnClose.setText(_translate("frmNITFAFNI", "Close"))
        self.btnAFNI.setText(_translate("frmNITFAFNI", "..."))
        self.label_36.setText(_translate("frmNITFAFNI", "AFNI Output"))
        self.btnFAFNI.setText(_translate("frmNITFAFNI", "..."))
        self.label_3.setText(_translate("frmNITFAFNI", "3drefit"))
        self.btnFSUMA.setText(_translate("frmNITFAFNI", "..."))
        self.label.setText(_translate("frmNITFAFNI", "3dcopy"))

