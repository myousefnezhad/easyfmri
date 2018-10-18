# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmDataEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDataEditor(object):
    def setupUi(self, frmDataEditor):
        frmDataEditor.setObjectName("frmDataEditor")
        frmDataEditor.resize(740, 584)
        self.centralwidget = QtWidgets.QWidget(frmDataEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_2.addWidget(self.label_33)
        self.txtInFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.horizontalLayout_2.addWidget(self.txtInFile)
        self.btnInFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnInFile.setObjectName("btnInFile")
        self.horizontalLayout_2.addWidget(self.btnInFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lwData = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lwData.setFont(font)
        self.lwData.setObjectName("lwData")
        self.lwData.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.lwData)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnValue = QtWidgets.QPushButton(self.centralwidget)
        self.btnValue.setObjectName("btnValue")
        self.horizontalLayout.addWidget(self.btnValue)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        frmDataEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmDataEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 20))
        self.menubar.setObjectName("menubar")
        frmDataEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmDataEditor)
        self.statusbar.setObjectName("statusbar")
        frmDataEditor.setStatusBar(self.statusbar)

        self.retranslateUi(frmDataEditor)
        QtCore.QMetaObject.connectSlotsByName(frmDataEditor)

    def retranslateUi(self, frmDataEditor):
        _translate = QtCore.QCoreApplication.translate
        frmDataEditor.setWindowTitle(_translate("frmDataEditor", "MainWindow"))
        self.label_33.setText(_translate("frmDataEditor", "Input Data "))
        self.btnInFile.setText(_translate("frmDataEditor", "..."))
        self.lwData.setSortingEnabled(True)
        self.btnClose.setText(_translate("frmDataEditor", "Close"))
        self.btnValue.setText(_translate("frmDataEditor", "View Value"))

