# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmSKModelEditorGUI.ui'
#
# Created by: PyQt6 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_frmSKModelEditor(object):
    def setupUi(self, frmSKModelEditor):
        frmSKModelEditor.setObjectName("frmSKModelEditor")
        frmSKModelEditor.resize(872, 686)
        self.txtInFile = QtWidgets.QLineEdit(frmSKModelEditor)
        self.txtInFile.setGeometry(QtCore.QRect(140, 20, 661, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnInFile = QtWidgets.QPushButton(frmSKModelEditor)
        self.btnInFile.setGeometry(QtCore.QRect(810, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmSKModelEditor)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnClose = QtWidgets.QPushButton(frmSKModelEditor)
        self.btnClose.setGeometry(QtCore.QRect(690, 640, 161, 29))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmSKModelEditor)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 831, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lwData = QtWidgets.QTreeWidget(self.tab)
        self.lwData.setGeometry(QtCore.QRect(13, 10, 801, 471))
        self.lwData.setObjectName("lwData")
        self.lwData.headerItem().setText(0, "1")
        self.btnValue = QtWidgets.QPushButton(self.tab)
        self.btnValue.setGeometry(QtCore.QRect(10, 490, 801, 32))
        self.btnValue.setObjectName("btnValue")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnTest = QtWidgets.QPushButton(self.tab_2)
        self.btnTest.setGeometry(QtCore.QRect(640, 490, 171, 32))
        self.btnTest.setObjectName("btnTest")
        self.btnInData = QtWidgets.QPushButton(self.tab_2)
        self.btnInData.setGeometry(QtCore.QRect(760, 20, 51, 32))
        self.btnInData.setObjectName("btnInData")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.label_34.setObjectName("label_34")
        self.txtInData = QtWidgets.QLineEdit(self.tab_2)
        self.txtInData.setGeometry(QtCore.QRect(140, 20, 611, 21))
        self.txtInData.setText("")
        self.txtInData.setObjectName("txtInData")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 181, 16))
        self.label_3.setObjectName("label_3")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab_2)
        self.txtITeLabel.setGeometry(QtCore.QRect(190, 100, 431, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab_2)
        self.txtITeData.setGeometry(QtCore.QRect(190, 60, 431, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 181, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 791, 241))
        self.groupBox.setObjectName("groupBox")
        self.cbPrecision = QtWidgets.QCheckBox(self.groupBox)
        self.cbPrecision.setGeometry(QtCore.QRect(20, 80, 181, 20))
        self.cbPrecision.setChecked(True)
        self.cbPrecision.setObjectName("cbPrecision")
        self.cbF1Avg = QtWidgets.QComboBox(self.groupBox)
        self.cbF1Avg.setGeometry(QtCore.QRect(260, 200, 501, 26))
        self.cbF1Avg.setObjectName("cbF1Avg")
        self.cbRecall = QtWidgets.QCheckBox(self.groupBox)
        self.cbRecall.setGeometry(QtCore.QRect(20, 160, 181, 20))
        self.cbRecall.setChecked(True)
        self.cbRecall.setObjectName("cbRecall")
        self.cbAPrecisionAvg = QtWidgets.QComboBox(self.groupBox)
        self.cbAPrecisionAvg.setGeometry(QtCore.QRect(260, 120, 501, 26))
        self.cbAPrecisionAvg.setObjectName("cbAPrecisionAvg")
        self.cbAverage = QtWidgets.QCheckBox(self.groupBox)
        self.cbAverage.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.cbAverage.setChecked(True)
        self.cbAverage.setObjectName("cbAverage")
        self.cbAPrecision = QtWidgets.QCheckBox(self.groupBox)
        self.cbAPrecision.setGeometry(QtCore.QRect(20, 120, 231, 20))
        self.cbAPrecision.setChecked(False)
        self.cbAPrecision.setObjectName("cbAPrecision")
        self.cbF1 = QtWidgets.QCheckBox(self.groupBox)
        self.cbF1.setGeometry(QtCore.QRect(20, 200, 181, 20))
        self.cbF1.setChecked(True)
        self.cbF1.setObjectName("cbF1")
        self.cbRecallAvg = QtWidgets.QComboBox(self.groupBox)
        self.cbRecallAvg.setGeometry(QtCore.QRect(260, 160, 501, 26))
        self.cbRecallAvg.setObjectName("cbRecallAvg")
        self.cbPrecisionAvg = QtWidgets.QComboBox(self.groupBox)
        self.cbPrecisionAvg.setGeometry(QtCore.QRect(260, 80, 501, 26))
        self.cbPrecisionAvg.setObjectName("cbPrecisionAvg")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(630, 140, 181, 20))
        self.label_5.setObjectName("label_5")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_2)
        self.txtFilter.setGeometry(QtCore.QRect(190, 140, 431, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 201, 16))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 180, 201, 16))
        self.label_10.setObjectName("label_10")
        self.txtClass = QtWidgets.QTextEdit(self.tab_2)
        self.txtClass.setGeometry(QtCore.QRect(190, 180, 611, 50))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.cbScale = QtWidgets.QCheckBox(self.tab_2)
        self.cbScale.setGeometry(QtCore.QRect(633, 60, 360, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.btnTestConfusion = QtWidgets.QPushButton(self.tab_2)
        self.btnTestConfusion.setGeometry(QtCore.QRect(460, 490, 171, 32))
        self.btnTestConfusion.setObjectName("btnTestConfusion")
        self.btnTestLabels = QtWidgets.QPushButton(self.tab_2)
        self.btnTestLabels.setGeometry(QtCore.QRect(280, 490, 171, 32))
        self.btnTestLabels.setObjectName("btnTestLabels")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmSKModelEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmSKModelEditor)
        frmSKModelEditor.setTabOrder(self.txtInFile, self.btnInFile)
        frmSKModelEditor.setTabOrder(self.btnInFile, self.btnClose)

    def retranslateUi(self, frmSKModelEditor):
        _translate = QtCore.QCoreApplication.translate
        frmSKModelEditor.setWindowTitle(_translate("frmSKModelEditor", "SK Learn Model Editor"))
        self.btnInFile.setText(_translate("frmSKModelEditor", "..."))
        self.label_33.setText(_translate("frmSKModelEditor", "Model File "))
        self.btnClose.setText(_translate("frmSKModelEditor", "Close"))
        self.lwData.setSortingEnabled(True)
        self.btnValue.setText(_translate("frmSKModelEditor", "View Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmSKModelEditor", "Parameters"))
        self.btnTest.setText(_translate("frmSKModelEditor", "Run Test Data"))
        self.btnInData.setText(_translate("frmSKModelEditor", "..."))
        self.label_34.setText(_translate("frmSKModelEditor", "Input Data "))
        self.label_3.setText(_translate("frmSKModelEditor", "Test Label"))
        self.label_2.setText(_translate("frmSKModelEditor", "Test Data"))
        self.groupBox.setTitle(_translate("frmSKModelEditor", "<Metrics>"))
        self.cbPrecision.setText(_translate("frmSKModelEditor", "Precision"))
        self.cbRecall.setText(_translate("frmSKModelEditor", "Recall"))
        self.cbAverage.setText(_translate("frmSKModelEditor", "Average"))
        self.cbAPrecision.setText(_translate("frmSKModelEditor", "Average of Precision"))
        self.cbF1.setText(_translate("frmSKModelEditor", "f1 score"))
        self.label_5.setText(_translate("frmSKModelEditor", "e.g. 0 or [1,2]"))
        self.txtFilter.setText(_translate("frmSKModelEditor", "0"))
        self.label_4.setText(_translate("frmSKModelEditor", "Remove Class IDs"))
        self.label_10.setText(_translate("frmSKModelEditor", "Existed Classes"))
        self.cbScale.setText(_translate("frmSKModelEditor", "Scale Data N(0,1)"))
        self.btnTestConfusion.setText(_translate("frmSKModelEditor", "Show Confusion Matrix"))
        self.btnTestLabels.setText(_translate("frmSKModelEditor", "Show Predicted Labels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmSKModelEditor", "Run Model"))

