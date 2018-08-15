# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCombineROIGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmCombineROI(object):
    def setupUi(self, frmCombineROI):
        frmCombineROI.setObjectName("frmCombineROI")
        frmCombineROI.resize(803, 241)
        self.btnClose = QtWidgets.QPushButton(frmCombineROI)
        self.btnClose.setGeometry(QtCore.QRect(20, 190, 113, 32))
        self.btnClose.setObjectName("btnClose")
        self.btnOROI = QtWidgets.QPushButton(frmCombineROI)
        self.btnOROI.setGeometry(QtCore.QRect(730, 100, 51, 32))
        self.btnOROI.setObjectName("btnOROI")
        self.txtOROI = QtWidgets.QLineEdit(frmCombineROI)
        self.txtOROI.setGeometry(QtCore.QRect(100, 100, 621, 21))
        self.txtOROI.setText("")
        self.txtOROI.setObjectName("txtOROI")
        self.btnRUN = QtWidgets.QPushButton(frmCombineROI)
        self.btnRUN.setGeometry(QtCore.QRect(670, 190, 113, 32))
        self.btnRUN.setObjectName("btnRUN")
        self.label_3 = QtWidgets.QLabel(frmCombineROI)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_3.setObjectName("label_3")
        self.txtSROI = QtWidgets.QLineEdit(frmCombineROI)
        self.txtSROI.setGeometry(QtCore.QRect(100, 60, 621, 21))
        self.txtSROI.setText("")
        self.txtSROI.setObjectName("txtSROI")
        self.label_4 = QtWidgets.QLabel(frmCombineROI)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.btnSROI = QtWidgets.QPushButton(frmCombineROI)
        self.btnSROI.setGeometry(QtCore.QRect(730, 60, 51, 32))
        self.btnSROI.setObjectName("btnSROI")
        self.txtFROI = QtWidgets.QLineEdit(frmCombineROI)
        self.txtFROI.setGeometry(QtCore.QRect(100, 20, 621, 21))
        self.txtFROI.setText("")
        self.txtFROI.setObjectName("txtFROI")
        self.label_5 = QtWidgets.QLabel(frmCombineROI)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_5.setObjectName("label_5")
        self.btnFROI = QtWidgets.QPushButton(frmCombineROI)
        self.btnFROI.setGeometry(QtCore.QRect(730, 20, 51, 32))
        self.btnFROI.setObjectName("btnFROI")
        self.label_6 = QtWidgets.QLabel(frmCombineROI)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 81, 16))
        self.label_6.setObjectName("label_6")
        self.cbMetric = QtWidgets.QComboBox(frmCombineROI)
        self.cbMetric.setGeometry(QtCore.QRect(100, 140, 241, 26))
        self.cbMetric.setObjectName("cbMetric")

        self.retranslateUi(frmCombineROI)
        QtCore.QMetaObject.connectSlotsByName(frmCombineROI)

    def retranslateUi(self, frmCombineROI):
        _translate = QtCore.QCoreApplication.translate
        frmCombineROI.setWindowTitle(_translate("frmCombineROI", "Combine ROI"))
        self.btnClose.setText(_translate("frmCombineROI", "Close"))
        self.btnOROI.setText(_translate("frmCombineROI", "..."))
        self.btnRUN.setText(_translate("frmCombineROI", "Run"))
        self.label_3.setText(_translate("frmCombineROI", "Output ROI"))
        self.label_4.setText(_translate("frmCombineROI", "Second ROI"))
        self.btnSROI.setText(_translate("frmCombineROI", "..."))
        self.label_5.setText(_translate("frmCombineROI", "First ROI"))
        self.btnFROI.setText(_translate("frmCombineROI", "..."))
        self.label_6.setText(_translate("frmCombineROI", "Metric"))

