# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmAAVoxelSelectionGUI.ui'
#
# Created by: PyQt6 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmAAVoxelSelection(object):
    def setupUi(self, frmAAVoxelSelection):
        frmAAVoxelSelection.setObjectName("frmAAVoxelSelection")
        frmAAVoxelSelection.resize(749, 714)
        self.centralwidget = QtWidgets.QWidget(frmAAVoxelSelection)
        self.centralwidget.setObjectName("centralwidget")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(20, 670, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_35.setObjectName("label_35")
        self.btnOutFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutFile.setGeometry(QtCore.QRect(680, 100, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnInFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnInFile.setGeometry(QtCore.QRect(680, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 140, 701, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 210, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 210, 111, 20))
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
        self.txtSubject.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOmLabel.setGeometry(QtCore.QRect(420, 210, 113, 21))
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
        self.txtCol.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
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
        self.txtOCol.setGeometry(QtCore.QRect(420, 130, 113, 21))
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
        self.txtOSubject.setGeometry(QtCore.QRect(420, 170, 113, 21))
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
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(140, 130, 101, 16))
        self.label_8.setObjectName("label_8")
        self.cbSubject = QtWidgets.QCheckBox(self.tab)
        self.cbSubject.setGeometry(QtCore.QRect(140, 170, 111, 20))
        self.cbSubject.setObjectName("cbSubject")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 681, 71))
        self.groupBox.setObjectName("groupBox")
        self.btnAcc = QtWidgets.QPushButton(self.groupBox)
        self.btnAcc.setGeometry(QtCore.QRect(180, 30, 141, 32))
        self.btnAcc.setObjectName("btnAcc")
        self.btnMask = QtWidgets.QPushButton(self.groupBox)
        self.btnMask.setGeometry(QtCore.QRect(20, 30, 141, 32))
        self.btnMask.setObjectName("btnMask")
        self.txtAcc = QtWidgets.QLineEdit(self.groupBox)
        self.txtAcc.setGeometry(QtCore.QRect(550, 30, 111, 23))
        self.txtAcc.setObjectName("txtAcc")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(450, 30, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 111, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(400, 98, 101, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.btnAdd = QtWidgets.QPushButton(self.tab_2)
        self.btnAdd.setGeometry(QtCore.QRect(330, 240, 41, 32))
        self.btnAdd.setObjectName("btnAdd")
        self.btnRemove = QtWidgets.QPushButton(self.tab_2)
        self.btnRemove.setGeometry(QtCore.QRect(330, 290, 41, 32))
        self.btnRemove.setObjectName("btnRemove")
        self.vwAvai = QtWidgets.QTableWidget(self.tab_2)
        self.vwAvai.setGeometry(QtCore.QRect(10, 131, 298, 351))
        self.vwAvai.setObjectName("vwAvai")
        self.vwAvai.setColumnCount(0)
        self.vwAvai.setRowCount(0)
        self.vwSele = QtWidgets.QTableWidget(self.tab_2)
        self.vwSele.setGeometry(QtCore.QRect(390, 131, 298, 351))
        self.vwSele.setObjectName("vwSele")
        self.vwSele.setColumnCount(0)
        self.vwSele.setRowCount(0)
        self.btnAvaiR = QtWidgets.QPushButton(self.tab_2)
        self.btnAvaiR.setGeometry(QtCore.QRect(270, 100, 31, 23))
        self.btnAvaiR.setObjectName("btnAvaiR")
        self.btnAvaiP = QtWidgets.QPushButton(self.tab_2)
        self.btnAvaiP.setGeometry(QtCore.QRect(230, 100, 31, 23))
        self.btnAvaiP.setObjectName("btnAvaiP")
        self.btnSeleR = QtWidgets.QPushButton(self.tab_2)
        self.btnSeleR.setGeometry(QtCore.QRect(655, 100, 31, 23))
        self.btnSeleR.setObjectName("btnSeleR")
        self.btnSeleP = QtWidgets.QPushButton(self.tab_2)
        self.btnSeleP.setGeometry(QtCore.QRect(615, 100, 31, 23))
        self.btnSeleP.setObjectName("btnSeleP")
        self.btnAvaiDS = QtWidgets.QPushButton(self.tab_2)
        self.btnAvaiDS.setGeometry(QtCore.QRect(190, 100, 31, 23))
        self.btnAvaiDS.setObjectName("btnAvaiDS")
        self.btnAvaiSA = QtWidgets.QPushButton(self.tab_2)
        self.btnAvaiSA.setGeometry(QtCore.QRect(150, 100, 31, 23))
        self.btnAvaiSA.setObjectName("btnAvaiSA")
        self.btnSeleDS = QtWidgets.QPushButton(self.tab_2)
        self.btnSeleDS.setGeometry(QtCore.QRect(575, 100, 31, 23))
        self.btnSeleDS.setObjectName("btnSeleDS")
        self.btnSeleSA = QtWidgets.QPushButton(self.tab_2)
        self.btnSeleSA.setGeometry(QtCore.QRect(536, 100, 31, 23))
        self.btnSeleSA.setObjectName("btnSeleSA")
        self.tabWidget.addTab(self.tab_2, "")
        self.txtInFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInFile.setGeometry(QtCore.QRect(150, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(580, 670, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.txtOutFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOutFile.setGeometry(QtCore.QRect(150, 100, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.txtAnFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAnFile.setGeometry(QtCore.QRect(150, 60, 521, 21))
        self.txtAnFile.setText("")
        self.txtAnFile.setObjectName("txtAnFile")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_34.setObjectName("label_34")
        self.btnAnFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnFile.setGeometry(QtCore.QRect(680, 60, 51, 32))
        self.btnAnFile.setObjectName("btnAnFile")
        self.btnVBA = QtWidgets.QPushButton(self.centralwidget)
        self.btnVBA.setGeometry(QtCore.QRect(430, 670, 141, 32))
        self.btnVBA.setObjectName("btnVBA")
        self.btnVBATemp = QtWidgets.QPushButton(self.centralwidget)
        self.btnVBATemp.setGeometry(QtCore.QRect(220, 670, 201, 32))
        self.btnVBATemp.setObjectName("btnVBATemp")
        frmAAVoxelSelection.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmAAVoxelSelection)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmAAVoxelSelection)

    def retranslateUi(self, frmAAVoxelSelection):
        _translate = QtCore.QCoreApplication.translate
        frmAAVoxelSelection.setWindowTitle(_translate("frmAAVoxelSelection", "MainWindow"))
        self.btnClose.setText(_translate("frmAAVoxelSelection", "Close"))
        self.label_35.setText(_translate("frmAAVoxelSelection", "Output Data"))
        self.btnOutFile.setText(_translate("frmAAVoxelSelection", "..."))
        self.label_33.setText(_translate("frmAAVoxelSelection", "Input Data"))
        self.btnInFile.setText(_translate("frmAAVoxelSelection", "..."))
        self.txtOTask.setText(_translate("frmAAVoxelSelection", "task"))
        self.cbmLabel.setText(_translate("frmAAVoxelSelection", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmAAVoxelSelection", "mlabel"))
        self.label_2.setText(_translate("frmAAVoxelSelection", "Data"))
        self.txtODM.setText(_translate("frmAAVoxelSelection", "design"))
        self.cbTask.setText(_translate("frmAAVoxelSelection", "Task"))
        self.label_3.setText(_translate("frmAAVoxelSelection", "Label"))
        self.cbNScan.setText(_translate("frmAAVoxelSelection", "NScan"))
        self.cbCond.setText(_translate("frmAAVoxelSelection", "Condition"))
        self.cbDM.setText(_translate("frmAAVoxelSelection", "Design Matrix"))
        self.txtOCond.setText(_translate("frmAAVoxelSelection", "condition"))
        self.label.setText(_translate("frmAAVoxelSelection", "Input"))
        self.txtOLabel.setText(_translate("frmAAVoxelSelection", "label"))
        self.txtOScan.setText(_translate("frmAAVoxelSelection", "nscan"))
        self.cbCounter.setText(_translate("frmAAVoxelSelection", "Counter"))
        self.txtOCol.setText(_translate("frmAAVoxelSelection", "coordinate"))
        self.label_5.setText(_translate("frmAAVoxelSelection", "Output"))
        self.txtOCounter.setText(_translate("frmAAVoxelSelection", "counter"))
        self.txtOSubject.setText(_translate("frmAAVoxelSelection", "subject"))
        self.cbRun.setText(_translate("frmAAVoxelSelection", "Run"))
        self.txtOData.setText(_translate("frmAAVoxelSelection", "data"))
        self.txtORun.setText(_translate("frmAAVoxelSelection", "run"))
        self.label_8.setText(_translate("frmAAVoxelSelection", "Coordinate"))
        self.cbSubject.setText(_translate("frmAAVoxelSelection", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmAAVoxelSelection", "Data"))
        self.groupBox.setTitle(_translate("frmAAVoxelSelection", "<Filter>"))
        self.btnAcc.setText(_translate("frmAAVoxelSelection", "Based on accuracy"))
        self.btnMask.setText(_translate("frmAAVoxelSelection", "Based on mask"))
        self.label_6.setText(_translate("frmAAVoxelSelection", "Min Accuracy:"))
        self.label_4.setText(_translate("frmAAVoxelSelection", "Available Loci"))
        self.label_7.setText(_translate("frmAAVoxelSelection", "Selected Loci"))
        self.btnAdd.setText(_translate("frmAAVoxelSelection", ">"))
        self.btnRemove.setText(_translate("frmAAVoxelSelection", "<"))
        self.btnAvaiR.setText(_translate("frmAAVoxelSelection", "R"))
        self.btnAvaiP.setText(_translate("frmAAVoxelSelection", "P"))
        self.btnSeleR.setText(_translate("frmAAVoxelSelection", "R"))
        self.btnSeleP.setText(_translate("frmAAVoxelSelection", "P"))
        self.btnAvaiDS.setText(_translate("frmAAVoxelSelection", "DS"))
        self.btnAvaiSA.setText(_translate("frmAAVoxelSelection", "SA"))
        self.btnSeleDS.setText(_translate("frmAAVoxelSelection", "DS"))
        self.btnSeleSA.setText(_translate("frmAAVoxelSelection", "SA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmAAVoxelSelection", "Selected Voxel"))
        self.btnConvert.setText(_translate("frmAAVoxelSelection", "Convert"))
        self.label_34.setText(_translate("frmAAVoxelSelection", "Input Voxel Analysis"))
        self.btnAnFile.setText(_translate("frmAAVoxelSelection", "..."))
        self.btnVBA.setText(_translate("frmAAVoxelSelection", "Voxel Analysis"))
        self.btnVBATemp.setText(_translate("frmAAVoxelSelection", "Make Empty Coordinates"))

