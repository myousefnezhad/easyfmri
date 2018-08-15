#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *

from Base.utility import getDirFSLAtlas
from Base.dialogs import LoadFile, SaveFile
from GUI.frmAtlasROIGUI import *


class frmAtlasROI(Ui_frmAtlasROI):
    ui = Ui_frmAtlasROI()
    dialog = None
    OutSize = None
    currentSize = None
    currentFile = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        global OutSize, currentFile, currentSize
        ui = Ui_frmAtlasROI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.tvArea.setColumnCount(4)
        ui.tvArea.setHeaderLabels(['Affine','From','To','File'])
        ui.tvArea.setColumnWidth(0,50)

        OutSize = None
        currentFile = None
        currentSize = None

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnOFile.clicked.connect(self.btnOFile_click)
        ui.btnFile.clicked.connect(self.btnFile_click)
        ui.btnAdd.clicked.connect(self.btnAdd_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)
        ui.btnRun.clicked.connect(self.btnRun_click)
        ui.btnAffine.clicked.connect(self.btnAffine_click)


    def btnClose_click(self):
        global dialog
        dialog.close()
        pass

    def btnOFile_click(self):
        global ui
        ofile = SaveFile('Save ROI ...',['ROI images (*.nii.gz)'],'nii.gz',os.path.dirname(ui.txtOFile.text()))
        if len(ofile):
                ui.txtOFile.setText(ofile)

    def btnFile_click(self):
        global ui, OutSize, currentFile, currentSize

        if len(ui.txtFile.text()):
            currDIR = os.path.dirname(ui.txtFile.text())
        else:
            currDIR = getDirFSLAtlas()
        filename = LoadFile('Open atlas image ...',['Atlas images (*.nii.gz)'],'nii.gz', currDIR)
        if len(filename):
            if not os.path.isfile(filename):
                print("Image file not found!")
                return
            ui.txtFile.setText(filename)
            try:
                fileHDR = nb.load(filename)
                fileIMG = fileHDR.get_data()
                fileSize = np.shape(fileIMG)


                if  (OutSize != None) and (OutSize != fileSize):
                    print("All input files must be in the same size!")
                    msgBox = QMessageBox()
                    msgBox.setText("All input files must be in the same size!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return

                minReg = np.min(fileIMG)
                maxReg = np.max(fileIMG)

                ui.txtRangeFrom.setMinimum(minReg)
                ui.txtRangeFrom.setValue(minReg)
                ui.txtRangeFrom.setMaximum(maxReg)

                ui.txtRangeTo.setMinimum(minReg)
                ui.txtRangeTo.setMaximum(maxReg)
                ui.txtRangeTo.setValue(minReg)

                print("File Size ", fileSize)
                print("Region ranges are from ", minReg , " to " ,maxReg)
                currentFile = filename
                currentSize = fileSize

                ui.txtCurrent.setText("Size: " + str(currentSize) + " Region: " + str(minReg) + "..." + str(maxReg) + " - " + currentFile)


            except Exception as e:
                print(e)
                print("Cannot load file!")
                msgBox = QMessageBox()
                msgBox.setText("Cannot load file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()

    def btnAdd_click(self):
        global currentFile, currentSize, OutSize
        RegFrom = ui.txtRangeFrom.value()
        RegTo   = ui.txtRangeTo.value()

        if (RegTo < RegFrom):
            print("Region To is smaller than Region From!")
            msgBox = QMessageBox()
            msgBox.setText("Region To is smaller than Region From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if currentFile is None:
            print("File not found!")
            msgBox = QMessageBox()
            msgBox.setText("Please select an Atlas!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        item = QtWidgets.QTreeWidgetItem()
        item.setText(0,"")
        item.setText(1, str(RegFrom))
        item.setText(2, str(RegTo))
        item.setText(3, str(currentFile))
        ui.tvArea.addTopLevelItem(item)

        if OutSize is None:
            OutSize = currentSize

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
        global OutSize
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

        print("Generating ROI ...")

        OutIMG = np.zeros(OutSize)


        for index in range(ui.tvArea.topLevelItemCount()):
            item = ui.tvArea.topLevelItem(index)
            RegFrom = np.double(item.text(1))
            RegTo   = np.double(item.text(2))
            filename= item.text(3)


            fileHDR = nb.load(filename)
            fileIMG = fileHDR.get_data()

            if len(item.text(0)):
                affine = fileHDR.affine


            fileIMG[np.where(fileIMG < RegFrom)] = 0
            fileIMG[np.where(fileIMG > RegTo)] = 0
            fileINDX = np.where(fileIMG != 0)
            OutIMG[fileINDX] = 1
            print(filename + " - is calculated!")

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
    frmAtlasROI.show(frmAtlasROI)
    sys.exit(app.exec_())