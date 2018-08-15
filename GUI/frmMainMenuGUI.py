# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMainMenuGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMainMenuGUI(object):
    def setupUi(self, frmMainMenuGUI):
        frmMainMenuGUI.setObjectName("frmMainMenuGUI")
        frmMainMenuGUI.resize(369, 417)
        self.label = QtWidgets.QLabel(frmMainMenuGUI)
        self.label.setGeometry(QtCore.QRect(0, 10, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnPreprocess = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnPreprocess.setGeometry(QtCore.QRect(30, 100, 311, 51))
        self.btnPreprocess.setObjectName("btnPreprocess")
        self.btnFeatureAnalysis = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnFeatureAnalysis.setGeometry(QtCore.QRect(30, 160, 311, 51))
        self.btnFeatureAnalysis.setObjectName("btnFeatureAnalysis")
        self.btnModelAnalysis = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnModelAnalysis.setGeometry(QtCore.QRect(30, 220, 311, 51))
        self.btnModelAnalysis.setObjectName("btnModelAnalysis")
        self.btnVisualization = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnVisualization.setGeometry(QtCore.QRect(30, 280, 311, 51))
        self.btnVisualization.setObjectName("btnVisualization")
        self.btnExit = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnExit.setGeometry(QtCore.QRect(191, 340, 150, 51))
        self.btnExit.setObjectName("btnExit")
        self.btnAbout = QtWidgets.QPushButton(frmMainMenuGUI)
        self.btnAbout.setGeometry(QtCore.QRect(30, 340, 150, 51))
        self.btnAbout.setObjectName("btnAbout")

        self.retranslateUi(frmMainMenuGUI)
        QtCore.QMetaObject.connectSlotsByName(frmMainMenuGUI)

    def retranslateUi(self, frmMainMenuGUI):
        _translate = QtCore.QCoreApplication.translate
        frmMainMenuGUI.setWindowTitle(_translate("frmMainMenuGUI", "easy fMRI (1.0)"))
        self.label.setText(_translate("frmMainMenuGUI", "easy fMRI"))
        self.btnPreprocess.setText(_translate("frmMainMenuGUI", "Preprocessing (FSL)"))
        self.btnFeatureAnalysis.setText(_translate("frmMainMenuGUI", "Feature Analysis"))
        self.btnModelAnalysis.setText(_translate("frmMainMenuGUI", "Model Analysis"))
        self.btnVisualization.setText(_translate("frmMainMenuGUI", "Visualization (AFNI)"))
        self.btnExit.setText(_translate("frmMainMenuGUI", "Exit"))
        self.btnAbout.setText(_translate("frmMainMenuGUI", "About"))

