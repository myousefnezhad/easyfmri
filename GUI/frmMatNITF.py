#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io

import nibabel as nb
import subprocess as sub

from PyQt5.QtWidgets import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import strRange
from Base.afni import AFNI
from Base.utility import getVersion, getBuild, getDirSpaceINI, getDirSpace
from GUI.frmMatNITFGUI import *

class frmMatNITF(Ui_frmMatNITF):
    ui = Ui_frmMatNITF()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMatNITF()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # SS Default Values for Space
        try:
            spaceINI = str.rsplit(open(getDirSpaceINI()).read(), "\n")
            for space in spaceINI:
                if len(space):
                    ui.txtSSSpace.addItem(getDirSpace() + space)

            ui.txtSSSpace.setCurrentIndex(1)
        except:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find MNI files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

        afni = AFNI()
        afni.setting()
        if not afni.Validate:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find AFNI setting!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            ui.txtFAFNI.setText(afni.COPY)
            ui.txtFSUMA.setText(afni.REFIT)


        # Default Values for Threshold type
        ui.cbThType.addItem("Without Thresholding", "no")
        ui.cbThType.addItem("Minimum Thresholding", "min")
        ui.cbThType.addItem("Maximum Thresholding", "max")
        ui.cbThType.addItem("Extremum Thresholding", "ext")

        dialog.setWindowTitle("easy fMRI Convert Matrix to Nifti1 - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnOutFile.clicked.connect(self.btnOutFile_click)
        ui.btnAFNI.clicked.connect(self.btnAFNI_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)
        ui.btnSSSpace.clicked.connect(self.btnSSSpace_click)
        ui.cbThType.currentIndexChanged.connect(self.cbThType_change)
        ui.btnFAFNI.clicked.connect(self.btnFAFNI_click)
        ui.btnFSUMA.clicked.connect(self.btnFSUMA_click)


    def btnClose_click(self):
        global dialog
        dialog.close()

    def cbThType_change(self):
        global ui
        if ui.cbThType.currentData() == "no":
            ui.txtThMin.setEnabled(False)
            ui.txtThMax.setEnabled(False)
        elif ui.cbThType.currentData() == "min":
            ui.txtThMin.setEnabled(True)
            ui.txtThMax.setEnabled(False)
        elif ui.cbThType.currentData() == "max":
            ui.txtThMin.setEnabled(False)
            ui.txtThMax.setEnabled(True)
        elif ui.cbThType.currentData() == "ext":
            ui.txtThMin.setEnabled(True)
            ui.txtThMax.setEnabled(True)



    def btnSSSpace_click(self):
        filename = LoadFile("Open Affine Reference Image ...",['Image files (*.nii.gz)','All files (*.*)'],\
                            'nii.gz',os.path.dirname(ui.txtSSSpace.currentText()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSSSpace.setCurrentText(filename)
            else:
                print("Image file not found!")


    def btnInFile_click(self):
        msgBox = QMessageBox()

        filename = LoadFile("Open MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    ui.lbMatrix.setText("Image Shape=" + str(data["imgShape"][0]))

                    cooShape = None
                    dataShape = None
                    # Train Data
                    ui.txtMatrix.clear()
                    HasDefualt = None
                    for key in Keys:
                        ui.txtMatrix.addItem(key)
                        if key == "train_data":
                            HasDefualt = key
                            dataShape = np.shape(data[key])
                            ui.txtTime.setText("[0-" + str(dataShape[0]) + "]")
                        if key == "data":
                            HasDefualt = key
                            dataShape = np.shape(data[key])
                            ui.txtTime.setText("[0-" + str(dataShape[0]) + "]")

                    if HasDefualt is not None:
                        ui.txtMatrix.setCurrentText(HasDefualt)

                    # Test Data
                    ui.txtCoord.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCoord.addItem(key)
                        if key == "coordinate":
                            ui.txtCoord.setCurrentText("coordinate")
                            cooShape = np.shape(data[key][0])[0]
                            ui.lbCoord.setText("ROI Size=" + str(cooShape))

                    if not cooShape == dataShape[1]:
                        print("WARNING: Coordinate size is not matched by data size!")
                        msgBox.setText("Coordinate size is not matched by data size!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()

                    if cooShape is None:
                        print("WARNING: Cannot find coordinate!")

                    if dataShape is None:
                        print("WARNING: Cannot find data matrix!")

                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        ofile = SaveFile("Save (f)MRI image ...",['Image files (*.nii.gz)'],'nii.gz',\
                         os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)


    def btnFAFNI_click(self):
        filename = LoadFile("Open 3dcopy binary file ...",currentDirectory=os.path.dirname(ui.txtFAFNI.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFAFNI.setText(filename)

    def btnFSUMA_click(self):
        filename = LoadFile("Open 3drefit binary file ...",currentDirectory=os.path.dirname(ui.txtFSUMA.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFSUMA.setText(filename)


    def btnAFNI_click(self):
        ofile = SaveFile("Save AFNI image ...",currentDirectory=os.path.dirname(ui.txtAFNI.text()))
        if len(ofile):
            ui.txtAFNI.setText(ofile)


    def btnConvert_click(self):
        msgBox = QMessageBox()

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        ThresholdType = ui.cbThType.currentData()
        MinTh = None
        MaxTh = None

        if (ThresholdType == "min") or (ThresholdType == "ext"):
                try:
                    MinTh = np.double(ui.txtThMin.text())
                except:
                    msgBox.setText("Min Threshold must be a number")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                print("Min Threshold is valid")

        if (ThresholdType == "max") or (ThresholdType == "ext"):
                try:
                    MaxTh = np.double(ui.txtThMax.text())
                except:
                    msgBox.setText("Max Threshold must be a number")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                print("Max Threshold is valid")

        # OutFile
        AFNI = ui.txtAFNI.text()
        if not len(AFNI):
            AFNI = None
        else:
            CopyFile = ui.txtFAFNI.text()
            if not len(CopyFile):
                msgBox.setText("Please select 3dcopy command!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            if not os.path.isfile(CopyFile):
                msgBox.setText("Please select 3dcopy command!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

            RefitFile = ui.txtFSUMA.text()
            if not len(RefitFile):
                msgBox.setText("Please select 3drefit command!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            if not os.path.isfile(RefitFile):
                msgBox.setText("Please select 3drefit command!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return


        # InFile
        InFile = ui.txtInFile.text()
        if not len(InFile):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(InFile):
            msgBox.setText("Input file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not len(ui.txtMatrix.currentText()):
            msgBox.setText("Matrix name not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not len(ui.txtCoord.currentText()):
            msgBox.setText("Coordinate name not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not len(ui.txtTime.text()):
            msgBox.setText("Time points not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        AffineFile = ui.txtSSSpace.currentText()
        if not len(AffineFile):
            msgBox.setText("Please enter affine reference!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(AffineFile):
            msgBox.setText("Affine reference not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        AffineHDR = nb.load(AffineFile)
        Affine = AffineHDR.affine

        Time = strRange(ui.txtTime.text())
        if Time is None:
            msgBox.setText("Time points is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        try:
            InData = io.loadmat(InFile)
            Mat = InData[ui.txtMatrix.currentText()]
            Coord = InData[ui.txtCoord.currentText()]
            imgShape = InData["imgShape"][0]

        except:
            print("Cannot load data!")
            msgBox.setText("Cannot load data!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        ImgData = None
        # Filter Mat
        for t in Time:
            vox = Mat[t, :]
            if ui.cbScale.isChecked():
                vox = preprocessing.scale(vox)
                print("Time Point: " + str(t) + " is normalized.")

            if MinTh is not None:
                vox[np.where(vox < MinTh)] = 0
                print("Time Point: " + str(t) +", Lower band thresholding is done!")

            if MaxTh is not None:
                vox[np.where(vox > MaxTh)] = 0
                print("Time Point: " + str(t) + ", Upper band thresholding is done!")


            img = np.zeros([imgShape[0], imgShape[1], imgShape[2], 1])
            for coIndx, _ in enumerate(Coord[0]):
                img[Coord[0][coIndx], Coord[1][coIndx], Coord[2][coIndx], 0] = vox[coIndx]
            ImgData = img if ImgData is None else np.concatenate((ImgData, img),axis=3)
            print("Time point: " + str(t) + " is done.")

        print("Saving image ...")
        NIF = nb.Nifti1Image(ImgData,Affine)
        nb.save(NIF,OutFile)
        if AFNI is not None:
            cmd = CopyFile + " " + OutFile + " " + AFNI
            print("Running: " + cmd)
            os.system(cmd)
            cmd = RefitFile + "  -view tlrc -space MNI " + AFNI + " " + AFNI + "+tlrc."
            print("Running: " + cmd)
            os.system(cmd)
        print("DONE!")
        msgBox.setText("Image file is generated.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMatNITF.show(frmMatNITF)
    sys.exit(app.exec_())