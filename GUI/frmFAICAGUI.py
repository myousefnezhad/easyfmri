# Form implementation generated from reading ui file 'frmFAICAGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmFAICA(object):
    def setupUi(self, frmFAICA):
        frmFAICA.setObjectName("frmFAICA")
        frmFAICA.resize(782, 775)
        self.btnInFile = QtWidgets.QPushButton(frmFAICA)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFAICA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFAICA)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFAICA)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 541, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFAICA)
        self.btnConvert.setGeometry(QtCore.QRect(620, 730, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFAICA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFAICA)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 541, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFAICA)
        self.btnClose.setGeometry(QtCore.QRect(30, 730, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFAICA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 731, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTrTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTrTask.setGeometry(QtCore.QRect(450, 300, 113, 21))
        self.txtOTrTask.setObjectName("txtOTrTask")
        self.txtITrmLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrmLabel.setGeometry(QtCore.QRect(140, 180, 121, 26))
        self.txtITrmLabel.setEditable(True)
        self.txtITrmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrmLabel.setObjectName("txtITrmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(20, 180, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtITrScan = QtWidgets.QComboBox(self.tab)
        self.txtITrScan.setGeometry(QtCore.QRect(140, 460, 121, 26))
        self.txtITrScan.setEditable(True)
        self.txtITrScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrScan.setObjectName("txtITrScan")
        self.txtITrTask = QtWidgets.QComboBox(self.tab)
        self.txtITrTask.setGeometry(QtCore.QRect(140, 300, 121, 26))
        self.txtITrTask.setEditable(True)
        self.txtITrTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrTask.setObjectName("txtITrTask")
        self.txtITrSubject = QtWidgets.QComboBox(self.tab)
        self.txtITrSubject.setGeometry(QtCore.QRect(140, 140, 121, 26))
        self.txtITrSubject.setEditable(True)
        self.txtITrSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrSubject.setObjectName("txtITrSubject")
        self.txtOTrmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTrmLabel.setGeometry(QtCore.QRect(450, 180, 113, 21))
        self.txtOTrmLabel.setObjectName("txtOTrmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtOTrDM = QtWidgets.QLineEdit(self.tab)
        self.txtOTrDM.setGeometry(QtCore.QRect(450, 260, 113, 21))
        self.txtOTrDM.setObjectName("txtOTrDM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(20, 300, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtITrDM = QtWidgets.QComboBox(self.tab)
        self.txtITrDM.setGeometry(QtCore.QRect(140, 260, 121, 26))
        self.txtITrDM.setEditable(True)
        self.txtITrDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrDM.setObjectName("txtITrDM")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        self.cbNScan.setGeometry(QtCore.QRect(20, 460, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        self.cbCond.setGeometry(QtCore.QRect(20, 420, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbDM = QtWidgets.QCheckBox(self.tab)
        self.cbDM.setGeometry(QtCore.QRect(20, 260, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(140, 220, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        self.cbCol.setGeometry(QtCore.QRect(20, 220, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(450, 420, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtOTrLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTrLabel.setGeometry(QtCore.QRect(450, 100, 113, 21))
        self.txtOTrLabel.setObjectName("txtOTrLabel")
        self.txtITrCounter = QtWidgets.QComboBox(self.tab)
        self.txtITrCounter.setGeometry(QtCore.QRect(140, 380, 121, 26))
        self.txtITrCounter.setEditable(True)
        self.txtITrCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrCounter.setObjectName("txtITrCounter")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(140, 100, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtOTrScan = QtWidgets.QLineEdit(self.tab)
        self.txtOTrScan.setGeometry(QtCore.QRect(450, 460, 113, 21))
        self.txtOTrScan.setObjectName("txtOTrScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(20, 380, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(450, 220, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(550, 10, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(140, 60, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITrRun = QtWidgets.QComboBox(self.tab)
        self.txtITrRun.setGeometry(QtCore.QRect(140, 340, 121, 26))
        self.txtITrRun.setEditable(True)
        self.txtITrRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrRun.setObjectName("txtITrRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(140, 420, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOTrCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOTrCounter.setGeometry(QtCore.QRect(450, 380, 113, 21))
        self.txtOTrCounter.setObjectName("txtOTrCounter")
        self.txtOTrSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOTrSubject.setGeometry(QtCore.QRect(450, 140, 113, 21))
        self.txtOTrSubject.setObjectName("txtOTrSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(20, 340, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOTrData = QtWidgets.QLineEdit(self.tab)
        self.txtOTrData.setGeometry(QtCore.QRect(450, 60, 113, 21))
        self.txtOTrData.setObjectName("txtOTrData")
        self.txtOTrRun = QtWidgets.QLineEdit(self.tab)
        self.txtOTrRun.setGeometry(QtCore.QRect(450, 340, 113, 21))
        self.txtOTrRun.setObjectName("txtOTrRun")
        self.txtITemLabel = QtWidgets.QComboBox(self.tab)
        self.txtITemLabel.setGeometry(QtCore.QRect(290, 180, 121, 26))
        self.txtITemLabel.setEditable(True)
        self.txtITemLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITemLabel.setObjectName("txtITemLabel")
        self.txtITeSubject = QtWidgets.QComboBox(self.tab)
        self.txtITeSubject.setGeometry(QtCore.QRect(290, 140, 121, 26))
        self.txtITeSubject.setEditable(True)
        self.txtITeSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeSubject.setObjectName("txtITeSubject")
        self.txtITeDM = QtWidgets.QComboBox(self.tab)
        self.txtITeDM.setGeometry(QtCore.QRect(290, 260, 121, 26))
        self.txtITeDM.setEditable(True)
        self.txtITeDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeDM.setObjectName("txtITeDM")
        self.txtITeCounter = QtWidgets.QComboBox(self.tab)
        self.txtITeCounter.setGeometry(QtCore.QRect(290, 380, 121, 26))
        self.txtITeCounter.setEditable(True)
        self.txtITeCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeCounter.setObjectName("txtITeCounter")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(290, 100, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(290, 60, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.txtITeTask = QtWidgets.QComboBox(self.tab)
        self.txtITeTask.setGeometry(QtCore.QRect(290, 300, 121, 26))
        self.txtITeTask.setEditable(True)
        self.txtITeTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeTask.setObjectName("txtITeTask")
        self.txtITeScan = QtWidgets.QComboBox(self.tab)
        self.txtITeScan.setGeometry(QtCore.QRect(290, 460, 121, 26))
        self.txtITeScan.setEditable(True)
        self.txtITeScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeScan.setObjectName("txtITeScan")
        self.txtITeRun = QtWidgets.QComboBox(self.tab)
        self.txtITeRun.setGeometry(QtCore.QRect(290, 340, 121, 26))
        self.txtITeRun.setEditable(True)
        self.txtITeRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeRun.setObjectName("txtITeRun")
        self.txtOTeLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTeLabel.setGeometry(QtCore.QRect(600, 100, 113, 21))
        self.txtOTeLabel.setObjectName("txtOTeLabel")
        self.txtOTeRun = QtWidgets.QLineEdit(self.tab)
        self.txtOTeRun.setGeometry(QtCore.QRect(600, 340, 113, 21))
        self.txtOTeRun.setObjectName("txtOTeRun")
        self.txtOTemLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTemLabel.setGeometry(QtCore.QRect(600, 180, 113, 21))
        self.txtOTemLabel.setObjectName("txtOTemLabel")
        self.txtOTeDM = QtWidgets.QLineEdit(self.tab)
        self.txtOTeDM.setGeometry(QtCore.QRect(600, 260, 113, 21))
        self.txtOTeDM.setObjectName("txtOTeDM")
        self.txtOTeData = QtWidgets.QLineEdit(self.tab)
        self.txtOTeData.setGeometry(QtCore.QRect(600, 60, 113, 21))
        self.txtOTeData.setObjectName("txtOTeData")
        self.txtOTeCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOTeCounter.setGeometry(QtCore.QRect(600, 380, 113, 21))
        self.txtOTeCounter.setObjectName("txtOTeCounter")
        self.txtOTeSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOTeSubject.setGeometry(QtCore.QRect(600, 140, 113, 21))
        self.txtOTeSubject.setObjectName("txtOTeSubject")
        self.txtOTeTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTeTask.setGeometry(QtCore.QRect(600, 300, 113, 21))
        self.txtOTeTask.setObjectName("txtOTeTask")
        self.txtOTeScan = QtWidgets.QLineEdit(self.tab)
        self.txtOTeScan.setGeometry(QtCore.QRect(600, 460, 113, 21))
        self.txtOTeScan.setObjectName("txtOTeScan")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(185, 30, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(330, 30, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(485, 30, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(630, 30, 81, 16))
        self.label_10.setObjectName("label_10")
        self.cbFoldID = QtWidgets.QCheckBox(self.tab)
        self.cbFoldID.setGeometry(QtCore.QRect(20, 500, 101, 20))
        self.cbFoldID.setChecked(True)
        self.cbFoldID.setObjectName("cbFoldID")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(140, 500, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.txtOFoldID = QtWidgets.QLineEdit(self.tab)
        self.txtOFoldID.setGeometry(QtCore.QRect(450, 500, 113, 21))
        self.txtOFoldID.setObjectName("txtOFoldID")
        self.txtFoldInfo = QtWidgets.QComboBox(self.tab)
        self.txtFoldInfo.setGeometry(QtCore.QRect(140, 540, 121, 26))
        self.txtFoldInfo.setEditable(True)
        self.txtFoldInfo.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFoldInfo.setObjectName("txtFoldInfo")
        self.cbFoldInfo = QtWidgets.QCheckBox(self.tab)
        self.cbFoldInfo.setGeometry(QtCore.QRect(20, 540, 101, 20))
        self.cbFoldInfo.setChecked(True)
        self.cbFoldInfo.setObjectName("cbFoldInfo")
        self.txtOFoldInfo = QtWidgets.QLineEdit(self.tab)
        self.txtOFoldInfo.setGeometry(QtCore.QRect(450, 540, 113, 21))
        self.txtOFoldInfo.setObjectName("txtOFoldInfo")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(290, 500, 121, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 121, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 671, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(40, 170, 231, 16))
        self.label_13.setObjectName("label_13")
        self.txtNumFea = QtWidgets.QSpinBox(self.tab_2)
        self.txtNumFea.setGeometry(QtCore.QRect(270, 130, 161, 24))
        self.txtNumFea.setMinimum(1)
        self.txtNumFea.setObjectName("txtNumFea")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(40, 210, 221, 16))
        self.label_11.setObjectName("label_11")
        self.lblFeaNum = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum.setGeometry(QtCore.QRect(450, 130, 191, 16))
        self.lblFeaNum.setObjectName("lblFeaNum")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(270, 250, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(270, 210, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 141, 16))
        self.label_4.setObjectName("label_4")
        self.cbAlg = QtWidgets.QComboBox(self.tab_2)
        self.cbAlg.setGeometry(QtCore.QRect(270, 170, 161, 26))
        self.cbAlg.setObjectName("cbAlg")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(40, 250, 231, 16))
        self.label_14.setObjectName("label_14")
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
        self.label_12 = QtWidgets.QLabel(frmFAICA)
        self.label_12.setGeometry(QtCore.QRect(185, 735, 421, 20))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(frmFAICA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFAICA)
        frmFAICA.setTabOrder(self.txtInFile, self.btnInFile)
        frmFAICA.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFAICA.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFAICA.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFAICA.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFAICA.setTabOrder(self.cbmLabel, self.cbCol)
        frmFAICA.setTabOrder(self.cbCol, self.cbDM)
        frmFAICA.setTabOrder(self.cbDM, self.cbTask)
        frmFAICA.setTabOrder(self.cbTask, self.cbRun)
        frmFAICA.setTabOrder(self.cbRun, self.cbCounter)
        frmFAICA.setTabOrder(self.cbCounter, self.cbCond)
        frmFAICA.setTabOrder(self.cbCond, self.cbNScan)
        frmFAICA.setTabOrder(self.cbNScan, self.txtITrData)
        frmFAICA.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmFAICA.setTabOrder(self.txtITrLabel, self.txtITrSubject)
        frmFAICA.setTabOrder(self.txtITrSubject, self.txtITrmLabel)
        frmFAICA.setTabOrder(self.txtITrmLabel, self.txtCol)
        frmFAICA.setTabOrder(self.txtCol, self.txtITrDM)
        frmFAICA.setTabOrder(self.txtITrDM, self.txtITrTask)
        frmFAICA.setTabOrder(self.txtITrTask, self.txtITrRun)
        frmFAICA.setTabOrder(self.txtITrRun, self.txtITrCounter)
        frmFAICA.setTabOrder(self.txtITrCounter, self.txtITrScan)
        frmFAICA.setTabOrder(self.txtITrScan, self.txtOTrData)
        frmFAICA.setTabOrder(self.txtOTrData, self.txtOTrLabel)
        frmFAICA.setTabOrder(self.txtOTrLabel, self.txtOTrSubject)
        frmFAICA.setTabOrder(self.txtOTrSubject, self.txtOTrmLabel)
        frmFAICA.setTabOrder(self.txtOTrmLabel, self.txtOCol)
        frmFAICA.setTabOrder(self.txtOCol, self.txtOTrDM)
        frmFAICA.setTabOrder(self.txtOTrDM, self.txtOTrTask)
        frmFAICA.setTabOrder(self.txtOTrTask, self.txtOTrRun)
        frmFAICA.setTabOrder(self.txtOTrRun, self.txtOTrCounter)
        frmFAICA.setTabOrder(self.txtOTrCounter, self.txtOCond)
        frmFAICA.setTabOrder(self.txtOCond, self.txtOTrScan)
        frmFAICA.setTabOrder(self.txtOTrScan, self.txtCond)
        frmFAICA.setTabOrder(self.txtCond, self.btnConvert)
        frmFAICA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFAICA):
        _translate = QtCore.QCoreApplication.translate
        frmFAICA.setWindowTitle(_translate("frmFAICA", "ICA Functional Alignment"))
        self.btnInFile.setText(_translate("frmFAICA", "..."))
        self.label_33.setText(_translate("frmFAICA", "Input Data"))
        self.btnOutFile.setText(_translate("frmFAICA", "..."))
        self.btnConvert.setText(_translate("frmFAICA", "Alignment"))
        self.label_35.setText(_translate("frmFAICA", "Output Data"))
        self.btnClose.setText(_translate("frmFAICA", "Close"))
        self.txtOTrTask.setText(_translate("frmFAICA", "train_task"))
        self.cbmLabel.setText(_translate("frmFAICA", "Label (matrix)"))
        self.txtOTrmLabel.setText(_translate("frmFAICA", "train_mlabel"))
        self.label_2.setText(_translate("frmFAICA", "Data"))
        self.txtOTrDM.setText(_translate("frmFAICA", "train_design"))
        self.cbTask.setText(_translate("frmFAICA", "Task"))
        self.label_3.setText(_translate("frmFAICA", "Label"))
        self.cbNScan.setText(_translate("frmFAICA", "NScan"))
        self.cbCond.setText(_translate("frmFAICA", "Condition"))
        self.cbDM.setText(_translate("frmFAICA", "Design Matrix"))
        self.cbCol.setText(_translate("frmFAICA", "Coordinate"))
        self.txtOCond.setText(_translate("frmFAICA", "condition"))
        self.label.setText(_translate("frmFAICA", "Input"))
        self.txtOTrLabel.setText(_translate("frmFAICA", "train_label"))
        self.txtOTrScan.setText(_translate("frmFAICA", "train_nscan"))
        self.cbCounter.setText(_translate("frmFAICA", "Counter"))
        self.txtOCol.setText(_translate("frmFAICA", "coordinate"))
        self.label_5.setText(_translate("frmFAICA", "Output"))
        self.txtOTrCounter.setText(_translate("frmFAICA", "train_counter"))
        self.txtOTrSubject.setText(_translate("frmFAICA", "train_subject"))
        self.cbRun.setText(_translate("frmFAICA", "Run"))
        self.txtOTrData.setText(_translate("frmFAICA", "train_data"))
        self.txtOTrRun.setText(_translate("frmFAICA", "train_run"))
        self.txtOTeLabel.setText(_translate("frmFAICA", "test_label"))
        self.txtOTeRun.setText(_translate("frmFAICA", "test_run"))
        self.txtOTemLabel.setText(_translate("frmFAICA", "test_mlabel"))
        self.txtOTeDM.setText(_translate("frmFAICA", "test_design"))
        self.txtOTeData.setText(_translate("frmFAICA", "test_data"))
        self.txtOTeCounter.setText(_translate("frmFAICA", "test_counter"))
        self.txtOTeSubject.setText(_translate("frmFAICA", "test_subject"))
        self.txtOTeTask.setText(_translate("frmFAICA", "test_task"))
        self.txtOTeScan.setText(_translate("frmFAICA", "test_nscan"))
        self.label_7.setText(_translate("frmFAICA", "Train"))
        self.label_8.setText(_translate("frmFAICA", "Test"))
        self.label_9.setText(_translate("frmFAICA", "Train"))
        self.label_10.setText(_translate("frmFAICA", "Test"))
        self.cbFoldID.setText(_translate("frmFAICA", "FoldID"))
        self.txtOFoldID.setText(_translate("frmFAICA", "FoldID"))
        self.cbFoldInfo.setText(_translate("frmFAICA", "FoldInfo"))
        self.txtOFoldInfo.setText(_translate("frmFAICA", "FoldInfo"))
        self.lbFoldID.setText(_translate("frmFAICA", "ID=None"))
        self.label_6.setText(_translate("frmFAICA", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFAICA", "Data"))
        self.groupBox.setTitle(_translate("frmFAICA", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmFAICA", "Scale Data X~N(0,1)"))
        self.label_13.setText(_translate("frmFAICA", "Algorithm"))
        self.label_11.setText(_translate("frmFAICA", "Tolerance"))
        self.lblFeaNum.setText(_translate("frmFAICA", "No Data"))
        self.txtMaxIter.setText(_translate("frmFAICA", "1000"))
        self.txtTole.setText(_translate("frmFAICA", "0.01"))
        self.label_4.setText(_translate("frmFAICA", "Number of features"))
        self.label_14.setText(_translate("frmFAICA", "Maximum Iterations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFAICA", "Parameters"))
        self.label_17.setText(_translate("frmFAICA", "From:"))
        self.label_44.setText(_translate("frmFAICA", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmFAICA", "Fold"))
        self.label_12.setText(_translate("frmFAICA", "$FOLD$ will be replaced by fold number."))
