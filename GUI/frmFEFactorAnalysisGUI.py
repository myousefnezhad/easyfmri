# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFEFactorAnalysisGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmFEFactorAnalysis(object):
    def setupUi(self, frmFEFactorAnalysis):
        frmFEFactorAnalysis.setObjectName("frmFEFactorAnalysis")
        frmFEFactorAnalysis.resize(758, 691)
        self.btnInFile = QtWidgets.QPushButton(frmFEFactorAnalysis)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFEFactorAnalysis)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFEFactorAnalysis)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFEFactorAnalysis)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFEFactorAnalysis)
        self.btnConvert.setGeometry(QtCore.QRect(590, 640, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFEFactorAnalysis)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFEFactorAnalysis)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFEFactorAnalysis)
        self.btnClose.setGeometry(QtCore.QRect(30, 640, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFEFactorAnalysis)
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
        self.txtNumFea = QtWidgets.QSpinBox(self.tab_2)
        self.txtNumFea.setGeometry(QtCore.QRect(260, 200, 161, 24))
        self.txtNumFea.setMinimum(1)
        self.txtNumFea.setObjectName("txtNumFea")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 141, 16))
        self.label_4.setObjectName("label_4")
        self.lblFeaNum = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum.setGeometry(QtCore.QRect(440, 200, 191, 16))
        self.lblFeaNum.setObjectName("lblFeaNum")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 641, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.rbScale = QtWidgets.QRadioButton(self.groupBox)
        self.rbScale.setGeometry(QtCore.QRect(210, 40, 161, 20))
        self.rbScale.setChecked(True)
        self.rbScale.setObjectName("rbScale")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(370, 40, 131, 20))
        self.radioButton.setObjectName("radioButton")
        self.txtPIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtPIter.setGeometry(QtCore.QRect(260, 360, 160, 21))
        self.txtPIter.setObjectName("txtPIter")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 231, 16))
        self.label_9.setObjectName("label_9")
        self.cbSVD = QtWidgets.QComboBox(self.tab_2)
        self.cbSVD.setGeometry(QtCore.QRect(260, 240, 161, 26))
        self.cbSVD.setObjectName("cbSVD")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(260, 280, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 360, 231, 16))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 280, 221, 16))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(30, 240, 231, 16))
        self.label_12.setObjectName("label_12")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(260, 320, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 100, 641, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 40, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.rbALScale = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbALScale.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.rbALScale.setChecked(True)
        self.rbALScale.setObjectName("rbALScale")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmFEFactorAnalysis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFEFactorAnalysis)
        frmFEFactorAnalysis.setTabOrder(self.txtInFile, self.btnInFile)
        frmFEFactorAnalysis.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFEFactorAnalysis.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFEFactorAnalysis.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFEFactorAnalysis.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFEFactorAnalysis.setTabOrder(self.cbmLabel, self.cbCol)
        frmFEFactorAnalysis.setTabOrder(self.cbCol, self.cbDM)
        frmFEFactorAnalysis.setTabOrder(self.cbDM, self.cbTask)
        frmFEFactorAnalysis.setTabOrder(self.cbTask, self.cbRun)
        frmFEFactorAnalysis.setTabOrder(self.cbRun, self.cbCounter)
        frmFEFactorAnalysis.setTabOrder(self.cbCounter, self.cbCond)
        frmFEFactorAnalysis.setTabOrder(self.cbCond, self.cbNScan)
        frmFEFactorAnalysis.setTabOrder(self.cbNScan, self.txtData)
        frmFEFactorAnalysis.setTabOrder(self.txtData, self.txtLabel)
        frmFEFactorAnalysis.setTabOrder(self.txtLabel, self.txtSubject)
        frmFEFactorAnalysis.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFEFactorAnalysis.setTabOrder(self.txtmLabel, self.txtCol)
        frmFEFactorAnalysis.setTabOrder(self.txtCol, self.txtDM)
        frmFEFactorAnalysis.setTabOrder(self.txtDM, self.txtTask)
        frmFEFactorAnalysis.setTabOrder(self.txtTask, self.txtRun)
        frmFEFactorAnalysis.setTabOrder(self.txtRun, self.txtCounter)
        frmFEFactorAnalysis.setTabOrder(self.txtCounter, self.txtScan)
        frmFEFactorAnalysis.setTabOrder(self.txtScan, self.txtOData)
        frmFEFactorAnalysis.setTabOrder(self.txtOData, self.txtOLabel)
        frmFEFactorAnalysis.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFEFactorAnalysis.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFEFactorAnalysis.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFEFactorAnalysis.setTabOrder(self.txtOCol, self.txtODM)
        frmFEFactorAnalysis.setTabOrder(self.txtODM, self.txtOTask)
        frmFEFactorAnalysis.setTabOrder(self.txtOTask, self.txtORun)
        frmFEFactorAnalysis.setTabOrder(self.txtORun, self.txtOCounter)
        frmFEFactorAnalysis.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFEFactorAnalysis.setTabOrder(self.txtOCond, self.txtOScan)
        frmFEFactorAnalysis.setTabOrder(self.txtOScan, self.txtCond)
        frmFEFactorAnalysis.setTabOrder(self.txtCond, self.cbScale)
        frmFEFactorAnalysis.setTabOrder(self.cbScale, self.rbScale)
        frmFEFactorAnalysis.setTabOrder(self.rbScale, self.radioButton)
        frmFEFactorAnalysis.setTabOrder(self.radioButton, self.txtNumFea)
        frmFEFactorAnalysis.setTabOrder(self.txtNumFea, self.btnConvert)
        frmFEFactorAnalysis.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFEFactorAnalysis):
        _translate = QtCore.QCoreApplication.translate
        frmFEFactorAnalysis.setWindowTitle(_translate("frmFEFactorAnalysis", "Factor Analysis"))
        self.btnInFile.setText(_translate("frmFEFactorAnalysis", "..."))
        self.label_33.setText(_translate("frmFEFactorAnalysis", "Input Data"))
        self.btnOutFile.setText(_translate("frmFEFactorAnalysis", "..."))
        self.btnConvert.setText(_translate("frmFEFactorAnalysis", "Convert"))
        self.label_35.setText(_translate("frmFEFactorAnalysis", "Output Data"))
        self.btnClose.setText(_translate("frmFEFactorAnalysis", "Close"))
        self.txtOTask.setText(_translate("frmFEFactorAnalysis", "task"))
        self.cbmLabel.setText(_translate("frmFEFactorAnalysis", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFEFactorAnalysis", "mlabel"))
        self.label_2.setText(_translate("frmFEFactorAnalysis", "Data"))
        self.txtODM.setText(_translate("frmFEFactorAnalysis", "design"))
        self.cbTask.setText(_translate("frmFEFactorAnalysis", "Task"))
        self.label_3.setText(_translate("frmFEFactorAnalysis", "Label"))
        self.cbNScan.setText(_translate("frmFEFactorAnalysis", "NScan"))
        self.cbCond.setText(_translate("frmFEFactorAnalysis", "Condition"))
        self.cbDM.setText(_translate("frmFEFactorAnalysis", "Design Matrix"))
        self.cbCol.setText(_translate("frmFEFactorAnalysis", "Coordinate"))
        self.txtOCond.setText(_translate("frmFEFactorAnalysis", "condition"))
        self.label.setText(_translate("frmFEFactorAnalysis", "Input"))
        self.txtOLabel.setText(_translate("frmFEFactorAnalysis", "label"))
        self.txtOScan.setText(_translate("frmFEFactorAnalysis", "nscan"))
        self.cbCounter.setText(_translate("frmFEFactorAnalysis", "Counter"))
        self.txtOCol.setText(_translate("frmFEFactorAnalysis", "coordinate"))
        self.label_5.setText(_translate("frmFEFactorAnalysis", "Output"))
        self.txtOCounter.setText(_translate("frmFEFactorAnalysis", "counter"))
        self.txtOSubject.setText(_translate("frmFEFactorAnalysis", "subject"))
        self.cbRun.setText(_translate("frmFEFactorAnalysis", "Run"))
        self.txtOData.setText(_translate("frmFEFactorAnalysis", "data"))
        self.txtORun.setText(_translate("frmFEFactorAnalysis", "run"))
        self.label_6.setText(_translate("frmFEFactorAnalysis", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFEFactorAnalysis", "Data"))
        self.label_4.setText(_translate("frmFEFactorAnalysis", "Number of features"))
        self.lblFeaNum.setText(_translate("frmFEFactorAnalysis", "No Data"))
        self.groupBox.setTitle(_translate("frmFEFactorAnalysis", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmFEFactorAnalysis", "Scale Data X~N(0,1)"))
        self.rbScale.setText(_translate("frmFEFactorAnalysis", "Subject Level"))
        self.radioButton.setText(_translate("frmFEFactorAnalysis", "Whole Data"))
        self.txtPIter.setText(_translate("frmFEFactorAnalysis", "3"))
        self.label_9.setText(_translate("frmFEFactorAnalysis", "Maximum Iterations"))
        self.txtTole.setText(_translate("frmFEFactorAnalysis", "0.01"))
        self.label_11.setText(_translate("frmFEFactorAnalysis", "Power Iterations"))
        self.label_10.setText(_translate("frmFEFactorAnalysis", "Tolerance"))
        self.label_12.setText(_translate("frmFEFactorAnalysis", "SVD Method"))
        self.txtMaxIter.setText(_translate("frmFEFactorAnalysis", "1000"))
        self.groupBox_2.setTitle(_translate("frmFEFactorAnalysis", "<Analysis Level>"))
        self.radioButton_2.setText(_translate("frmFEFactorAnalysis", "Whole Data"))
        self.rbALScale.setText(_translate("frmFEFactorAnalysis", "Subject Level"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFEFactorAnalysis", "Parameters"))

