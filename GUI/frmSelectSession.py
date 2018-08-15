from PyQt5.QtWidgets import *


class frmSelectSession(QDialog):
    def __init__(self, parent=None,setting=None):
        super(frmSelectSession, self).__init__(parent)
        # inputs
        self.SubFrom = setting.SubFrom
        self.SubTo   = setting.SubTo

        self.ConFrom = setting.ConFrom
        self.ConTo   = setting.ConTo

        self.Run     = setting.Run
        # outputs
        self.SubID   = None
        self.RunID   = None
        self.ConID   = None
        self.PASS    = False

        layout = QFormLayout()

        self.btnSub = QPushButton("Subject")
        self.btnSub.clicked.connect(self.getSub_onclick)
        self.txtSub = QLineEdit()
        self.txtSub.setReadOnly(True)
        layout.addRow(self.btnSub, self.txtSub)

        self.btnRun = QPushButton("Run")
        self.btnRun.clicked.connect(self.getRun_onclick)
        self.txtRun = QLineEdit()
        self.txtRun.setReadOnly(True)
        layout.addRow(self.btnRun, self.txtRun)


        self.lblTask = QLabel()
        self.lblTask.setText("Task:")
        self.txtTask = QLineEdit()
        self.txtTask.setText(setting.Task)
        self.txtTask.setReadOnly(True)
        layout.addRow(self.lblTask,self.txtTask)

        self.btnCon = QPushButton("Counter")
        self.btnCon.clicked.connect(self.getCon_onclick)
        self.txtCon = QLineEdit()
        self.txtCon.setReadOnly(True)
        layout.addRow(self.btnCon, self.txtCon)

        self.btnOK = QPushButton("OK")
        self.btnOK.clicked.connect(self.btnOK_onclick)

        self.btnCan = QPushButton("Cancel")
        self.btnCan.clicked.connect(self.btnCan_onclick)
        layout.addRow(self.btnCan,self.btnOK)


        self.setLayout(layout)
        self.setWindowTitle("Session Selector")
        self.exec_()


    def getSub_onclick(self):
        num, ok = QInputDialog.getInt(self, "Select Subject", "Enter Subject Number",value=self.SubFrom,min=self.SubFrom,max=self.SubTo)

        if ok:
            self.txtSub.setText(str(num))
            self.txtRun.setText("")
            self.SubID = num

    def getCon_onclick(self):
        num, ok = QInputDialog.getInt(self, "Select Counter", "Enter Subject Number",value=self.ConFrom,min=self.ConFrom,max=self.ConTo)

        if ok:
            self.txtCon.setText(str(num))
            self.ConID = num

    def getRun_onclick(self):
        import numpy as np
        if self.txtSub.text() == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select a subject first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            Run = np.int32(str(self.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())
            maxRun = Run[self.SubID - self.SubFrom]

            num, ok = QInputDialog.getInt(self, "Select Run", "Enter Run Number", value=1,
                                          min=1, max=maxRun)

            if ok:
                self.txtRun.setText(str(num))
                self.RunID = num
            pass


    def btnOK_onclick(self):
        if self.txtSub.text() == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select a subject first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        elif self.txtRun.text() == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select a run first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        elif self.txtCon.text() == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select a counter first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            self.PASS = True
            self.close()
        pass

    def btnCan_onclick(self):
        self.PASS = False
        self.close()
        pass
