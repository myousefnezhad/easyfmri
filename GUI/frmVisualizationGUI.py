# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmVisualizationGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmVisalization(object):
    def setupUi(self, frmVisalization):
        frmVisalization.setObjectName("frmVisalization")
        frmVisalization.resize(866, 432)
        self.tabWidget = QtWidgets.QTabWidget(frmVisalization)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 831, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtWork = QtWidgets.QLineEdit(self.tab)
        self.txtWork.setGeometry(QtCore.QRect(185, 20, 561, 21))
        self.txtWork.setObjectName("txtWork")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(15, 20, 181, 16))
        self.label_3.setObjectName("label_3")
        self.btnWork = QtWidgets.QPushButton(self.tab)
        self.btnWork.setGeometry(QtCore.QRect(760, 20, 51, 32))
        self.btnWork.setObjectName("btnWork")
        self.btnAFNI = QtWidgets.QPushButton(self.tab)
        self.btnAFNI.setGeometry(QtCore.QRect(16, 260, 391, 32))
        self.btnAFNI.setObjectName("btnAFNI")
        self.btnSUMA = QtWidgets.QPushButton(self.tab)
        self.btnSUMA.setGeometry(QtCore.QRect(420, 260, 391, 32))
        self.btnSUMA.setObjectName("btnSUMA")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(15, 60, 171, 16))
        self.label_9.setObjectName("label_9")
        self.cbHemisphere = QtWidgets.QComboBox(self.tab)
        self.cbHemisphere.setGeometry(QtCore.QRect(180, 60, 311, 26))
        self.cbHemisphere.setObjectName("cbHemisphere")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnMNConvert = QtWidgets.QPushButton(self.tab_2)
        self.btnMNConvert.setGeometry(QtCore.QRect(20, 30, 791, 32))
        self.btnMNConvert.setObjectName("btnMNConvert")
        self.btnNAConvert = QtWidgets.QPushButton(self.tab_2)
        self.btnNAConvert.setGeometry(QtCore.QRect(20, 90, 791, 32))
        self.btnNAConvert.setObjectName("btnNAConvert")
        self.btnTranformation = QtWidgets.QPushButton(self.tab_2)
        self.btnTranformation.setGeometry(QtCore.QRect(20, 150, 791, 32))
        self.btnTranformation.setObjectName("btnTranformation")
        self.btnImageInfo = QtWidgets.QPushButton(self.tab_2)
        self.btnImageInfo.setGeometry(QtCore.QRect(20, 210, 791, 32))
        self.btnImageInfo.setObjectName("btnImageInfo")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 181, 16))
        self.label_2.setObjectName("label_2")
        self.txtFAFNI = QtWidgets.QLineEdit(self.tab_3)
        self.txtFAFNI.setGeometry(QtCore.QRect(210, 20, 541, 21))
        self.txtFAFNI.setObjectName("txtFAFNI")
        self.txtFSUMA = QtWidgets.QLineEdit(self.tab_3)
        self.txtFSUMA.setGeometry(QtCore.QRect(210, 60, 541, 21))
        self.txtFSUMA.setObjectName("txtFSUMA")
        self.btnFAFNI = QtWidgets.QPushButton(self.tab_3)
        self.btnFAFNI.setGeometry(QtCore.QRect(760, 20, 51, 32))
        self.btnFAFNI.setObjectName("btnFAFNI")
        self.btnFSUMA = QtWidgets.QPushButton(self.tab_3)
        self.btnFSUMA.setGeometry(QtCore.QRect(760, 60, 51, 32))
        self.btnFSUMA.setObjectName("btnFSUMA")
        self.txtDSUMA = QtWidgets.QLineEdit(self.tab_3)
        self.txtDSUMA.setGeometry(QtCore.QRect(210, 100, 541, 21))
        self.txtDSUMA.setObjectName("txtDSUMA")
        self.btnDSUMA = QtWidgets.QPushButton(self.tab_3)
        self.btnDSUMA.setGeometry(QtCore.QRect(760, 100, 51, 32))
        self.btnDSUMA.setObjectName("btnDSUMA")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 181, 16))
        self.label_5.setObjectName("label_5")
        self.txtSUMAMNI = QtWidgets.QLineEdit(self.tab_3)
        self.txtSUMAMNI.setGeometry(QtCore.QRect(210, 140, 591, 21))
        self.txtSUMAMNI.setObjectName("txtSUMAMNI")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 191, 16))
        self.label_6.setObjectName("label_6")
        self.txtBSUMA = QtWidgets.QLineEdit(self.tab_3)
        self.txtBSUMA.setGeometry(QtCore.QRect(210, 180, 591, 21))
        self.txtBSUMA.setObjectName("txtBSUMA")
        self.txtLSUMA = QtWidgets.QLineEdit(self.tab_3)
        self.txtLSUMA.setGeometry(QtCore.QRect(210, 220, 591, 21))
        self.txtLSUMA.setObjectName("txtLSUMA")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 191, 16))
        self.label_7.setObjectName("label_7")
        self.txtRSUMA = QtWidgets.QLineEdit(self.tab_3)
        self.txtRSUMA.setGeometry(QtCore.QRect(210, 260, 591, 21))
        self.txtRSUMA.setObjectName("txtRSUMA")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 191, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.btnClose = QtWidgets.QPushButton(frmVisalization)
        self.btnClose.setGeometry(QtCore.QRect(20, 380, 831, 32))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(frmVisalization)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmVisalization)

    def retranslateUi(self, frmVisalization):
        _translate = QtCore.QCoreApplication.translate
        frmVisalization.setWindowTitle(_translate("frmVisalization", "Visualization"))
        self.label_3.setText(_translate("frmVisalization", "Working Directory"))
        self.btnWork.setText(_translate("frmVisalization", "..."))
        self.btnAFNI.setText(_translate("frmVisalization", "Run AFNI"))
        self.btnSUMA.setText(_translate("frmVisalization", "Run SUMA"))
        self.label_9.setText(_translate("frmVisalization", "Brain Hemisphere"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmVisalization", "AFNI"))
        self.btnMNConvert.setText(_translate("frmVisalization", "Convert Matrix to Nifti1"))
        self.btnNAConvert.setText(_translate("frmVisalization", "Convert Nifti1 to AFNI"))
        self.btnTranformation.setText(_translate("frmVisalization", "Create Transformation Matrix"))
        self.btnImageInfo.setText(_translate("frmVisalization", "Image Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmVisalization", "Tools"))
        self.label.setText(_translate("frmVisalization", "AFNI"))
        self.label_2.setText(_translate("frmVisalization", "SUMA"))
        self.btnFAFNI.setText(_translate("frmVisalization", "..."))
        self.btnFSUMA.setText(_translate("frmVisalization", "..."))
        self.btnDSUMA.setText(_translate("frmVisalization", "..."))
        self.label_4.setText(_translate("frmVisalization", "SUMA Directory"))
        self.label_5.setText(_translate("frmVisalization", "SUMA MNI"))
        self.label_6.setText(_translate("frmVisalization", "SUMA Both Hemisphere"))
        self.label_7.setText(_translate("frmVisalization", "SUMA Left Hemisphere"))
        self.label_8.setText(_translate("frmVisalization", "SUMA Right Hemisphere"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmVisalization", "System"))
        self.btnClose.setText(_translate("frmVisalization", "Close"))
