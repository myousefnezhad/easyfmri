#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
import platform
import subprocess
from frmTransformationMatrixGUI import *


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


        if platform.system() == "Linux":
            ui.txtFSLDIR.setText("")
            if os.path.isfile("/usr/bin/fsl5.0-Flirt") and os.path.isfile("/usr/bin/fsl5.0-flirt"):
                ui.txtFlirt.setText("/usr/bin/fsl5.0-flirt")
                ui.txtFlirtGUI.setText("/usr/bin/fsl5.0-Flirt")
            else:
                msgBox = QMessageBox()
                msgBox.setText("fsl5.0 cmds are not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()

        else:
            hasFSL = False
            FSLDIR = str(os.environ["FSLDIR"])
            if FSLDIR == "":
                msgBox = QMessageBox()
                msgBox.setText("Cannot find $FSLDIR variable!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
            else:
                if (os.path.isdir(FSLDIR) == False):
                    msgBox = QMessageBox()
                    msgBox.setText("$FSLDIR does not exist!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                else:
                    ui.txtFSLDIR.setText(os.environ["FSLDIR"])
                    hasFSL = True


            if hasFSL:
                if (os.path.isfile(FSLDIR + "/bin/flirt") == False):
                    ui.txtFlirt.setText("")
                    msgBox = QMessageBox()
                    msgBox.setText("Cannot find flirt cmd!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                if (os.path.isfile(FSLDIR + "/bin/Flirt_gui") == False):
                    # For Linux
                    if os.path.isfile(FSLDIR + "/bin/Flirt"):
                        ui.txtFlirtGUI.setText("/bin/Flirt")
                    else:
                        ui.txtFlirtGUI.setText("")
                        msgBox = QMessageBox()
                        msgBox.setText("Cannot find Feat_gui cmd!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
            else:
                ui.txtFlirt.setText("")
                ui.txtFlirtGUI.setText("")

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_defaults(self):
        from utility import getDirSpace, getDirSpaceINI
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
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

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
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open image file ...", os.path.dirname(ui.txtImgFile.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtImgFile.setText(filename)
            else:
                print("Image file not found!")


    def btnSpace_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open space file ...", os.path.dirname(ui.txtSpace.currentText()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSpace.setCurrentText(filename)
            else:
                print("Image file not found!")

    def btnMatFile_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getSaveFileName(None, "Save matrix file ...", os.path.dirname(ui.txtMatFile.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
                ui.txtMatFile.setText(filename)


    def btnExaFile_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getSaveFileName(None, "Save Example file ...", os.path.dirname(ui.txtExaFile.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
                ui.txtExaFile.setText(filename)


    def btnFlirtGUI_click(self):
        global ui
        FlirtGUI = ui.txtFSLDIR.text() + ui.txtFlirtGUI.text()
        if not os.path.isfile(FlirtGUI):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find Flirt_gui cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        subprocess.Popen([FlirtGUI])


    def btnRun_click(self):
        global ui
        if not len(ui.txtImgFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Please select an original image file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not os.path.isfile(ui.txtImgFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Original image file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        ImgFile = ui.txtImgFile.text()

        if not len(ui.txtSpace.currentText()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a standard space file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if not os.path.isfile(ui.txtSpace.currentText()):
            msgBox = QMessageBox()
            msgBox.setText("Standard space file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        Space = ui.txtSpace.currentText()

        if not len(ui.txtMatFile.text()):
            msgBox = QMessageBox()
            msgBox.setText("Please enter an address for the transformation matrix output!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
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
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        RunScript = Flirt + " -in " + ImgFile + " -ref " + Space + ExaFile + " -omat " + MatFile + " -bins " +\
                str(ui.txtBins.value()) + " -cost " + ui.cbCostFunction.currentData() + " -searchrx " +\
                str(ui.txtXmin.value()) + " " + str(ui.txtXmax.value()) + " -searchry " + str(ui.txtYmin.value()) +\
                " " + str(ui.txtYmax.value()) + " -searchrz " + str(ui.txtZmin.value()) + " " + str(ui.txtZmax.value()) +\
                " -dof 12 -interp " + ui.cbInter.currentData()

        os.system(RunScript)
        msgBox = QMessageBox()
        msgBox.setText("Transformation matrix is created!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmTansformationMatrix.show(frmTansformationMatrix)
    sys.exit(app.exec_())