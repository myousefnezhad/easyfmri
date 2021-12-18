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

from PyQt5.QtWidgets import *
from Preprocess.BIDS import strTaskList,strRange,strMultiRange,strMultiLineRuns
import numpy as np


class frmSelectSession(QDialog):
    def __init__(self, parent=None,setting=None):
        super(frmSelectSession, self).__init__(parent)
        # inputs
        self.Tasks          = strTaskList(setting.Task)
        if self.Tasks is None:
            print("Tasks cannot find!")
            return
        
        self.SubRange       = strRange(setting.SubRange,Unique=True)
        if self.SubRange is None:
            print("Subject Range is wrong!")
            return
        self.SubSize        = len(self.SubRange)
        self.ConRange       = strMultiRange(setting.ConRange, self.SubSize)
        if self.ConRange is None:
            print("Counter Range is wrong!")
            return

        self.RunRange       = strMultiLineRuns(setting.RunRange, self.SubRange, self.ConRange, setting.RunLen, setting.RunPer, False)
        if self.RunRange is None:
            print("Run Range is wrong!")
            return

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
        for taskindx, task in enumerate(self.Tasks):
            self.txtTask.addItem(str(task), taskindx)
        layout.addRow(self.lblTask, self.txtTask)

        self.lblSub = QLabel("Subject: ")
        self.txtSub = QComboBox()
        self.txtSub.addItem("",None)
        for subindx, sub in enumerate(self.SubRange):
            self.txtSub.addItem(str(sub),subindx)
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
        self.exec_()


    def txtSub_isChenged(self):
        subindx = self.txtSub.currentData()
        self.txtRun.clear()
        self.txtCon.clear()
        if subindx is not None:
            self.txtCon.addItem("")
            for conindx, con in enumerate(self.ConRange[subindx]):
                self.txtCon.addItem(str(con), conindx)

    def txtCon_isChanged(self):
        subindx = self.txtSub.currentData()
        conindx = self.txtCon.currentData()
        self.txtRun.clear()
        if (subindx is not None) and (conindx is not None):
            self.txtRun.addItem("")
            for runindx, run in enumerate(self.RunRange[subindx][conindx]):
                self.txtRun.addItem(str(run), runindx)


    def btnOK_onclick(self):
        try:
            self.TaskID = self.txtTask.currentText()
            if self.TaskID is None or not len(str(self.TaskID).strip()):
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Task is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        try:
            self.SubID  = np.int32(self.txtSub.currentText())
            SubIndex = None
            for subinx,sub in enumerate(self.SubRange):
                if sub == self.SubID:
                    SubIndex = subinx
                    break
            if SubIndex is None:
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Subject is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        try:
            self.ConID = np.int32(self.txtCon.currentText())
            find = False
            CondIndex = None
            for condindx, cond in enumerate(self.ConRange[SubIndex]):
                if self.ConID == cond:
                    CondIndex = condindx
                    find = True
                    break
            if not find or CondIndex is None:
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Counter is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return


        try:
            self.RunID = np.int32(self.txtRun.currentText())
            find = False
            for run in self.RunRange[SubIndex][CondIndex]:
                if self.RunID == run:
                    find = True
                    break
            if not find:
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Run is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return


        self.PASS = True
        self.close()


    def btnCan_onclick(self):
        self.PASS = False
        self.close()
