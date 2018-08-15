#!/usr/bin/env python3
import configparser as cp
import os
import platform
import sys

import subprocess as sub

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *

from GUI.frmTransformationMatrix import *

from Base.utility import getSUMADir, getSUMABothHem, getSUMALeftHem, getSUMARightHem, getSUMAMNI, RunCMD

from GUI.frmVisualizationGUI import *
from GUI.frmMatNITF import *
from GUI.frmNITFAFNI import *


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

        ui.cbHemisphere.addItem("Both")
        ui.cbHemisphere.addItem("Left")
        ui.cbHemisphere.addItem("Right")

        p = sub.Popen(['which', 'afni'], stdout=sub.PIPE, stderr=sub.PIPE)
        FAFNI, errors = p.communicate()
        FAFNI = FAFNI.decode("utf-8").replace("\n","")
        if not len(FAFNI):
            print("Cannot find AFNI Path!")
        elif not os.path.isfile(FAFNI):
            print("Cannot find AFNI binary file!")
        else:
            ui.txtFAFNI.setText(FAFNI)

        p = sub.Popen(['which', 'suma'], stdout=sub.PIPE, stderr=sub.PIPE)
        FSUMA, errors = p.communicate()
        FSUMA = FSUMA.decode("utf-8").replace("\n","")
        if not len(FSUMA):
            print("Cannot find SUMA Path!")
        elif not os.path.isfile(FSUMA):
            print("Cannot find SUMA binary file!")
        else:
            ui.txtFSUMA.setText(FSUMA)

        if not os.path.isdir(getSUMADir()):
            print("Cannot find SUMA directory!")
        else:
            ui.txtDSUMA.setText(getSUMADir())
            ui.txtSUMAMNI.setText(getSUMAMNI())

            if not os.path.isfile(getSUMADir() + getSUMABothHem()):
                print("Cannot find SUMA Both Hemisphere!")
            else:
                ui.txtBSUMA.setText(getSUMABothHem())

            if not os.path.isfile(getSUMADir() + getSUMALeftHem()):
                print("Cannot find SUMA Left Hemisphere!")
            else:
                ui.txtLSUMA.setText(getSUMALeftHem())

            if not os.path.isfile(getSUMADir() + getSUMARightHem()):
                print("Cannot find SUMA Right Hemisphere!")
            else:
                ui.txtRSUMA.setText(getSUMARightHem())

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
        ui.btnMNConvert.clicked.connect(self.btnMNConvert_click)
        ui.btnNAConvert.clicked.connect(self.btnNAConvert_click)
        ui.btnTranformation.clicked.connect(self.btnTranformation_click)

# Exit function
    def btnClose_click(self):
       global dialog, parent
       dialog.close()

    def btnMNConvert_click(self):
        frmMatNITF.show(frmMatNITF)

    def btnNAConvert_click(self):
        frmNITFAFNI.show(frmNITFAFNI)

    def btnTranformation_click(self):
        frmTansformationMatrix.show(frmTansformationMatrix)

    def btnFAFNI_click(self):
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open AFNI file ...", os.path.dirname(ui.txtFAFNI.text()),
                                           options=QFileDialog.DontUseNativeDialog)[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFAFNI.setText(filename)

    def btnFSUMA_click(self):
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open SUMA file ...", os.path.dirname(ui.txtFSUMA.text()),
                                           options=QFileDialog.DontUseNativeDialog)[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFSUMA.setText(filename)

    def btnWork_click(self):
        current = ui.txtWork.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        directory = dialog.getExistingDirectory(None,"Open Working Directory",current,flags)
        if len(directory):
            if os.path.isdir(directory):
                ui.txtWork.setText(directory)

    def btnDSUMA_click(self):
        current = ui.txtDSUMA.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        directory = dialog.getExistingDirectory(None,"Open SUMA Directory",current,flags)
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