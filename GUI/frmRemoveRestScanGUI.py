# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmRemoveRestScanGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmRemoveRestScan(object):
    def setupUi(self, frmRemoveRestScan):
        frmRemoveRestScan.setObjectName("frmRemoveRestScan")
        frmRemoveRestScan.resize(881, 380)
        self.cbNScan = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbNScan.setGeometry(QtCore.QRect(520, 120, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbCond.setGeometry(QtCore.QRect(280, 280, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbCounter = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbCounter.setGeometry(QtCore.QRect(280, 240, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.cbmLabel = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbmLabel.setGeometry(QtCore.QRect(20, 200, 161, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.cbCol = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbCol.setGeometry(QtCore.QRect(20, 240, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.cbDM = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbDM.setGeometry(QtCore.QRect(20, 280, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.cbTask = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbTask.setGeometry(QtCore.QRect(280, 160, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.cbSubject = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbSubject.setGeometry(QtCore.QRect(280, 120, 81, 20))
        self.cbSubject.setChecked(True)
        self.cbSubject.setObjectName("cbSubject")
        self.cbRun = QtWidgets.QCheckBox(frmRemoveRestScan)
        self.cbRun.setGeometry(QtCore.QRect(280, 200, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.label_33 = QtWidgets.QLabel(frmRemoveRestScan)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_33.setObjectName("label_33")
        self.btnInFile = QtWidgets.QPushButton(frmRemoveRestScan)
        self.btnInFile.setGeometry(QtCore.QRect(810, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.txtInFile = QtWidgets.QLineEdit(frmRemoveRestScan)
        self.txtInFile.setGeometry(QtCore.QRect(140, 20, 661, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.label_34 = QtWidgets.QLabel(frmRemoveRestScan)
        self.label_34.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_34.setObjectName("label_34")
        self.txtOutFile = QtWidgets.QLineEdit(frmRemoveRestScan)
        self.txtOutFile.setGeometry(QtCore.QRect(140, 60, 661, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnOutFile = QtWidgets.QPushButton(frmRemoveRestScan)
        self.btnOutFile.setGeometry(QtCore.QRect(810, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.btnConvert = QtWidgets.QPushButton(frmRemoveRestScan)
        self.btnConvert.setGeometry(QtCore.QRect(720, 330, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label = QtWidgets.QLabel(frmRemoveRestScan)
        self.label.setGeometry(QtCore.QRect(520, 160, 91, 16))
        self.label.setObjectName("label")
        self.txtClassID = QtWidgets.QLineEdit(frmRemoveRestScan)
        self.txtClassID.setGeometry(QtCore.QRect(650, 160, 113, 21))
        self.txtClassID.setObjectName("txtClassID")
        self.txtData = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtData.setGeometry(QtCore.QRect(140, 120, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtLabel = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtLabel.setGeometry(QtCore.QRect(140, 160, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtmLabel = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtmLabel.setGeometry(QtCore.QRect(140, 200, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.txtCol = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtCol.setGeometry(QtCore.QRect(140, 240, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.txtDM = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtDM.setGeometry(QtCore.QRect(140, 280, 121, 26))
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.txtSubject = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtSubject.setGeometry(QtCore.QRect(380, 120, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtTask = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtTask.setGeometry(QtCore.QRect(380, 160, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtRun = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtRun.setGeometry(QtCore.QRect(380, 200, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCounter = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtCounter.setGeometry(QtCore.QRect(380, 240, 121, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtCond = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtCond.setGeometry(QtCore.QRect(380, 280, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtNScan = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtNScan.setGeometry(QtCore.QRect(647, 120, 121, 26))
        self.txtNScan.setEditable(True)
        self.txtNScan.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtNScan.setObjectName("txtNScan")
        self.btnClose = QtWidgets.QPushButton(frmRemoveRestScan)
        self.btnClose.setGeometry(QtCore.QRect(10, 330, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.label_2 = QtWidgets.QLabel(frmRemoveRestScan)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frmRemoveRestScan)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(frmRemoveRestScan)
        self.label_4.setGeometry(QtCore.QRect(520, 200, 111, 16))
        self.label_4.setObjectName("label_4")
        self.txtClassName = QtWidgets.QComboBox(frmRemoveRestScan)
        self.txtClassName.setGeometry(QtCore.QRect(647, 200, 121, 26))
        self.txtClassName.setEditable(True)
        self.txtClassName.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtClassName.setObjectName("txtClassName")
        self.btnReadClassName = QtWidgets.QPushButton(frmRemoveRestScan)
        self.btnReadClassName.setGeometry(QtCore.QRect(780, 200, 81, 32))
        self.btnReadClassName.setObjectName("btnReadClassName")

        self.retranslateUi(frmRemoveRestScan)
        QtCore.QMetaObject.connectSlotsByName(frmRemoveRestScan)
        frmRemoveRestScan.setTabOrder(self.txtInFile, self.btnInFile)
        frmRemoveRestScan.setTabOrder(self.btnInFile, self.txtOutFile)
        frmRemoveRestScan.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmRemoveRestScan.setTabOrder(self.btnOutFile, self.txtData)
        frmRemoveRestScan.setTabOrder(self.txtData, self.txtLabel)
        frmRemoveRestScan.setTabOrder(self.txtLabel, self.cbmLabel)
        frmRemoveRestScan.setTabOrder(self.cbmLabel, self.txtmLabel)
        frmRemoveRestScan.setTabOrder(self.txtmLabel, self.cbCol)
        frmRemoveRestScan.setTabOrder(self.cbCol, self.txtCol)
        frmRemoveRestScan.setTabOrder(self.txtCol, self.cbDM)
        frmRemoveRestScan.setTabOrder(self.cbDM, self.txtDM)
        frmRemoveRestScan.setTabOrder(self.txtDM, self.cbSubject)
        frmRemoveRestScan.setTabOrder(self.cbSubject, self.txtSubject)
        frmRemoveRestScan.setTabOrder(self.txtSubject, self.cbTask)
        frmRemoveRestScan.setTabOrder(self.cbTask, self.txtTask)
        frmRemoveRestScan.setTabOrder(self.txtTask, self.cbRun)
        frmRemoveRestScan.setTabOrder(self.cbRun, self.txtRun)
        frmRemoveRestScan.setTabOrder(self.txtRun, self.cbCounter)
        frmRemoveRestScan.setTabOrder(self.cbCounter, self.txtCounter)
        frmRemoveRestScan.setTabOrder(self.txtCounter, self.cbCond)
        frmRemoveRestScan.setTabOrder(self.cbCond, self.txtCond)
        frmRemoveRestScan.setTabOrder(self.txtCond, self.cbNScan)
        frmRemoveRestScan.setTabOrder(self.cbNScan, self.txtNScan)
        frmRemoveRestScan.setTabOrder(self.txtNScan, self.txtClassID)
        frmRemoveRestScan.setTabOrder(self.txtClassID, self.btnConvert)
        frmRemoveRestScan.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmRemoveRestScan):
        _translate = QtCore.QCoreApplication.translate
        frmRemoveRestScan.setWindowTitle(_translate("frmRemoveRestScan", "Remove Rest Scan"))
        self.cbNScan.setText(_translate("frmRemoveRestScan", "NScan"))
        self.cbCond.setText(_translate("frmRemoveRestScan", "Condition"))
        self.cbCounter.setText(_translate("frmRemoveRestScan", "Counter"))
        self.cbmLabel.setText(_translate("frmRemoveRestScan", "Label (matrix)"))
        self.cbCol.setText(_translate("frmRemoveRestScan", "Coordinate"))
        self.cbDM.setText(_translate("frmRemoveRestScan", "Design Matrix"))
        self.cbTask.setText(_translate("frmRemoveRestScan", "Task"))
        self.cbSubject.setText(_translate("frmRemoveRestScan", "Subject"))
        self.cbRun.setText(_translate("frmRemoveRestScan", "Run"))
        self.label_33.setText(_translate("frmRemoveRestScan", "Input Data File"))
        self.btnInFile.setText(_translate("frmRemoveRestScan", "..."))
        self.label_34.setText(_translate("frmRemoveRestScan", "Output Data File"))
        self.btnOutFile.setText(_translate("frmRemoveRestScan", "..."))
        self.btnConvert.setText(_translate("frmRemoveRestScan", "Convert"))
        self.label.setText(_translate("frmRemoveRestScan", "Rest Class ID"))
        self.txtClassID.setText(_translate("frmRemoveRestScan", "0"))
        self.btnClose.setText(_translate("frmRemoveRestScan", "Close"))
        self.label_2.setText(_translate("frmRemoveRestScan", "Data"))
        self.label_3.setText(_translate("frmRemoveRestScan", "Label"))
        self.label_4.setText(_translate("frmRemoveRestScan", "Rest Class Name"))
        self.btnReadClassName.setText(_translate("frmRemoveRestScan", "Load"))

