# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMatNITFGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMatNITF(object):
    def setupUi(self, frmMatNITF):
        frmMatNITF.setObjectName("frmMatNITF")
        frmMatNITF.resize(841, 435)
        self.tabWidget = QtWidgets.QTabWidget(frmMatNITF)
        self.tabWidget.setGeometry(QtCore.QRect(20, 190, 801, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.label_2.setObjectName("label_2")
        self.txtMatrix = QtWidgets.QComboBox(self.tab)
        self.txtMatrix.setGeometry(QtCore.QRect(230, 30, 121, 26))
        self.txtMatrix.setEditable(True)
        self.txtMatrix.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtMatrix.setObjectName("txtMatrix")
        self.txtCoord = QtWidgets.QComboBox(self.tab)
        self.txtCoord.setGeometry(QtCore.QRect(230, 70, 121, 26))
        self.txtCoord.setEditable(True)
        self.txtCoord.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCoord.setObjectName("txtCoord")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 211, 16))
        self.label_9.setObjectName("label_9")
        self.lbCoord = QtWidgets.QLabel(self.tab)
        self.lbCoord.setGeometry(QtCore.QRect(380, 70, 401, 16))
        self.lbCoord.setObjectName("lbCoord")
        self.lbMatrix = QtWidgets.QLabel(self.tab)
        self.lbMatrix.setGeometry(QtCore.QRect(380, 30, 401, 16))
        self.lbMatrix.setObjectName("lbMatrix")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 211, 16))
        self.label_10.setObjectName("label_10")
        self.txtTime = QtWidgets.QLineEdit(self.tab)
        self.txtTime.setGeometry(QtCore.QRect(234, 110, 361, 21))
        self.txtTime.setObjectName("txtTime")
        self.lbFoldID_3 = QtWidgets.QLabel(self.tab)
        self.lbFoldID_3.setGeometry(QtCore.QRect(610, 110, 170, 16))
        self.lbFoldID_3.setObjectName("lbFoldID_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.cbScale = QtWidgets.QCheckBox(self.tab_2)
        self.cbScale.setGeometry(QtCore.QRect(20, 20, 411, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtThMin = QtWidgets.QLineEdit(self.tab_3)
        self.txtThMin.setEnabled(False)
        self.txtThMin.setGeometry(QtCore.QRect(140, 63, 113, 21))
        self.txtThMin.setObjectName("txtThMin")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 63, 111, 16))
        self.label_8.setObjectName("label_8")
        self.cbThType = QtWidgets.QComboBox(self.tab_3)
        self.cbThType.setGeometry(QtCore.QRect(140, 20, 361, 26))
        self.cbThType.setObjectName("cbThType")
        self.txtThMax = QtWidgets.QLineEdit(self.tab_3)
        self.txtThMax.setEnabled(False)
        self.txtThMax.setGeometry(QtCore.QRect(140, 100, 113, 21))
        self.txtThMax.setObjectName("txtThMax")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.txtFSUMA = QtWidgets.QLineEdit(self.tab_4)
        self.txtFSUMA.setGeometry(QtCore.QRect(115, 60, 601, 21))
        self.txtFSUMA.setObjectName("txtFSUMA")
        self.btnFSUMA = QtWidgets.QPushButton(self.tab_4)
        self.btnFSUMA.setGeometry(QtCore.QRect(730, 60, 51, 32))
        self.btnFSUMA.setObjectName("btnFSUMA")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(15, 60, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(15, 20, 121, 16))
        self.label.setObjectName("label")
        self.txtFAFNI = QtWidgets.QLineEdit(self.tab_4)
        self.txtFAFNI.setGeometry(QtCore.QRect(115, 20, 601, 21))
        self.txtFAFNI.setObjectName("txtFAFNI")
        self.btnFAFNI = QtWidgets.QPushButton(self.tab_4)
        self.btnFAFNI.setGeometry(QtCore.QRect(730, 20, 51, 32))
        self.btnFAFNI.setObjectName("btnFAFNI")
        self.tabWidget.addTab(self.tab_4, "")
        self.txtInFile = QtWidgets.QLineEdit(frmMatNITF)
        self.txtInFile.setGeometry(QtCore.QRect(200, 20, 561, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.label_33 = QtWidgets.QLabel(frmMatNITF)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnInFile = QtWidgets.QPushButton(frmMatNITF)
        self.btnInFile.setGeometry(QtCore.QRect(770, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.btnOutFile = QtWidgets.QPushButton(frmMatNITF)
        self.btnOutFile.setGeometry(QtCore.QRect(770, 100, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.btnConvert = QtWidgets.QPushButton(frmMatNITF)
        self.btnConvert.setGeometry(QtCore.QRect(680, 390, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMatNITF)
        self.label_35.setGeometry(QtCore.QRect(20, 100, 211, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMatNITF)
        self.txtOutFile.setGeometry(QtCore.QRect(200, 100, 561, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMatNITF)
        self.btnClose.setGeometry(QtCore.QRect(20, 390, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.txtAFNI = QtWidgets.QLineEdit(frmMatNITF)
        self.txtAFNI.setGeometry(QtCore.QRect(200, 140, 561, 21))
        self.txtAFNI.setText("")
        self.txtAFNI.setObjectName("txtAFNI")
        self.btnAFNI = QtWidgets.QPushButton(frmMatNITF)
        self.btnAFNI.setGeometry(QtCore.QRect(770, 140, 51, 32))
        self.btnAFNI.setObjectName("btnAFNI")
        self.label_36 = QtWidgets.QLabel(frmMatNITF)
        self.label_36.setGeometry(QtCore.QRect(20, 140, 211, 16))
        self.label_36.setObjectName("label_36")
        self.btnSSSpace = QtWidgets.QPushButton(frmMatNITF)
        self.btnSSSpace.setGeometry(QtCore.QRect(770, 60, 51, 32))
        self.btnSSSpace.setObjectName("btnSSSpace")
        self.txtSSSpace = QtWidgets.QComboBox(frmMatNITF)
        self.txtSSSpace.setGeometry(QtCore.QRect(200, 60, 561, 26))
        self.txtSSSpace.setEditable(True)
        self.txtSSSpace.setObjectName("txtSSSpace")
        self.label_5 = QtWidgets.QLabel(frmMatNITF)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 171, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(frmMatNITF)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMatNITF)

    def retranslateUi(self, frmMatNITF):
        _translate = QtCore.QCoreApplication.translate
        frmMatNITF.setWindowTitle(_translate("frmMatNITF", "Matrix to NITF"))
        self.label_2.setText(_translate("frmMatNITF", "Marix"))
        self.label_9.setText(_translate("frmMatNITF", "Coordinate"))
        self.lbCoord.setText(_translate("frmMatNITF", "ROI Size=None"))
        self.lbMatrix.setText(_translate("frmMatNITF", "Image Shape=None"))
        self.label_10.setText(_translate("frmMatNITF", "Selected Time Points"))
        self.lbFoldID_3.setText(_translate("frmMatNITF", "e.g. [0, 1, 3-8, 2, 9]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMatNITF", "Data"))
        self.cbScale.setText(_translate("frmMatNITF", "Scale Image~N(0,1)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMatNITF", "Normalization"))
        self.label_8.setText(_translate("frmMatNITF", "Min:"))
        self.label_7.setText(_translate("frmMatNITF", "Type:"))
        self.label_22.setText(_translate("frmMatNITF", "Max:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMatNITF", "Thresholding"))
        self.btnFSUMA.setText(_translate("frmMatNITF", "..."))
        self.label_3.setText(_translate("frmMatNITF", "3drefit"))
        self.label.setText(_translate("frmMatNITF", "3dcopy"))
        self.btnFAFNI.setText(_translate("frmMatNITF", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMatNITF", "System"))
        self.label_33.setText(_translate("frmMatNITF", "Input Matrix"))
        self.btnInFile.setText(_translate("frmMatNITF", "..."))
        self.btnOutFile.setText(_translate("frmMatNITF", "..."))
        self.btnConvert.setText(_translate("frmMatNITF", "Convert"))
        self.label_35.setText(_translate("frmMatNITF", "Nifti1 Output"))
        self.btnClose.setText(_translate("frmMatNITF", "Close"))
        self.btnAFNI.setText(_translate("frmMatNITF", "..."))
        self.label_36.setText(_translate("frmMatNITF", "AFNI Output (opt)"))
        self.btnSSSpace.setText(_translate("frmMatNITF", "..."))
        self.label_5.setText(_translate("frmMatNITF", "Affine Reference"))
