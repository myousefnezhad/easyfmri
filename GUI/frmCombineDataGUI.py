# Form implementation generated from reading ui file 'frmCombineDataGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmCombineData(object):
    def setupUi(self, frmCombineData):
        frmCombineData.setObjectName("frmCombineData")
        frmCombineData.resize(734, 706)
        self.txtInFFile = QtWidgets.QLineEdit(frmCombineData)
        self.txtInFFile.setGeometry(QtCore.QRect(140, 20, 521, 21))
        self.txtInFFile.setText("")
        self.txtInFFile.setObjectName("txtInFFile")
        self.label_33 = QtWidgets.QLabel(frmCombineData)
        self.label_33.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnInFFile = QtWidgets.QPushButton(frmCombineData)
        self.btnInFFile.setGeometry(QtCore.QRect(670, 20, 51, 32))
        self.btnInFFile.setObjectName("btnInFFile")
        self.txtInSFile = QtWidgets.QLineEdit(frmCombineData)
        self.txtInSFile.setGeometry(QtCore.QRect(140, 60, 521, 21))
        self.txtInSFile.setText("")
        self.txtInSFile.setObjectName("txtInSFile")
        self.label_34 = QtWidgets.QLabel(frmCombineData)
        self.label_34.setGeometry(QtCore.QRect(10, 60, 131, 16))
        self.label_34.setObjectName("label_34")
        self.btnInSFile = QtWidgets.QPushButton(frmCombineData)
        self.btnInSFile.setGeometry(QtCore.QRect(670, 60, 51, 32))
        self.btnInSFile.setObjectName("btnInSFile")
        self.label_35 = QtWidgets.QLabel(frmCombineData)
        self.label_35.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label_35.setObjectName("label_35")
        self.btnOutFile = QtWidgets.QPushButton(frmCombineData)
        self.btnOutFile.setGeometry(QtCore.QRect(670, 100, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtOutFile = QtWidgets.QLineEdit(frmCombineData)
        self.txtOutFile.setGeometry(QtCore.QRect(140, 100, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.txtFData = QtWidgets.QComboBox(frmCombineData)
        self.txtFData.setGeometry(QtCore.QRect(150, 170, 121, 26))
        self.txtFData.setEditable(True)
        self.txtFData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFData.setObjectName("txtFData")
        self.txtFLabel = QtWidgets.QComboBox(frmCombineData)
        self.txtFLabel.setGeometry(QtCore.QRect(150, 210, 121, 26))
        self.txtFLabel.setEditable(True)
        self.txtFLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFLabel.setObjectName("txtFLabel")
        self.txtFDM = QtWidgets.QComboBox(frmCombineData)
        self.txtFDM.setGeometry(QtCore.QRect(150, 330, 121, 26))
        self.txtFDM.setEditable(True)
        self.txtFDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFDM.setObjectName("txtFDM")
        self.label_3 = QtWidgets.QLabel(frmCombineData)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 60, 16))
        self.label_3.setObjectName("label_3")
        self.cbDM = QtWidgets.QCheckBox(frmCombineData)
        self.cbDM.setGeometry(QtCore.QRect(30, 330, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.label_2 = QtWidgets.QLabel(frmCombineData)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtFCol = QtWidgets.QComboBox(frmCombineData)
        self.txtFCol.setGeometry(QtCore.QRect(150, 290, 121, 26))
        self.txtFCol.setEditable(True)
        self.txtFCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFCol.setObjectName("txtFCol")
        self.cbCol = QtWidgets.QCheckBox(frmCombineData)
        self.cbCol.setGeometry(QtCore.QRect(30, 290, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.cbmLabel = QtWidgets.QCheckBox(frmCombineData)
        self.cbmLabel.setGeometry(QtCore.QRect(30, 250, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtFSubject = QtWidgets.QComboBox(frmCombineData)
        self.txtFSubject.setGeometry(QtCore.QRect(150, 370, 121, 26))
        self.txtFSubject.setEditable(True)
        self.txtFSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFSubject.setObjectName("txtFSubject")
        self.txtFTask = QtWidgets.QComboBox(frmCombineData)
        self.txtFTask.setGeometry(QtCore.QRect(150, 410, 121, 26))
        self.txtFTask.setEditable(True)
        self.txtFTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFTask.setObjectName("txtFTask")
        self.cbCond = QtWidgets.QCheckBox(frmCombineData)
        self.cbCond.setGeometry(QtCore.QRect(30, 530, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbTask = QtWidgets.QCheckBox(frmCombineData)
        self.cbTask.setGeometry(QtCore.QRect(30, 410, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtFCond = QtWidgets.QComboBox(frmCombineData)
        self.txtFCond.setGeometry(QtCore.QRect(150, 530, 121, 26))
        self.txtFCond.setEditable(True)
        self.txtFCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFCond.setObjectName("txtFCond")
        self.cbSubject = QtWidgets.QCheckBox(frmCombineData)
        self.cbSubject.setGeometry(QtCore.QRect(30, 370, 81, 20))
        self.cbSubject.setChecked(True)
        self.cbSubject.setObjectName("cbSubject")
        self.txtFCounter = QtWidgets.QComboBox(frmCombineData)
        self.txtFCounter.setGeometry(QtCore.QRect(150, 490, 121, 26))
        self.txtFCounter.setEditable(True)
        self.txtFCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFCounter.setObjectName("txtFCounter")
        self.cbCounter = QtWidgets.QCheckBox(frmCombineData)
        self.cbCounter.setGeometry(QtCore.QRect(30, 490, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.cbRun = QtWidgets.QCheckBox(frmCombineData)
        self.cbRun.setGeometry(QtCore.QRect(30, 450, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtFRun = QtWidgets.QComboBox(frmCombineData)
        self.txtFRun.setGeometry(QtCore.QRect(150, 450, 121, 26))
        self.txtFRun.setEditable(True)
        self.txtFRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFRun.setObjectName("txtFRun")
        self.cbNScan = QtWidgets.QCheckBox(frmCombineData)
        self.cbNScan.setGeometry(QtCore.QRect(30, 610, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.txtFScan = QtWidgets.QComboBox(frmCombineData)
        self.txtFScan.setGeometry(QtCore.QRect(150, 610, 121, 26))
        self.txtFScan.setEditable(True)
        self.txtFScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtFScan.setObjectName("txtFScan")
        self.txtSCond = QtWidgets.QComboBox(frmCombineData)
        self.txtSCond.setGeometry(QtCore.QRect(298, 530, 121, 26))
        self.txtSCond.setEditable(True)
        self.txtSCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSCond.setObjectName("txtSCond")
        self.txtSCounter = QtWidgets.QComboBox(frmCombineData)
        self.txtSCounter.setGeometry(QtCore.QRect(298, 490, 121, 26))
        self.txtSCounter.setEditable(True)
        self.txtSCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSCounter.setObjectName("txtSCounter")
        self.txtSSubject = QtWidgets.QComboBox(frmCombineData)
        self.txtSSubject.setGeometry(QtCore.QRect(298, 370, 121, 26))
        self.txtSSubject.setEditable(True)
        self.txtSSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSSubject.setObjectName("txtSSubject")
        self.txtSScan = QtWidgets.QComboBox(frmCombineData)
        self.txtSScan.setGeometry(QtCore.QRect(298, 610, 121, 26))
        self.txtSScan.setEditable(True)
        self.txtSScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSScan.setObjectName("txtSScan")
        self.txtSCol = QtWidgets.QComboBox(frmCombineData)
        self.txtSCol.setGeometry(QtCore.QRect(298, 290, 121, 26))
        self.txtSCol.setEditable(True)
        self.txtSCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSCol.setObjectName("txtSCol")
        self.txtSDM = QtWidgets.QComboBox(frmCombineData)
        self.txtSDM.setGeometry(QtCore.QRect(298, 330, 121, 26))
        self.txtSDM.setEditable(True)
        self.txtSDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSDM.setObjectName("txtSDM")
        self.txtSLabel = QtWidgets.QComboBox(frmCombineData)
        self.txtSLabel.setGeometry(QtCore.QRect(298, 210, 121, 26))
        self.txtSLabel.setEditable(True)
        self.txtSLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSLabel.setObjectName("txtSLabel")
        self.txtSTask = QtWidgets.QComboBox(frmCombineData)
        self.txtSTask.setGeometry(QtCore.QRect(298, 410, 121, 26))
        self.txtSTask.setEditable(True)
        self.txtSTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSTask.setObjectName("txtSTask")
        self.txtSRun = QtWidgets.QComboBox(frmCombineData)
        self.txtSRun.setGeometry(QtCore.QRect(298, 450, 121, 26))
        self.txtSRun.setEditable(True)
        self.txtSRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSRun.setObjectName("txtSRun")
        self.txtSData = QtWidgets.QComboBox(frmCombineData)
        self.txtSData.setGeometry(QtCore.QRect(298, 170, 121, 26))
        self.txtSData.setEditable(True)
        self.txtSData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSData.setObjectName("txtSData")
        self.label = QtWidgets.QLabel(frmCombineData)
        self.label.setGeometry(QtCore.QRect(180, 140, 61, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(frmCombineData)
        self.label_4.setGeometry(QtCore.QRect(320, 140, 80, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(frmCombineData)
        self.label_5.setGeometry(QtCore.QRect(480, 140, 61, 16))
        self.label_5.setObjectName("label_5")
        self.btnClose = QtWidgets.QPushButton(frmCombineData)
        self.btnClose.setGeometry(QtCore.QRect(20, 660, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.btnConvert = QtWidgets.QPushButton(frmCombineData)
        self.btnConvert.setGeometry(QtCore.QRect(570, 660, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.txtOLabel = QtWidgets.QLineEdit(frmCombineData)
        self.txtOLabel.setGeometry(QtCore.QRect(450, 210, 113, 21))
        self.txtOLabel.setObjectName("txtOLabel")
        self.txtOmLabel = QtWidgets.QLineEdit(frmCombineData)
        self.txtOmLabel.setGeometry(QtCore.QRect(450, 250, 113, 21))
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.txtOData = QtWidgets.QLineEdit(frmCombineData)
        self.txtOData.setGeometry(QtCore.QRect(450, 170, 113, 21))
        self.txtOData.setObjectName("txtOData")
        self.txtOCoI = QtWidgets.QLineEdit(frmCombineData)
        self.txtOCoI.setGeometry(QtCore.QRect(450, 290, 113, 21))
        self.txtOCoI.setObjectName("txtOCoI")
        self.txtODM = QtWidgets.QLineEdit(frmCombineData)
        self.txtODM.setGeometry(QtCore.QRect(450, 330, 113, 21))
        self.txtODM.setObjectName("txtODM")
        self.txtOSubject = QtWidgets.QLineEdit(frmCombineData)
        self.txtOSubject.setGeometry(QtCore.QRect(450, 370, 113, 21))
        self.txtOSubject.setObjectName("txtOSubject")
        self.txtORun = QtWidgets.QLineEdit(frmCombineData)
        self.txtORun.setGeometry(QtCore.QRect(450, 450, 113, 21))
        self.txtORun.setObjectName("txtORun")
        self.txtOCounter = QtWidgets.QLineEdit(frmCombineData)
        self.txtOCounter.setGeometry(QtCore.QRect(450, 490, 113, 21))
        self.txtOCounter.setObjectName("txtOCounter")
        self.txtOTask = QtWidgets.QLineEdit(frmCombineData)
        self.txtOTask.setGeometry(QtCore.QRect(450, 410, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtOCond = QtWidgets.QLineEdit(frmCombineData)
        self.txtOCond.setGeometry(QtCore.QRect(450, 530, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.txtOScan = QtWidgets.QLineEdit(frmCombineData)
        self.txtOScan.setGeometry(QtCore.QRect(450, 610, 113, 21))
        self.txtOScan.setObjectName("txtOScan")
        self.cbRelabeling = QtWidgets.QCheckBox(frmCombineData)
        self.cbRelabeling.setGeometry(QtCore.QRect(590, 210, 121, 20))
        self.cbRelabeling.setObjectName("cbRelabeling")
        self.label_28 = QtWidgets.QLabel(frmCombineData)
        self.label_28.setGeometry(QtCore.QRect(30, 570, 111, 16))
        self.label_28.setObjectName("label_28")
        self.txtOCondPre = QtWidgets.QLineEdit(frmCombineData)
        self.txtOCondPre.setGeometry(QtCore.QRect(450, 570, 113, 21))
        self.txtOCondPre.setObjectName("txtOCondPre")
        self.cbCondUnion = QtWidgets.QCheckBox(frmCombineData)
        self.cbCondUnion.setGeometry(QtCore.QRect(588, 530, 121, 20))
        self.cbCondUnion.setObjectName("cbCondUnion")
        self.txtFCondPre = QtWidgets.QLineEdit(frmCombineData)
        self.txtFCondPre.setGeometry(QtCore.QRect(150, 570, 113, 21))
        self.txtFCondPre.setObjectName("txtFCondPre")
        self.txtSCondPre = QtWidgets.QLineEdit(frmCombineData)
        self.txtSCondPre.setGeometry(QtCore.QRect(300, 570, 113, 21))
        self.txtSCondPre.setObjectName("txtSCondPre")

        self.retranslateUi(frmCombineData)
        QtCore.QMetaObject.connectSlotsByName(frmCombineData)
        frmCombineData.setTabOrder(self.txtInFFile, self.btnInFFile)
        frmCombineData.setTabOrder(self.btnInFFile, self.txtInSFile)
        frmCombineData.setTabOrder(self.txtInSFile, self.btnInSFile)
        frmCombineData.setTabOrder(self.btnInSFile, self.txtOutFile)
        frmCombineData.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmCombineData.setTabOrder(self.btnOutFile, self.cbmLabel)
        frmCombineData.setTabOrder(self.cbmLabel, self.cbCol)
        frmCombineData.setTabOrder(self.cbCol, self.cbDM)
        frmCombineData.setTabOrder(self.cbDM, self.cbSubject)
        frmCombineData.setTabOrder(self.cbSubject, self.cbTask)
        frmCombineData.setTabOrder(self.cbTask, self.cbRun)
        frmCombineData.setTabOrder(self.cbRun, self.cbCounter)
        frmCombineData.setTabOrder(self.cbCounter, self.cbCond)
        frmCombineData.setTabOrder(self.cbCond, self.cbNScan)
        frmCombineData.setTabOrder(self.cbNScan, self.txtFData)
        frmCombineData.setTabOrder(self.txtFData, self.txtFLabel)
        frmCombineData.setTabOrder(self.txtFLabel, self.txtFCol)
        frmCombineData.setTabOrder(self.txtFCol, self.txtFDM)
        frmCombineData.setTabOrder(self.txtFDM, self.txtFSubject)
        frmCombineData.setTabOrder(self.txtFSubject, self.txtFTask)
        frmCombineData.setTabOrder(self.txtFTask, self.txtFRun)
        frmCombineData.setTabOrder(self.txtFRun, self.txtFCounter)
        frmCombineData.setTabOrder(self.txtFCounter, self.txtFCond)
        frmCombineData.setTabOrder(self.txtFCond, self.txtFCondPre)
        frmCombineData.setTabOrder(self.txtFCondPre, self.txtFScan)
        frmCombineData.setTabOrder(self.txtFScan, self.txtSData)
        frmCombineData.setTabOrder(self.txtSData, self.txtSLabel)
        frmCombineData.setTabOrder(self.txtSLabel, self.txtSCol)
        frmCombineData.setTabOrder(self.txtSCol, self.txtSDM)
        frmCombineData.setTabOrder(self.txtSDM, self.txtSSubject)
        frmCombineData.setTabOrder(self.txtSSubject, self.txtSTask)
        frmCombineData.setTabOrder(self.txtSTask, self.txtSRun)
        frmCombineData.setTabOrder(self.txtSRun, self.txtSCounter)
        frmCombineData.setTabOrder(self.txtSCounter, self.txtSCond)
        frmCombineData.setTabOrder(self.txtSCond, self.txtSCondPre)
        frmCombineData.setTabOrder(self.txtSCondPre, self.txtSScan)
        frmCombineData.setTabOrder(self.txtSScan, self.txtOData)
        frmCombineData.setTabOrder(self.txtOData, self.txtOLabel)
        frmCombineData.setTabOrder(self.txtOLabel, self.txtOmLabel)
        frmCombineData.setTabOrder(self.txtOmLabel, self.txtOCoI)
        frmCombineData.setTabOrder(self.txtOCoI, self.txtODM)
        frmCombineData.setTabOrder(self.txtODM, self.txtOSubject)
        frmCombineData.setTabOrder(self.txtOSubject, self.txtOTask)
        frmCombineData.setTabOrder(self.txtOTask, self.txtORun)
        frmCombineData.setTabOrder(self.txtORun, self.txtOCounter)
        frmCombineData.setTabOrder(self.txtOCounter, self.txtOCond)
        frmCombineData.setTabOrder(self.txtOCond, self.txtOCondPre)
        frmCombineData.setTabOrder(self.txtOCondPre, self.txtOScan)
        frmCombineData.setTabOrder(self.txtOScan, self.cbRelabeling)
        frmCombineData.setTabOrder(self.cbRelabeling, self.cbCondUnion)
        frmCombineData.setTabOrder(self.cbCondUnion, self.btnConvert)
        frmCombineData.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmCombineData):
        _translate = QtCore.QCoreApplication.translate
        frmCombineData.setWindowTitle(_translate("frmCombineData", "Dialog"))
        self.label_33.setText(_translate("frmCombineData", "Input First Data"))
        self.btnInFFile.setText(_translate("frmCombineData", "..."))
        self.label_34.setText(_translate("frmCombineData", "Input Second Data"))
        self.btnInSFile.setText(_translate("frmCombineData", "..."))
        self.label_35.setText(_translate("frmCombineData", "Output Data File"))
        self.btnOutFile.setText(_translate("frmCombineData", "..."))
        self.label_3.setText(_translate("frmCombineData", "Label"))
        self.cbDM.setText(_translate("frmCombineData", "Design Matrix"))
        self.label_2.setText(_translate("frmCombineData", "Data"))
        self.cbCol.setText(_translate("frmCombineData", "Coordinate"))
        self.cbmLabel.setText(_translate("frmCombineData", "Label (matrix)"))
        self.cbCond.setText(_translate("frmCombineData", "Condition"))
        self.cbTask.setText(_translate("frmCombineData", "Task"))
        self.cbSubject.setText(_translate("frmCombineData", "Subject"))
        self.cbCounter.setText(_translate("frmCombineData", "Counter"))
        self.cbRun.setText(_translate("frmCombineData", "Run"))
        self.cbNScan.setText(_translate("frmCombineData", "NScan"))
        self.label.setText(_translate("frmCombineData", "First File"))
        self.label_4.setText(_translate("frmCombineData", "Second File"))
        self.label_5.setText(_translate("frmCombineData", "Out File"))
        self.btnClose.setText(_translate("frmCombineData", "Close"))
        self.btnConvert.setText(_translate("frmCombineData", "Convert"))
        self.txtOLabel.setText(_translate("frmCombineData", "label"))
        self.txtOmLabel.setText(_translate("frmCombineData", "mlabel"))
        self.txtOData.setText(_translate("frmCombineData", "data"))
        self.txtOCoI.setText(_translate("frmCombineData", "coordinate"))
        self.txtODM.setText(_translate("frmCombineData", "design"))
        self.txtOSubject.setText(_translate("frmCombineData", "subject"))
        self.txtORun.setText(_translate("frmCombineData", "run"))
        self.txtOCounter.setText(_translate("frmCombineData", "counter"))
        self.txtOTask.setText(_translate("frmCombineData", "task"))
        self.txtOCond.setText(_translate("frmCombineData", "condition"))
        self.txtOScan.setText(_translate("frmCombineData", "nscan"))
        self.cbRelabeling.setText(_translate("frmCombineData", "Re-Labeling"))
        self.label_28.setText(_translate("frmCombineData", "Condition Prefix:"))
        self.txtOCondPre.setText(_translate("frmCombineData", "cond"))
        self.cbCondUnion.setText(_translate("frmCombineData", "Just Union"))
        self.txtFCondPre.setText(_translate("frmCombineData", "cond"))
        self.txtSCondPre.setText(_translate("frmCombineData", "cond"))
