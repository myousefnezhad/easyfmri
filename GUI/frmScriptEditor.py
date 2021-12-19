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

import os
import sys

import numpy as np
from PyQt5.QtWidgets import *
from Base.utility import fixstr, setParameters3
from Base.dialogs import SelectDir
from GUI.frmScriptEditorGUI import *
from Preprocess.BIDS import BIDS

class frmScriptEditor(Ui_frmScriptEditor):
    ui = Ui_frmScriptEditor()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, SubRange=None, SubLen=None, SubPer=None, ConRange=None, ConLen=None, ConPer=None,\
            RunRange=None, RunLen=None, RunPer=None, Task=None, DIR=None):
        global dialog
        global ui
        ui = Ui_frmScriptEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        self.set_value(self=self,SubRange=SubRange, SubLen=SubLen, SubPer=SubPer, ConRange=ConRange, ConLen=ConLen,\
                        ConPer=ConPer, RunRange=RunRange, RunLen=RunLen, RunPer=RunPer, Task=Task, DIR=DIR)
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_events(self):
        global ui
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnDIR.clicked.connect(self.btnDIR_click)
        ui.btnRun.clicked.connect(self.btnRun_onclick)


    def set_value(self, SubRange=None, SubLen=None, SubPer=None, ConRange=None, ConLen=None, ConPer=None,\
                RunRange=None, RunLen=None, RunPer=None, Task=None, DIR=None):
        global ui
        try:
            ui.txtSubRange.setText(SubRange)
        except:
            pass
        try:
            ui.txtSubLen.setValue(int(SubLen))
        except:
            pass
        if SubPer is not None:
            ui.txtSubPer.setText(SubPer)
        try:
            ui.txtRunRange.setText(RunRange)
        except:
            pass
        try:
            ui.txtRunLen.setValue(int(RunLen))
        except:
            pass
        if RunPer is not None:
            ui.txtRunPer.setText(RunPer)
        try:
            ui.txtConRange.setText(ConRange)
        except:
            pass
        try:
            ui.txtConLen.setValue(int(ConLen))
        except:
            pass
        if ConPer is not None:
            ui.txtConPer.setText(ConPer)
        if DIR is not None:
            ui.txtDIR.setText(DIR)
        if Task is not None:
            ui.txtTask.setText(Task)


    def btnExit_click(self):
        global dialog
        dialog.close()

    def btnDIR_click(self):
            global ui
            directory = SelectDir("Open Main Directory",ui.txtDIR.text())
            if len(directory):
                if os.path.isdir(directory) == False:
                    ui.txtDIR.setText("")
                else:
                    ui.txtDIR.setText(directory)

    def btnRun_onclick(self):
        # from Base.utility import strRange, strMultiRange
        # SubPer  = ui.txtSubPer.text()
        # RunPer  = ui.txtRunPer.text()
        # ConPer  = ui.txtConPer.text()
        # Task    = ui.txtTask.text()

        global ui
        msgBox = QMessageBox()
        Input   = ui.txtInput.text()
        Output  = ui.txtOutput.text()
        DIR     = ui.txtDIR.text()
        Script  = ui.txtScript.text()

        try:
            bids = BIDS(ui.txtTask.text(), ui.txtSubRange.text(), ui.txtSubLen.text(), ui.txtSubPer.text(),
                                            ui.txtConRange.text(), ui.txtConLen.text(), ui.txtConPer.text(),
                                            ui.txtRunRange.text(), ui.txtRunLen.text(), ui.txtRunPer.text())
        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        # try:
        #     SubRange = strRange(ui.txtSubRange.text(),Unique=True)
        #     if SubRange is None:
        #         raise Exception
        #     SubSize = len(SubRange)
        # except:
        #     msgBox.setText("Subject Range is wrong!")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Range of subjects is okay!")
        # try:
        #     SubLen = np.int32(ui.txtSubLen.text())
        #     1 / SubLen
        # except:
        #     msgBox.setText("Length of subjects must be an integer number")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Length of subjects is okay!")


        # try:
        #     ConRange = strMultiRange(ui.txtConRange.text(),SubSize)
        #     if ConRange is None:
        #         raise Exception
        #     if not (len(ConRange) == SubSize):
        #         msgBox.setText("Counter Size must be equal to Subject Size!")
        #         msgBox.setIcon(QMessageBox.Critical)
        #         msgBox.setStandardButtons(QMessageBox.Ok)
        #         msgBox.exec_()
        #         return False
        # except:
        #     msgBox.setText("Counter Range is wrong!")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Counter Range is okay!")
        # try:
        #     ConLen = np.int32(ui.txtConLen.text())
        #     1 / ConLen
        # except:
        #     msgBox.setText("Length of counter must be an integer number")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Length of Counter is okay!")


        # try:
        #     RunRange = strMultiRange(ui.txtRunRange.text(),SubSize)
        #     if RunRange is None:
        #         raise Exception
        #     if not (len(RunRange) == SubSize):
        #         msgBox.setText("Run Size must be equal to Subject Size!")
        #         msgBox.setIcon(QMessageBox.Critical)
        #         msgBox.setStandardButtons(QMessageBox.Ok)
        #         msgBox.exec_()
        #         return False
        # except:
        #     msgBox.setText("Run Range is wrong!")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Run Range is okay!")
        # try:
        #     RunLen = np.int32(ui.txtRunLen.value())
        #     1 / RunLen
        # except:
        #     msgBox.setText("Length of runs must be an integer number")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return False
        # print("Length of runs is valid")

        # if Task == "":
        #     msgBox = QMessageBox()
        #     msgBox.setText("There is no Task name")
        #     msgBox.setIcon(QMessageBox.Critical)
        #     msgBox.setStandardButtons(QMessageBox.Ok)
        #     msgBox.exec_()
        #     return

        if Input == "":
            msgBox = QMessageBox()
            msgBox.setText("There is no input structure")
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

        if Script == "":
            msgBox = QMessageBox()
            msgBox.setText("Script structure is not found!")
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

        RepCount = 0

        for (_, t, _, s, _, c, runs) in bids:
        # for si, s in enumerate(SubRange):
        #     for c in ConRange[si]:
                for r in runs:
                    SFile   =  setParameters3(Script, DIR, s, r, t, c)
                    if ui.cbInDynamic.isChecked():
                        InValue = setParameters3(Input,DIR, s, r, t, c)
                    else:
                        InValue = Input

                    if ui.cbOutDynamic.isChecked():
                        OutValue = setParameters3(Output,DIR, s, r, t, c)
                    else:
                        OutValue = Output

                    CountCurrRep = RepCount
                    print("SCRIPT: " + SFile)
                    print("Replacing " + InValue + " to " + OutValue + "...")
                    try:
                        if not os.path.isfile(SFile):
                            print(SFile + " - not found!")
                        else:
                            print(f"Processing {SFile}...")

                            scriptFile = open(SFile,"r")
                            scriptContent = scriptFile.read()
                            scriptFile.close()
                            while scriptContent.find(InValue) != -1:

                                scriptContent = scriptContent.replace(InValue, OutValue, 1)
                                RepCount = RepCount + 1
                    except Exception as e:
                        print(e)
                    CountCurrRep = RepCount - CountCurrRep

                    if not ui.cbDEMO.isChecked():
                        scriptFile = open(SFile,"w")
                        scriptFile.write(scriptContent)
                        scriptFile.close()
                        print(str(CountCurrRep) + " is replaced!")
                    else:
                        print("DEMO: " + str(CountCurrRep) + " is found!")

        if ui.cbDEMO.isChecked():
            msgBox.setText(str(RepCount) + " items are found!")
        else:
            msgBox.setText(str(RepCount) + " items are replaced!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmScriptEditor.show(frmScriptEditor)
    sys.exit(app.exec_())
