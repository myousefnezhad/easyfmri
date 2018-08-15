# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmManuallyDesignROIGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmManuallyDesignROI(object):
    def setupUi(self, frmManuallyDesignROI):
        frmManuallyDesignROI.setObjectName("frmManuallyDesignROI")
        frmManuallyDesignROI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(frmManuallyDesignROI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setObjectName("btnNew")
        self.horizontalLayout.addWidget(self.btnNew)
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout.addWidget(self.btnRun)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Code = QtWidgets.QWidget(self.centralwidget)
        self.Code.setObjectName("Code")
        self.gridLayout = QtWidgets.QGridLayout(self.Code)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.txtCode = QtWidgets.QTextEdit(self.Code)
        self.txtCode.setObjectName("txtCode")
        self.gridLayout.addWidget(self.txtCode, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.Code)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        frmManuallyDesignROI.setCentralWidget(self.centralwidget)
        self.stb = QtWidgets.QStatusBar(frmManuallyDesignROI)
        self.stb.setObjectName("stb")
        frmManuallyDesignROI.setStatusBar(self.stb)

        self.retranslateUi(frmManuallyDesignROI)
        QtCore.QMetaObject.connectSlotsByName(frmManuallyDesignROI)

    def retranslateUi(self, frmManuallyDesignROI):
        _translate = QtCore.QCoreApplication.translate
        frmManuallyDesignROI.setWindowTitle(_translate("frmManuallyDesignROI", "Manually Design ROI"))
        self.btnNew.setText(_translate("frmManuallyDesignROI", "New"))
        self.btnOpen.setText(_translate("frmManuallyDesignROI", "Open"))
        self.btnSave.setText(_translate("frmManuallyDesignROI", "Save"))
        self.btnRun.setText(_translate("frmManuallyDesignROI", "Run"))
        self.btnClose.setText(_translate("frmManuallyDesignROI", "Close"))

