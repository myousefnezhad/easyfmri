#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
import numpy as np
import nibabel as nb
from frmfMRIConcatenatorGUI import *

from utility import fixstr,setParameters



class frmfMRIConcatenator(Ui_frmfMRIConcatenator):
    ui = Ui_frmfMRIConcatenator()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmfMRIConcatenator()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnFFile.clicked.connect(self.btnFFile_click)
        ui.btnSFile.clicked.connect(self.btnSFile_click)
        ui.btnOFile.clicked.connect(self.btnOFile_click)
        ui.btnConcatenate.clicked.connect(self.btnConcatenate_click)



    def btnClose_click(self):
        global dialog
        dialog.close()
        pass

    def btnFFile_click(self):
        global ui
        current = ui.txtFFile.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        ffile = dialog.getOpenFileName(None,"Open First File",current,"","",flags)[0]
        if len(ffile):
            if os.path.isfile(ffile) == False:
                ui.txtFFile.setText("")
            else:
                ui.txtFFile.setText(ffile)

    def btnSFile_click(self):
        global ui
        current = ui.txtSFile.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        sfile = dialog.getOpenFileName(None,"Open Second File",current,"","",flags)[0]
        if len(sfile):
            if os.path.isfile(sfile) == False:
                ui.txtSFile.setText("")
            else:
                ui.txtSFile.setText(sfile)

    def btnOFile_click(self):
        global ui
        current = ui.txtOFile.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        ofile = dialog.getSaveFileName(None,"Output File",current,"","",flags)[0]
        if len(ofile):
                ui.txtOFile.setText(ofile)


    def btnConcatenate_click(self):
        global ui
        ffile = ui.txtFFile.text()
        if not len(ffile):
            print("Please enter First File!")
            return
        if not os.path.isfile(ffile):
            print("First File not found!")
            return

        sfile = ui.txtSFile.text()
        if not len(sfile):
            print("Please enter Second File!")
            return

        if not os.path.isfile(sfile):
            print("First Second not found!")
            return

        ofile = ui.txtOFile.text()
        if not len(ofile):
            print("Please enter Output File!")
            return
        try:
            dim = np.int32(ui.txtDim.value()) - 1
        except:
            return
        print("Generating Output File ...")
        try:
            ffileHDR = nb.load(ffile)
            ffileIMG = ffileHDR.get_data()
        except:
            print("Cannot load First File!")
            return
        try:
            sfileHDR = nb.load(sfile)
            sfileIMG = sfileHDR.get_data()
        except:
            print("Cannot load Second File!")
            return

        ofileIMG = np.concatenate((ffileIMG,sfileIMG),axis=dim)
        ofileHDR = nb.Nifti1Image(ofileIMG,ffileHDR.affine)
        nb.save(ofileHDR,ofile)

        print("Output is generated!")
        msgBox = QMessageBox()
        msgBox.setText("Output is generated!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmfMRIConcatenator.show(frmfMRIConcatenator)
    sys.exit(app.exec_())