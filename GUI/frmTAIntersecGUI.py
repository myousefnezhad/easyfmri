# Form implementation generated from reading ui file 'frmTAIntersecGUI.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmTAInterSec(object):
    def setupUi(self, frmTAInterSec):
        frmTAInterSec.setObjectName("frmTAInterSec")
        frmTAInterSec.resize(744, 639)
        self.centralwidget = QtWidgets.QWidget(frmTAInterSec)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout.addWidget(self.label_33)
        self.txtInFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.horizontalLayout.addWidget(self.txtInFile)
        self.btnInFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnInFile.setObjectName("btnInFile")
        self.horizontalLayout.addWidget(self.btnInFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_2.addWidget(self.label_35)
        self.txtOutFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.horizontalLayout_2.addWidget(self.txtOutFile)
        self.btnOutFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutFile.setObjectName("btnOutFile")
        self.horizontalLayout_2.addWidget(self.btnOutFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.txtData = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtData.sizePolicy().hasHeightForWidth())
        self.txtData.setSizePolicy(sizePolicy)
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.horizontalLayout_6.addWidget(self.txtData)
        self.txtOData = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOData.sizePolicy().hasHeightForWidth())
        self.txtOData.setSizePolicy(sizePolicy)
        self.txtOData.setObjectName("txtOData")
        self.horizontalLayout_6.addWidget(self.txtOData)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtLabel.sizePolicy().hasHeightForWidth())
        self.txtLabel.setSizePolicy(sizePolicy)
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.horizontalLayout_7.addWidget(self.txtLabel)
        self.txtOLabel = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOLabel.sizePolicy().hasHeightForWidth())
        self.txtOLabel.setSizePolicy(sizePolicy)
        self.txtOLabel.setObjectName("txtOLabel")
        self.horizontalLayout_7.addWidget(self.txtOLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSubject.sizePolicy().hasHeightForWidth())
        self.txtSubject.setSizePolicy(sizePolicy)
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.horizontalLayout_8.addWidget(self.txtSubject)
        self.txtOSubject = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOSubject.sizePolicy().hasHeightForWidth())
        self.txtOSubject.setSizePolicy(sizePolicy)
        self.txtOSubject.setObjectName("txtOSubject")
        self.horizontalLayout_8.addWidget(self.txtOSubject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.txtRun = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRun.sizePolicy().hasHeightForWidth())
        self.txtRun.setSizePolicy(sizePolicy)
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.horizontalLayout_13.addWidget(self.txtRun)
        self.txtORun = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtORun.sizePolicy().hasHeightForWidth())
        self.txtORun.setSizePolicy(sizePolicy)
        self.txtORun.setObjectName("txtORun")
        self.horizontalLayout_13.addWidget(self.txtORun)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.txtTask = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTask.sizePolicy().hasHeightForWidth())
        self.txtTask.setSizePolicy(sizePolicy)
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.horizontalLayout_12.addWidget(self.txtTask)
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOTask.sizePolicy().hasHeightForWidth())
        self.txtOTask.setSizePolicy(sizePolicy)
        self.txtOTask.setObjectName("txtOTask")
        self.horizontalLayout_12.addWidget(self.txtOTask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCounter.sizePolicy().hasHeightForWidth())
        self.txtCounter.setSizePolicy(sizePolicy)
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.horizontalLayout_14.addWidget(self.txtCounter)
        self.txtOCounter = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOCounter.sizePolicy().hasHeightForWidth())
        self.txtOCounter.setSizePolicy(sizePolicy)
        self.txtOCounter.setObjectName("txtOCounter")
        self.horizontalLayout_14.addWidget(self.txtOCounter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbmLabel.sizePolicy().hasHeightForWidth())
        self.cbmLabel.setSizePolicy(sizePolicy)
        self.cbmLabel.setObjectName("cbmLabel")
        self.horizontalLayout_9.addWidget(self.cbmLabel)
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtmLabel.sizePolicy().hasHeightForWidth())
        self.txtmLabel.setSizePolicy(sizePolicy)
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.horizontalLayout_9.addWidget(self.txtmLabel)
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOmLabel.sizePolicy().hasHeightForWidth())
        self.txtOmLabel.setSizePolicy(sizePolicy)
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.horizontalLayout_9.addWidget(self.txtOmLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCol.sizePolicy().hasHeightForWidth())
        self.cbCol.setSizePolicy(sizePolicy)
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.horizontalLayout_10.addWidget(self.cbCol)
        self.txtCol = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCol.sizePolicy().hasHeightForWidth())
        self.txtCol.setSizePolicy(sizePolicy)
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.horizontalLayout_10.addWidget(self.txtCol)
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOCol.sizePolicy().hasHeightForWidth())
        self.txtOCol.setSizePolicy(sizePolicy)
        self.txtOCol.setObjectName("txtOCol")
        self.horizontalLayout_10.addWidget(self.txtOCol)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cbDM = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDM.sizePolicy().hasHeightForWidth())
        self.cbDM.setSizePolicy(sizePolicy)
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.horizontalLayout_11.addWidget(self.cbDM)
        self.txtDM = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDM.sizePolicy().hasHeightForWidth())
        self.txtDM.setSizePolicy(sizePolicy)
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.horizontalLayout_11.addWidget(self.txtDM)
        self.txtODM = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtODM.sizePolicy().hasHeightForWidth())
        self.txtODM.setSizePolicy(sizePolicy)
        self.txtODM.setObjectName("txtODM")
        self.horizontalLayout_11.addWidget(self.txtODM)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCond.sizePolicy().hasHeightForWidth())
        self.cbCond.setSizePolicy(sizePolicy)
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.horizontalLayout_15.addWidget(self.cbCond)
        self.txtCond = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCond.sizePolicy().hasHeightForWidth())
        self.txtCond.setSizePolicy(sizePolicy)
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.horizontalLayout_15.addWidget(self.txtCond)
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOCond.sizePolicy().hasHeightForWidth())
        self.txtOCond.setSizePolicy(sizePolicy)
        self.txtOCond.setObjectName("txtOCond")
        self.horizontalLayout_15.addWidget(self.txtOCond)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbNScan.sizePolicy().hasHeightForWidth())
        self.cbNScan.setSizePolicy(sizePolicy)
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.horizontalLayout_16.addWidget(self.cbNScan)
        self.txtScan = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtScan.sizePolicy().hasHeightForWidth())
        self.txtScan.setSizePolicy(sizePolicy)
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.horizontalLayout_16.addWidget(self.txtScan)
        self.txtOScan = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOScan.sizePolicy().hasHeightForWidth())
        self.txtOScan.setSizePolicy(sizePolicy)
        self.txtOScan.setObjectName("txtOScan")
        self.horizontalLayout_16.addWidget(self.txtOScan)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cbFSubject = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFSubject.setChecked(True)
        self.cbFSubject.setObjectName("cbFSubject")
        self.verticalLayout_10.addWidget(self.cbFSubject)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.rbFRun = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbFRun.setObjectName("rbFRun")
        self.horizontalLayout_22.addWidget(self.rbFRun)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_22.addWidget(self.radioButton_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_22)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.horizontalLayout_21.addWidget(self.groupBox_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.cbFCounter = QtWidgets.QCheckBox(self.tab_3)
        self.cbFCounter.setObjectName("cbFCounter")
        self.verticalLayout_11.addWidget(self.cbFCounter)
        self.cbFTask = QtWidgets.QCheckBox(self.tab_3)
        self.cbFTask.setObjectName("cbFTask")
        self.verticalLayout_11.addWidget(self.cbFTask)
        self.horizontalLayout_21.addLayout(self.verticalLayout_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_21)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_23.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_24.addWidget(self.label_8)
        self.txtFLabels = QtWidgets.QTextBrowser(self.tab_4)
        self.txtFLabels.setReadOnly(False)
        self.txtFLabels.setObjectName("txtFLabels")
        self.horizontalLayout_24.addWidget(self.txtFLabels)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_24.addWidget(self.label_13)
        self.txtClassList = QtWidgets.QTextEdit(self.tab_4)
        self.txtClassList.setReadOnly(True)
        self.txtClassList.setObjectName("txtClassList")
        self.horizontalLayout_24.addWidget(self.txtClassList)
        self.verticalLayout_12.addLayout(self.horizontalLayout_24)
        self.cbBalence = QtWidgets.QCheckBox(self.tab_4)
        self.cbBalence.setObjectName("cbBalence")
        self.verticalLayout_12.addWidget(self.cbBalence)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_12.addItem(spacerItem3)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_25.addWidget(self.label_9)
        self.txtFFold = QtWidgets.QTextBrowser(self.tab_4)
        self.txtFFold.setReadOnly(False)
        self.txtFFold.setObjectName("txtFFold")
        self.horizontalLayout_25.addWidget(self.txtFFold)
        self.verticalLayout_12.addLayout(self.horizontalLayout_25)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_26.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setObjectName("btnConvert")
        self.horizontalLayout_3.addWidget(self.btnConvert)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        frmTAInterSec.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmTAInterSec)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmTAInterSec)

    def retranslateUi(self, frmTAInterSec):
        _translate = QtCore.QCoreApplication.translate
        frmTAInterSec.setWindowTitle(_translate("frmTAInterSec", "MainWindow"))
        self.label_33.setText(_translate("frmTAInterSec", "Input Data"))
        self.btnInFile.setText(_translate("frmTAInterSec", "..."))
        self.label_35.setText(_translate("frmTAInterSec", "Output Data"))
        self.btnOutFile.setText(_translate("frmTAInterSec", "..."))
        self.label.setText(_translate("frmTAInterSec", "Input"))
        self.label_5.setText(_translate("frmTAInterSec", "Output"))
        self.label_2.setText(_translate("frmTAInterSec", "Data"))
        self.txtOData.setText(_translate("frmTAInterSec", "data"))
        self.label_3.setText(_translate("frmTAInterSec", "Label"))
        self.txtOLabel.setText(_translate("frmTAInterSec", "label"))
        self.label_6.setText(_translate("frmTAInterSec", "Subject"))
        self.txtOSubject.setText(_translate("frmTAInterSec", "subject"))
        self.label_10.setText(_translate("frmTAInterSec", "Run"))
        self.txtORun.setText(_translate("frmTAInterSec", "run"))
        self.label_11.setText(_translate("frmTAInterSec", "Task"))
        self.txtOTask.setText(_translate("frmTAInterSec", "task"))
        self.label_12.setText(_translate("frmTAInterSec", "Counter"))
        self.txtOCounter.setText(_translate("frmTAInterSec", "counter"))
        self.cbmLabel.setText(_translate("frmTAInterSec", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmTAInterSec", "mlabel"))
        self.cbCol.setText(_translate("frmTAInterSec", "Coordinate"))
        self.txtOCol.setText(_translate("frmTAInterSec", "coordinate"))
        self.cbDM.setText(_translate("frmTAInterSec", "Design Matrix"))
        self.txtODM.setText(_translate("frmTAInterSec", "design"))
        self.cbCond.setText(_translate("frmTAInterSec", "Condition"))
        self.txtOCond.setText(_translate("frmTAInterSec", "condition"))
        self.cbNScan.setText(_translate("frmTAInterSec", "NScan"))
        self.txtOScan.setText(_translate("frmTAInterSec", "nscan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmTAInterSec", "Data"))
        self.groupBox_3.setTitle(_translate("frmTAInterSec", "<Subject Level>"))
        self.cbFSubject.setText(_translate("frmTAInterSec", "Subject"))
        self.rbFRun.setText(_translate("frmTAInterSec", "With Run"))
        self.radioButton_3.setText(_translate("frmTAInterSec", "Without Run"))
        self.cbFCounter.setText(_translate("frmTAInterSec", "Counter"))
        self.cbFTask.setText(_translate("frmTAInterSec", "Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmTAInterSec", "Level"))
        self.label_8.setText(_translate("frmTAInterSec", "<html><head/><body><p>Excluded Labels</p><p>(each label per line)</p></body></html>"))
        self.txtFLabels.setHtml(_translate("frmTAInterSec", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_13.setText(_translate("frmTAInterSec", "List of Classes"))
        self.cbBalence.setText(_translate("frmTAInterSec", "Balance all class labels"))
        self.label_9.setText(_translate("frmTAInterSec", "<html><head/><body><p>Excluded Folds</p><p>(each fold per line)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmTAInterSec", "Filter"))
        self.btnClose.setText(_translate("frmTAInterSec", "Close"))
        self.btnConvert.setText(_translate("frmTAInterSec", "Convert"))
