# Form implementation generated from reading ui file 'frmMANuSVMGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmMANuSVM(object):
    def setupUi(self, frmMANuSVM):
        frmMANuSVM.setObjectName("frmMANuSVM")
        frmMANuSVM.resize(782, 764)
        self.btnInFile = QtWidgets.QPushButton(frmMANuSVM)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMANuSVM)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 191, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmMANuSVM)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmMANuSVM)
        self.txtInFile.setGeometry(QtCore.QRect(200, 20, 501, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMANuSVM)
        self.btnConvert.setGeometry(QtCore.QRect(620, 715, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMANuSVM)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 181, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMANuSVM)
        self.txtOutFile.setGeometry(QtCore.QRect(200, 60, 501, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMANuSVM)
        self.btnClose.setGeometry(QtCore.QRect(30, 715, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMANuSVM)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 731, 551))
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
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(240, 70, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(390, 110, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(390, 70, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
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
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 671, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtGamma = QtWidgets.QLineEdit(self.tab_2)
        self.txtGamma.setGeometry(QtCore.QRect(260, 240, 160, 21))
        self.txtGamma.setObjectName("txtGamma")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(260, 400, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(260, 360, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.lblFeaNum_3 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_3.setGeometry(QtCore.QRect(440, 240, 281, 16))
        self.lblFeaNum_3.setObjectName("lblFeaNum_3")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 360, 221, 16))
        self.label_14.setObjectName("label_14")
        self.lblFeaNum_4 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_4.setGeometry(QtCore.QRect(440, 320, 271, 16))
        self.lblFeaNum_4.setObjectName("lblFeaNum_4")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 320, 231, 16))
        self.label_18.setObjectName("label_18")
        self.cbKernel = QtWidgets.QComboBox(self.tab_2)
        self.cbKernel.setGeometry(QtCore.QRect(260, 160, 161, 26))
        self.cbKernel.setObjectName("cbKernel")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 221, 16))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 280, 231, 16))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 231, 16))
        self.label_13.setObjectName("label_13")
        self.txtCoef0 = QtWidgets.QLineEdit(self.tab_2)
        self.txtCoef0.setGeometry(QtCore.QRect(260, 320, 160, 21))
        self.txtCoef0.setObjectName("txtCoef0")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 400, 251, 16))
        self.label_16.setObjectName("label_16")
        self.lblFeaNum_5 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_5.setGeometry(QtCore.QRect(440, 360, 281, 16))
        self.lblFeaNum_5.setObjectName("lblFeaNum_5")
        self.lblFeaNum_2 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_2.setGeometry(QtCore.QRect(440, 280, 281, 16))
        self.lblFeaNum_2.setObjectName("lblFeaNum_2")
        self.txtDegree = QtWidgets.QLineEdit(self.tab_2)
        self.txtDegree.setGeometry(QtCore.QRect(260, 280, 160, 21))
        self.txtDegree.setObjectName("txtDegree")
        self.cbMode = QtWidgets.QComboBox(self.tab_2)
        self.cbMode.setGeometry(QtCore.QRect(260, 120, 161, 26))
        self.cbMode.setObjectName("cbMode")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 120, 231, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 200, 221, 16))
        self.label_20.setObjectName("label_20")
        self.txtNu = QtWidgets.QLineEdit(self.tab_2)
        self.txtNu.setGeometry(QtCore.QRect(260, 200, 160, 21))
        self.txtNu.setObjectName("txtNu")
        self.cbProbablity = QtWidgets.QCheckBox(self.tab_2)
        self.cbProbablity.setGeometry(QtCore.QRect(20, 440, 641, 20))
        self.cbProbablity.setObjectName("cbProbablity")
        self.cbShrink = QtWidgets.QCheckBox(self.tab_2)
        self.cbShrink.setGeometry(QtCore.QRect(20, 480, 661, 20))
        self.cbShrink.setChecked(True)
        self.cbShrink.setObjectName("cbShrink")
        self.lblFeaNum_6 = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum_6.setGeometry(QtCore.QRect(440, 200, 281, 16))
        self.lblFeaNum_6.setObjectName("lblFeaNum_6")
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
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(15, 230, 701, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFilterTrID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTrID.setGeometry(QtCore.QRect(20, 40, 191, 21))
        self.cbFilterTrID.setObjectName("cbFilterTrID")
        self.txtFilterTrID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTrID.setGeometry(QtCore.QRect(190, 40, 231, 26))
        self.txtFilterTrID.setEditable(True)
        self.txtFilterTrID.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFilterTrID.setObjectName("txtFilterTrID")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(570, 80, 111, 16))
        self.label_21.setObjectName("label_21")
        self.txtFilterTrContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTrContent.setGeometry(QtCore.QRect(190, 80, 371, 21))
        self.txtFilterTrContent.setText("")
        self.txtFilterTrContent.setObjectName("txtFilterTrContent")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(570, 160, 111, 16))
        self.label_22.setObjectName("label_22")
        self.cbFilterTeID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTeID.setGeometry(QtCore.QRect(20, 120, 191, 21))
        self.cbFilterTeID.setObjectName("cbFilterTeID")
        self.txtFilterTeContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTeContent.setGeometry(QtCore.QRect(190, 160, 371, 21))
        self.txtFilterTeContent.setText("")
        self.txtFilterTeContent.setObjectName("txtFilterTeContent")
        self.txtFilterTeID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTeID.setGeometry(QtCore.QRect(190, 120, 231, 26))
        self.txtFilterTeID.setEditable(True)
        self.txtFilterTeID.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFilterTeID.setObjectName("txtFilterTeID")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(20, 160, 201, 16))
        self.label_23.setObjectName("label_23")
        self.btnShowFilterContent = QtWidgets.QPushButton(self.groupBox_3)
        self.btnShowFilterContent.setGeometry(QtCore.QRect(550, 40, 141, 23))
        self.btnShowFilterContent.setObjectName("btnShowFilterContent")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(15, 20, 701, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtFilter.setGeometry(QtCore.QRect(190, 40, 381, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(580, 40, 111, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 231, 121))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
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
        self.label_12 = QtWidgets.QLabel(frmMANuSVM)
        self.label_12.setGeometry(QtCore.QRect(185, 720, 421, 20))
        self.label_12.setObjectName("label_12")
        self.btnOutModel = QtWidgets.QPushButton(frmMANuSVM)
        self.btnOutModel.setGeometry(QtCore.QRect(710, 100, 51, 32))
        self.btnOutModel.setObjectName("btnOutModel")
        self.label_36 = QtWidgets.QLabel(frmMANuSVM)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 231, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutModel = QtWidgets.QLineEdit(frmMANuSVM)
        self.txtOutModel.setGeometry(QtCore.QRect(200, 100, 501, 21))
        self.txtOutModel.setText("")
        self.txtOutModel.setObjectName("txtOutModel")

        self.retranslateUi(frmMANuSVM)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMANuSVM)
        frmMANuSVM.setTabOrder(self.txtInFile, self.btnInFile)
        frmMANuSVM.setTabOrder(self.btnInFile, self.txtOutFile)
        frmMANuSVM.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmMANuSVM.setTabOrder(self.btnOutFile, self.tabWidget)
        frmMANuSVM.setTabOrder(self.tabWidget, self.txtITrData)
        frmMANuSVM.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmMANuSVM.setTabOrder(self.txtITrLabel, self.btnConvert)
        frmMANuSVM.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMANuSVM):
        _translate = QtCore.QCoreApplication.translate
        frmMANuSVM.setWindowTitle(_translate("frmMANuSVM", "Nu Support Vector Classification"))
        self.btnInFile.setText(_translate("frmMANuSVM", "..."))
        self.label_33.setText(_translate("frmMANuSVM", "Input Data (per fold)"))
        self.btnOutFile.setText(_translate("frmMANuSVM", "..."))
        self.btnConvert.setText(_translate("frmMANuSVM", "Analyze"))
        self.label_35.setText(_translate("frmMANuSVM", "Analysis Results"))
        self.btnClose.setText(_translate("frmMANuSVM", "Close"))
        self.label_2.setText(_translate("frmMANuSVM", "Data"))
        self.label_3.setText(_translate("frmMANuSVM", "Label"))
        self.label.setText(_translate("frmMANuSVM", "Input"))
        self.label_7.setText(_translate("frmMANuSVM", "Train"))
        self.label_8.setText(_translate("frmMANuSVM", "Test"))
        self.label_9.setText(_translate("frmMANuSVM", "FoldID"))
        self.lbFoldID.setText(_translate("frmMANuSVM", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMANuSVM", "Data"))
        self.groupBox.setTitle(_translate("frmMANuSVM", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMANuSVM", "Scale Data Train~N(0,1) and Test~N(0,1)"))
        self.txtGamma.setText(_translate("frmMANuSVM", "0"))
        self.txtMaxIter.setText(_translate("frmMANuSVM", "-1"))
        self.txtTole.setText(_translate("frmMANuSVM", "0.001"))
        self.lblFeaNum_3.setText(_translate("frmMANuSVM", "Coefficient for rbf, poly and sigmoid."))
        self.label_14.setText(_translate("frmMANuSVM", "Tolerance"))
        self.lblFeaNum_4.setText(_translate("frmMANuSVM", "Term in poly and sigmoid kernels. "))
        self.label_18.setText(_translate("frmMANuSVM", "Coef0"))
        self.label_11.setText(_translate("frmMANuSVM", "Gamma (Auto=0)"))
        self.label_15.setText(_translate("frmMANuSVM", "Degree"))
        self.label_13.setText(_translate("frmMANuSVM", "Kernel"))
        self.txtCoef0.setText(_translate("frmMANuSVM", "0"))
        self.label_16.setText(_translate("frmMANuSVM", "Maximum Iterations (No Limit=-1)"))
        self.lblFeaNum_5.setText(_translate("frmMANuSVM", "Tolerance for stopping criterion"))
        self.lblFeaNum_2.setText(_translate("frmMANuSVM", "Degree for poly kernels."))
        self.txtDegree.setText(_translate("frmMANuSVM", "3"))
        self.label_19.setText(_translate("frmMANuSVM", "Mode"))
        self.label_20.setText(_translate("frmMANuSVM", "Nu"))
        self.txtNu.setText(_translate("frmMANuSVM", "0.5"))
        self.cbProbablity.setText(_translate("frmMANuSVM", "Enable probability estimates"))
        self.cbShrink.setText(_translate("frmMANuSVM", "Use shrinking heuristic"))
        self.lblFeaNum_6.setText(_translate("frmMANuSVM", "Bound on fraction of errors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMANuSVM", "Parameters"))
        self.label_17.setText(_translate("frmMANuSVM", "From:"))
        self.label_44.setText(_translate("frmMANuSVM", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMANuSVM", "Fold"))
        self.groupBox_3.setTitle(_translate("frmMANuSVM", "<Based on a reference>"))
        self.cbFilterTrID.setText(_translate("frmMANuSVM", "Filter training based on"))
        self.label_6.setText(_translate("frmMANuSVM", "Remove training contents"))
        self.label_21.setText(_translate("frmMANuSVM", "e.g. 0 or [1,2]"))
        self.label_22.setText(_translate("frmMANuSVM", "e.g. 0 or [1,2]"))
        self.cbFilterTeID.setText(_translate("frmMANuSVM", "Filter testing based on"))
        self.label_23.setText(_translate("frmMANuSVM", "Remove testing contents"))
        self.btnShowFilterContent.setText(_translate("frmMANuSVM", "Show Content"))
        self.groupBox_2.setTitle(_translate("frmMANuSVM", "<Filter based on Class ID>"))
        self.label_10.setText(_translate("frmMANuSVM", "Existed Classes"))
        self.label_4.setText(_translate("frmMANuSVM", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMANuSVM", "0"))
        self.label_5.setText(_translate("frmMANuSVM", "e.g. 0 or [1,2]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMANuSVM", "Filter"))
        self.cbAverage.setText(_translate("frmMANuSVM", "Average"))
        self.cbPrecision.setText(_translate("frmMANuSVM", "Precision"))
        self.cbAPrecision.setText(_translate("frmMANuSVM", "Average of Precision"))
        self.cbRecall.setText(_translate("frmMANuSVM", "Recall"))
        self.cbF1.setText(_translate("frmMANuSVM", "f1 score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMANuSVM", "Metrics"))
        self.label_12.setText(_translate("frmMANuSVM", "$FOLD$ will be replaced by fold number."))
        self.btnOutModel.setText(_translate("frmMANuSVM", "..."))
        self.label_36.setText(_translate("frmMANuSVM", "Models (per fold/opt)"))
