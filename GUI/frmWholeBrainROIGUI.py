# Form implementation generated from reading ui file 'frmWholeBrainROIGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmWholeBrainROI(object):
    def setupUi(self, frmWholeBrainROI):
        frmWholeBrainROI.setObjectName("frmWholeBrainROI")
        frmWholeBrainROI.resize(802, 404)
        self.label_6 = QtWidgets.QLabel(frmWholeBrainROI)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_6.setObjectName("label_6")
        self.btnSSSetting = QtWidgets.QPushButton(frmWholeBrainROI)
        self.btnSSSetting.setGeometry(QtCore.QRect(740, 20, 51, 32))
        self.btnSSSetting.setObjectName("btnSSSetting")
        self.txtSSSetting = QtWidgets.QComboBox(frmWholeBrainROI)
        self.txtSSSetting.setGeometry(QtCore.QRect(98, 20, 541, 26))
        self.txtSSSetting.setEditable(True)
        self.txtSSSetting.setObjectName("txtSSSetting")
        self.btnSSSettingReload = QtWidgets.QPushButton(frmWholeBrainROI)
        self.btnSSSettingReload.setGeometry(QtCore.QRect(650, 20, 81, 32))
        self.btnSSSettingReload.setObjectName("btnSSSettingReload")
        self.tabWidget_2 = QtWidgets.QTabWidget(frmWholeBrainROI)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 150, 761, 141))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.txtSSDIR = QtWidgets.QLineEdit(self.tab_9)
        self.txtSSDIR.setGeometry(QtCore.QRect(140, 26, 601, 21))
        self.txtSSDIR.setStatusTip("")
        self.txtSSDIR.setText("")
        self.txtSSDIR.setObjectName("txtSSDIR")
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setGeometry(QtCore.QRect(10, 26, 131, 16))
        self.label_4.setToolTip("")
        self.label_4.setStatusTip("")
        self.label_4.setProperty("toolTipDuration", -1)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.tab_9)
        self.label_9.setGeometry(QtCore.QRect(11, 60, 131, 16))
        self.label_9.setObjectName("label_9")
        self.txtSSTask = QtWidgets.QLineEdit(self.tab_9)
        self.txtSSTask.setGeometry(QtCore.QRect(140, 60, 601, 21))
        self.txtSSTask.setStatusTip("")
        self.txtSSTask.setText("")
        self.txtSSTask.setObjectName("txtSSTask")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_12 = QtWidgets.QLabel(self.tab_8)
        self.label_12.setGeometry(QtCore.QRect(550, 20, 60, 16))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.tab_8)
        self.label_11.setGeometry(QtCore.QRect(370, 20, 60, 21))
        self.label_11.setObjectName("label_11")
        self.txtSSSubPer = QtWidgets.QLineEdit(self.tab_8)
        self.txtSSSubPer.setGeometry(QtCore.QRect(600, 20, 80, 21))
        self.txtSSSubPer.setObjectName("txtSSSubPer")
        self.txtSSSubLen = QtWidgets.QSpinBox(self.tab_8)
        self.txtSSSubLen.setGeometry(QtCore.QRect(440, 20, 80, 24))
        self.txtSSSubLen.setMinimum(1)
        self.txtSSSubLen.setMaximum(999999999)
        self.txtSSSubLen.setSingleStep(1)
        self.txtSSSubLen.setProperty("value", 2)
        self.txtSSSubLen.setObjectName("txtSSSubLen")
        self.txtSSSubRange = QtWidgets.QLineEdit(self.tab_8)
        self.txtSSSubRange.setGeometry(QtCore.QRect(140, 20, 211, 21))
        self.txtSSSubRange.setObjectName("txtSSSubRange")
        self.label_7 = QtWidgets.QLabel(self.tab_8)
        self.label_7.setGeometry(QtCore.QRect(80, 20, 71, 16))
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.txtSSRunLen = QtWidgets.QSpinBox(self.tab_10)
        self.txtSSRunLen.setGeometry(QtCore.QRect(440, 20, 80, 24))
        self.txtSSRunLen.setMinimum(1)
        self.txtSSRunLen.setMaximum(999999999)
        self.txtSSRunLen.setProperty("value", 2)
        self.txtSSRunLen.setObjectName("txtSSRunLen")
        self.txtSSRunPer = QtWidgets.QLineEdit(self.tab_10)
        self.txtSSRunPer.setGeometry(QtCore.QRect(600, 20, 80, 21))
        self.txtSSRunPer.setObjectName("txtSSRunPer")
        self.label_18 = QtWidgets.QLabel(self.tab_10)
        self.label_18.setGeometry(QtCore.QRect(370, 20, 60, 21))
        self.label_18.setObjectName("label_18")
        self.label_21 = QtWidgets.QLabel(self.tab_10)
        self.label_21.setGeometry(QtCore.QRect(550, 20, 60, 16))
        self.label_21.setObjectName("label_21")
        self.txtSSRunRange = QtWidgets.QLineEdit(self.tab_10)
        self.txtSSRunRange.setGeometry(QtCore.QRect(135, 20, 211, 21))
        self.txtSSRunRange.setObjectName("txtSSRunRange")
        self.label_22 = QtWidgets.QLabel(self.tab_10)
        self.label_22.setGeometry(QtCore.QRect(70, 20, 71, 16))
        self.label_22.setObjectName("label_22")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.txtSSConLen = QtWidgets.QSpinBox(self.tab_11)
        self.txtSSConLen.setGeometry(QtCore.QRect(440, 20, 80, 24))
        self.txtSSConLen.setMaximum(100000)
        self.txtSSConLen.setSingleStep(1)
        self.txtSSConLen.setProperty("value", 2)
        self.txtSSConLen.setObjectName("txtSSConLen")
        self.label_43 = QtWidgets.QLabel(self.tab_11)
        self.label_43.setGeometry(QtCore.QRect(370, 20, 60, 21))
        self.label_43.setObjectName("label_43")
        self.label_42 = QtWidgets.QLabel(self.tab_11)
        self.label_42.setGeometry(QtCore.QRect(540, 20, 60, 16))
        self.label_42.setObjectName("label_42")
        self.txtSSConPer = QtWidgets.QLineEdit(self.tab_11)
        self.txtSSConPer.setGeometry(QtCore.QRect(590, 20, 80, 21))
        self.txtSSConPer.setObjectName("txtSSConPer")
        self.txtSSConRange = QtWidgets.QLineEdit(self.tab_11)
        self.txtSSConRange.setGeometry(QtCore.QRect(150, 20, 201, 21))
        self.txtSSConRange.setObjectName("txtSSConRange")
        self.label_16 = QtWidgets.QLabel(self.tab_11)
        self.label_16.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_16.setObjectName("label_16")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.cbMetric = QtWidgets.QComboBox(self.tab)
        self.cbMetric.setGeometry(QtCore.QRect(100, 20, 331, 26))
        self.cbMetric.setObjectName("cbMetric")
        self.txtSSSpace = QtWidgets.QComboBox(self.tab)
        self.txtSSSpace.setGeometry(QtCore.QRect(100, 60, 581, 26))
        self.txtSSSpace.setEditable(True)
        self.txtSSSpace.setObjectName("txtSSSpace")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_5.setObjectName("label_5")
        self.btnSSSpace = QtWidgets.QPushButton(self.tab)
        self.btnSSSpace.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnSSSpace.setObjectName("btnSSSpace")
        self.tabWidget_2.addTab(self.tab, "")
        self.btnClose = QtWidgets.QPushButton(frmWholeBrainROI)
        self.btnClose.setGeometry(QtCore.QRect(20, 360, 113, 32))
        self.btnClose.setObjectName("btnClose")
        self.btnRUN = QtWidgets.QPushButton(frmWholeBrainROI)
        self.btnRUN.setGeometry(QtCore.QRect(670, 360, 113, 32))
        self.btnRUN.setObjectName("btnRUN")
        self.label_2 = QtWidgets.QLabel(frmWholeBrainROI)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.txtSSInFile = QtWidgets.QComboBox(frmWholeBrainROI)
        self.txtSSInFile.setGeometry(QtCore.QRect(150, 60, 631, 26))
        self.txtSSInFile.setEditable(True)
        self.txtSSInFile.setObjectName("txtSSInFile")
        self.label_23 = QtWidgets.QLabel(frmWholeBrainROI)
        self.label_23.setGeometry(QtCore.QRect(20, 310, 771, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_23.setObjectName("label_23")
        self.btnOutROI = QtWidgets.QPushButton(frmWholeBrainROI)
        self.btnOutROI.setGeometry(QtCore.QRect(740, 100, 51, 32))
        self.btnOutROI.setObjectName("btnOutROI")
        self.label_3 = QtWidgets.QLabel(frmWholeBrainROI)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_3.setObjectName("label_3")
        self.txtOutROI = QtWidgets.QLineEdit(frmWholeBrainROI)
        self.txtOutROI.setGeometry(QtCore.QRect(120, 100, 611, 21))
        self.txtOutROI.setText("")
        self.txtOutROI.setObjectName("txtOutROI")

        self.retranslateUi(frmWholeBrainROI)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmWholeBrainROI)
        frmWholeBrainROI.setTabOrder(self.txtSSSetting, self.btnSSSettingReload)
        frmWholeBrainROI.setTabOrder(self.btnSSSettingReload, self.btnSSSetting)
        frmWholeBrainROI.setTabOrder(self.btnSSSetting, self.txtSSInFile)
        frmWholeBrainROI.setTabOrder(self.txtSSInFile, self.txtOutROI)
        frmWholeBrainROI.setTabOrder(self.txtOutROI, self.btnOutROI)
        frmWholeBrainROI.setTabOrder(self.btnOutROI, self.tabWidget_2)
        frmWholeBrainROI.setTabOrder(self.tabWidget_2, self.txtSSDIR)
        frmWholeBrainROI.setTabOrder(self.txtSSDIR, self.txtSSTask)
        frmWholeBrainROI.setTabOrder(self.txtSSTask, self.txtSSSubLen)
        frmWholeBrainROI.setTabOrder(self.txtSSSubLen, self.txtSSSubPer)
        frmWholeBrainROI.setTabOrder(self.txtSSSubPer, self.txtSSRunLen)
        frmWholeBrainROI.setTabOrder(self.txtSSRunLen, self.txtSSRunPer)
        frmWholeBrainROI.setTabOrder(self.txtSSRunPer, self.txtSSConLen)
        frmWholeBrainROI.setTabOrder(self.txtSSConLen, self.txtSSConPer)
        frmWholeBrainROI.setTabOrder(self.txtSSConPer, self.cbMetric)
        frmWholeBrainROI.setTabOrder(self.cbMetric, self.txtSSSpace)
        frmWholeBrainROI.setTabOrder(self.txtSSSpace, self.btnSSSpace)
        frmWholeBrainROI.setTabOrder(self.btnSSSpace, self.btnRUN)
        frmWholeBrainROI.setTabOrder(self.btnRUN, self.btnClose)

    def retranslateUi(self, frmWholeBrainROI):
        _translate = QtCore.QCoreApplication.translate
        frmWholeBrainROI.setWindowTitle(_translate("frmWholeBrainROI", "Whole Brain ROI"))
        self.label_6.setText(_translate("frmWholeBrainROI", "Setting:"))
        self.btnSSSetting.setText(_translate("frmWholeBrainROI", "..."))
        self.btnSSSettingReload.setText(_translate("frmWholeBrainROI", "Reload"))
        self.txtSSDIR.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt;\">mainDIR: main folder that is included all dataset files, i.e. support BIDS format: </span><a href=\"https://www.nature.com/articles/sdata201644\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://www.nature.com/articles/sdata201644</span></a></p></body></html>"))
        self.label_4.setText(_translate("frmWholeBrainROI", "Main Directory:"))
        self.label_4.setProperty("setToolTip", _translate("frmWholeBrainROI", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.label_9.setText(_translate("frmWholeBrainROI", "Task Name(s):"))
        self.txtSSTask.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">Task Names: a unique array of integers, i.e., [task1, task2, ...]</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">, is the separator</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("frmWholeBrainROI", "General"))
        self.label_12.setText(_translate("frmWholeBrainROI", "Perfix:"))
        self.label_11.setText(_translate("frmWholeBrainROI", "Length:"))
        self.txtSSSubPer.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">SubPer: content of subject counter, e.g. SubPer = 0 -&gt; sub-001 OR SubPer = A -&gt; sub-AA1</span></p></body></html>"))
        self.txtSSSubPer.setText(_translate("frmWholeBrainROI", "0"))
        self.txtSSSubLen.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">SubLen: the length of subject counter, e.g. SubLen=3 -&gt; output sub-001, sub-002</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">SubLen &gt; 1</span></p></body></html>"))
        self.txtSSSubRange.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">SubRange: a unique range of integers, i.e. Range=[1, 4-8, 10, 12-14]</span></p></body></html>"))
        self.txtSSSubRange.setText(_translate("frmWholeBrainROI", "[1-1]"))
        self.label_7.setText(_translate("frmWholeBrainROI", "Range:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("frmWholeBrainROI", "Subjects"))
        self.txtSSRunLen.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">RunLen: the length of run counter, e.g. RunLen=3 -&gt; output run-001, rub-002</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">RunLen &gt; 1</span></p></body></html>"))
        self.txtSSRunPer.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">RunPer: content of subject counter, e.g. RunPer = 0 -&gt; run-001 OR RunPer = A -&gt; run-AA1</span></p></body></html>"))
        self.txtSSRunPer.setText(_translate("frmWholeBrainROI", "0"))
        self.label_18.setText(_translate("frmWholeBrainROI", "Length:"))
        self.label_21.setText(_translate("frmWholeBrainROI", "Perfix:"))
        self.txtSSRunRange.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">RunRange is a 3D tensor --- defining as {ax[b*c-d];...}</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">a is the number of subjects that [b*c-d] will be applied to them</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">b denotes the number of counters in &quot;a&quot; subjects with c-d runs</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">c-d is an interval of runs for the corresponding counters and subjects</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">; is the separator for subjects</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">, is the separator for counters</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">A single 1 coefficient can be interpreted as all subjects/counters as well</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">Example 1: If we have 12 subjects with 3 counters, each has runs from 5 to 10: {12x[3*5-10]}</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">Example 2: If we have 6 subjects with 3 counters + 5 subjects with 2 counters, each has runs from 1 to 6: {6x[3*1-6];5x[2*1-6]}</span></p><p><span style=\" font-size:18pt; color:#0000ff;\">Example 3: If we have 2 subjects with 6 counters, where the first 3 counters have 1-8 runs and the second 2 counters have 4-9 runs, and the last counter only has run 7: {2x[3*1-8, 2*4-9, 7]}</span></p><p><br/></p></body></html>"))
        self.txtSSRunRange.setText(_translate("frmWholeBrainROI", "{1x[1*1-1]}"))
        self.label_22.setText(_translate("frmWholeBrainROI", "Ranges:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("frmWholeBrainROI", "Run"))
        self.label_43.setText(_translate("frmWholeBrainROI", "Length:"))
        self.label_42.setText(_translate("frmWholeBrainROI", "Perfix:"))
        self.txtSSConPer.setText(_translate("frmWholeBrainROI", "0"))
        self.txtSSConRange.setToolTip(_translate("frmWholeBrainROI", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">CounterRange: sequence of ranges, i.e. If all 12 subjects have runs from 2 to 5 then Range=[12*2-5]; If 3 subjects have runs from 1 to 4 and 2 subjects have runs from 5 to 7 then Range=[3*1-4, 2*5-7]</span></p></body></html>"))
        self.txtSSConRange.setText(_translate("frmWholeBrainROI", "[1*1-1]"))
        self.label_16.setText(_translate("frmWholeBrainROI", "Ranges:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("frmWholeBrainROI", "Counter"))
        self.label.setText(_translate("frmWholeBrainROI", "Metric"))
        self.label_5.setText(_translate("frmWholeBrainROI", "Affine file:"))
        self.btnSSSpace.setText(_translate("frmWholeBrainROI", "..."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("frmWholeBrainROI", "Parameters"))
        self.btnClose.setText(_translate("frmWholeBrainROI", "Close"))
        self.btnRUN.setText(_translate("frmWholeBrainROI", "Run"))
        self.label_2.setText(_translate("frmWholeBrainROI", "Mask File Name"))
        self.label_23.setText(_translate("frmWholeBrainROI", "$MAINDIR$, $SUB$, $TASK$, $RUN$, $COUNT$ will be replaced by the preprocessing parameters.\n"
"It\'s case sensitive."))
        self.btnOutROI.setText(_translate("frmWholeBrainROI", "..."))
        self.label_3.setText(_translate("frmWholeBrainROI", "Output ROI"))
