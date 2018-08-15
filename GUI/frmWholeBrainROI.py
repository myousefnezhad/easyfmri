#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
from PyQt5.QtWidgets import *
from Base.Setting import *
from Base.SettingHistory import History
from Base.utility import getVersion, getBuild, setParameters3, fixstr, getSettingVersion, strRange, strMultiRange
from Base.dialogs import LoadFile, SaveFile
from GUI.frmWholeBrainROIGUI import *


def DefaultSpace():
    return "Consider the first mask as affine file"


class frmWholeBrainROI(Ui_frmWholeBrainROI):
    ui = Ui_frmWholeBrainROI()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        from Base.utility import getDirSpace, getDirSpaceINI
        global dialog
        global ui
        ui = Ui_frmWholeBrainROI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget_2.setCurrentIndex(0)

        # Load Setting History
        history = History()
        histories = history.load_history()
        ui.txtSSSetting.clear()
        for history in histories:
            ui.txtSSSetting.addItem(history)
        ui.txtSSSetting.setCurrentText("")

        # Default Values for Input File
        ui.txtSSInFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/mask.nii.gz")
        ui.txtSSInFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/std_mask.nii.gz")

        # Default Values for Metric
        ui.cbMetric.addItem("Intersection of voxels from all masks","inter")

        # Default Values for Space
        ui.txtSSSpace.addItem(DefaultSpace())
        ProgramPath = os.path.dirname(os.path.abspath(__file__))
        try:
            spaceINI = str.rsplit(open(getDirSpaceINI()).read(),"\n")
            for space in spaceINI:
                if len(space):
                    ui.txtSSSpace.addItem(getDirSpace() + space)

            ui.txtSSSpace.setCurrentIndex(0)
        except:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find MNI files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()


        dialog.setWindowTitle("easy fMRI whole brain ROI - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnSSSetting.clicked.connect(self.btnSSSetting_click)
        ui.btnSSSettingReload.clicked.connect(self.btnSSSettingReload_click)
        ui.btnRUN.clicked.connect(self.btnRUN_click)
        ui.btnSSSpace.clicked.connect(self.btnSSSpace_click)
        ui.btnOutROI.clicked.connect(self.btnOutROI_click)



    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnSSSetting_click(self):
        global ui

        if os.path.isfile(ui.txtSSSetting.currentText()):
            currDir = os.path.dirname(ui.txtSSSetting.currentText())
        else:
            currDir = ""
        filename = LoadFile("Open setting file ...",['easy fMRI setting (*.ez)'],'ez',currDir)
        if len(filename):
            if not os.path.isfile(filename):
                msgBox = QMessageBox()
                msgBox.setText("Setting file not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

            setting = Setting()
            setting.Load(filename)

            if np.double(setting.Version) < np.double(getSettingVersion()):
                print("WARNING: You are using different version of Easy fMRI!!!")
                msgBox = QMessageBox()
                msgBox.setText("This version of setting is not supported!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

            if not setting.empty:
                ui.txtSSSetting.setCurrentText(filename)
                ui.txtSSDIR.setText(setting.mainDIR)
                ui.txtSSTask.setText(setting.Task)
                ui.txtSSSubRange.setText(setting.SubRange)
                ui.txtSSSubLen.setValue(setting.SubLen)
                ui.txtSSSubPer.setText(setting.SubPer)
                ui.txtSSConRange.setText(setting.ConRange)
                ui.txtSSConLen.setValue(setting.ConLen)
                ui.txtSSConPer.setText(setting.ConPer)
                ui.txtSSRunRange.setText(setting.RunRange)
                ui.txtSSRunPer.setText(setting.RunPer)
                ui.txtSSRunLen.setValue(setting.RunLen)


    def btnSSSettingReload_click(self):
        global ui
        filename = ui.txtSSSetting.currentText()
        if os.path.isfile(filename):
                if len(filename):
                    setting = Setting()
                    setting.Load(filename)

                    if np.double(setting.Version) < np.double(getSettingVersion()):
                        print("WARNING: You are using different version of Easy fMRI!!!")
                        msgBox = QMessageBox()
                        msgBox.setText("This version of setting is not supported!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return

                    if not setting.empty:
                        ui.txtSSSetting.setCurrentText(filename)
                        ui.txtSSDIR.setText(setting.mainDIR)
                        ui.txtSSTask.setText(setting.Task)
                        ui.txtSSSubRange.setText(setting.SubRange)
                        ui.txtSSSubLen.setValue(setting.SubLen)
                        ui.txtSSSubPer.setText(setting.SubPer)
                        ui.txtSSConRange.setText(setting.ConRange)
                        ui.txtSSConLen.setValue(setting.ConLen)
                        ui.txtSSConPer.setText(setting.ConPer)
                        ui.txtSSRunRange.setText(setting.RunRange)
                        ui.txtSSRunPer.setText(setting.RunPer)
                        ui.txtSSRunLen.setValue(setting.RunLen)
        else:
            print("Setting file not found!")

    def btnSSSpace_click(self):
        global ui

        filename = LoadFile('Open affine image ...',['Affine images (*.nii.gz)'],'nii.gz',\
                            os.path.dirname(ui.txtSSSpace.currentText()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSSSpace.setCurrentText(filename)
            else:
                print("Image file not found!")


    def btnOutROI_click(self):
        global ui
        filename = SaveFile('Save ROI ...',['ROI images (*.nii.gz)'],'nii.gz',os.path.dirname(ui.txtOutROI.text()))
        if len(filename):
                ui.txtOutROI.setText(filename)


    def btnRUN_click(self):
        global ui
        msgBox = QMessageBox()

        mainDIR = ui.txtSSDIR.text()
        Task = ui.txtSSTask.text()
        # Check Directory
        if not len(mainDIR):
            msgBox.setText("There is no main directory")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isdir(mainDIR):
            msgBox.setText("Main directory doesn't exist")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Main directory is okay.")
        if not len(Task):
            msgBox.setText("There is no task title")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubRange = strRange(ui.txtSSSubRange.text(),Unique=True)
            if SubRange is None:
                raise Exception
            SubSize = len(SubRange)
        except:
            msgBox.setText("Subject Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Range of subjects is okay!")
        try:
            SubLen = np.int32(ui.txtSSSubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is okay!")


        try:
            ConRange = strMultiRange(ui.txtSSConRange.text(),SubSize)
            if ConRange is None:
                raise Exception
            if not (len(ConRange) == SubSize):
                msgBox.setText("Counter Size must be equal to Subject Size!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        except:
            msgBox.setText("Counter Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter Range is okay!")
        try:
            ConLen = np.int32(ui.txtSSConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of Counter is okay!")


        try:
            RunRange = strMultiRange(ui.txtSSRunRange.text(),SubSize)
            if RunRange is None:
                raise Exception
            if not (len(RunRange) == SubSize):
                msgBox.setText("Run Size must be equal to Subject Size!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        except:
            msgBox.setText("Run Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Run Range is okay!")
        try:
            RunLen = np.int32(ui.txtSSRunLen.value())
            1 / RunLen
        except:
            msgBox.setText("Length of runs must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of runs is valid")

        Space = ui.txtSSSpace.currentText()
        if not len(Space):
            msgBox.setText("Please enter a affine file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not Space == DefaultSpace():
            if not os.path.isfile(Space):
                msgBox = QMessageBox()
                msgBox.setText("Affine file not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
        print("Affine file is okay.")

        In = ui.txtSSInFile.currentText()
        if not len(In):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        Out = ui.txtOutROI.text()
        if not len(Out):
            msgBox.setText("Please enter output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        print("Checking files ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s,cnt))
                for r in RunRange[si]:

                    InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()),\
                                    fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(),\
                                    fixstr(cnt, ConLen, ui.txtSSConPer.text()))
                    if os.path.isfile(InFile):
                        print(InFile + " - is OKAY.")
                    else:
                        print(InFile + " - not found!")
                        return

        if ui.cbMetric.currentData() == "inter":
            print("Calculating ROI ...")


            ROIData = None
            for si, s in enumerate(SubRange):
                for cnt in ConRange[si]:
                    print("Analyzing Subject %d, Counter %d ..." % (s,cnt))
                    for r in RunRange[si]:
                        InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                                fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                                fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                        MaskHDR = nb.load(InFile)
                        MaskData = MaskHDR.get_data()
                        MaskData[np.where(MaskData != 0)] = 1
                        if ROIData is None:
                            if Space == DefaultSpace():
                                affineHDR = nb.load(InFile)
                            else:
                                affineHDR = nb.load(Space)

                            ROIData = MaskData.copy()
                        else:
                            if not np.shape(ROIData) == np.shape(MaskData):
                                print("All mask must include the same size data (tensor)")
                                return
                            else:
                                ROIData = ROIData * MaskData
                        print(InFile + " - is calculated!")

            ROIHDR = nb.Nifti1Image(ROIData, affineHDR.affine)
            nb.save(ROIHDR,Out)

            NumVoxels = np.shape(ROIData)
            NumVoxels = NumVoxels[0] * NumVoxels[1] * NumVoxels[2]
            print("Number of all voxels: %d " % NumVoxels)
            NumROIVoxel = len(ROIData[np.where(ROIData != 0)])
            print("Number of selected voxles in ROI: %d" % NumROIVoxel)
            print("ROI is generated!")

            msgBox.setText("ROI is generated!\nNumber of all voxels: " + str(NumVoxels) + \
                           "\nNumber of selected voxles in ROI: " + str(NumROIVoxel))
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmWholeBrainROI.show(frmWholeBrainROI)
    sys.exit(app.exec_())