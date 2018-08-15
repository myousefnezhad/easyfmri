# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmDataEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDataEditor(object):
    def setupUi(self, frmDataEditor):
        frmDataEditor.setObjectName("frmDataEditor")
        frmDataEditor.resize(742, 470)
        self.txtInFile = QtWidgets.QLineEdit(frmDataEditor)
        self.txtInFile.setGeometry(QtCore.QRect(140, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnInFile = QtWidgets.QPushButton(frmDataEditor)
        self.btnInFile.setGeometry(QtCore.QRect(670, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmDataEditor)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnClose = QtWidgets.QPushButton(frmDataEditor)
        self.btnClose.setGeometry(QtCore.QRect(20, 430, 131, 29))
        self.btnClose.setObjectName("btnClose")
        self.lwData = QtWidgets.QTreeWidget(frmDataEditor)
        self.lwData.setGeometry(QtCore.QRect(20, 60, 701, 361))
        self.lwData.setObjectName("lwData")
        self.lwData.headerItem().setText(0, "1")
        self.btnValue = QtWidgets.QPushButton(frmDataEditor)
        self.btnValue.setGeometry(QtCore.QRect(570, 430, 151, 32))
        self.btnValue.setObjectName("btnValue")

        self.retranslateUi(frmDataEditor)
        QtCore.QMetaObject.connectSlotsByName(frmDataEditor)
        frmDataEditor.setTabOrder(self.txtInFile, self.btnInFile)
        frmDataEditor.setTabOrder(self.btnInFile, self.lwData)
        frmDataEditor.setTabOrder(self.lwData, self.btnValue)
        frmDataEditor.setTabOrder(self.btnValue, self.btnClose)

    def retranslateUi(self, frmDataEditor):
        _translate = QtCore.QCoreApplication.translate
        frmDataEditor.setWindowTitle(_translate("frmDataEditor", "Data Editor"))
        self.btnInFile.setText(_translate("frmDataEditor", "..."))
        self.label_33.setText(_translate("frmDataEditor", "Input Data "))
        self.btnClose.setText(_translate("frmDataEditor", "Close"))
        self.lwData.setSortingEnabled(True)
        self.btnValue.setText(_translate("frmDataEditor", "View Value"))

