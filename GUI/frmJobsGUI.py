# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmJobsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmJobs(object):
    def setupUi(self, frmJobs):
        frmJobs.setObjectName("frmJobs")
        frmJobs.resize(820, 649)
        self.centralwidget = QtWidgets.QWidget(frmJobs)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout.addWidget(self.btnRun)
        self.btnDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnDown.setObjectName("btnDown")
        self.horizontalLayout.addWidget(self.btnDown)
        self.btnUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnUp.setObjectName("btnUp")
        self.horizontalLayout.addWidget(self.btnUp)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnReport = QtWidgets.QPushButton(self.centralwidget)
        self.btnReport.setObjectName("btnReport")
        self.horizontalLayout.addWidget(self.btnReport)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtActive = QtWidgets.QSpinBox(self.centralwidget)
        self.txtActive.setMinimum(1)
        self.txtActive.setObjectName("txtActive")
        self.horizontalLayout.addWidget(self.txtActive)
        self.cbOpen = QtWidgets.QCheckBox(self.centralwidget)
        self.cbOpen.setChecked(True)
        self.cbOpen.setObjectName("cbOpen")
        self.horizontalLayout.addWidget(self.cbOpen)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lvJobs = QtWidgets.QTreeWidget(self.centralwidget)
        self.lvJobs.setObjectName("lvJobs")
        self.lvJobs.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.lvJobs)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        frmJobs.setCentralWidget(self.centralwidget)
        self.stb = QtWidgets.QStatusBar(frmJobs)
        self.stb.setObjectName("stb")
        frmJobs.setStatusBar(self.stb)

        self.retranslateUi(frmJobs)
        QtCore.QMetaObject.connectSlotsByName(frmJobs)

    def retranslateUi(self, frmJobs):
        _translate = QtCore.QCoreApplication.translate
        frmJobs.setWindowTitle(_translate("frmJobs", "Job Manager"))
        self.btnRun.setText(_translate("frmJobs", "Run"))
        self.btnDown.setText(_translate("frmJobs", "Down"))
        self.btnUp.setText(_translate("frmJobs", "Up"))
        self.btnDelete.setText(_translate("frmJobs", "Delete"))
        self.btnReport.setText(_translate("frmJobs", "Report"))
        self.label.setText(_translate("frmJobs", "Active Session:"))
        self.cbOpen.setText(_translate("frmJobs", "Open Output"))
        self.btnClose.setText(_translate("frmJobs", "Close"))
        self.lvJobs.setSortingEnabled(True)

