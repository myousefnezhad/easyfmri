# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMAGradientEncodingAnalysisGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMAGradientEncodingAnalysis(object):
    def setupUi(self, frmMAGradientEncodingAnalysis):
        frmMAGradientEncodingAnalysis.setObjectName("frmMAGradientEncodingAnalysis")
        frmMAGradientEncodingAnalysis.resize(842, 662)
        self.btnInFile = QtWidgets.QPushButton(frmMAGradientEncodingAnalysis)
        self.btnInFile.setGeometry(QtCore.QRect(770, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMAGradientEncodingAnalysis)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.txtInFile = QtWidgets.QLineEdit(frmMAGradientEncodingAnalysis)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 581, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMAGradientEncodingAnalysis)
        self.btnConvert.setGeometry(QtCore.QRect(680, 610, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmMAGradientEncodingAnalysis)
        self.btnClose.setGeometry(QtCore.QRect(30, 610, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMAGradientEncodingAnalysis)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 791, 441))
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
        self.txtSubject.setGeometry(QtCore.QRect(180, 210, 181, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.label_6.setObjectName("label_6")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(180, 250, 181, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 60, 16))
        self.label_7.setObjectName("label_7")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(180, 290, 181, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 290, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 10, 51, 17))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 330, 131, 16))
        self.label_9.setObjectName("label_9")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(180, 330, 181, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtRunVal = QtWidgets.QComboBox(self.tab)
        self.txtRunVal.setGeometry(QtCore.QRect(400, 250, 181, 26))
        self.txtRunVal.setEditable(True)
        self.txtRunVal.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRunVal.setObjectName("txtRunVal")
        self.txtTaskVal = QtWidgets.QComboBox(self.tab)
        self.txtTaskVal.setGeometry(QtCore.QRect(400, 330, 181, 26))
        self.txtTaskVal.setEditable(True)
        self.txtTaskVal.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTaskVal.setObjectName("txtTaskVal")
        self.txtSubjectVal = QtWidgets.QComboBox(self.tab)
        self.txtSubjectVal.setGeometry(QtCore.QRect(400, 210, 181, 26))
        self.txtSubjectVal.setEditable(True)
        self.txtSubjectVal.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubjectVal.setObjectName("txtSubjectVal")
        self.txtCounterVal = QtWidgets.QComboBox(self.tab)
        self.txtCounterVal.setGeometry(QtCore.QRect(400, 250, 181, 26))
        self.txtCounterVal.setEditable(True)
        self.txtCounterVal.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounterVal.setObjectName("txtCounterVal")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(470, 10, 111, 17))
        self.label_11.setObjectName("label_11")
        self.btnRef = QtWidgets.QPushButton(self.tab)
        self.btnRef.setGeometry(QtCore.QRect(630, 370, 131, 29))
        self.btnRef.setObjectName("btnRef")
        self.txtDesign = QtWidgets.QComboBox(self.tab)
        self.txtDesign.setGeometry(QtCore.QRect(180, 130, 181, 26))
        self.txtDesign.setEditable(True)
        self.txtDesign.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDesign.setObjectName("txtDesign")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.label_12.setObjectName("label_12")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(180, 170, 181, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 751, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(False)
        self.cbScale.setObjectName("cbScale")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 250, 201, 16))
        self.label_16.setObjectName("label_16")
        self.txtIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtIter.setGeometry(QtCore.QRect(220, 250, 160, 21))
        self.txtIter.setObjectName("txtIter")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(20, 290, 201, 16))
        self.label_17.setObjectName("label_17")
        self.txtBatch = QtWidgets.QLineEdit(self.tab_2)
        self.txtBatch.setGeometry(QtCore.QRect(220, 290, 160, 21))
        self.txtBatch.setObjectName("txtBatch")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 330, 201, 16))
        self.label_18.setObjectName("label_18")
        self.txtReportStep = QtWidgets.QLineEdit(self.tab_2)
        self.txtReportStep.setGeometry(QtCore.QRect(220, 330, 160, 21))
        self.txtReportStep.setObjectName("txtReportStep")
        self.txtRate = QtWidgets.QLineEdit(self.tab_2)
        self.txtRate.setGeometry(QtCore.QRect(220, 370, 160, 21))
        self.txtRate.setObjectName("txtRate")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(20, 370, 201, 16))
        self.label_19.setObjectName("label_19")
        self.txtLParam = QtWidgets.QLineEdit(self.tab_2)
        self.txtLParam.setGeometry(QtCore.QRect(600, 130, 160, 21))
        self.txtLParam.setObjectName("txtLParam")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(400, 130, 201, 16))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(400, 170, 201, 16))
        self.label_22.setObjectName("label_22")
        self.txtEL1 = QtWidgets.QLineEdit(self.tab_2)
        self.txtEL1.setGeometry(QtCore.QRect(600, 170, 160, 21))
        self.txtEL1.setObjectName("txtEL1")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(400, 210, 201, 16))
        self.label_23.setObjectName("label_23")
        self.txtEL2 = QtWidgets.QLineEdit(self.tab_2)
        self.txtEL2.setGeometry(QtCore.QRect(600, 210, 160, 21))
        self.txtEL2.setObjectName("txtEL2")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(400, 250, 201, 16))
        self.label_24.setObjectName("label_24")
        self.txtRRP = QtWidgets.QLineEdit(self.tab_2)
        self.txtRRP.setGeometry(QtCore.QRect(600, 250, 160, 21))
        self.txtRRP.setObjectName("txtRRP")
        self.cbVerbose = QtWidgets.QCheckBox(self.tab_2)
        self.cbVerbose.setGeometry(QtCore.QRect(400, 370, 371, 20))
        self.cbVerbose.setChecked(True)
        self.cbVerbose.setObjectName("cbVerbose")
        self.cbMethod = QtWidgets.QComboBox(self.tab_2)
        self.cbMethod.setGeometry(QtCore.QRect(220, 130, 161, 26))
        self.cbMethod.setObjectName("cbMethod")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 130, 201, 16))
        self.label_13.setObjectName("label_13")
        self.cbLossType = QtWidgets.QComboBox(self.tab_2)
        self.cbLossType.setGeometry(QtCore.QRect(220, 170, 161, 26))
        self.cbLossType.setObjectName("cbLossType")
        self.cbOptim = QtWidgets.QComboBox(self.tab_2)
        self.cbOptim.setGeometry(QtCore.QRect(220, 210, 161, 26))
        self.cbOptim.setObjectName("cbOptim")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 170, 201, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 210, 201, 16))
        self.label_15.setObjectName("label_15")
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtTitleCorr = QtWidgets.QLineEdit(self.tab_3)
        self.txtTitleCorr.setGeometry(QtCore.QRect(280, 133, 481, 35))
        self.txtTitleCorr.setObjectName("txtTitleCorr")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(30, 39, 71, 16))
        self.label_27.setObjectName("label_27")
        self.txtFontSize = QtWidgets.QSpinBox(self.tab_3)
        self.txtFontSize.setGeometry(QtCore.QRect(230, 33, 171, 35))
        self.txtFontSize.setMinimum(1)
        self.txtFontSize.setMaximum(1000)
        self.txtFontSize.setProperty("value", 14)
        self.txtFontSize.setObjectName("txtFontSize")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(30, 139, 221, 20))
        self.label_29.setObjectName("label_29")
        self.txtTitleDen = QtWidgets.QLineEdit(self.tab_3)
        self.txtTitleDen.setGeometry(QtCore.QRect(280, 184, 481, 35))
        self.txtTitleDen.setObjectName("txtTitleDen")
        self.txtTitleCov = QtWidgets.QLineEdit(self.tab_3)
        self.txtTitleCov.setGeometry(QtCore.QRect(280, 83, 481, 35))
        self.txtTitleCov.setObjectName("txtTitleCov")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(30, 190, 221, 20))
        self.label_30.setObjectName("label_30")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(30, 90, 221, 20))
        self.label_28.setObjectName("label_28")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_35 = QtWidgets.QLabel(frmMAGradientEncodingAnalysis)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMAGradientEncodingAnalysis)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 60, 581, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnOutFile = QtWidgets.QPushButton(frmMAGradientEncodingAnalysis)
        self.btnOutFile.setGeometry(QtCore.QRect(770, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.cbDiagram = QtWidgets.QCheckBox(frmMAGradientEncodingAnalysis)
        self.cbDiagram.setGeometry(QtCore.QRect(30, 100, 341, 22))
        self.cbDiagram.setChecked(True)
        self.cbDiagram.setObjectName("cbDiagram")
        self.cbBeta = QtWidgets.QCheckBox(frmMAGradientEncodingAnalysis)
        self.cbBeta.setGeometry(QtCore.QRect(250, 100, 341, 22))
        self.cbBeta.setChecked(True)
        self.cbBeta.setObjectName("cbBeta")
        self.btnRedraw = QtWidgets.QPushButton(frmMAGradientEncodingAnalysis)
        self.btnRedraw.setGeometry(QtCore.QRect(520, 610, 141, 32))
        self.btnRedraw.setObjectName("btnRedraw")
        self.label_26 = QtWidgets.QLabel(frmMAGradientEncodingAnalysis)
        self.label_26.setGeometry(QtCore.QRect(510, 100, 81, 16))
        self.label_26.setObjectName("label_26")
        self.cbDevice = QtWidgets.QComboBox(frmMAGradientEncodingAnalysis)
        self.cbDevice.setGeometry(QtCore.QRect(590, 100, 171, 26))
        self.cbDevice.setObjectName("cbDevice")

        self.retranslateUi(frmMAGradientEncodingAnalysis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMAGradientEncodingAnalysis)
        frmMAGradientEncodingAnalysis.setTabOrder(self.txtInFile, self.btnInFile)
        frmMAGradientEncodingAnalysis.setTabOrder(self.btnInFile, self.tabWidget)
        frmMAGradientEncodingAnalysis.setTabOrder(self.tabWidget, self.txtData)
        frmMAGradientEncodingAnalysis.setTabOrder(self.txtData, self.txtLabel)
        frmMAGradientEncodingAnalysis.setTabOrder(self.txtLabel, self.btnConvert)
        frmMAGradientEncodingAnalysis.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMAGradientEncodingAnalysis):
        _translate = QtCore.QCoreApplication.translate
        frmMAGradientEncodingAnalysis.setWindowTitle(_translate("frmMAGradientEncodingAnalysis", "Gradient RAS"))
        self.btnInFile.setText(_translate("frmMAGradientEncodingAnalysis", "..."))
        self.label_33.setText(_translate("frmMAGradientEncodingAnalysis", "Input Data "))
        self.btnConvert.setText(_translate("frmMAGradientEncodingAnalysis", "Analyze"))
        self.btnClose.setText(_translate("frmMAGradientEncodingAnalysis", "Close"))
        self.label_2.setText(_translate("frmMAGradientEncodingAnalysis", "Data"))
        self.label_3.setText(_translate("frmMAGradientEncodingAnalysis", "Label"))
        self.label_6.setText(_translate("frmMAGradientEncodingAnalysis", "Subject"))
        self.label_7.setText(_translate("frmMAGradientEncodingAnalysis", "Run"))
        self.label_8.setText(_translate("frmMAGradientEncodingAnalysis", "Counter"))
        self.label.setText(_translate("frmMAGradientEncodingAnalysis", "ID"))
        self.label_9.setText(_translate("frmMAGradientEncodingAnalysis", "Task"))
        self.label_11.setText(_translate("frmMAGradientEncodingAnalysis", "Value"))
        self.btnRef.setText(_translate("frmMAGradientEncodingAnalysis", "Referesh"))
        self.label_12.setText(_translate("frmMAGradientEncodingAnalysis", "Design"))
        self.label_31.setText(_translate("frmMAGradientEncodingAnalysis", "Condition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMAGradientEncodingAnalysis", "Data"))
        self.groupBox.setTitle(_translate("frmMAGradientEncodingAnalysis", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMAGradientEncodingAnalysis", "Scale Data~N(0,1)"))
        self.label_16.setText(_translate("frmMAGradientEncodingAnalysis", "Epoch"))
        self.txtIter.setText(_translate("frmMAGradientEncodingAnalysis", "10"))
        self.label_17.setText(_translate("frmMAGradientEncodingAnalysis", "Batch Size"))
        self.txtBatch.setText(_translate("frmMAGradientEncodingAnalysis", "10"))
        self.label_18.setText(_translate("frmMAGradientEncodingAnalysis", "Report Step every"))
        self.txtReportStep.setText(_translate("frmMAGradientEncodingAnalysis", "2"))
        self.txtRate.setText(_translate("frmMAGradientEncodingAnalysis", "0.1"))
        self.label_19.setText(_translate("frmMAGradientEncodingAnalysis", "Learning Rate"))
        self.txtLParam.setText(_translate("frmMAGradientEncodingAnalysis", "1"))
        self.label_20.setText(_translate("frmMAGradientEncodingAnalysis", "LASSO Alpha"))
        self.label_22.setText(_translate("frmMAGradientEncodingAnalysis", "Elastic L1 ratio"))
        self.txtEL1.setText(_translate("frmMAGradientEncodingAnalysis", "0.5"))
        self.label_23.setText(_translate("frmMAGradientEncodingAnalysis", "Elastic Alpha"))
        self.txtEL2.setText(_translate("frmMAGradientEncodingAnalysis", "1"))
        self.label_24.setText(_translate("frmMAGradientEncodingAnalysis", "Ridge Regression Param"))
        self.txtRRP.setText(_translate("frmMAGradientEncodingAnalysis", "1"))
        self.cbVerbose.setText(_translate("frmMAGradientEncodingAnalysis", "Verbose"))
        self.label_13.setText(_translate("frmMAGradientEncodingAnalysis", "Method"))
        self.label_14.setText(_translate("frmMAGradientEncodingAnalysis", "Loss Type"))
        self.label_15.setText(_translate("frmMAGradientEncodingAnalysis", "Optimization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMAGradientEncodingAnalysis", "Parameters"))
        self.label_4.setText(_translate("frmMAGradientEncodingAnalysis", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMAGradientEncodingAnalysis", "0"))
        self.label_5.setText(_translate("frmMAGradientEncodingAnalysis", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMAGradientEncodingAnalysis", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMAGradientEncodingAnalysis", "Filter Class ID"))
        self.cbCov.setText(_translate("frmMAGradientEncodingAnalysis", "Covariance"))
        self.cbCorr.setText(_translate("frmMAGradientEncodingAnalysis", "Correlation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMAGradientEncodingAnalysis", "Metrics"))
        self.label_27.setText(_translate("frmMAGradientEncodingAnalysis", "Font Size"))
        self.label_29.setText(_translate("frmMAGradientEncodingAnalysis", "Figure Title: Corr (Null = Auto)"))
        self.label_30.setText(_translate("frmMAGradientEncodingAnalysis", "Figure Title: Den (Null = Auto)"))
        self.label_28.setText(_translate("frmMAGradientEncodingAnalysis", "Figure Title: Cov (Null = Auto)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMAGradientEncodingAnalysis", "Options"))
        self.label_35.setText(_translate("frmMAGradientEncodingAnalysis", "Output Data"))
        self.btnOutFile.setText(_translate("frmMAGradientEncodingAnalysis", "..."))
        self.cbDiagram.setText(_translate("frmMAGradientEncodingAnalysis", "Show Diagrams"))
        self.cbBeta.setText(_translate("frmMAGradientEncodingAnalysis", "Save Beta and Eps Values"))
        self.btnRedraw.setText(_translate("frmMAGradientEncodingAnalysis", "Redraw"))
        self.label_26.setText(_translate("frmMAGradientEncodingAnalysis", "Device"))

