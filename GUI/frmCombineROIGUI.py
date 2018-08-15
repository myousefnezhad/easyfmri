# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCombineROIGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmCombineROI(object):
    def setupUi(self, frmCombineROI):
        frmCombineROI.setObjectName("frmCombineROI")
        frmCombineROI.resize(715, 655)
        self.tvArea = QtWidgets.QTreeWidget(frmCombineROI)
        self.tvArea.setGeometry(QtCore.QRect(12, 98, 691, 501))
        self.tvArea.setMinimumSize(QtCore.QSize(691, 300))
        self.tvArea.setObjectName("tvArea")
        self.tvArea.headerItem().setText(0, "1")
        self.btnRun = QtWidgets.QPushButton(frmCombineROI)
        self.btnRun.setGeometry(QtCore.QRect(580, 610, 121, 32))
        self.btnRun.setObjectName("btnRun")
        self.btnClose = QtWidgets.QPushButton(frmCombineROI)
        self.btnClose.setGeometry(QtCore.QRect(14, 610, 121, 32))
        self.btnClose.setObjectName("btnClose")
        self.txtOFile = QtWidgets.QLineEdit(frmCombineROI)
        self.txtOFile.setGeometry(QtCore.QRect(100, 15, 541, 21))
        self.txtOFile.setStatusTip("")
        self.txtOFile.setText("")
        self.txtOFile.setObjectName("txtOFile")
        self.label_5 = QtWidgets.QLabel(frmCombineROI)
        self.label_5.setGeometry(QtCore.QRect(10, 15, 101, 17))
        self.label_5.setObjectName("label_5")
        self.btnOFile = QtWidgets.QPushButton(frmCombineROI)
        self.btnOFile.setGeometry(QtCore.QRect(650, 10, 51, 32))
        self.btnOFile.setObjectName("btnOFile")
        self.btnRemove = QtWidgets.QPushButton(frmCombineROI)
        self.btnRemove.setGeometry(QtCore.QRect(525, 50, 91, 32))
        self.btnRemove.setObjectName("btnRemove")
        self.btnAffine = QtWidgets.QPushButton(frmCombineROI)
        self.btnAffine.setGeometry(QtCore.QRect(420, 50, 91, 32))
        self.btnAffine.setObjectName("btnAffine")
        self.btnAdd = QtWidgets.QPushButton(frmCombineROI)
        self.btnAdd.setGeometry(QtCore.QRect(630, 50, 71, 32))
        self.btnAdd.setObjectName("btnAdd")
        self.label_6 = QtWidgets.QLabel(frmCombineROI)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_6.setObjectName("label_6")
        self.cbMetric = QtWidgets.QComboBox(frmCombineROI)
        self.cbMetric.setGeometry(QtCore.QRect(100, 50, 241, 26))
        self.cbMetric.setObjectName("cbMetric")

        self.retranslateUi(frmCombineROI)
        QtCore.QMetaObject.connectSlotsByName(frmCombineROI)
        frmCombineROI.setTabOrder(self.txtOFile, self.btnOFile)
        frmCombineROI.setTabOrder(self.btnOFile, self.tvArea)
        frmCombineROI.setTabOrder(self.tvArea, self.btnRun)
        frmCombineROI.setTabOrder(self.btnRun, self.btnClose)

    def retranslateUi(self, frmCombineROI):
        _translate = QtCore.QCoreApplication.translate
        frmCombineROI.setWindowTitle(_translate("frmCombineROI", "Combine ROI"))
        self.btnRun.setText(_translate("frmCombineROI", "Run"))
        self.btnClose.setText(_translate("frmCombineROI", "Close"))
        self.txtOFile.setToolTip(_translate("frmCombineROI", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_5.setText(_translate("frmCombineROI", "Output:"))
        self.btnOFile.setText(_translate("frmCombineROI", "..."))
        self.btnRemove.setText(_translate("frmCombineROI", "Remove"))
        self.btnAffine.setText(_translate("frmCombineROI", "Affine"))
        self.btnAdd.setText(_translate("frmCombineROI", "Add"))
        self.label_6.setText(_translate("frmCombineROI", "Metric"))

