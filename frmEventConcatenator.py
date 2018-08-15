#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
import numpy as np
import nibabel as nb
from frmEventConcatenatorGUI import *

from utility import fixstr,setParameters



class frmEventConcatenator(Ui_frmEventConcatenator):
    ui = Ui_frmEventConcatenator()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmEventConcatenator()
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

        if ofile == ffile:
            print("Output file cannot be equal with the First File")
            return

        if ofile == sfile:
            print("Output file cannot be equal with the Second File")
            return

        try:
            offset1 = np.int32(ui.txtfDim.value()) - 1
        except:
            return

        try:
            offset2 = np.int32(ui.txtsDim.value()) - 1
        except:
            return

        offset = [offset1, offset2]

        print("Generating Output File ...")

        files = [ffile, sfile]
        with open(ofile,"w") as outfile:
            if len(ui.txtHDR.text()):
                outfile.write(ui.txtHDR.text())
            for fnameinx, fname in enumerate(files):
                with open(fname) as infile:
                    for lineinx, line in enumerate(infile):
                        if lineinx > offset[fnameinx]:
                            outfile.write(line)

        print("Output is generated!")
        msgBox = QMessageBox()
        msgBox.setText("Output is generated!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmEventConcatenator.show(frmEventConcatenator)
    sys.exit(app.exec_())