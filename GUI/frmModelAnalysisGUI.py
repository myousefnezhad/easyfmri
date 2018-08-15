# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmModelAnalysisGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmModelAnalysis(object):
    def setupUi(self, frmModelAnalysis):
        frmModelAnalysis.setObjectName("frmModelAnalysis")
        frmModelAnalysis.resize(727, 401)
        self.tabWidget = QtWidgets.QTabWidget(frmModelAnalysis)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 691, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnMAURun = QtWidgets.QPushButton(self.tab)
        self.btnMAURun.setGeometry(QtCore.QRect(22, 80, 641, 32))
        self.btnMAURun.setObjectName("btnMAURun")
        self.btnMASRun = QtWidgets.QPushButton(self.tab)
        self.btnMASRun.setGeometry(QtCore.QRect(22, 220, 641, 32))
        self.btnMASRun.setObjectName("btnMASRun")
        self.cbMAS = QtWidgets.QComboBox(self.tab)
        self.cbMAS.setGeometry(QtCore.QRect(220, 160, 441, 26))
        self.cbMAS.setObjectName("cbMAS")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(30, 20, 181, 16))
        self.label_40.setObjectName("label_40")
        self.label_50 = QtWidgets.QLabel(self.tab)
        self.label_50.setGeometry(QtCore.QRect(30, 160, 181, 16))
        self.label_50.setObjectName("label_50")
        self.cbMAU = QtWidgets.QComboBox(self.tab)
        self.cbMAU.setGeometry(QtCore.QRect(220, 20, 441, 26))
        self.cbMAU.setObjectName("cbMAU")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnDataEditor = QtWidgets.QPushButton(self.tab_2)
        self.btnDataEditor.setGeometry(QtCore.QRect(20, 30, 641, 32))
        self.btnDataEditor.setObjectName("btnDataEditor")
        self.btnSKModel = QtWidgets.QPushButton(self.tab_2)
        self.btnSKModel.setGeometry(QtCore.QRect(20, 80, 641, 32))
        self.btnSKModel.setObjectName("btnSKModel")
        self.btnSKCModel = QtWidgets.QPushButton(self.tab_2)
        self.btnSKCModel.setGeometry(QtCore.QRect(20, 130, 641, 32))
        self.btnSKCModel.setObjectName("btnSKCModel")
        self.tabWidget.addTab(self.tab_2, "")
        self.btnClose = QtWidgets.QPushButton(frmModelAnalysis)
        self.btnClose.setGeometry(QtCore.QRect(20, 350, 691, 32))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(frmModelAnalysis)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmModelAnalysis)

    def retranslateUi(self, frmModelAnalysis):
        _translate = QtCore.QCoreApplication.translate
        frmModelAnalysis.setWindowTitle(_translate("frmModelAnalysis", "Model Analysis"))
        self.btnMAURun.setText(_translate("frmModelAnalysis", "Run"))
        self.btnMASRun.setText(_translate("frmModelAnalysis", "Run"))
        self.label_40.setText(_translate("frmModelAnalysis", "Unsupervised Method"))
        self.label_50.setText(_translate("frmModelAnalysis", "Supervised Method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmModelAnalysis", "Analysis"))
        self.btnDataEditor.setText(_translate("frmModelAnalysis", "Data/Result Viewer"))
        self.btnSKModel.setText(_translate("frmModelAnalysis", "SK Classification Model Viewer"))
        self.btnSKCModel.setText(_translate("frmModelAnalysis", "SK Clustring Model Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmModelAnalysis", "Tools"))
        self.btnClose.setText(_translate("frmModelAnalysis", "Close"))

