# Form implementation generated from reading ui file 'frmFAKHAGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmFAKHA(object):
    def setupUi(self, frmFAKHA):
        frmFAKHA.setObjectName("frmFAKHA")
        frmFAKHA.resize(899, 775)
        self.btnInFile = QtWidgets.QPushButton(frmFAKHA)
        self.btnInFile.setGeometry(QtCore.QRect(820, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFAKHA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFAKHA)
        self.btnOutFile.setGeometry(QtCore.QRect(820, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFAKHA)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 651, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFAKHA)
        self.btnConvert.setGeometry(QtCore.QRect(730, 730, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFAKHA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFAKHA)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 651, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFAKHA)
        self.btnClose.setGeometry(QtCore.QRect(30, 730, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFAKHA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 841, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTrTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTrTask.setGeometry(QtCore.QRect(520, 300, 113, 21))
        self.txtOTrTask.setObjectName("txtOTrTask")
        self.txtITrmLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrmLabel.setGeometry(QtCore.QRect(180, 180, 121, 26))
        self.txtITrmLabel.setEditable(True)
        self.txtITrmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrmLabel.setObjectName("txtITrmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(20, 180, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtITrScan = QtWidgets.QComboBox(self.tab)
        self.txtITrScan.setGeometry(QtCore.QRect(180, 460, 121, 26))
        self.txtITrScan.setEditable(True)
        self.txtITrScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrScan.setObjectName("txtITrScan")
        self.txtITrTask = QtWidgets.QComboBox(self.tab)
        self.txtITrTask.setGeometry(QtCore.QRect(180, 300, 121, 26))
        self.txtITrTask.setEditable(True)
        self.txtITrTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrTask.setObjectName("txtITrTask")
        self.txtITrSubject = QtWidgets.QComboBox(self.tab)
        self.txtITrSubject.setGeometry(QtCore.QRect(180, 140, 121, 26))
        self.txtITrSubject.setEditable(True)
        self.txtITrSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrSubject.setObjectName("txtITrSubject")
        self.txtOTrmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTrmLabel.setGeometry(QtCore.QRect(520, 180, 113, 21))
        self.txtOTrmLabel.setObjectName("txtOTrmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtOTrDM = QtWidgets.QLineEdit(self.tab)
        self.txtOTrDM.setGeometry(QtCore.QRect(520, 260, 113, 21))
        self.txtOTrDM.setObjectName("txtOTrDM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(20, 300, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtITrDM = QtWidgets.QComboBox(self.tab)
        self.txtITrDM.setGeometry(QtCore.QRect(180, 260, 121, 26))
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
        self.txtCol.setGeometry(QtCore.QRect(180, 220, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        self.cbCol.setGeometry(QtCore.QRect(20, 220, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(520, 420, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtOTrLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTrLabel.setGeometry(QtCore.QRect(520, 100, 113, 21))
        self.txtOTrLabel.setObjectName("txtOTrLabel")
        self.txtITrCounter = QtWidgets.QComboBox(self.tab)
        self.txtITrCounter.setGeometry(QtCore.QRect(180, 380, 121, 26))
        self.txtITrCounter.setEditable(True)
        self.txtITrCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrCounter.setObjectName("txtITrCounter")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(180, 100, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtOTrScan = QtWidgets.QLineEdit(self.tab)
        self.txtOTrScan.setGeometry(QtCore.QRect(520, 460, 113, 21))
        self.txtOTrScan.setObjectName("txtOTrScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(20, 380, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(520, 220, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(620, 10, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(180, 60, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITrRun = QtWidgets.QComboBox(self.tab)
        self.txtITrRun.setGeometry(QtCore.QRect(180, 340, 121, 26))
        self.txtITrRun.setEditable(True)
        self.txtITrRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITrRun.setObjectName("txtITrRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(180, 420, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOTrCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOTrCounter.setGeometry(QtCore.QRect(520, 380, 113, 21))
        self.txtOTrCounter.setObjectName("txtOTrCounter")
        self.txtOTrSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOTrSubject.setGeometry(QtCore.QRect(520, 140, 113, 21))
        self.txtOTrSubject.setObjectName("txtOTrSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(20, 340, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOTrData = QtWidgets.QLineEdit(self.tab)
        self.txtOTrData.setGeometry(QtCore.QRect(520, 60, 113, 21))
        self.txtOTrData.setObjectName("txtOTrData")
        self.txtOTrRun = QtWidgets.QLineEdit(self.tab)
        self.txtOTrRun.setGeometry(QtCore.QRect(520, 340, 113, 21))
        self.txtOTrRun.setObjectName("txtOTrRun")
        self.txtITemLabel = QtWidgets.QComboBox(self.tab)
        self.txtITemLabel.setGeometry(QtCore.QRect(330, 180, 121, 26))
        self.txtITemLabel.setEditable(True)
        self.txtITemLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITemLabel.setObjectName("txtITemLabel")
        self.txtITeSubject = QtWidgets.QComboBox(self.tab)
        self.txtITeSubject.setGeometry(QtCore.QRect(330, 140, 121, 26))
        self.txtITeSubject.setEditable(True)
        self.txtITeSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeSubject.setObjectName("txtITeSubject")
        self.txtITeDM = QtWidgets.QComboBox(self.tab)
        self.txtITeDM.setGeometry(QtCore.QRect(330, 260, 121, 26))
        self.txtITeDM.setEditable(True)
        self.txtITeDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeDM.setObjectName("txtITeDM")
        self.txtITeCounter = QtWidgets.QComboBox(self.tab)
        self.txtITeCounter.setGeometry(QtCore.QRect(330, 380, 121, 26))
        self.txtITeCounter.setEditable(True)
        self.txtITeCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeCounter.setObjectName("txtITeCounter")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(330, 100, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(330, 60, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.txtITeTask = QtWidgets.QComboBox(self.tab)
        self.txtITeTask.setGeometry(QtCore.QRect(330, 300, 121, 26))
        self.txtITeTask.setEditable(True)
        self.txtITeTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeTask.setObjectName("txtITeTask")
        self.txtITeScan = QtWidgets.QComboBox(self.tab)
        self.txtITeScan.setGeometry(QtCore.QRect(330, 460, 121, 26))
        self.txtITeScan.setEditable(True)
        self.txtITeScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeScan.setObjectName("txtITeScan")
        self.txtITeRun = QtWidgets.QComboBox(self.tab)
        self.txtITeRun.setGeometry(QtCore.QRect(330, 340, 121, 26))
        self.txtITeRun.setEditable(True)
        self.txtITeRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtITeRun.setObjectName("txtITeRun")
        self.txtOTeLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTeLabel.setGeometry(QtCore.QRect(670, 100, 113, 21))
        self.txtOTeLabel.setObjectName("txtOTeLabel")
        self.txtOTeRun = QtWidgets.QLineEdit(self.tab)
        self.txtOTeRun.setGeometry(QtCore.QRect(670, 340, 113, 21))
        self.txtOTeRun.setObjectName("txtOTeRun")
        self.txtOTemLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOTemLabel.setGeometry(QtCore.QRect(670, 180, 113, 21))
        self.txtOTemLabel.setObjectName("txtOTemLabel")
        self.txtOTeDM = QtWidgets.QLineEdit(self.tab)
        self.txtOTeDM.setGeometry(QtCore.QRect(670, 260, 113, 21))
        self.txtOTeDM.setObjectName("txtOTeDM")
        self.txtOTeData = QtWidgets.QLineEdit(self.tab)
        self.txtOTeData.setGeometry(QtCore.QRect(670, 60, 113, 21))
        self.txtOTeData.setObjectName("txtOTeData")
        self.txtOTeCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOTeCounter.setGeometry(QtCore.QRect(670, 380, 113, 21))
        self.txtOTeCounter.setObjectName("txtOTeCounter")
        self.txtOTeSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOTeSubject.setGeometry(QtCore.QRect(670, 140, 113, 21))
        self.txtOTeSubject.setObjectName("txtOTeSubject")
        self.txtOTeTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTeTask.setGeometry(QtCore.QRect(670, 300, 113, 21))
        self.txtOTeTask.setObjectName("txtOTeTask")
        self.txtOTeScan = QtWidgets.QLineEdit(self.tab)
        self.txtOTeScan.setGeometry(QtCore.QRect(670, 460, 113, 21))
        self.txtOTeScan.setObjectName("txtOTeScan")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(225, 30, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(370, 30, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(555, 30, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(700, 30, 81, 16))
        self.label_10.setObjectName("label_10")
        self.cbFoldID = QtWidgets.QCheckBox(self.tab)
        self.cbFoldID.setGeometry(QtCore.QRect(20, 500, 101, 20))
        self.cbFoldID.setChecked(True)
        self.cbFoldID.setObjectName("cbFoldID")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(180, 500, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.txtOFoldID = QtWidgets.QLineEdit(self.tab)
        self.txtOFoldID.setGeometry(QtCore.QRect(520, 500, 113, 21))
        self.txtOFoldID.setObjectName("txtOFoldID")
        self.txtFoldInfo = QtWidgets.QComboBox(self.tab)
        self.txtFoldInfo.setGeometry(QtCore.QRect(180, 540, 121, 26))
        self.txtFoldInfo.setEditable(True)
        self.txtFoldInfo.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFoldInfo.setObjectName("txtFoldInfo")
        self.cbFoldInfo = QtWidgets.QCheckBox(self.tab)
        self.cbFoldInfo.setGeometry(QtCore.QRect(20, 540, 101, 20))
        self.cbFoldInfo.setChecked(True)
        self.cbFoldInfo.setObjectName("cbFoldInfo")
        self.txtOFoldInfo = QtWidgets.QLineEdit(self.tab)
        self.txtOFoldInfo.setGeometry(QtCore.QRect(520, 540, 113, 21))
        self.txtOFoldInfo.setObjectName("txtOFoldInfo")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(330, 500, 121, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 121, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 791, 80))
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 120, 791, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cbFTask = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbFTask.setGeometry(QtCore.QRect(550, 65, 111, 20))
        self.cbFTask.setObjectName("cbFTask")
        self.cbFCounter = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbFCounter.setGeometry(QtCore.QRect(670, 65, 111, 20))
        self.cbFCounter.setObjectName("cbFCounter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 531, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFSubject = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFSubject.setGeometry(QtCore.QRect(10, 30, 130, 20))
        self.cbFSubject.setChecked(True)
        self.cbFSubject.setObjectName("cbFSubject")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 30, 201, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.rbFRun = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbFRun.setGeometry(QtCore.QRect(370, 30, 141, 20))
        self.rbFRun.setObjectName("rbFRun")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(420, 300, 221, 16))
        self.label_11.setObjectName("label_11")
        self.txtRegularization = QtWidgets.QLineEdit(self.tab_2)
        self.txtRegularization.setGeometry(QtCore.QRect(650, 300, 160, 21))
        self.txtRegularization.setObjectName("txtRegularization")
        self.lblFeaNum = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum.setGeometry(QtCore.QRect(420, 260, 191, 16))
        self.lblFeaNum.setObjectName("lblFeaNum")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 221, 16))
        self.label_4.setObjectName("label_4")
        self.txtNumFea = QtWidgets.QSpinBox(self.tab_2)
        self.txtNumFea.setGeometry(QtCore.QRect(220, 260, 161, 24))
        self.txtNumFea.setMinimum(1)
        self.txtNumFea.setObjectName("txtNumFea")
        self.cbMethod = QtWidgets.QComboBox(self.tab_2)
        self.cbMethod.setGeometry(QtCore.QRect(220, 300, 161, 26))
        self.cbMethod.setObjectName("cbMethod")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(30, 300, 231, 16))
        self.label_21.setObjectName("label_21")
        self.cbKernel = QtWidgets.QComboBox(self.tab_2)
        self.cbKernel.setGeometry(QtCore.QRect(220, 340, 161, 26))
        self.cbKernel.setObjectName("cbKernel")
        self.txtCoef0 = QtWidgets.QLineEdit(self.tab_2)
        self.txtCoef0.setGeometry(QtCore.QRect(220, 460, 160, 21))
        self.txtCoef0.setObjectName("txtCoef0")
        self.txtDegree = QtWidgets.QLineEdit(self.tab_2)
        self.txtDegree.setGeometry(QtCore.QRect(220, 420, 160, 21))
        self.txtDegree.setObjectName("txtDegree")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 380, 221, 16))
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 340, 231, 16))
        self.label_18.setObjectName("label_18")
        self.txtGamma = QtWidgets.QLineEdit(self.tab_2)
        self.txtGamma.setGeometry(QtCore.QRect(220, 380, 160, 21))
        self.txtGamma.setObjectName("txtGamma")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 460, 231, 16))
        self.label_20.setObjectName("label_20")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 420, 231, 16))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(420, 460, 231, 16))
        self.label_13.setObjectName("label_13")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(420, 380, 221, 16))
        self.label_19.setObjectName("label_19")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(420, 340, 231, 16))
        self.label_16.setObjectName("label_16")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(650, 380, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(650, 420, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(420, 420, 231, 16))
        self.label_22.setObjectName("label_22")
        self.txtJobs = QtWidgets.QLineEdit(self.tab_2)
        self.txtJobs.setGeometry(QtCore.QRect(650, 460, 160, 21))
        self.txtJobs.setObjectName("txtJobs")
        self.txtBatch = QtWidgets.QSpinBox(self.tab_2)
        self.txtBatch.setGeometry(QtCore.QRect(220, 500, 161, 24))
        self.txtBatch.setMinimum(0)
        self.txtBatch.setMaximum(999999999)
        self.txtBatch.setProperty("value", 0)
        self.txtBatch.setObjectName("txtBatch")
        self.txtAlpha = QtWidgets.QLineEdit(self.tab_2)
        self.txtAlpha.setGeometry(QtCore.QRect(650, 340, 160, 21))
        self.txtAlpha.setObjectName("txtAlpha")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(30, 500, 171, 16))
        self.label_23.setObjectName("label_23")
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
        self.label_12 = QtWidgets.QLabel(frmFAKHA)
        self.label_12.setGeometry(QtCore.QRect(185, 735, 421, 20))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(frmFAKHA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFAKHA)
        frmFAKHA.setTabOrder(self.txtInFile, self.btnInFile)
        frmFAKHA.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFAKHA.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFAKHA.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFAKHA.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFAKHA.setTabOrder(self.cbmLabel, self.cbCol)
        frmFAKHA.setTabOrder(self.cbCol, self.cbDM)
        frmFAKHA.setTabOrder(self.cbDM, self.cbTask)
        frmFAKHA.setTabOrder(self.cbTask, self.cbRun)
        frmFAKHA.setTabOrder(self.cbRun, self.cbCounter)
        frmFAKHA.setTabOrder(self.cbCounter, self.cbCond)
        frmFAKHA.setTabOrder(self.cbCond, self.cbNScan)
        frmFAKHA.setTabOrder(self.cbNScan, self.txtITrData)
        frmFAKHA.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmFAKHA.setTabOrder(self.txtITrLabel, self.txtITrSubject)
        frmFAKHA.setTabOrder(self.txtITrSubject, self.txtITrmLabel)
        frmFAKHA.setTabOrder(self.txtITrmLabel, self.txtCol)
        frmFAKHA.setTabOrder(self.txtCol, self.txtITrDM)
        frmFAKHA.setTabOrder(self.txtITrDM, self.txtITrTask)
        frmFAKHA.setTabOrder(self.txtITrTask, self.txtITrRun)
        frmFAKHA.setTabOrder(self.txtITrRun, self.txtITrCounter)
        frmFAKHA.setTabOrder(self.txtITrCounter, self.txtITrScan)
        frmFAKHA.setTabOrder(self.txtITrScan, self.txtOTrData)
        frmFAKHA.setTabOrder(self.txtOTrData, self.txtOTrLabel)
        frmFAKHA.setTabOrder(self.txtOTrLabel, self.txtOTrSubject)
        frmFAKHA.setTabOrder(self.txtOTrSubject, self.txtOTrmLabel)
        frmFAKHA.setTabOrder(self.txtOTrmLabel, self.txtOCol)
        frmFAKHA.setTabOrder(self.txtOCol, self.txtOTrDM)
        frmFAKHA.setTabOrder(self.txtOTrDM, self.txtOTrTask)
        frmFAKHA.setTabOrder(self.txtOTrTask, self.txtOTrRun)
        frmFAKHA.setTabOrder(self.txtOTrRun, self.txtOTrCounter)
        frmFAKHA.setTabOrder(self.txtOTrCounter, self.txtOCond)
        frmFAKHA.setTabOrder(self.txtOCond, self.txtOTrScan)
        frmFAKHA.setTabOrder(self.txtOTrScan, self.txtCond)
        frmFAKHA.setTabOrder(self.txtCond, self.btnConvert)
        frmFAKHA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFAKHA):
        _translate = QtCore.QCoreApplication.translate
        frmFAKHA.setWindowTitle(_translate("frmFAKHA", "Kernel/SVD Hyperalignment"))
        self.btnInFile.setText(_translate("frmFAKHA", "..."))
        self.label_33.setText(_translate("frmFAKHA", "Input Data"))
        self.btnOutFile.setText(_translate("frmFAKHA", "..."))
        self.btnConvert.setText(_translate("frmFAKHA", "Alignment"))
        self.label_35.setText(_translate("frmFAKHA", "Output Data"))
        self.btnClose.setText(_translate("frmFAKHA", "Close"))
        self.txtOTrTask.setText(_translate("frmFAKHA", "train_task"))
        self.cbmLabel.setText(_translate("frmFAKHA", "Label (matrix)"))
        self.txtOTrmLabel.setText(_translate("frmFAKHA", "train_mlabel"))
        self.label_2.setText(_translate("frmFAKHA", "Data"))
        self.txtOTrDM.setText(_translate("frmFAKHA", "train_design"))
        self.cbTask.setText(_translate("frmFAKHA", "Task"))
        self.label_3.setText(_translate("frmFAKHA", "Label"))
        self.cbNScan.setText(_translate("frmFAKHA", "NScan"))
        self.cbCond.setText(_translate("frmFAKHA", "Condition"))
        self.cbDM.setText(_translate("frmFAKHA", "Design Matrix"))
        self.cbCol.setText(_translate("frmFAKHA", "Coordinate"))
        self.txtOCond.setText(_translate("frmFAKHA", "condition"))
        self.label.setText(_translate("frmFAKHA", "Input"))
        self.txtOTrLabel.setText(_translate("frmFAKHA", "train_label"))
        self.txtOTrScan.setText(_translate("frmFAKHA", "train_nscan"))
        self.cbCounter.setText(_translate("frmFAKHA", "Counter"))
        self.txtOCol.setText(_translate("frmFAKHA", "coordinate"))
        self.label_5.setText(_translate("frmFAKHA", "Output"))
        self.txtOTrCounter.setText(_translate("frmFAKHA", "train_counter"))
        self.txtOTrSubject.setText(_translate("frmFAKHA", "train_subject"))
        self.cbRun.setText(_translate("frmFAKHA", "Run"))
        self.txtOTrData.setText(_translate("frmFAKHA", "train_data"))
        self.txtOTrRun.setText(_translate("frmFAKHA", "train_run"))
        self.txtOTeLabel.setText(_translate("frmFAKHA", "test_label"))
        self.txtOTeRun.setText(_translate("frmFAKHA", "test_run"))
        self.txtOTemLabel.setText(_translate("frmFAKHA", "test_mlabel"))
        self.txtOTeDM.setText(_translate("frmFAKHA", "test_design"))
        self.txtOTeData.setText(_translate("frmFAKHA", "test_data"))
        self.txtOTeCounter.setText(_translate("frmFAKHA", "test_counter"))
        self.txtOTeSubject.setText(_translate("frmFAKHA", "test_subject"))
        self.txtOTeTask.setText(_translate("frmFAKHA", "test_task"))
        self.txtOTeScan.setText(_translate("frmFAKHA", "test_nscan"))
        self.label_7.setText(_translate("frmFAKHA", "Train"))
        self.label_8.setText(_translate("frmFAKHA", "Test"))
        self.label_9.setText(_translate("frmFAKHA", "Train"))
        self.label_10.setText(_translate("frmFAKHA", "Test"))
        self.cbFoldID.setText(_translate("frmFAKHA", "FoldID"))
        self.txtOFoldID.setText(_translate("frmFAKHA", "FoldID"))
        self.cbFoldInfo.setText(_translate("frmFAKHA", "FoldInfo"))
        self.txtOFoldInfo.setText(_translate("frmFAKHA", "FoldInfo"))
        self.lbFoldID.setText(_translate("frmFAKHA", "ID=None"))
        self.label_6.setText(_translate("frmFAKHA", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFAKHA", "Data"))
        self.groupBox.setTitle(_translate("frmFAKHA", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmFAKHA", "Scale Data X~N(0,1)"))
        self.rbScale.setText(_translate("frmFAKHA", "Subject Level"))
        self.radioButton.setText(_translate("frmFAKHA", "Whole Data"))
        self.groupBox_2.setTitle(_translate("frmFAKHA", "<Alignment Level>"))
        self.cbFTask.setText(_translate("frmFAKHA", "Task"))
        self.cbFCounter.setText(_translate("frmFAKHA", "Counter"))
        self.groupBox_3.setTitle(_translate("frmFAKHA", "<Subject Level>"))
        self.cbFSubject.setText(_translate("frmFAKHA", "Subject"))
        self.radioButton_2.setText(_translate("frmFAKHA", "Without Run"))
        self.rbFRun.setText(_translate("frmFAKHA", "With Run"))
        self.label_11.setText(_translate("frmFAKHA", "Regularization"))
        self.txtRegularization.setText(_translate("frmFAKHA", "0.0001"))
        self.lblFeaNum.setText(_translate("frmFAKHA", "No Data"))
        self.label_4.setText(_translate("frmFAKHA", "Number of features"))
        self.label_21.setText(_translate("frmFAKHA", "Method"))
        self.txtCoef0.setText(_translate("frmFAKHA", "1"))
        self.txtDegree.setText(_translate("frmFAKHA", "3"))
        self.label_14.setText(_translate("frmFAKHA", "Gamma (None=0)"))
        self.label_18.setText(_translate("frmFAKHA", "Kernel"))
        self.txtGamma.setText(_translate("frmFAKHA", "0"))
        self.label_20.setText(_translate("frmFAKHA", "Coef0"))
        self.label_15.setText(_translate("frmFAKHA", "Degree"))
        self.label_13.setText(_translate("frmFAKHA", "Number of parallel jobs"))
        self.label_19.setText(_translate("frmFAKHA", "Tolerance"))
        self.label_16.setText(_translate("frmFAKHA", "Alpha"))
        self.txtTole.setText(_translate("frmFAKHA", "0"))
        self.txtMaxIter.setText(_translate("frmFAKHA", "0"))
        self.label_22.setText(_translate("frmFAKHA", "Maximum Iterations (None=0)"))
        self.txtJobs.setText(_translate("frmFAKHA", "-1"))
        self.txtAlpha.setText(_translate("frmFAKHA", "1"))
        self.label_23.setText(_translate("frmFAKHA", "Batch Size (0 = None) "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFAKHA", "Parameters"))
        self.label_17.setText(_translate("frmFAKHA", "From:"))
        self.label_44.setText(_translate("frmFAKHA", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmFAKHA", "Fold"))
        self.label_12.setText(_translate("frmFAKHA", "$FOLD$ will be replaced by fold number."))
