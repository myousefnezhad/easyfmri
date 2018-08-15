#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from Base.utility import getVersion, getBuild, LoadEzData
from Base.dialogs import LoadFile, SaveFile


from GUI.frmEzMatGUI import *


class frmEzMat(Ui_frmEzMat):
    ui = Ui_frmEzMat()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmEzMat()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        dialog.setWindowTitle("easy fMRI Convert Easy Data to Matlab - V" + getVersion() + "B" + getBuild())
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
        file = SaveFile("Save MatLab file ...",["MatLab data (*.mat)"],'mat',\
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
        print("STEP1: Load data to memory ...")
        Out = LoadEzData(InFile)
        print("STEP2: Saving ...")
        io.savemat(OutFile,Out,appendmat=False,do_compression=True)
        print("DONE!")
        msgBox.setText("Data is converted")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmEzMat.show(frmEzMat)
    sys.exit(app.exec_())