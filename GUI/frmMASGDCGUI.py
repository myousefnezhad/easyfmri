# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMASGDCGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMASGDC(object):
    def setupUi(self, frmMASGDC):
        frmMASGDC.setObjectName("frmMASGDC")
        frmMASGDC.resize(869, 698)
        self.btnInFile = QtWidgets.QPushButton(frmMASGDC)
        self.btnInFile.setGeometry(QtCore.QRect(800, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMASGDC)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmMASGDC)
        self.btnOutFile.setGeometry(QtCore.QRect(800, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmMASGDC)
        self.txtInFile.setGeometry(QtCore.QRect(210, 20, 581, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMASGDC)
        self.btnConvert.setGeometry(QtCore.QRect(700, 645, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMASGDC)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 211, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMASGDC)
        self.txtOutFile.setGeometry(QtCore.QRect(210, 60, 581, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMASGDC)
        self.btnClose.setGeometry(QtCore.QRect(30, 645, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMASGDC)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 811, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(360, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(240, 110, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(240, 70, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(390, 110, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(390, 70, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(285, 40, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(240, 150, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(390, 150, 251, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 761, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtPowert = QtWidgets.QLineEdit(self.tab_2)
        self.txtPowert.setGeometry(QtCore.QRect(620, 200, 160, 21))
        self.txtPowert.setObjectName("txtPowert")
        self.cbWarmStart = QtWidgets.QCheckBox(self.tab_2)
        self.cbWarmStart.setGeometry(QtCore.QRect(240, 360, 191, 20))
        self.cbWarmStart.setChecked(False)
        self.cbWarmStart.setObjectName("cbWarmStart")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(430, 240, 181, 16))
        self.label_22.setObjectName("label_22")
        self.txtNJobs = QtWidgets.QLineEdit(self.tab_2)
        self.txtNJobs.setGeometry(QtCore.QRect(620, 320, 160, 21))
        self.txtNJobs.setObjectName("txtNJobs")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(430, 160, 181, 16))
        self.label_20.setObjectName("label_20")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(40, 240, 191, 16))
        self.label_24.setObjectName("label_24")
        self.txtL1Rate = QtWidgets.QLineEdit(self.tab_2)
        self.txtL1Rate.setGeometry(QtCore.QRect(620, 160, 160, 21))
        self.txtL1Rate.setObjectName("txtL1Rate")
        self.cbAverageParm = QtWidgets.QCheckBox(self.tab_2)
        self.cbAverageParm.setGeometry(QtCore.QRect(40, 360, 191, 20))
        self.cbAverageParm.setChecked(False)
        self.cbAverageParm.setObjectName("cbAverageParm")
        self.cbFitIntercept = QtWidgets.QCheckBox(self.tab_2)
        self.cbFitIntercept.setGeometry(QtCore.QRect(240, 400, 191, 20))
        self.cbFitIntercept.setChecked(True)
        self.cbFitIntercept.setObjectName("cbFitIntercept")
        self.cbLearningRate = QtWidgets.QComboBox(self.tab_2)
        self.cbLearningRate.setGeometry(QtCore.QRect(240, 160, 161, 26))
        self.cbLearningRate.setObjectName("cbLearningRate")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(40, 320, 191, 16))
        self.label_28.setObjectName("label_28")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(430, 280, 181, 16))
        self.label_25.setObjectName("label_25")
        self.txtAlpha = QtWidgets.QLineEdit(self.tab_2)
        self.txtAlpha.setGeometry(QtCore.QRect(620, 240, 160, 21))
        self.txtAlpha.setObjectName("txtAlpha")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(430, 200, 181, 16))
        self.label_23.setObjectName("label_23")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(40, 120, 191, 16))
        self.label_19.setObjectName("label_19")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(240, 240, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.cbLoss = QtWidgets.QComboBox(self.tab_2)
        self.cbLoss.setGeometry(QtCore.QRect(240, 120, 161, 26))
        self.cbLoss.setObjectName("cbLoss")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(430, 360, 191, 16))
        self.label_30.setObjectName("label_30")
        self.txtEta0 = QtWidgets.QLineEdit(self.tab_2)
        self.txtEta0.setGeometry(QtCore.QRect(240, 200, 160, 21))
        self.txtEta0.setObjectName("txtEta0")
        self.txtVerbose = QtWidgets.QLineEdit(self.tab_2)
        self.txtVerbose.setGeometry(QtCore.QRect(240, 280, 160, 21))
        self.txtVerbose.setObjectName("txtVerbose")
        self.txtTol = QtWidgets.QLineEdit(self.tab_2)
        self.txtTol.setGeometry(QtCore.QRect(620, 280, 160, 21))
        self.txtTol.setObjectName("txtTol")
        self.cbPenalty = QtWidgets.QComboBox(self.tab_2)
        self.cbPenalty.setGeometry(QtCore.QRect(620, 120, 161, 26))
        self.cbPenalty.setObjectName("cbPenalty")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(430, 120, 181, 16))
        self.label_13.setObjectName("label_13")
        self.cbShuffle = QtWidgets.QCheckBox(self.tab_2)
        self.cbShuffle.setGeometry(QtCore.QRect(40, 400, 191, 20))
        self.cbShuffle.setChecked(True)
        self.cbShuffle.setObjectName("cbShuffle")
        self.txtEpochs = QtWidgets.QLineEdit(self.tab_2)
        self.txtEpochs.setGeometry(QtCore.QRect(240, 320, 160, 21))
        self.txtEpochs.setObjectName("txtEpochs")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(40, 200, 191, 16))
        self.label_15.setObjectName("label_15")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(40, 160, 191, 16))
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(40, 280, 191, 16))
        self.label_27.setObjectName("label_27")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(430, 320, 181, 16))
        self.label_26.setObjectName("label_26")
        self.txtEpsilon = QtWidgets.QLineEdit(self.tab_2)
        self.txtEpsilon.setGeometry(QtCore.QRect(620, 360, 160, 21))
        self.txtEpsilon.setObjectName("txtEpsilon")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(100, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(270, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(210, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 771, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtFilter.setGeometry(QtCore.QRect(190, 40, 441, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(640, 40, 111, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 231, 121))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 771, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFilterTrID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTrID.setGeometry(QtCore.QRect(20, 40, 191, 21))
        self.cbFilterTrID.setObjectName("cbFilterTrID")
        self.txtFilterTrID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTrID.setGeometry(QtCore.QRect(190, 40, 231, 26))
        self.txtFilterTrID.setEditable(True)
        self.txtFilterTrID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFilterTrID.setObjectName("txtFilterTrID")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(640, 80, 111, 16))
        self.label_11.setObjectName("label_11")
        self.txtFilterTrContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTrContent.setGeometry(QtCore.QRect(190, 80, 441, 21))
        self.txtFilterTrContent.setText("")
        self.txtFilterTrContent.setObjectName("txtFilterTrContent")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(640, 160, 111, 16))
        self.label_14.setObjectName("label_14")
        self.cbFilterTeID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTeID.setGeometry(QtCore.QRect(20, 120, 191, 21))
        self.cbFilterTeID.setObjectName("cbFilterTeID")
        self.txtFilterTeContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTeContent.setGeometry(QtCore.QRect(190, 160, 441, 21))
        self.txtFilterTeContent.setText("")
        self.txtFilterTeContent.setObjectName("txtFilterTeContent")
        self.txtFilterTeID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTeID.setGeometry(QtCore.QRect(190, 120, 231, 26))
        self.txtFilterTeID.setEditable(True)
        self.txtFilterTeID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFilterTeID.setObjectName("txtFilterTeID")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(20, 160, 201, 16))
        self.label_16.setObjectName("label_16")
        self.btnShowFilterContent = QtWidgets.QPushButton(self.groupBox_3)
        self.btnShowFilterContent.setGeometry(QtCore.QRect(620, 40, 141, 23))
        self.btnShowFilterContent.setObjectName("btnShowFilterContent")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbAverage = QtWidgets.QCheckBox(self.tab_5)
        self.cbAverage.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.cbAverage.setChecked(True)
        self.cbAverage.setObjectName("cbAverage")
        self.cbPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbPrecision.setGeometry(QtCore.QRect(20, 70, 181, 20))
        self.cbPrecision.setChecked(True)
        self.cbPrecision.setObjectName("cbPrecision")
        self.cbPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbPrecisionAvg.setGeometry(QtCore.QRect(240, 70, 321, 26))
        self.cbPrecisionAvg.setObjectName("cbPrecisionAvg")
        self.cbAPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbAPrecisionAvg.setGeometry(QtCore.QRect(240, 110, 321, 26))
        self.cbAPrecisionAvg.setObjectName("cbAPrecisionAvg")
        self.cbAPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbAPrecision.setGeometry(QtCore.QRect(20, 110, 231, 20))
        self.cbAPrecision.setChecked(False)
        self.cbAPrecision.setObjectName("cbAPrecision")
        self.cbRecallAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbRecallAvg.setGeometry(QtCore.QRect(240, 150, 321, 26))
        self.cbRecallAvg.setObjectName("cbRecallAvg")
        self.cbRecall = QtWidgets.QCheckBox(self.tab_5)
        self.cbRecall.setGeometry(QtCore.QRect(20, 150, 181, 20))
        self.cbRecall.setChecked(True)
        self.cbRecall.setObjectName("cbRecall")
        self.cbF1 = QtWidgets.QCheckBox(self.tab_5)
        self.cbF1.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.cbF1.setChecked(True)
        self.cbF1.setObjectName("cbF1")
        self.cbF1Avg = QtWidgets.QComboBox(self.tab_5)
        self.cbF1Avg.setGeometry(QtCore.QRect(240, 190, 321, 26))
        self.cbF1Avg.setObjectName("cbF1Avg")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_12 = QtWidgets.QLabel(frmMASGDC)
        self.label_12.setGeometry(QtCore.QRect(185, 650, 501, 20))
        self.label_12.setObjectName("label_12")
        self.btnOutModel = QtWidgets.QPushButton(frmMASGDC)
        self.btnOutModel.setGeometry(QtCore.QRect(800, 100, 51, 32))
        self.btnOutModel.setObjectName("btnOutModel")
        self.label_36 = QtWidgets.QLabel(frmMASGDC)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 231, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutModel = QtWidgets.QLineEdit(frmMASGDC)
        self.txtOutModel.setGeometry(QtCore.QRect(210, 100, 581, 21))
        self.txtOutModel.setText("")
        self.txtOutModel.setObjectName("txtOutModel")

        self.retranslateUi(frmMASGDC)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMASGDC)
        frmMASGDC.setTabOrder(self.txtInFile, self.btnInFile)
        frmMASGDC.setTabOrder(self.btnInFile, self.txtOutFile)
        frmMASGDC.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmMASGDC.setTabOrder(self.btnOutFile, self.tabWidget)
        frmMASGDC.setTabOrder(self.tabWidget, self.txtITrData)
        frmMASGDC.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmMASGDC.setTabOrder(self.txtITrLabel, self.btnConvert)
        frmMASGDC.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMASGDC):
        _translate = QtCore.QCoreApplication.translate
        frmMASGDC.setWindowTitle(_translate("frmMASGDC", "Stochastic Gradient Descent Classification"))
        self.btnInFile.setText(_translate("frmMASGDC", "..."))
        self.label_33.setText(_translate("frmMASGDC", "Input Data (per fold)"))
        self.btnOutFile.setText(_translate("frmMASGDC", "..."))
        self.btnConvert.setText(_translate("frmMASGDC", "Analyze"))
        self.label_35.setText(_translate("frmMASGDC", "Analysis Results"))
        self.btnClose.setText(_translate("frmMASGDC", "Close"))
        self.label_2.setText(_translate("frmMASGDC", "Data"))
        self.label_3.setText(_translate("frmMASGDC", "Label"))
        self.label.setText(_translate("frmMASGDC", "Input"))
        self.label_7.setText(_translate("frmMASGDC", "Train"))
        self.label_8.setText(_translate("frmMASGDC", "Test"))
        self.label_9.setText(_translate("frmMASGDC", "FoldID"))
        self.lbFoldID.setText(_translate("frmMASGDC", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMASGDC", "Data"))
        self.groupBox.setTitle(_translate("frmMASGDC", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMASGDC", "Scale Data Train~N(0,1) and Test~N(0,1)"))
        self.txtPowert.setText(_translate("frmMASGDC", "0.5"))
        self.cbWarmStart.setText(_translate("frmMASGDC", "Warm Start"))
        self.label_22.setText(_translate("frmMASGDC", "Alpha"))
        self.txtNJobs.setText(_translate("frmMASGDC", "1"))
        self.label_20.setText(_translate("frmMASGDC", "L1 Ratio"))
        self.label_24.setText(_translate("frmMASGDC", "Max Iteration"))
        self.txtL1Rate.setText(_translate("frmMASGDC", "0.15"))
        self.cbAverageParm.setText(_translate("frmMASGDC", "Average"))
        self.cbFitIntercept.setText(_translate("frmMASGDC", "Fit Intercept"))
        self.label_28.setText(_translate("frmMASGDC", "Num Iter No Change"))
        self.label_25.setText(_translate("frmMASGDC", "Tolerance (None=0)"))
        self.txtAlpha.setText(_translate("frmMASGDC", "0.0001"))
        self.label_23.setText(_translate("frmMASGDC", "power_t"))
        self.label_19.setText(_translate("frmMASGDC", "Loss"))
        self.txtMaxIter.setText(_translate("frmMASGDC", "1000"))
        self.label_30.setText(_translate("frmMASGDC", "Epsilon"))
        self.txtEta0.setText(_translate("frmMASGDC", "0"))
        self.txtVerbose.setText(_translate("frmMASGDC", "0"))
        self.txtTol.setText(_translate("frmMASGDC", "0.0001"))
        self.label_13.setText(_translate("frmMASGDC", "Penalty"))
        self.cbShuffle.setText(_translate("frmMASGDC", "Shuffle"))
        self.txtEpochs.setText(_translate("frmMASGDC", "5"))
        self.label_15.setText(_translate("frmMASGDC", "eta0"))
        self.label_21.setText(_translate("frmMASGDC", "Learning Rate"))
        self.label_27.setText(_translate("frmMASGDC", "Verbose"))
        self.label_26.setText(_translate("frmMASGDC", "n_jobs (All = -1)"))
        self.txtEpsilon.setText(_translate("frmMASGDC", "0.1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMASGDC", "Parameters"))
        self.label_17.setText(_translate("frmMASGDC", "From:"))
        self.label_44.setText(_translate("frmMASGDC", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMASGDC", "Fold"))
        self.groupBox_2.setTitle(_translate("frmMASGDC", "<Filter based on Class ID>"))
        self.label_10.setText(_translate("frmMASGDC", "Existed Classes"))
        self.label_4.setText(_translate("frmMASGDC", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMASGDC", "0"))
        self.label_5.setText(_translate("frmMASGDC", "e.g. 0 or [1,2]"))
        self.groupBox_3.setTitle(_translate("frmMASGDC", "<Based on a reference>"))
        self.cbFilterTrID.setText(_translate("frmMASGDC", "Filter training based on"))
        self.label_6.setText(_translate("frmMASGDC", "Remove training contents"))
        self.label_11.setText(_translate("frmMASGDC", "e.g. 0 or [1,2]"))
        self.label_14.setText(_translate("frmMASGDC", "e.g. 0 or [1,2]"))
        self.cbFilterTeID.setText(_translate("frmMASGDC", "Filter testing based on"))
        self.label_16.setText(_translate("frmMASGDC", "Remove testing contents"))
        self.btnShowFilterContent.setText(_translate("frmMASGDC", "Show Content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMASGDC", "Filter"))
        self.cbAverage.setText(_translate("frmMASGDC", "Average"))
        self.cbPrecision.setText(_translate("frmMASGDC", "Precision"))
        self.cbAPrecision.setText(_translate("frmMASGDC", "Average of Precision"))
        self.cbRecall.setText(_translate("frmMASGDC", "Recall"))
        self.cbF1.setText(_translate("frmMASGDC", "f1 score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMASGDC", "Metrics"))
        self.label_12.setText(_translate("frmMASGDC", "$FOLD$ will be replaced by fold number."))
        self.btnOutModel.setText(_translate("frmMASGDC", "..."))
        self.label_36.setText(_translate("frmMASGDC", "Models (per fold/opt)"))

