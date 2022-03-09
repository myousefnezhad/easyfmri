# This file is part of the easy fMRI distribution 
#
# Copyright (c) 2014—2021 Tony Muhammad Yousefnezhad.
#
# Website: https://easyfmri.learningbymachine.com
# GitLab:  https://gitlab.com/easyfmri/easyfmri
# GitHub:  https://github.com/easyfmri/easyfmri
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#

from PyQt6.QtWidgets import *
from Preprocess.BIDS import BIDS
import numpy as np


class frmSelectSession(QDialog):
    def __init__(self, parent=None,setting=None):
        super(frmSelectSession, self).__init__(parent)
        # inputs

        try:
            self.bids = BIDS(Tasks=setting.Task,
                            SubRange=setting.SubRange, SubLen=setting.SubLen, SubPrefix=setting.SubPer,
                            SesRange=setting.ConRange, SesLen=setting.ConLen, SesPrefix=setting.ConPer,
                            RunRange=setting.RunRange, RunLen=setting.RunLen, RunPrefix=setting.RunPer)
        except Exception as e:
            print(str(e))
            return

        # self.Tasks          = strTaskList(setting.Task)
        # if self.Tasks is None:
        #     print("Tasks cannot find!")
        #     return        
        # self.SubRange       = strRange(setting.SubRange,Unique=True)
        # if self.SubRange is None:
        #     print("Subject Range is wrong!")
        #     return
        # self.SubSize        = len(self.SubRange)
        # self.ConRange       = strMultiRange(setting.ConRange, self.SubSize)
        # if self.ConRange is None:
        #     print("Counter Range is wrong!")
        #     return

        # self.RunRange       = strMultiLineRuns(setting.RunRange, self.SubRange, self.ConRange, setting.RunLen, setting.RunPer, False)
        # if self.RunRange is None:
        #     print("Run Range is wrong!")
        #     return

        # outputs
        self.TaskID  = None
        self.SubID   = None
        self.RunID   = None
        self.ConID   = None
        self.PASS    = False

        layout = QFormLayout()

        self.lblTask = QLabel("Task: ")
        self.txtTask = QComboBox()
        self.txtTask.addItem("", None)

        
        for task in np.unique([b[1] for b in self.bids]):
            self.txtTask.addItem(str(task))
        layout.addRow(self.lblTask, self.txtTask)

        self.lblSub = QLabel("Subject: ")
        self.txtSub = QComboBox()
        self.txtSub.addItem("",None)
        for sub in np.unique([b[3] for b in self.bids]):
            self.txtSub.addItem(str(sub))
        self.txtSub.currentIndexChanged.connect(self.txtSub_isChenged)
        layout.addRow(self.lblSub, self.txtSub)

        self.lblCon = QLabel("Counter: ")
        self.txtCon = QComboBox()
        self.txtCon.currentIndexChanged.connect(self.txtCon_isChanged)
        layout.addRow(self.lblCon, self.txtCon)

        self.lblRun = QLabel("Run: ")
        self.txtRun = QComboBox()
        layout.addRow(self.lblRun, self.txtRun)

        self.btnOK = QPushButton("OK")
        self.btnOK.clicked.connect(self.btnOK_onclick)

        self.btnCan = QPushButton("Cancel")
        self.btnCan.clicked.connect(self.btnCan_onclick)
        layout.addRow(self.btnCan,self.btnOK)


        self.setLayout(layout)
        self.setWindowTitle("Session Selector")
        self.exec()


    def txtSub_isChenged(self):
        sub = self.txtSub.currentText()
        self.txtRun.clear()
        self.txtCon.clear()
        if len(str(sub).strip()):
            self.txtCon.addItem("")

            condList = list() 
            for b in self.bids:
                if b[3] == sub:
                    condList.append(b[5])
            for con in np.unique(condList):
                self.txtCon.addItem(str(con))

    def txtCon_isChanged(self):
        sub = self.txtSub.currentText()
        con = self.txtCon.currentText()
        self.txtRun.clear()
        if len(str(sub).strip()) and len(str(con).strip()):
            self.txtRun.addItem("")
            runList = list() 
            for b in self.bids:
                if b[3] == sub and b[5] == con:
                    runList.append(np.reshape(b[6], -1))

            for run in np.unique(runList):
                self.txtRun.addItem(str(run))


    def btnOK_onclick(self):
        try:
            self.TaskID = self.txtTask.currentText()
            if not len(str(self.TaskID).strip()):
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Task is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        try:
            self.SubID  = self.txtSub.currentText()
            if not len(str(self.SubID).strip()):
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Subject is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        try:
            self.ConID = self.txtCon.currentText()
            if not len(str(self.ConID).strip()):
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Counter is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return


        try:
            self.RunID = self.txtRun.currentText()
            if not len(str(self.RunID).strip()):
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Run is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return


        self.PASS = True
        self.close()


    def btnCan_onclick(self):
        self.PASS = False
        self.close()
