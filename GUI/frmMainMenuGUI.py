# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMainMenuGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMainMenuGUI(object):
    def setupUi(self, frmMainMenuGUI):
        frmMainMenuGUI.setObjectName("frmMainMenuGUI")
        frmMainMenuGUI.resize(555, 480)
        self.label = QtWidgets.QLabel(frmMainMenuGUI)
        self.label.setGeometry(QtCore.QRect(0, 0, 551, 80))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(frmMainMenuGUI)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 521, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnFeatureAnalysis = QtWidgets.QPushButton(self.tab)
        self.btnFeatureAnalysis.setGeometry(QtCore.QRect(10, 80, 490, 51))
        self.btnFeatureAnalysis.setObjectName("btnFeatureAnalysis")
        self.btnModelAnalysis = QtWidgets.QPushButton(self.tab)
        self.btnModelAnalysis.setGeometry(QtCore.QRect(10, 140, 490, 51))
        self.btnModelAnalysis.setObjectName("btnModelAnalysis")
        self.btnPreprocess = QtWidgets.QPushButton(self.tab)
        self.btnPreprocess.setGeometry(QtCore.QRect(10, 20, 490, 51))
        self.btnPreprocess.setObjectName("btnPreprocess")
        self.btnVisualization = QtWidgets.QPushButton(self.tab)
        self.btnVisualization.setGeometry(QtCore.QRect(10, 200, 490, 51))
        self.btnVisualization.setObjectName("btnVisualization")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.cbTools = QtWidgets.QComboBox(self.tab_2)
        self.cbTools.setGeometry(QtCore.QRect(10, 40, 490, 26))
        self.cbTools.setObjectName("cbTools")
        self.btnTools = QtWidgets.QPushButton(self.tab_2)
        self.btnTools.setGeometry(QtCore.QRect(10, 90, 490, 51))
        self.btnTools.setObjectName("btnTools")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 471, 20))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.btnExit = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnExit.setGeometry(QtCore.QRect(290, 410, 255, 51))
        self.btnExit.setObjectName("btnExit")
        self.btnAbout = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnAbout.setGeometry(QtCore.QRect(20, 410, 255, 51))
        self.btnAbout.setObjectName("btnAbout")

        self.retranslateUi(frmMainMenuGUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMainMenuGUI)

    def retranslateUi(self, frmMainMenuGUI):
        _translate = QtCore.QCoreApplication.translate
        frmMainMenuGUI.setWindowTitle(_translate("frmMainMenuGUI", "easy fMRI (2.0)"))
        self.label.setText(_translate("frmMainMenuGUI", "easy fMRI"))
        self.btnFeatureAnalysis.setText(_translate("frmMainMenuGUI", "Feature Analysis"))
        self.btnModelAnalysis.setText(_translate("frmMainMenuGUI", "Model Analysis"))
        self.btnPreprocess.setText(_translate("frmMainMenuGUI", "Preprocessing (FSL)"))
        self.btnVisualization.setText(_translate("frmMainMenuGUI", "Visualization (AFNI)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMainMenuGUI", "Main"))
        self.btnTools.setText(_translate("frmMainMenuGUI", "Run"))
        self.label_2.setText(_translate("frmMainMenuGUI", "Select a tool:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMainMenuGUI", "Tools"))
        self.btnExit.setText(_translate("frmMainMenuGUI", "Exit"))
        self.btnAbout.setText(_translate("frmMainMenuGUI", "About"))

