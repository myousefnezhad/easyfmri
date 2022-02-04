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

import configparser as cp
import os
import platform
import sys
import subprocess as sub

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *

from Base.utility import RunCMD
from Base.afni import AFNI
from Base.tools import Tools
from Base.dialogs import LoadFile, SaveFile, SelectDir

from GUI.frmVisualizationGUI import *


class MainWindow(QtWidgets.QMainWindow):
    parent = None
    def __init__(self,parentin=None):
        super().__init__()
        global parent
        if parentin is not None:
            parent = parentin

    def closeEvent(self,event):
        global parent
        try:
            if parent is not None:
                parent.show()
        except:
            pass
    pass

class frmVisalization(Ui_frmVisalization):
    ui      = Ui_frmVisalization()
    dialog  = None
# This function is run when the main form start
# and initiate the default parameters.
    def show(self,parentin=None):
        from Base.utility import getVersion, getBuild, getDirSpaceINI, getDirSpace
        global dialog, ui, parent
        ui = Ui_frmVisalization()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        if parentin is not None:
            dialog = MainWindow(parentin)
        else:
            dialog = MainWindow()
        ui.setupUi(dialog)
        ui.tabWidget.setCurrentIndex(0)
        self.set_events(self)

        tools = Tools()
        tools.combo(ui.cbTools)

        ui.cbHemisphere.addItem("Both")
        ui.cbHemisphere.addItem("Left")
        ui.cbHemisphere.addItem("Right")


        afni = AFNI()
        afni.setting()

        if not afni.Validate:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find AFNI setting!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            ui.txtFAFNI.setText(afni.AFNI)
            ui.txtFSUMA.setText(afni.SUMA)
            ui.txtDSUMA.setText(afni.SUMADIR)
            ui.txtSUMAMNI.setText(afni.MNI)
            ui.txtBSUMA.setText(afni.Both)
            ui.txtLSUMA.setText(afni.Left)
            ui.txtRSUMA.setText(afni.Right)

        dialog.setWindowTitle("easy fMRI visualization - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

# This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnFAFNI.clicked.connect(self.btnFAFNI_click)
        ui.btnFSUMA.clicked.connect(self.btnFSUMA_click)
        ui.btnWork.clicked.connect(self.btnWork_click)
        ui.btnDSUMA.clicked.connect(self.btnDSUMA_click)
        ui.btnAFNI.clicked.connect(self.btnRunAFNI_click)
        ui.btnSUMA.clicked.connect(self.btnRunSUMA_click)
        ui.btnTools.clicked.connect(self.btnTools_click)


# Exit function
    def btnClose_click(self):
       global dialog, parent
       dialog.close()

    def btnTools_click(self):
        tools = Tools()
        tools.run(ui.cbTools.currentData())


    def btnFAFNI_click(self):
        filename = LoadFile("Open AFNI binary file ...",currentDirectory=os.path.dirname(ui.txtFAFNI.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFAFNI.setText(filename)

    def btnFSUMA_click(self):
        filename = LoadFile("Open SUMA binary file ...",currentDirectory=os.path.dirname(ui.txtFSUMA.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFSUMA.setText(filename)

    def btnWork_click(self):
        directory = SelectDir("Open Working Directory",ui.txtWork.text())
        if len(directory):
            if os.path.isdir(directory):
                ui.txtWork.setText(directory)

    def btnDSUMA_click(self):
        directory = SelectDir("Open SUMA Visualization Directory",ui.txtDSUMA.text())
        if len(directory):
            if os.path.isdir(directory):
                ui.txtDSUMA.setText(directory)

    def btnRunAFNI_click(self):
        msgBox = QMessageBox()
        afniCMD = ui.txtFAFNI.text()
        if not os.path.isfile(afniCMD):
            msgBox.setText("Cannot find afni binary file")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        directory = ui.txtWork.text()
        if not os.path.isdir(directory):
            directory = os.getcwd()
        RunCMD("cd " + directory + " && " + afniCMD + " -niml &")

    def btnRunSUMA_click(self):
        msgBox = QMessageBox()
        sumaCMD = ui.txtFSUMA.text()
        if not os.path.isfile(sumaCMD):
            msgBox.setText("Cannot find SUMA binary file")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        sumaDIR = ui.txtDSUMA.text()
        if not os.path.isdir(sumaDIR):
            msgBox.setText("Cannot find SUMA directory")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        sumaSpect = None
        if ui.cbHemisphere.currentText() == "Both":
            sumaSpect = sumaDIR + ui.txtBSUMA.text()
        elif ui.cbHemisphere.currentText() == "Left":
            sumaSpect = sumaDIR + ui.txtLSUMA.text()
        elif ui.cbHemisphere.currentText() == "Right":
            sumaSpect = sumaDIR + ui.txtRSUMA.text()

        if sumaSpect is None:
            msgBox.setText("Cannot find SUMA Hemisphere!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not len(ui.txtSUMAMNI.text()):
            msgBox.setText("Cannot find SUMA MNI File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        sumaMNI = sumaDIR + ui.txtSUMAMNI.text()
        RunCMD("cd " + sumaDIR + " && " + sumaCMD + " -spec " + sumaSpect + " -sv " + sumaMNI)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmVisalization.show(frmVisalization)
    sys.exit(app.exec_())