#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from Base.Setting import *
from Base.SettingHistory import History
from Base.dialogs import SaveFile, LoadFile
from Base.utility import getVersion, getBuild, setParameters3, fixstr, getSettingVersion, strRange, strMultiRange
from GUI.frmSelectSession import frmSelectSession
from GUI.frmProbabilisticROIGUI import *
from dir import getDIR

def DefaultSpace():
    return "Consider the first mask as affine file"


class frmProbabilisticROI(Ui_frmProbabilisticROI):
    ui = Ui_frmProbabilisticROI()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        from Base.utility import getDirSpace, getDirSpaceINI
        global dialog
        global ui
        ui = Ui_frmProbabilisticROI()
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
        ui.txtSSInFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/thresh_zstat$COND$.nii.gz")
        ui.txtSSInFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/cluster_mask_zstat$COND$.nii.gz")

        # Default Values for Metric
        ui.cbMetric.addItem("Intersection of voxels in all masks","inter")

        # Default Values for Threshold type
        ui.cbThType.addItem("Without Thresholding", "no")
        ui.cbThType.addItem("Minimum Thresholding", "min")
        ui.cbThType.addItem("Maximum Thresholding", "max")
        ui.cbThType.addItem("Extremum Thresholding", "ext")


        # Default Values for Space
        ui.txtSSSpace.addItem(DefaultSpace())
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

        dialog.setWindowTitle("easy fMRI probabilistic ROI - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.cbThType.currentIndexChanged.connect(self.cbThType_change)
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnSSSetting.clicked.connect(self.btnSSSetting_click)
        ui.btnSSSettingReload.clicked.connect(self.btnSSSettingReload_click)
        ui.btnRUN.clicked.connect(self.btnRUN_click)
        ui.btnSSSpace.clicked.connect(self.btnSSSpace_click)
        ui.btnOutROI.clicked.connect(self.btnOutROI_click)
        ui.btnLoadEvent.clicked.connect(self.btnLoadEvent_click)


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
                ui.txtSSSubLen.setValue(setting.SubLen)
                ui.txtSSSubPer.setText(setting.SubPer)
                ui.txtSSConLen.setValue(setting.ConLen)
                ui.txtSSConPer.setText(setting.ConPer)
                ui.txtSSRunPer.setText(setting.RunPer)
                ui.txtSSRunLen.setValue(setting.RunLen)
                ui.txtSSSubRange.setText(setting.SubRange)
                ui.txtSSConRange.setText(setting.ConRange)
                ui.txtSSRunRange.setText(setting.RunRange)
                ui.txtEventDIR.setText(setting.EventFolder)
                ui.txtCondPre.setText(setting.CondPre)

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
                        ui.txtSSSubLen.setValue(setting.SubLen)
                        ui.txtSSSubPer.setText(setting.SubPer)
                        ui.txtSSConLen.setValue(setting.ConLen)
                        ui.txtSSConPer.setText(setting.ConPer)
                        ui.txtSSRunPer.setText(setting.RunPer)
                        ui.txtSSRunLen.setValue(setting.RunLen)
                        ui.txtSSSubRange.setText(setting.SubRange)
                        ui.txtSSConRange.setText(setting.ConRange)
                        ui.txtSSRunRange.setText(setting.RunRange)
                        ui.txtEventDIR.setText(setting.EventFolder)
                        ui.txtCondPre.setText(setting.CondPre)
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

        try:
            CondFrom = np.int32(ui.txtSSCondFrom.value())
            1 / CondFrom
        except:
            msgBox.setText("Condition From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            CondTo = np.int32(ui.txtSSCondTo.value())
            1 / CondTo
        except:
            msgBox.setText("Condition To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if CondTo < CondFrom:
            msgBox.setText("Condition To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter is valid")
        try:
            CondLen = np.int32(ui.txtSSCondLen.text())
            1 / CondLen
        except:
            msgBox.setText("Length of condition must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of condition is valid")


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

        ThresholdType = ui.cbThType.currentData()

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

        print("Checking files ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s,cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in RunRange[si]:
                    for cnd in range(CondFrom, CondTo + 1):

                        InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()),\
                                    fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(),\
                                    fixstr(cnt, ConLen, ui.txtSSConPer.text()), fixstr(cnd, CondLen, ui.txtSSCondPer.text()))
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
                        for cnd in range(CondFrom, CondTo + 1):
                            InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                                    fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                                    fixstr(cnt, ConLen, ui.txtSSConPer.text()),
                                                    fixstr(cnd, CondLen, ui.txtSSCondPer.text()))

                            MaskHDR = nb.load(InFile)
                            MaskData = MaskHDR.get_data()
                            if ThresholdType == "no":
                                MaskData[np.where(MaskData != 0)] = 1
                            elif ThresholdType == "min":
                                MaskData[np.where(MaskData < MinTh)] = 0
                                MaskData[np.where(MaskData != 0)] = 1
                            elif ThresholdType == "max":
                                MaskData[np.where(MaskData > MaxTh)] = 0
                                MaskData[np.where(MaskData != 0)] = 1
                            elif ThresholdType == "ext":
                                MaskData[np.where(MaskData > MaxTh)] = 0
                                MaskData[np.where(MaskData < MinTh)] = 0
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
                                    ROIData = ROIData + MaskData
                                    ROIData[np.where(ROIData != 0)] = 1

                            print(InFile + " - is calculated!")
            NumVoxels = np.shape(ROIData)
            NumVoxels = NumVoxels[0] * NumVoxels[1] * NumVoxels[2]
            print("Number of all voxels: %d " % NumVoxels)
            NumROIVoxel = len(ROIData[np.where(ROIData != 0)])
            print("Number of selected voxles in ROI: %d" % NumROIVoxel)
            ROIHDR = nb.Nifti1Image(ROIData, affineHDR.affine)
            nb.save(ROIHDR,Out)
            print("ROI is generated!")

            msgBox.setText("ROI is generated!\nNumber of all voxels: " + str(NumVoxels) + \
                           "\nNumber of selected voxles in ROI: " + str(NumROIVoxel))
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def btnLoadEvent_click(self):
        global ui, dialog

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


        if ui.txtEventDIR.text() == "":
            msgBox.setText("Structure of the event folders is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtCondPre.text() == "":
            msgBox.setText("The prefix of condition files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        setting         = Setting()

        setting.mainDIR = mainDIR
        setting.Task    = Task

        setting.SubRange= ui.txtSSSubRange.text()
        setting.SubLen  = np.int32(SubLen)
        setting.SubPer  = ui.txtSSSubPer.text()

        setting.ConRange= ui.txtSSConRange.text()
        setting.ConLen  = np.int32(ConLen)
        setting.ConPer  = ui.txtSSConPer.text()

        setting.RunRange= ui.txtSSRunRange.text()
        setting.RunLen  = np.int32(RunLen)
        setting.RunPer  = ui.txtSSRunPer.text()

        sSess = frmSelectSession(None, setting=setting)
        if not sSess.PASS:
            return

        EventFolder = setParameters3(ui.txtEventDIR.text(), mainDIR, fixstr(int(sSess.SubID), setting.SubLen, setting.SubPer), \
                                               fixstr(int(sSess.RunID), int(setting.RunLen), setting.RunPer), setting.Task, \
                                               fixstr(sSess.ConID, int(setting.ConLen), setting.ConPer))

        CondFile = EventFolder + ui.txtCondPre.text() + ".mat"

        if not os.path.isfile(CondFile):
            print("Cannot find condition mat file!")
            return
        try:
            conditions = io.loadmat(CondFile)
        except:
            print("Cannot load condition mat file!")
            return

        NumCond = len(conditions["Cond"])
        ui.txtSSCondFrom.setValue(1)
        ui.txtSSCondTo.setValue(NumCond)
        ui.txtSSCondLen.setValue(len(str(NumCond)))
        ui.txtSSCondPer.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmProbabilisticROI.show(frmProbabilisticROI)
    sys.exit(app.exec_())