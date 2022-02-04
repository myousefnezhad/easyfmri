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
from IO.easyX import easyX
import numpy as np
import scipy.io as io
from PyQt6.QtWidgets import *
from Base.utility import getVersion, getBuild
from IO.EasyData import LoadEzData
from Base.dialogs import LoadFile, SaveFile


from GUI.frmEzEzxGUI import *


class frmEzEzX(Ui_frmEzEzx):
    ui = Ui_frmEzEzx()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmEzEzx()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        dialog.setWindowTitle("easy fMRI Convert Easy Data to easyX - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnLoadInFile_click)
        ui.btnOutFile.clicked.connect(self.btnSaveOutFile_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)

    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnLoadInFile_click(self):
        file = LoadFile("Load easy data header file ...",["easy data header (*.ezdata)"],'ezdata',\
                        os.path.dirname(ui.txtInFile.text()))
        if len(file):
            ui.txtInFile.setText(file)


    def btnSaveOutFile_click(self):
        file = SaveFile("Save easyX file ...",["easyX (*.ezx)"],'ezx',\
                        os.path.dirname(ui.btnOutFile.text()))
        if len(file):
            ui.txtOutFile.setText(file)


    def btnConvert_click(self):
        msgBox = QMessageBox()
        InFile = ui.txtInFile.text()
        if not len(InFile):
            msgBox.setText("Please enter easy data header file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(InFile):
            msgBox.setText("Easy data header file is not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter MatLab file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        print("Converting ...")
        try:
            print("STEP1: Load data to memory ...")
            Out = LoadEzData(InFile)
            assert Out is not None, "Cannot load easy data file!"
            print("STEP2: Saving ...")
            ezx = easyX()
            ezx.save(Out, OutFile)
        except Exception as e:
            print(str(e))
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        print("DONE!")
        msgBox.setText("Data is converted")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmEzEzX.show(frmEzEzX)
    sys.exit(app.exec_())