# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFENormalizationGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmFENormalization(object):
    def setupUi(self, frmFENormalization):
        frmFENormalization.setObjectName("frmFENormalization")
        frmFENormalization.resize(758, 691)
        self.btnInFile = QtWidgets.QPushButton(frmFENormalization)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFENormalization)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFENormalization)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFENormalization)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFENormalization)
        self.btnConvert.setGeometry(QtCore.QRect(590, 640, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFENormalization)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFENormalization)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFENormalization)
        self.btnClose.setGeometry(QtCore.QRect(30, 640, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFENormalization)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 701, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 170, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtScan = QtWidgets.QComboBox(self.tab)
        self.txtScan.setGeometry(QtCore.QRect(260, 450, 121, 26))
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(260, 290, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOmLabel.setGeometry(QtCore.QRect(420, 170, 113, 21))
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtODM = QtWidgets.QLineEdit(self.tab)
        self.txtODM.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.txtODM.setObjectName("txtODM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(140, 290, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtDM = QtWidgets.QComboBox(self.tab)
        self.txtDM.setGeometry(QtCore.QRect(260, 250, 121, 26))
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        self.cbNScan.setGeometry(QtCore.QRect(140, 450, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        self.cbCond.setGeometry(QtCore.QRect(140, 410, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbDM = QtWidgets.QCheckBox(self.tab)
        self.cbDM.setGeometry(QtCore.QRect(140, 250, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(260, 210, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        self.cbCol.setGeometry(QtCore.QRect(140, 210, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(420, 410, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtOLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOLabel.setGeometry(QtCore.QRect(420, 90, 113, 21))
        self.txtOLabel.setObjectName("txtOLabel")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(260, 370, 121, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(260, 90, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtOScan = QtWidgets.QLineEdit(self.tab)
        self.txtOScan.setGeometry(QtCore.QRect(420, 450, 113, 21))
        self.txtOScan.setObjectName("txtOScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(140, 370, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(420, 210, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(260, 50, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(260, 330, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(260, 410, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOCounter.setGeometry(QtCore.QRect(420, 370, 113, 21))
        self.txtOCounter.setObjectName("txtOCounter")
        self.txtOSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOSubject.setGeometry(QtCore.QRect(420, 130, 113, 21))
        self.txtOSubject.setObjectName("txtOSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(140, 330, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOData = QtWidgets.QLineEdit(self.tab)
        self.txtOData.setGeometry(QtCore.QRect(420, 50, 113, 21))
        self.txtOData.setObjectName("txtOData")
        self.txtORun = QtWidgets.QLineEdit(self.tab)
        self.txtORun.setGeometry(QtCore.QRect(420, 330, 113, 21))
        self.txtORun.setObjectName("txtORun")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 130, 60, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 641, 80))
        self.groupBox.setObjectName("groupBox")
        self.rbScale = QtWidgets.QRadioButton(self.groupBox)
        self.rbScale.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.rbScale.setChecked(True)
        self.rbScale.setObjectName("rbScale")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(190, 40, 131, 20))
        self.radioButton.setObjectName("radioButton")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmFENormalization)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmFENormalization)
        frmFENormalization.setTabOrder(self.txtInFile, self.btnInFile)
        frmFENormalization.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFENormalization.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFENormalization.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFENormalization.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFENormalization.setTabOrder(self.cbmLabel, self.cbCol)
        frmFENormalization.setTabOrder(self.cbCol, self.cbDM)
        frmFENormalization.setTabOrder(self.cbDM, self.cbTask)
        frmFENormalization.setTabOrder(self.cbTask, self.cbRun)
        frmFENormalization.setTabOrder(self.cbRun, self.cbCounter)
        frmFENormalization.setTabOrder(self.cbCounter, self.cbCond)
        frmFENormalization.setTabOrder(self.cbCond, self.cbNScan)
        frmFENormalization.setTabOrder(self.cbNScan, self.txtData)
        frmFENormalization.setTabOrder(self.txtData, self.txtLabel)
        frmFENormalization.setTabOrder(self.txtLabel, self.txtSubject)
        frmFENormalization.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFENormalization.setTabOrder(self.txtmLabel, self.txtCol)
        frmFENormalization.setTabOrder(self.txtCol, self.txtDM)
        frmFENormalization.setTabOrder(self.txtDM, self.txtTask)
        frmFENormalization.setTabOrder(self.txtTask, self.txtRun)
        frmFENormalization.setTabOrder(self.txtRun, self.txtCounter)
        frmFENormalization.setTabOrder(self.txtCounter, self.txtScan)
        frmFENormalization.setTabOrder(self.txtScan, self.txtOData)
        frmFENormalization.setTabOrder(self.txtOData, self.txtOLabel)
        frmFENormalization.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFENormalization.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFENormalization.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFENormalization.setTabOrder(self.txtOCol, self.txtODM)
        frmFENormalization.setTabOrder(self.txtODM, self.txtOTask)
        frmFENormalization.setTabOrder(self.txtOTask, self.txtORun)
        frmFENormalization.setTabOrder(self.txtORun, self.txtOCounter)
        frmFENormalization.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFENormalization.setTabOrder(self.txtOCond, self.txtOScan)
        frmFENormalization.setTabOrder(self.txtOScan, self.txtCond)
        frmFENormalization.setTabOrder(self.txtCond, self.rbScale)
        frmFENormalization.setTabOrder(self.rbScale, self.radioButton)
        frmFENormalization.setTabOrder(self.radioButton, self.btnConvert)
        frmFENormalization.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFENormalization):
        _translate = QtCore.QCoreApplication.translate
        frmFENormalization.setWindowTitle(_translate("frmFENormalization", "Data Normalization"))
        self.btnInFile.setText(_translate("frmFENormalization", "..."))
        self.label_33.setText(_translate("frmFENormalization", "Input Data"))
        self.btnOutFile.setText(_translate("frmFENormalization", "..."))
        self.btnConvert.setText(_translate("frmFENormalization", "Convert"))
        self.label_35.setText(_translate("frmFENormalization", "Output Data"))
        self.btnClose.setText(_translate("frmFENormalization", "Close"))
        self.txtOTask.setText(_translate("frmFENormalization", "task"))
        self.cbmLabel.setText(_translate("frmFENormalization", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFENormalization", "mlabel"))
        self.label_2.setText(_translate("frmFENormalization", "Data"))
        self.txtODM.setText(_translate("frmFENormalization", "design"))
        self.cbTask.setText(_translate("frmFENormalization", "Task"))
        self.label_3.setText(_translate("frmFENormalization", "Label"))
        self.cbNScan.setText(_translate("frmFENormalization", "NScan"))
        self.cbCond.setText(_translate("frmFENormalization", "Condition"))
        self.cbDM.setText(_translate("frmFENormalization", "Design Matrix"))
        self.cbCol.setText(_translate("frmFENormalization", "Coordinate"))
        self.txtOCond.setText(_translate("frmFENormalization", "condition"))
        self.label.setText(_translate("frmFENormalization", "Input"))
        self.txtOLabel.setText(_translate("frmFENormalization", "label"))
        self.txtOScan.setText(_translate("frmFENormalization", "nscan"))
        self.cbCounter.setText(_translate("frmFENormalization", "Counter"))
        self.txtOCol.setText(_translate("frmFENormalization", "coordinate"))
        self.label_5.setText(_translate("frmFENormalization", "Output"))
        self.txtOCounter.setText(_translate("frmFENormalization", "counter"))
        self.txtOSubject.setText(_translate("frmFENormalization", "subject"))
        self.cbRun.setText(_translate("frmFENormalization", "Run"))
        self.txtOData.setText(_translate("frmFENormalization", "data"))
        self.txtORun.setText(_translate("frmFENormalization", "run"))
        self.label_6.setText(_translate("frmFENormalization", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFENormalization", "Data"))
        self.groupBox.setTitle(_translate("frmFENormalization", "<Input Data>"))
        self.rbScale.setText(_translate("frmFENormalization", "Subject Level"))
        self.radioButton.setText(_translate("frmFENormalization", "Whole Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFENormalization", "Parameters"))

