# Form implementation generated from reading ui file 'frmFELDAGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmFELDA(object):
    def setupUi(self, frmFELDA):
        frmFELDA.setObjectName("frmFELDA")
        frmFELDA.resize(782, 775)
        self.btnInFile = QtWidgets.QPushButton(frmFELDA)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFELDA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFELDA)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFELDA)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 541, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFELDA)
        self.btnConvert.setGeometry(QtCore.QRect(620, 730, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFELDA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFELDA)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 541, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFELDA)
        self.btnClose.setGeometry(QtCore.QRect(30, 730, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFELDA)
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
        self.cbSubject = QtWidgets.QCheckBox(self.tab)
        self.cbSubject.setGeometry(QtCore.QRect(20, 140, 111, 20))
        self.cbSubject.setObjectName("cbSubject")
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.txtNumFea = QtWidgets.QSpinBox(self.tab_2)
        self.txtNumFea.setGeometry(QtCore.QRect(260, 120, 161, 24))
        self.txtNumFea.setMinimum(1)
        self.txtNumFea.setObjectName("txtNumFea")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_4.setObjectName("label_4")
        self.lblFeaNum = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum.setGeometry(QtCore.QRect(440, 120, 191, 16))
        self.lblFeaNum.setObjectName("lblFeaNum")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 641, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(30, 160, 231, 16))
        self.label_12.setObjectName("label_12")
        self.cbSolver = QtWidgets.QComboBox(self.tab_2)
        self.cbSolver.setGeometry(QtCore.QRect(260, 160, 361, 26))
        self.cbSolver.setObjectName("cbSolver")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(31, 200, 221, 16))
        self.label_11.setObjectName("label_11")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(261, 200, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(80, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(250, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(190, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_6 = QtWidgets.QLabel(frmFELDA)
        self.label_6.setGeometry(QtCore.QRect(190, 736, 421, 20))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(frmFELDA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFELDA)
        frmFELDA.setTabOrder(self.txtInFile, self.btnInFile)
        frmFELDA.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFELDA.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFELDA.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFELDA.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFELDA.setTabOrder(self.cbmLabel, self.cbCol)
        frmFELDA.setTabOrder(self.cbCol, self.cbDM)
        frmFELDA.setTabOrder(self.cbDM, self.cbTask)
        frmFELDA.setTabOrder(self.cbTask, self.cbRun)
        frmFELDA.setTabOrder(self.cbRun, self.cbCounter)
        frmFELDA.setTabOrder(self.cbCounter, self.cbCond)
        frmFELDA.setTabOrder(self.cbCond, self.cbNScan)
        frmFELDA.setTabOrder(self.cbNScan, self.txtITrData)
        frmFELDA.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmFELDA.setTabOrder(self.txtITrLabel, self.txtITrSubject)
        frmFELDA.setTabOrder(self.txtITrSubject, self.txtITrmLabel)
        frmFELDA.setTabOrder(self.txtITrmLabel, self.txtCol)
        frmFELDA.setTabOrder(self.txtCol, self.txtITrDM)
        frmFELDA.setTabOrder(self.txtITrDM, self.txtITrTask)
        frmFELDA.setTabOrder(self.txtITrTask, self.txtITrRun)
        frmFELDA.setTabOrder(self.txtITrRun, self.txtITrCounter)
        frmFELDA.setTabOrder(self.txtITrCounter, self.txtITrScan)
        frmFELDA.setTabOrder(self.txtITrScan, self.txtOTrData)
        frmFELDA.setTabOrder(self.txtOTrData, self.txtOTrLabel)
        frmFELDA.setTabOrder(self.txtOTrLabel, self.txtOTrSubject)
        frmFELDA.setTabOrder(self.txtOTrSubject, self.txtOTrmLabel)
        frmFELDA.setTabOrder(self.txtOTrmLabel, self.txtOCol)
        frmFELDA.setTabOrder(self.txtOCol, self.txtOTrDM)
        frmFELDA.setTabOrder(self.txtOTrDM, self.txtOTrTask)
        frmFELDA.setTabOrder(self.txtOTrTask, self.txtOTrRun)
        frmFELDA.setTabOrder(self.txtOTrRun, self.txtOTrCounter)
        frmFELDA.setTabOrder(self.txtOTrCounter, self.txtOCond)
        frmFELDA.setTabOrder(self.txtOCond, self.txtOTrScan)
        frmFELDA.setTabOrder(self.txtOTrScan, self.txtCond)
        frmFELDA.setTabOrder(self.txtCond, self.cbScale)
        frmFELDA.setTabOrder(self.cbScale, self.txtNumFea)
        frmFELDA.setTabOrder(self.txtNumFea, self.btnConvert)
        frmFELDA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFELDA):
        _translate = QtCore.QCoreApplication.translate
        frmFELDA.setWindowTitle(_translate("frmFELDA", "Linear Discriminant Analysis (LDA)"))
        self.btnInFile.setText(_translate("frmFELDA", "..."))
        self.label_33.setText(_translate("frmFELDA", "Input Data"))
        self.btnOutFile.setText(_translate("frmFELDA", "..."))
        self.btnConvert.setText(_translate("frmFELDA", "Convert"))
        self.label_35.setText(_translate("frmFELDA", "Output Data"))
        self.btnClose.setText(_translate("frmFELDA", "Close"))
        self.txtOTrTask.setText(_translate("frmFELDA", "train_task"))
        self.cbmLabel.setText(_translate("frmFELDA", "Label (matrix)"))
        self.txtOTrmLabel.setText(_translate("frmFELDA", "train_mlabel"))
        self.label_2.setText(_translate("frmFELDA", "Data"))
        self.txtOTrDM.setText(_translate("frmFELDA", "train_design"))
        self.cbTask.setText(_translate("frmFELDA", "Task"))
        self.label_3.setText(_translate("frmFELDA", "Label"))
        self.cbNScan.setText(_translate("frmFELDA", "NScan"))
        self.cbCond.setText(_translate("frmFELDA", "Condition"))
        self.cbDM.setText(_translate("frmFELDA", "Design Matrix"))
        self.cbCol.setText(_translate("frmFELDA", "Coordinate"))
        self.txtOCond.setText(_translate("frmFELDA", "condition"))
        self.label.setText(_translate("frmFELDA", "Input"))
        self.txtOTrLabel.setText(_translate("frmFELDA", "train_label"))
        self.txtOTrScan.setText(_translate("frmFELDA", "train_nscan"))
        self.cbCounter.setText(_translate("frmFELDA", "Counter"))
        self.txtOCol.setText(_translate("frmFELDA", "coordinate"))
        self.label_5.setText(_translate("frmFELDA", "Output"))
        self.txtOTrCounter.setText(_translate("frmFELDA", "train_counter"))
        self.txtOTrSubject.setText(_translate("frmFELDA", "train_subject"))
        self.cbRun.setText(_translate("frmFELDA", "Run"))
        self.txtOTrData.setText(_translate("frmFELDA", "train_data"))
        self.txtOTrRun.setText(_translate("frmFELDA", "train_run"))
        self.txtOTeLabel.setText(_translate("frmFELDA", "test_label"))
        self.txtOTeRun.setText(_translate("frmFELDA", "test_run"))
        self.txtOTemLabel.setText(_translate("frmFELDA", "test_mlabel"))
        self.txtOTeDM.setText(_translate("frmFELDA", "test_design"))
        self.txtOTeData.setText(_translate("frmFELDA", "test_data"))
        self.txtOTeCounter.setText(_translate("frmFELDA", "test_counter"))
        self.txtOTeSubject.setText(_translate("frmFELDA", "test_subject"))
        self.txtOTeTask.setText(_translate("frmFELDA", "test_task"))
        self.txtOTeScan.setText(_translate("frmFELDA", "test_nscan"))
        self.label_7.setText(_translate("frmFELDA", "Train"))
        self.label_8.setText(_translate("frmFELDA", "Test"))
        self.label_9.setText(_translate("frmFELDA", "Train"))
        self.label_10.setText(_translate("frmFELDA", "Test"))
        self.cbSubject.setText(_translate("frmFELDA", "Subject"))
        self.cbFoldID.setText(_translate("frmFELDA", "FoldID"))
        self.txtOFoldID.setText(_translate("frmFELDA", "FoldID"))
        self.cbFoldInfo.setText(_translate("frmFELDA", "FoldInfo"))
        self.txtOFoldInfo.setText(_translate("frmFELDA", "FoldInfo"))
        self.lbFoldID.setText(_translate("frmFELDA", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFELDA", "Data"))
        self.label_4.setText(_translate("frmFELDA", "Number of features"))
        self.lblFeaNum.setText(_translate("frmFELDA", "No Data"))
        self.groupBox.setTitle(_translate("frmFELDA", "<Input Data>"))
        self.cbScale.setText(_translate("frmFELDA", "Scale Whole Data X~N(0,1)"))
        self.label_12.setText(_translate("frmFELDA", "Solver"))
        self.label_11.setText(_translate("frmFELDA", "Tolerance"))
        self.txtTole.setText(_translate("frmFELDA", "0.0001"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFELDA", "Parameters"))
        self.label_17.setText(_translate("frmFELDA", "From:"))
        self.label_44.setText(_translate("frmFELDA", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmFELDA", "Fold"))
        self.label_6.setText(_translate("frmFELDA", "$FOLD$ will be replaced by fold number."))
