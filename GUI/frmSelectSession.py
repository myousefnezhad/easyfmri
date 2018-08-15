from PyQt5.QtWidgets import *
from Base.utility import strRange,strMultiRange
import numpy as np


class frmSelectSession(QDialog):
    def __init__(self, parent=None,setting=None):
        super(frmSelectSession, self).__init__(parent)
        # inputs
        self.SubRange       = strRange(setting.SubRange,Unique=True)
        if self.SubRange is None:
            print("Subject Range is wrong!")
            return
        self.SubSize        = len(self.SubRange)
        self.ConRange       = strMultiRange(setting.ConRange, self.SubSize)
        if self.ConRange is None:
            print("Counter Range is wrong!")
            return

        self.RunRange       = strMultiRange(setting.RunRange, self.SubSize)
        if self.RunRange is None:
            print("Run Range is wrong!")
            return

        # outputs
        self.SubID   = None
        self.RunID   = None
        self.ConID   = None
        self.PASS    = False

        layout = QFormLayout()

        self.lblSub = QLabel("Subject: ")
        self.txtSub = QComboBox()
        self.txtSub.addItem("",None)
        for subindx, sub in enumerate(self.SubRange):
            self.txtSub.addItem(str(sub),subindx)
        self.txtSub.currentIndexChanged.connect(self.txtSub_isChenged)
        layout.addRow(self.lblSub, self.txtSub)

        self.lblRun = QLabel("Run: ")
        self.txtRun = QComboBox()
        layout.addRow(self.lblRun, self.txtRun)

        self.lblCon = QLabel("Counter: ")
        self.txtCon = QComboBox()
        layout.addRow(self.lblCon, self.txtCon)


        self.lblTask = QLabel()
        self.lblTask.setText("Task:")
        self.txtTask = QLineEdit()
        self.txtTask.setText(setting.Task)
        self.txtTask.setReadOnly(True)
        layout.addRow(self.lblTask,self.txtTask)


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
            self.txtRun.addItem("")
            for run in self.RunRange[subindx]:
                self.txtRun.addItem(str(run))

            self.txtCon.addItem("")
            for con in self.ConRange[subindx]:
                self.txtCon.addItem(str(con))


    def btnOK_onclick(self):
        try:
            self.SubID = np.int32(self.txtSub.currentText())
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
            self.RunID = np.int32(self.txtRun.currentText())
            find = False
            for run in self.RunRange[SubIndex]:
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
        try:
            self.ConID = np.int32(self.txtCon.currentText())
            find = False
            for cond in self.ConRange[SubIndex]:
                if self.ConID == cond:
                    find = True
                    break
            if not find:
                raise Exception
        except:
            msgBox = QMessageBox()
            msgBox.setText("Counter is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        self.PASS = True
        self.close()


    def btnCan_onclick(self):
        self.PASS = False
        self.close()
