# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMAGradientRSAGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmMAGradientRSA(object):
    def setupUi(self, frmMAGradientRSA):
        frmMAGradientRSA.setObjectName("frmMAGradientRSA")
        frmMAGradientRSA.resize(857, 723)
        self.btnInFile = QtWidgets.QPushButton(frmMAGradientRSA)
        self.btnInFile.setGeometry(QtCore.QRect(790, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMAGradientRSA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.txtInFile = QtWidgets.QLineEdit(frmMAGradientRSA)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 601, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMAGradientRSA)
        self.btnConvert.setGeometry(QtCore.QRect(690, 670, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmMAGradientRSA)
        self.btnClose.setGeometry(QtCore.QRect(30, 670, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMAGradientRSA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 130, 801, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.label_3.setObjectName("label_3")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(180, 90, 181, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(180, 50, 181, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(180, 170, 181, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_6.setObjectName("label_6")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(180, 210, 181, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 60, 16))
        self.label_7.setObjectName("label_7")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(180, 250, 181, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 10, 51, 17))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 131, 16))
        self.label_9.setObjectName("label_9")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(180, 290, 181, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtDesign = QtWidgets.QComboBox(self.tab)
        self.txtDesign.setGeometry(QtCore.QRect(180, 130, 181, 26))
        self.txtDesign.setEditable(True)
        self.txtDesign.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDesign.setObjectName("txtDesign")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.label_12.setObjectName("label_12")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(20, 330, 131, 16))
        self.label_31.setObjectName("label_31")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(180, 330, 181, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 30, 451, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFSubject = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFSubject.setGeometry(QtCore.QRect(10, 30, 130, 20))
        self.cbFSubject.setChecked(False)
        self.cbFSubject.setObjectName("cbFSubject")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.rbFRun = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbFRun.setGeometry(QtCore.QRect(220, 60, 221, 20))
        self.rbFRun.setObjectName("rbFRun")
        self.cbFTask = QtWidgets.QCheckBox(self.tab_3)
        self.cbFTask.setGeometry(QtCore.QRect(510, 60, 161, 20))
        self.cbFTask.setObjectName("cbFTask")
        self.cbFCounter = QtWidgets.QCheckBox(self.tab_3)
        self.cbFCounter.setGeometry(QtCore.QRect(510, 100, 161, 20))
        self.cbFCounter.setObjectName("cbFCounter")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(40, 160, 121, 16))
        self.label_11.setObjectName("label_11")
        self.txtUnit = QtWidgets.QSpinBox(self.tab_3)
        self.txtUnit.setGeometry(QtCore.QRect(160, 160, 181, 24))
        self.txtUnit.setMinimum(1)
        self.txtUnit.setMaximum(1000000000)
        self.txtUnit.setObjectName("txtUnit")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 741, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.cbScale.setChecked(False)
        self.cbScale.setObjectName("cbScale")
        self.rbScale = QtWidgets.QRadioButton(self.groupBox)
        self.rbScale.setGeometry(QtCore.QRect(190, 40, 161, 20))
        self.rbScale.setChecked(True)
        self.rbScale.setObjectName("rbScale")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 40, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 120, 741, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rbAvg = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbAvg.setGeometry(QtCore.QRect(20, 30, 116, 22))
        self.rbAvg.setChecked(True)
        self.rbAvg.setObjectName("rbAvg")
        self.rbMax = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbMax.setGeometry(QtCore.QRect(170, 30, 116, 22))
        self.rbMax.setObjectName("rbMax")
        self.rbMin = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbMin.setGeometry(QtCore.QRect(330, 30, 116, 22))
        self.rbMin.setObjectName("rbMin")
        self.txtEL1 = QtWidgets.QLineEdit(self.tab_2)
        self.txtEL1.setGeometry(QtCore.QRect(610, 250, 160, 21))
        self.txtEL1.setObjectName("txtEL1")
        self.cbVerbose = QtWidgets.QCheckBox(self.tab_2)
        self.cbVerbose.setGeometry(QtCore.QRect(410, 450, 371, 20))
        self.cbVerbose.setChecked(True)
        self.cbVerbose.setObjectName("cbVerbose")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 210, 201, 16))
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 330, 201, 16))
        self.label_16.setObjectName("label_16")
        self.txtBatch = QtWidgets.QLineEdit(self.tab_2)
        self.txtBatch.setGeometry(QtCore.QRect(230, 370, 160, 21))
        self.txtBatch.setObjectName("txtBatch")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(410, 250, 201, 16))
        self.label_22.setObjectName("label_22")
        self.txtLParam = QtWidgets.QLineEdit(self.tab_2)
        self.txtLParam.setGeometry(QtCore.QRect(610, 210, 160, 21))
        self.txtLParam.setObjectName("txtLParam")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 410, 201, 16))
        self.label_18.setObjectName("label_18")
        self.cbLossType = QtWidgets.QComboBox(self.tab_2)
        self.cbLossType.setGeometry(QtCore.QRect(230, 250, 161, 26))
        self.cbLossType.setObjectName("cbLossType")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 370, 201, 16))
        self.label_17.setObjectName("label_17")
        self.txtEL2 = QtWidgets.QLineEdit(self.tab_2)
        self.txtEL2.setGeometry(QtCore.QRect(610, 290, 160, 21))
        self.txtEL2.setObjectName("txtEL2")
        self.txtRRP = QtWidgets.QLineEdit(self.tab_2)
        self.txtRRP.setGeometry(QtCore.QRect(610, 330, 160, 21))
        self.txtRRP.setObjectName("txtRRP")
        self.txtIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtIter.setGeometry(QtCore.QRect(230, 330, 160, 21))
        self.txtIter.setObjectName("txtIter")
        self.cbMethod = QtWidgets.QComboBox(self.tab_2)
        self.cbMethod.setGeometry(QtCore.QRect(230, 210, 161, 26))
        self.cbMethod.setObjectName("cbMethod")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 450, 201, 16))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(410, 290, 201, 16))
        self.label_23.setObjectName("label_23")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 290, 201, 16))
        self.label_15.setObjectName("label_15")
        self.txtReportStep = QtWidgets.QLineEdit(self.tab_2)
        self.txtReportStep.setGeometry(QtCore.QRect(230, 410, 160, 21))
        self.txtReportStep.setObjectName("txtReportStep")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 250, 201, 16))
        self.label_14.setObjectName("label_14")
        self.txtRate = QtWidgets.QLineEdit(self.tab_2)
        self.txtRate.setGeometry(QtCore.QRect(230, 450, 160, 21))
        self.txtRate.setObjectName("txtRate")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(410, 210, 201, 16))
        self.label_20.setObjectName("label_20")
        self.cbOptim = QtWidgets.QComboBox(self.tab_2)
        self.cbOptim.setGeometry(QtCore.QRect(230, 290, 161, 26))
        self.cbOptim.setObjectName("cbOptim")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(410, 330, 201, 16))
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_4)
        self.txtFilter.setGeometry(QtCore.QRect(190, 30, 291, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 211, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.tab_4)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 91, 221))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbCov = QtWidgets.QCheckBox(self.tab_5)
        self.cbCov.setGeometry(QtCore.QRect(20, 30, 391, 20))
        self.cbCov.setChecked(True)
        self.cbCov.setObjectName("cbCov")
        self.cbCorr = QtWidgets.QCheckBox(self.tab_5)
        self.cbCorr.setGeometry(QtCore.QRect(20, 70, 391, 20))
        self.cbCorr.setChecked(True)
        self.cbCorr.setObjectName("cbCorr")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.txtTitleCorr = QtWidgets.QLineEdit(self.tab_6)
        self.txtTitleCorr.setGeometry(QtCore.QRect(280, 133, 481, 35))
        self.txtTitleCorr.setObjectName("txtTitleCorr")
        self.txtFontSize = QtWidgets.QSpinBox(self.tab_6)
        self.txtFontSize.setGeometry(QtCore.QRect(230, 33, 171, 35))
        self.txtFontSize.setMinimum(1)
        self.txtFontSize.setMaximum(1000)
        self.txtFontSize.setProperty("value", 14)
        self.txtFontSize.setObjectName("txtFontSize")
        self.label_29 = QtWidgets.QLabel(self.tab_6)
        self.label_29.setGeometry(QtCore.QRect(30, 139, 221, 20))
        self.label_29.setObjectName("label_29")
        self.txtTitleDen = QtWidgets.QLineEdit(self.tab_6)
        self.txtTitleDen.setGeometry(QtCore.QRect(280, 184, 481, 35))
        self.txtTitleDen.setObjectName("txtTitleDen")
        self.label_28 = QtWidgets.QLabel(self.tab_6)
        self.label_28.setGeometry(QtCore.QRect(30, 90, 221, 20))
        self.label_28.setObjectName("label_28")
        self.txtTitleCov = QtWidgets.QLineEdit(self.tab_6)
        self.txtTitleCov.setGeometry(QtCore.QRect(280, 83, 481, 35))
        self.txtTitleCov.setObjectName("txtTitleCov")
        self.label_27 = QtWidgets.QLabel(self.tab_6)
        self.label_27.setGeometry(QtCore.QRect(30, 39, 71, 16))
        self.label_27.setObjectName("label_27")
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setGeometry(QtCore.QRect(30, 190, 221, 20))
        self.label_30.setObjectName("label_30")
        self.tabWidget.addTab(self.tab_6, "")
        self.label_35 = QtWidgets.QLabel(frmMAGradientRSA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMAGradientRSA)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 60, 601, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnOutFile = QtWidgets.QPushButton(frmMAGradientRSA)
        self.btnOutFile.setGeometry(QtCore.QRect(790, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.cbDiagram = QtWidgets.QCheckBox(frmMAGradientRSA)
        self.cbDiagram.setGeometry(QtCore.QRect(30, 90, 341, 22))
        self.cbDiagram.setChecked(True)
        self.cbDiagram.setObjectName("cbDiagram")
        self.cbBeta = QtWidgets.QCheckBox(frmMAGradientRSA)
        self.cbBeta.setGeometry(QtCore.QRect(250, 90, 341, 22))
        self.cbBeta.setChecked(True)
        self.cbBeta.setObjectName("cbBeta")
        self.btnRedraw = QtWidgets.QPushButton(frmMAGradientRSA)
        self.btnRedraw.setGeometry(QtCore.QRect(530, 670, 141, 32))
        self.btnRedraw.setObjectName("btnRedraw")
        self.cbDevice = QtWidgets.QComboBox(frmMAGradientRSA)
        self.cbDevice.setGeometry(QtCore.QRect(610, 90, 171, 26))
        self.cbDevice.setObjectName("cbDevice")
        self.label_26 = QtWidgets.QLabel(frmMAGradientRSA)
        self.label_26.setGeometry(QtCore.QRect(530, 90, 81, 16))
        self.label_26.setObjectName("label_26")

        self.retranslateUi(frmMAGradientRSA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMAGradientRSA)
        frmMAGradientRSA.setTabOrder(self.txtInFile, self.btnInFile)
        frmMAGradientRSA.setTabOrder(self.btnInFile, self.tabWidget)
        frmMAGradientRSA.setTabOrder(self.tabWidget, self.txtData)
        frmMAGradientRSA.setTabOrder(self.txtData, self.txtLabel)
        frmMAGradientRSA.setTabOrder(self.txtLabel, self.btnConvert)
        frmMAGradientRSA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMAGradientRSA):
        _translate = QtCore.QCoreApplication.translate
        frmMAGradientRSA.setWindowTitle(_translate("frmMAGradientRSA", "RAS"))
        self.btnInFile.setText(_translate("frmMAGradientRSA", "..."))
        self.label_33.setText(_translate("frmMAGradientRSA", "Input Data "))
        self.btnConvert.setText(_translate("frmMAGradientRSA", "Analyze"))
        self.btnClose.setText(_translate("frmMAGradientRSA", "Close"))
        self.label_2.setText(_translate("frmMAGradientRSA", "Data"))
        self.label_3.setText(_translate("frmMAGradientRSA", "Label"))
        self.label_6.setText(_translate("frmMAGradientRSA", "Subject"))
        self.label_7.setText(_translate("frmMAGradientRSA", "Run"))
        self.label_8.setText(_translate("frmMAGradientRSA", "Counter"))
        self.label.setText(_translate("frmMAGradientRSA", "ID"))
        self.label_9.setText(_translate("frmMAGradientRSA", "Task"))
        self.label_12.setText(_translate("frmMAGradientRSA", "Design"))
        self.label_31.setText(_translate("frmMAGradientRSA", "Condition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMAGradientRSA", "Data"))
        self.groupBox_3.setTitle(_translate("frmMAGradientRSA", "<Subject Level>"))
        self.cbFSubject.setText(_translate("frmMAGradientRSA", "Subject"))
        self.radioButton.setText(_translate("frmMAGradientRSA", "Without Run"))
        self.rbFRun.setText(_translate("frmMAGradientRSA", "With Run"))
        self.cbFTask.setText(_translate("frmMAGradientRSA", "Task"))
        self.cbFCounter.setText(_translate("frmMAGradientRSA", "Counter"))
        self.label_11.setText(_translate("frmMAGradientRSA", "Unit number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMAGradientRSA", "Level"))
        self.groupBox.setTitle(_translate("frmMAGradientRSA", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMAGradientRSA", "Scale Data~N(0,1)"))
        self.rbScale.setText(_translate("frmMAGradientRSA", "Session Level"))
        self.radioButton_2.setText(_translate("frmMAGradientRSA", "Whole Data"))
        self.groupBox_2.setTitle(_translate("frmMAGradientRSA", "<Integration Metric>"))
        self.rbAvg.setText(_translate("frmMAGradientRSA", "Average"))
        self.rbMax.setText(_translate("frmMAGradientRSA", "Max"))
        self.rbMin.setText(_translate("frmMAGradientRSA", "Min"))
        self.txtEL1.setText(_translate("frmMAGradientRSA", "0.5"))
        self.cbVerbose.setText(_translate("frmMAGradientRSA", "Verbose"))
        self.label_13.setText(_translate("frmMAGradientRSA", "Method"))
        self.label_16.setText(_translate("frmMAGradientRSA", "Epoch"))
        self.txtBatch.setText(_translate("frmMAGradientRSA", "10"))
        self.label_22.setText(_translate("frmMAGradientRSA", "Elastic Lambda 1"))
        self.txtLParam.setText(_translate("frmMAGradientRSA", "1"))
        self.label_18.setText(_translate("frmMAGradientRSA", "Report Step every"))
        self.label_17.setText(_translate("frmMAGradientRSA", "Batch Size"))
        self.txtEL2.setText(_translate("frmMAGradientRSA", "1"))
        self.txtRRP.setText(_translate("frmMAGradientRSA", "1"))
        self.txtIter.setText(_translate("frmMAGradientRSA", "10"))
        self.label_19.setText(_translate("frmMAGradientRSA", "Learning Rate"))
        self.label_23.setText(_translate("frmMAGradientRSA", "Elastic Alpha"))
        self.label_15.setText(_translate("frmMAGradientRSA", "Optimization"))
        self.txtReportStep.setText(_translate("frmMAGradientRSA", "2"))
        self.label_14.setText(_translate("frmMAGradientRSA", "Loss Type"))
        self.txtRate.setText(_translate("frmMAGradientRSA", "0.1"))
        self.label_20.setText(_translate("frmMAGradientRSA", "LASSO Alpha"))
        self.label_24.setText(_translate("frmMAGradientRSA", "Ridge Regression Param"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMAGradientRSA", "Parameters"))
        self.label_4.setText(_translate("frmMAGradientRSA", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMAGradientRSA", "0"))
        self.label_5.setText(_translate("frmMAGradientRSA", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMAGradientRSA", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMAGradientRSA", "Filter Class ID"))
        self.cbCov.setText(_translate("frmMAGradientRSA", "Covariance"))
        self.cbCorr.setText(_translate("frmMAGradientRSA", "Correlation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMAGradientRSA", "Metrics"))
        self.label_29.setText(_translate("frmMAGradientRSA", "Figure Title: Corr (Null = Auto)"))
        self.label_28.setText(_translate("frmMAGradientRSA", "Figure Title: Cov (Null = Auto)"))
        self.label_27.setText(_translate("frmMAGradientRSA", "Font Size"))
        self.label_30.setText(_translate("frmMAGradientRSA", "Figure Title: Den (Null = Auto)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("frmMAGradientRSA", "Options"))
        self.label_35.setText(_translate("frmMAGradientRSA", "Output Data"))
        self.btnOutFile.setText(_translate("frmMAGradientRSA", "..."))
        self.cbDiagram.setText(_translate("frmMAGradientRSA", "Show Diagrams"))
        self.cbBeta.setText(_translate("frmMAGradientRSA", "Save Beta Values"))
        self.btnRedraw.setText(_translate("frmMAGradientRSA", "Redraw"))
        self.label_26.setText(_translate("frmMAGradientRSA", "Device"))

