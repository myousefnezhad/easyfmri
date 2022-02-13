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
import platform
import subprocess
import sys
from PyQt6.QtWidgets import *
from GUI.frmTransformationMatrixGUI import *
from Base.fsl import FSL
from Base.dialogs import LoadFile, SaveFile


class frmTansformationMatrix(Ui_frmTansformationMatrix):
    ui = Ui_frmTansformationMatrix()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmTansformationMatrix()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_defaults(self)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        fsl = FSL()
        fsl.setting()
        if not fsl.Validate:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find FSL setting!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
        else:
            ui.txtFSLDIR.setText(fsl.FSLDIR)
            ui.txtFlirt.setText(fsl.flirt)
            ui.txtFlirtGUI.setText(fsl.FlirtGUI)



        # dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        # dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_defaults(self):
        from Base.utility import getDirSpace, getDirSpaceINI
        global ui
        # Default Values for Space
        ui.txtSpace.clear()
        try:
            spaceINI = str.rsplit(open(getDirSpaceINI()).read(), "\n")
            for space in spaceINI:
                if len(space):
                    ui.txtSpace.addItem(getDirSpace() + space)
            ui.txtSpace.setCurrentIndex(0)
        except:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find MNI files!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()

        # Search items
        ui.cbSearch.clear()
        ui.cbSearch.addItem("Already virtually aligned (no search)")
        ui.cbSearch.addItem("Not aligned, but same orientation")
        ui.cbSearch.addItem("Incorrect oriented")
        ui.cbSearch.setCurrentIndex(1)

        # Cost Function
        ui.cbCostFunction.clear()
        ui.cbCostFunction.addItem("Correlation Ratio","corratio")
        ui.cbCostFunction.addItem("Mutual Information","mutualinfo")
        ui.cbCostFunction.addItem("Normalised Mutual Information","normmi")
        ui.cbCostFunction.addItem("Normalised Correlation (intra-modal)","normcorr")
        ui.cbCostFunction.addItem("Least Squares (intra-modal)","leastsq")

        # Interpolation
        ui.cbInter.clear()
        ui.cbInter.addItem("Tri-Linear","trilinear")
        ui.cbInter.addItem("Nearest Neighbour","nearestneighbour")
        ui.cbInter.addItem("Spline","spline")


    def set_events(self):
        global ui
        ui.cbSearch.currentIndexChanged.connect(self.cbSearch_change)
        ui.cbCostFunction.currentIndexChanged.connect(self.cbCostFunction_change)
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnImgFile.clicked.connect(self.btnImgFile_click)
        ui.btnSpace.clicked.connect(self.btnSpace_click)
        ui.btnMatFile.clicked.connect(self.btnMatFile_click)
        ui.btnExaFile.clicked.connect(self.btnExaFile_click)
        ui.btnRun.clicked.connect(self.btnRun_click)
        ui.btnFlirtGUI.clicked.connect(self.btnFlirtGUI_click)


    def btnClose_click(self):
        global dialog
        dialog.close()
        pass


    def cbSearch_change(self):
        global ui
        currInx = ui.cbSearch.currentIndex()
        if (currInx == 0):
            ui.txtXmax.setEnabled(False)
            ui.txtXmax.setValue(0)
            ui.txtXmin.setEnabled(False)
            ui.txtXmin.setValue(0)
            ui.txtYmax.setEnabled(False)
            ui.txtYmax.setValue(0)
            ui.txtYmin.setEnabled(False)
            ui.txtYmin.setValue(0)
            ui.txtZmax.setEnabled(False)
            ui.txtZmax.setValue(0)
            ui.txtZmin.setEnabled(False)
            ui.txtZmin.setValue(0)
        elif (currInx == 1):
            ui.txtXmax.setEnabled(True)
            ui.txtXmax.setValue(90)
            ui.txtXmin.setEnabled(True)
            ui.txtXmin.setValue(-90)
            ui.txtYmax.setEnabled(True)
            ui.txtYmax.setValue(90)
            ui.txtYmin.setEnabled(True)
            ui.txtYmin.setValue(-90)
            ui.txtZmax.setEnabled(True)
            ui.txtZmax.setValue(90)
            ui.txtZmin.setEnabled(True)
            ui.txtZmin.setValue(-90)
        elif (currInx == 2):
            ui.txtXmax.setEnabled(True)
            ui.txtXmax.setValue(180)
            ui.txtXmin.setEnabled(True)
            ui.txtXmin.setValue(-180)
            ui.txtYmax.setEnabled(True)
            ui.txtYmax.setValue(180)
            ui.txtYmin.setEnabled(True)
            ui.txtYmin.setValue(-180)
            ui.txtZmax.setEnabled(True)
            ui.txtZmax.setValue(180)
            ui.txtZmin.setEnabled(True)
            ui.txtZmin.setValue(-180)


    def cbCostFunction_change(self):
        global ui
        currInx = ui.cbCostFunction.currentIndex()
        if (currInx < 3):
            ui.txtBins.setEnabled(True)
        else:
            ui.txtBins.setEnabled(False)


    def btnImgFile_click(self):
        filename = LoadFile("Load (f)MRI file ...",['Image files (*.nii.gz)','All files (*.*)'],'nii.gz',\
                            os.path.dirname(ui.txtImgFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtImgFile.setText(filename)
            else:
                print("Image file not found!")


    def btnSpace_click(self):
        filename = LoadFile("Load (f)MRI file ...",['Image files (*.nii.gz)','All files (*.*)'],'nii.gz',\
                            os.path.dirname(ui.txtSpace.currentText()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSpace.setCurrentText(filename)
            else:
                print("Image file not found!")

    def btnMatFile_click(self):
        filename = SaveFile("Saving matrix file ...",['Matrix file (*.mat)'],'mat', \
                            os.path.dirname(ui.txtMatFile.text()))
        if len(filename):
                ui.txtMatFile.setText(filename)


    def btnExaFile_click(self):
        filename = SaveFile("Load (f)MRI file ...",['Image files (*.nii.gz)','All files (*.*)'],'nii.gz',\
                            os.path.dirname(ui.txtExaFile.text()))
        if len(filename):
                ui.txtExaFile.setText(filename)


    def btnFlirtGUI_click(self):
        global ui
        FlirtGUI = ui.txtFSLDIR.text() + ui.txtFlirtGUI.text()
        if not os.path.isfile(FlirtGUI):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find Flirt_gui cmd!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        subprocess.Popen([FlirtGUI])


    def btnRun_click(self):
        global ui
        if not len(ui.txtImgFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Please select an original image file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        if not os.path.isfile(ui.txtImgFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Original image file not found!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        ImgFile = ui.txtImgFile.text()

        if not len(ui.txtSpace.currentText()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a standard space file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        if not os.path.isfile(ui.txtSpace.currentText()):
            msgBox = QMessageBox()
            msgBox.setText("Standard space file not found!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        Space = ui.txtSpace.currentText()

        if not len(ui.txtMatFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Please enter an address for the transformation matrix output!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        MatFile = ui.txtMatFile.text()

        if len(ui.txtExaFile.text()):
            ExaFile = " -out " + ui.txtExaFile.text()
        else:
            ExaFile = " "

        Flirt = ui.txtFSLDIR.text() + ui.txtFlirt.text()
        if not os.path.isfile(Flirt):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find flirt cmd!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return

        RunScript = Flirt + " -in " + ImgFile + " -ref " + Space + ExaFile + " -omat " + MatFile + " -bins " +\
                str(ui.txtBins.value()) + " -cost " + ui.cbCostFunction.currentData() + " -searchrx " +\
                str(ui.txtXmin.value()) + " " + str(ui.txtXmax.value()) + " -searchry " + str(ui.txtYmin.value()) +\
                " " + str(ui.txtYmax.value()) + " -searchrz " + str(ui.txtZmin.value()) + " " + str(ui.txtZmax.value()) +\
                " -dof 12 -interp " + ui.cbInter.currentData()

        os.system(RunScript)
        msgBox = QMessageBox()
        msgBox.setText("Transformation matrix is created!")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmTansformationMatrix.show(frmTansformationMatrix)
    sys.exit(app.exec())