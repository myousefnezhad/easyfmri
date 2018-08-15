#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
import numpy as np
from frmRenameFileGUI import *

from utility import fixstr,setParameters3



class frmRenameFile(Ui_frmRenameFile):
    ui = Ui_frmRenameFile()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, SubFrom=None, SubTo=None, SubLen=None, SubPer=None,\
             Run=None, RunLen=None, RunPer=None, Task=None, DIR=None):
        global dialog
        global ui
        ui = Ui_frmRenameFile()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)



        self.set_value(self=self,SubFrom=SubFrom, SubTo=SubTo, SubLen=SubLen, SubPer=SubPer,Run=Run, RunLen=RunLen, RunPer=RunPer, Task=Task, DIR=DIR)

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_events(self):
        global ui
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnDIR.clicked.connect(self.btnDIR_click)
        ui.btnRun.clicked.connect(self.btnRun_onclick)


    def set_value(self, SubFrom=None, SubTo=None, SubLen=None, SubPer=None,\
                 Run=None, RunLen=None, RunPer=None, Task=None, DIR=None):
        global ui
        try:
            ui.txtSubFrom.setValue(int(SubFrom))
        except:
            pass
        try:
            ui.txtSubTo.setValue(int(SubTo))
        except:
            pass

        try:
            ui.txtSubLen.setValue(int(SubLen))
        except:
            pass

        if SubPer is not None:
            ui.txtSubPer.setText(SubPer)

        if Run is not None:
            ui.txtRunNum.setText(Run)

        try:
            ui.txtRunLen.setValue(int(RunLen))
        except:
            pass

        if RunPer is not None:
            ui.txtRunPer.setText(RunPer)

        if DIR is not None:
            ui.txtDIR.setText(DIR)

        if Task is not None:
            ui.txtTask.setText(Task)

    def btnExit_click(self):
        global dialog
        dialog.close()

        pass

    def btnDIR_click(self):
            import numpy as np
            global ui
            current = ui.txtDIR.text()
            if not len(current):
                current = os.getcwd()
            flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
            dialog = QFileDialog()
            directory = dialog.getExistingDirectory(None, "Open Main Directory", current, flags)
            if len(directory):
                if os.path.isdir(directory) == False:
                    ui.txtDIR.setText("")
                else:
                    ui.txtDIR.setText(directory)

    def btnRun_onclick(self):
        global ui

        SubFrom = np.int32(ui.txtSubFrom.value())
        SubTo   = np.int32(ui.txtSubTo.value())
        SubLen  = np.int32(ui.txtSubLen.value())
        SubPer  = ui.txtSubPer.text()

        RunLen  = np.int32(ui.txtRunLen.value())
        RunPer  = ui.txtRunPer.text()

        ConFrom = np.int32(ui.txtConFrom.value())
        ConTo   = np.int32(ui.txtConTo.value())
        ConLen  = np.int32(ui.txtConLen.value())
        ConPer  = ui.txtConPer.text()

        Input   = ui.txtInput.text()
        Output  = ui.txtOutput.text()

        Task    = ui.txtTask.text()
        DIR     = ui.txtDIR.text()


        if SubFrom > SubTo:
            msgBox = QMessageBox()
            msgBox.setText("Subject To must be greater than Subject From")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if SubLen < 1:
            msgBox = QMessageBox()
            msgBox.setText("Subject Len must be greater than 1!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if len(ui.txtRunNum.text()) <= 0:
            msgBox = QMessageBox()
            msgBox.setText("There is no Run Number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        RunList = np.int32(ui.txtRunNum.text().replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())
        Run = []
        if len(RunList) == 1:
            for _ in range(SubFrom, SubTo + 1):
                Run.append(RunList[0])

        elif (len(RunList) == (SubTo - SubFrom + 1)):
            Run = RunList.copy()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Run Number has wrong elements")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ConTo < ConFrom:
            msgBox = QMessageBox()
            msgBox.setText("Counter To is smaller than From")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ConLen < 1:
            msgBox = QMessageBox()
            msgBox.setText("Counter Len is smaller than 1")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return


        if Input == "":
            msgBox = QMessageBox()
            msgBox.setText("There is no input structure")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if Output == "":
            msgBox = QMessageBox()
            msgBox.setText("There is no output structure")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if Task == "":
            msgBox = QMessageBox()
            msgBox.setText("There is no Task name")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if DIR == "":
            msgBox = QMessageBox()
            msgBox.setText("Please select the main directory")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not os.path.isdir(DIR):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find the main directory")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return


        for si, s in enumerate(range(SubFrom, SubTo + 1)):
            for r in range(1, Run[si] + 1):
                for c in range(ConFrom, ConTo+1):
                    InAdd = setParameters3(Input,DIR, fixstr(s,SubLen,SubPer),\
                                               fixstr(r,RunLen,RunPer),Task,\
                                               fixstr(c,ConLen,ConPer))
                    OutAdd = setParameters3(Output,DIR,fixstr(s,SubLen,SubPer),\
                                               fixstr(r,RunLen,RunPer),Task,\
                                               fixstr(c,ConLen,ConPer))
                    try:
                        if not os.path.isfile(InAdd):
                            print(InAdd + " - not found!")
                        else:
                            print("MOVE: " + InAdd + " - running ...")
                            os.rename(InAdd,OutAdd)
                            print("TO: " + OutAdd + " - DONE!")
                    except Exception as e:
                        print(e)

    pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmRenameFile.show(frmRenameFile)
    sys.exit(app.exec_())
