#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *

from Base.utility import getVersion, getBuild
from GUI.frmCombineROIGUI import *


class frmCombineROI(Ui_frmCombineROI):
    ui = Ui_frmCombineROI()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmCombineROI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        ui.cbMetric.addItem("Intersection","int")
        ui.cbMetric.addItem("Union","uni")

        dialog.setWindowTitle("easy fMRI combine ROI - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnFROI.clicked.connect(self.btnFROI_click)
        ui.btnSROI.clicked.connect(self.btnSROI_click)
        ui.btnOROI.clicked.connect(self.btnOROI_click)
        ui.btnRUN.clicked.connect(self.btnRun_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnFROI_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open image file ...", os.path.dirname(ui.txtFROI.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFROI.setText(filename)
            else:
                print("Image file not found!")


    def btnSROI_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open image file ...", os.path.dirname(ui.txtSROI.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSROI.setText(filename)
            else:
                print("Image file not found!")


    def btnOROI_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getSaveFileName(None, "Save matrix file ...", os.path.dirname(ui.txtOROI.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
                ui.txtOROI.setText(filename)


    def btnRun_click(self):
        global ui

        msgBox = QMessageBox()

        FROI = ui.txtFROI.text()
        if not len(FROI):
            msgBox.setText("Please enter first ROI file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not os.path.isfile(FROI):
            msgBox.setText("The first ROI file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        SROI = ui.txtSROI.text()
        if not len(SROI):
            msgBox.setText("Please enter second ROI file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not os.path.isfile(SROI):
            msgBox.setText("The second ROI file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        OROI = ui.txtOROI.text()
        if not len(OROI):
            msgBox.setText("Please enter output ROI file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        try:
            FROIHDR = nb.load(FROI)
        except:
            print("Cannot load first ROI!")
            return
        FROIIMG = FROIHDR.get_data()

        try:
            SROIHDR = nb.load(SROI)
        except:
            print("Cannot load second ROI!")
            return
        SROIIMG = SROIHDR.get_data()

        if not np.shape(FROIIMG) == np.shape(SROIIMG):
            print("ROIs must be the same size!")
            return



        if ui.cbMetric.currentData() == "uni":
            OROIIMG = np.zeros(np.shape(FROIIMG))
            OROIIMG[np.where(FROIIMG != 0)] = 1
            OROIIMG[np.where(SROIIMG != 0)] = 1
        elif ui.cbMetric.currentData() == "int":
            FROIIMG[np.where(FROIIMG != 0)] = 1
            SROIIMG[np.where(SROIIMG != 0)] = 1
            OROIIMG = FROIIMG + SROIIMG
            OROIIMG[np.where(OROIIMG < 2)] = 0
            OROIIMG[np.where(OROIIMG != 0)] = 1

        OROIHDR = nb.Nifti1Image(OROIIMG,FROIHDR.affine)
        nb.save(OROIHDR,OROI)

        NumVoxels = np.shape(OROIIMG)
        NumVoxels = NumVoxels[0] * NumVoxels[1] * NumVoxels[2]
        print("Number of all voxels: %d " % NumVoxels)
        NumROIVoxel = len(OROIIMG[np.where(OROIIMG != 0)])
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