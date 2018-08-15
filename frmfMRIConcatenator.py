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
        ui.btnAdd.clicked.connect(self.btnAdd_click)
        ui.btnOFile.clicked.connect(self.btnOFile_click)
        ui.btnConcatenate.clicked.connect(self.btnConcatenate_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)



    def btnClose_click(self):
        global dialog
        dialog.close()
        pass



    def btnAdd_click(self):
        global ui
        current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        ifile = dialog.getOpenFileName(None,"Open First File",current,"","",flags)[0]
        if len(ifile):
            if os.path.isfile(ifile):
                item = QtWidgets.QListWidgetItem(ifile)
                ui.lwFiles.addItem(item)

    def btnRemove_click(self):
        if not len(ui.lwFiles.selectedItems()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        ui.lwFiles.takeItem(ui.lwFiles.currentRow())



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

        if ui.lwFiles.count() < 1:
            msgBox = QMessageBox()
            msgBox.setText("There is no input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.lwFiles.count() < 2:
            msgBox = QMessageBox()
            msgBox.setText("You must select at least two files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        files = []
        for index in range(ui.lwFiles.count()):
            file = ui.lwFiles.item(index).text()
            if not os.path.isfile(file):
                print(file + " not found!")
                return
            files.append(file)

        ofile = ui.txtOFile.text()
        if not len(ofile):
            print("Please enter Output File!")
            msgBox = QMessageBox()
            msgBox.setText("Please enter Output File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        try:
            dim = np.int32(ui.txtDim.value()) - 1
        except:
            return
        print("Generating Output File ...")

        ofileIMG = None
        try:
            for filename in files:
                fileHDR = nb.load(filename)
                fileIMG = fileHDR.get_data()
                print("Loading File: " + filename)
                if ofileIMG is None:
                    ofileIMG = fileIMG.copy()
                else:
                    ofileIMG = np.concatenate((ofileIMG, fileIMG), axis=dim)
        except:
            print("Cannot load files!")
            return
        ofileHDR = nb.Nifti1Image(ofileIMG,fileHDR.affine)
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