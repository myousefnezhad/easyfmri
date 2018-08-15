#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *

from Base.utility import getDirFSLAtlas, getVersion, getBuild
from Base.dialogs import LoadFile, SaveFile, LoadMultiFile
from GUI.frmCombineROIGUI import *


class frmCombineROI(Ui_frmCombineROI):
    ui = Ui_frmCombineROI()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        global OutSize, currentFile, currentSize
        ui = Ui_frmCombineROI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.tvArea.setColumnCount(2)
        ui.tvArea.setHeaderLabels(['Affine', 'File'])
        ui.tvArea.setColumnWidth(0,50)

        ui.cbMetric.addItem("Intersection","int")
        ui.cbMetric.addItem("Union","uni")

        dialog.setWindowTitle("easy fMRI combine ROI - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnOFile.clicked.connect(self.btnOFile_click)
        ui.btnAdd.clicked.connect(self.btnAdd_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)
        ui.btnAffine.clicked.connect(self.btnAffine_click)
        ui.btnRun.clicked.connect(self.btnRun_click)


    def btnClose_click(self):
        global dialog
        dialog.close()
        pass

    def btnOFile_click(self):
        global ui
        ofile = SaveFile('Save ROI ...',['ROI images (*.nii.gz)'],'nii.gz',os.path.dirname(ui.txtOFile.text()))
        if len(ofile):
                ui.txtOFile.setText(ofile)

    def btnAdd_click(self):
        filenames = LoadMultiFile('Save ROI ...',['ROI images (*.nii.gz *.nii)', 'All files (*.*)'],'nii.gz')
        for file in filenames:
            if len(file):
                item = QtWidgets.QTreeWidgetItem()
                item.setText(0,"")
                item.setText(1, str(file))
                ui.tvArea.addTopLevelItem(item)

    def btnRemove_click(self):
        if not len(ui.tvArea.selectedItems()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        ui.tvArea.takeTopLevelItem(ui.tvArea.indexOfTopLevelItem(ui.tvArea.selectedItems()[0]))

    def btnAffine_click(self):
        if not len(ui.tvArea.selectedItems()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        aindx = ui.tvArea.indexOfTopLevelItem(ui.tvArea.selectedItems()[0])
        for index in range(ui.tvArea.topLevelItemCount()):
            ui.tvArea.topLevelItem(index).setText(0, "*") if index == aindx else ui.tvArea.topLevelItem(index).setText(0, "")


    def btnRun_click(self):
        msgBox = QMessageBox()

        if ui.tvArea.topLevelItemCount() < 1:
            msgBox.setText("There is no input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        ofile = ui.txtOFile.text()
        if not len(ofile):
            print("Please enter Output File!")
            msgBox.setText("Please enter Output File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        aindx = -1
        for index in range(ui.tvArea.topLevelItemCount()):
            if (ui.tvArea.topLevelItem(index).text(0) == "*"):
                aindx = index

        if aindx < 0:
            print("Please select affine file")
            msgBox.setText("Please select affine file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        print("Combining ROI ...")
        OutIMG = None
        OutSize = None
        affine = None
        counter = 0
        for index in range(ui.tvArea.topLevelItemCount()):
            # Get file name
            filename = ui.tvArea.topLevelItem(index).text(1)
            if not os.path.isfile(filename):
                print("Cannot find input file: " + filename)
                msgBox.setText("Cannot find input file: " + filename)
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            # Load Data
            try:
                fileHDR = nb.load(filename)
                fileIMG = fileHDR.get_data()
            except:
                print("Cannot load input file: " + filename)
                msgBox.setText("Cannot load input file: " + filename)
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            # Check Size
            if OutSize is None:
                OutSize = np.shape(fileIMG)
                OutIMG  = np.zeros(OutSize)
            elif OutSize != np.shape(fileIMG):
                print("Size of file: " + filename + " is not matched!")
                msgBox.setText("Size of file: " + filename + " is not matched!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            # Get Affine
            if len(ui.tvArea.topLevelItem(index).text(1)):
                affine = fileHDR.affine
            # Normalization
            fileIMG = fileIMG / np.max(fileIMG)
            # Store
            OutIMG = OutIMG + fileIMG
            # Counting files
            counter = counter + 1

        if affine is None:
            print("Cannot find affine!")
            msgBox.setText("Cannot find affine!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.cbMetric.currentData() == "int":
            OutIMG = OutIMG / counter
            OutIMG[np.where(OutIMG < 1)] = 0
        # For both intersection and union
        OutIMG[np.where(OutIMG != 0)] = 1


        OutHDR = nb.Nifti1Image(OutIMG,affine)
        nb.save(OutHDR,ofile)

        NumVoxels = np.shape(OutIMG)
        NumVoxels = NumVoxels[0] * NumVoxels[1] * NumVoxels[2]
        print("Number of all voxels: %d " % NumVoxels)
        NumROIVoxel = len(OutIMG[np.where(OutIMG != 0)])
        print("Number of selected voxles in ROI: %d" % NumROIVoxel)
        print("ROI is generated!")

        msgBox.setText("ROI is generated!\nNumber of all voxels: " + str(NumVoxels) + \
                       "\nNumber of selected voxles in ROI: " + str(NumROIVoxel))
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmCombineROI.show(frmCombineROI)
    sys.exit(app.exec_())