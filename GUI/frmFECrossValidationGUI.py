# Form implementation generated from reading ui file 'frmFECrossValidationGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmFECrossValidation(object):
    def setupUi(self, frmFECrossValidation):
        frmFECrossValidation.setObjectName("frmFECrossValidation")
        frmFECrossValidation.resize(758, 716)
        self.btnInFile = QtWidgets.QPushButton(frmFECrossValidation)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFECrossValidation)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFECrossValidation)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFECrossValidation)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 501, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFECrossValidation)
        self.btnConvert.setGeometry(QtCore.QRect(590, 670, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFECrossValidation)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 151, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutDIR = QtWidgets.QLineEdit(frmFECrossValidation)
        self.txtOutDIR.setGeometry(QtCore.QRect(180, 60, 501, 21))
        self.txtOutDIR.setText("")
        self.txtOutDIR.setObjectName("txtOutDIR")
        self.btnClose = QtWidgets.QPushButton(frmFECrossValidation)
        self.btnClose.setGeometry(QtCore.QRect(30, 670, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFECrossValidation)
        self.tabWidget.setGeometry(QtCore.QRect(30, 140, 701, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 170, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtScan = QtWidgets.QComboBox(self.tab)
        self.txtScan.setGeometry(QtCore.QRect(260, 450, 121, 26))
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(260, 290, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(260, 90, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(260, 330, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(260, 410, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.cbSubject = QtWidgets.QCheckBox(self.tab)
        self.cbSubject.setGeometry(QtCore.QRect(140, 130, 111, 20))
        self.cbSubject.setObjectName("cbSubject")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 141, 16))
        self.label_4.setObjectName("label_4")
        self.txtTrain = QtWidgets.QLineEdit(self.tab_2)
        self.txtTrain.setGeometry(QtCore.QRect(230, 30, 181, 21))
        self.txtTrain.setObjectName("txtTrain")
        self.txtTest = QtWidgets.QLineEdit(self.tab_2)
        self.txtTest.setGeometry(QtCore.QRect(230, 70, 181, 21))
        self.txtTest.setObjectName("txtTest")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 70, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 191, 16))
        self.label_8.setObjectName("label_8")
        self.txtUnit = QtWidgets.QSpinBox(self.tab_2)
        self.txtUnit.setGeometry(QtCore.QRect(230, 110, 181, 24))
        self.txtUnit.setMinimum(1)
        self.txtUnit.setMaximum(1000000000)
        self.txtUnit.setObjectName("txtUnit")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 651, 141))
        self.groupBox.setObjectName("groupBox")
        self.cbFTask = QtWidgets.QCheckBox(self.groupBox)
        self.cbFTask.setGeometry(QtCore.QRect(480, 60, 161, 20))
        self.cbFTask.setObjectName("cbFTask")
        self.cbFCounter = QtWidgets.QCheckBox(self.groupBox)
        self.cbFCounter.setGeometry(QtCore.QRect(480, 100, 161, 20))
        self.cbFCounter.setObjectName("cbFCounter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 451, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cbFSubject = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbFSubject.setGeometry(QtCore.QRect(10, 30, 130, 20))
        self.cbFSubject.setChecked(True)
        self.cbFSubject.setObjectName("cbFSubject")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.rbFRun = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbFRun.setGeometry(QtCore.QRect(220, 60, 221, 20))
        self.rbFRun.setObjectName("rbFRun")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_36 = QtWidgets.QLabel(frmFECrossValidation)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 151, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutFile = QtWidgets.QLineEdit(frmFECrossValidation)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 100, 501, 21))
        self.txtOutFile.setObjectName("txtOutFile")
        self.label_6 = QtWidgets.QLabel(frmFECrossValidation)
        self.label_6.setGeometry(QtCore.QRect(190, 674, 380, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(frmFECrossValidation)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFECrossValidation)
        frmFECrossValidation.setTabOrder(self.txtInFile, self.btnInFile)
        frmFECrossValidation.setTabOrder(self.btnInFile, self.txtOutDIR)
        frmFECrossValidation.setTabOrder(self.txtOutDIR, self.btnOutFile)
        frmFECrossValidation.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFECrossValidation.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFECrossValidation.setTabOrder(self.cbmLabel, self.cbCol)
        frmFECrossValidation.setTabOrder(self.cbCol, self.cbDM)
        frmFECrossValidation.setTabOrder(self.cbDM, self.cbTask)
        frmFECrossValidation.setTabOrder(self.cbTask, self.cbRun)
        frmFECrossValidation.setTabOrder(self.cbRun, self.cbCounter)
        frmFECrossValidation.setTabOrder(self.cbCounter, self.cbCond)
        frmFECrossValidation.setTabOrder(self.cbCond, self.cbNScan)
        frmFECrossValidation.setTabOrder(self.cbNScan, self.txtData)
        frmFECrossValidation.setTabOrder(self.txtData, self.txtLabel)
        frmFECrossValidation.setTabOrder(self.txtLabel, self.txtSubject)
        frmFECrossValidation.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFECrossValidation.setTabOrder(self.txtmLabel, self.txtCol)
        frmFECrossValidation.setTabOrder(self.txtCol, self.txtDM)
        frmFECrossValidation.setTabOrder(self.txtDM, self.txtTask)
        frmFECrossValidation.setTabOrder(self.txtTask, self.txtRun)
        frmFECrossValidation.setTabOrder(self.txtRun, self.txtCounter)
        frmFECrossValidation.setTabOrder(self.txtCounter, self.txtScan)
        frmFECrossValidation.setTabOrder(self.txtScan, self.txtOData)
        frmFECrossValidation.setTabOrder(self.txtOData, self.txtOLabel)
        frmFECrossValidation.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFECrossValidation.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFECrossValidation.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFECrossValidation.setTabOrder(self.txtOCol, self.txtODM)
        frmFECrossValidation.setTabOrder(self.txtODM, self.txtOTask)
        frmFECrossValidation.setTabOrder(self.txtOTask, self.txtORun)
        frmFECrossValidation.setTabOrder(self.txtORun, self.txtOCounter)
        frmFECrossValidation.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFECrossValidation.setTabOrder(self.txtOCond, self.txtOScan)
        frmFECrossValidation.setTabOrder(self.txtOScan, self.txtCond)
        frmFECrossValidation.setTabOrder(self.txtCond, self.btnConvert)
        frmFECrossValidation.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFECrossValidation):
        _translate = QtCore.QCoreApplication.translate
        frmFECrossValidation.setWindowTitle(_translate("frmFECrossValidation", "Cross Validation"))
        self.btnInFile.setText(_translate("frmFECrossValidation", "..."))
        self.label_33.setText(_translate("frmFECrossValidation", "Input Data"))
        self.btnOutFile.setText(_translate("frmFECrossValidation", "..."))
        self.btnConvert.setText(_translate("frmFECrossValidation", "Convert"))
        self.label_35.setText(_translate("frmFECrossValidation", "Output Directory"))
        self.btnClose.setText(_translate("frmFECrossValidation", "Close"))
        self.txtOTask.setText(_translate("frmFECrossValidation", "task"))
        self.cbmLabel.setText(_translate("frmFECrossValidation", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFECrossValidation", "mlabel"))
        self.label_2.setText(_translate("frmFECrossValidation", "Data"))
        self.txtODM.setText(_translate("frmFECrossValidation", "design"))
        self.cbTask.setText(_translate("frmFECrossValidation", "Task"))
        self.label_3.setText(_translate("frmFECrossValidation", "Label"))
        self.cbNScan.setText(_translate("frmFECrossValidation", "NScan"))
        self.cbCond.setText(_translate("frmFECrossValidation", "Condition"))
        self.cbDM.setText(_translate("frmFECrossValidation", "Design Matrix"))
        self.cbCol.setText(_translate("frmFECrossValidation", "Coordinate"))
        self.txtOCond.setText(_translate("frmFECrossValidation", "condition"))
        self.label.setText(_translate("frmFECrossValidation", "Input"))
        self.txtOLabel.setText(_translate("frmFECrossValidation", "label"))
        self.txtOScan.setText(_translate("frmFECrossValidation", "nscan"))
        self.cbCounter.setText(_translate("frmFECrossValidation", "Counter"))
        self.txtOCol.setText(_translate("frmFECrossValidation", "coordinate"))
        self.label_5.setText(_translate("frmFECrossValidation", "Output"))
        self.txtOCounter.setText(_translate("frmFECrossValidation", "counter"))
        self.txtOSubject.setText(_translate("frmFECrossValidation", "subject"))
        self.cbRun.setText(_translate("frmFECrossValidation", "Run"))
        self.txtOData.setText(_translate("frmFECrossValidation", "data"))
        self.txtORun.setText(_translate("frmFECrossValidation", "run"))
        self.cbSubject.setText(_translate("frmFECrossValidation", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFECrossValidation", "Data"))
        self.label_4.setText(_translate("frmFECrossValidation", "Training Perfix"))
        self.txtTrain.setText(_translate("frmFECrossValidation", "train_"))
        self.txtTest.setText(_translate("frmFECrossValidation", "test_"))
        self.label_7.setText(_translate("frmFECrossValidation", "Testing Perfix"))
        self.label_8.setText(_translate("frmFECrossValidation", "Unit number for test set"))
        self.groupBox.setTitle(_translate("frmFECrossValidation", "<Fold Level>"))
        self.cbFTask.setText(_translate("frmFECrossValidation", "Task"))
        self.cbFCounter.setText(_translate("frmFECrossValidation", "Counter"))
        self.groupBox_2.setTitle(_translate("frmFECrossValidation", "<Subject Level>"))
        self.cbFSubject.setText(_translate("frmFECrossValidation", "Subject"))
        self.radioButton.setText(_translate("frmFECrossValidation", "Without Run"))
        self.rbFRun.setText(_translate("frmFECrossValidation", "With Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFECrossValidation", "Parameters"))
        self.label_36.setText(_translate("frmFECrossValidation", "Output Files"))
        self.txtOutFile.setText(_translate("frmFECrossValidation", "/data_fold$FOLD$.ezx"))
        self.label_6.setText(_translate("frmFECrossValidation", "$FOLD$ will be replaced by fold number."))
