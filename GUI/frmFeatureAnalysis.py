#!/usr/bin/env python3
import os
import platform
import sys

import PyQt5.QtWidgets as QtWidgets
import matplotlib
import nibabel as nb
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from sklearn.preprocessing import label_binarize
import threading

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from GUI.frmFeatureAnalysisGUI import *
from GUI.frmTransformationMatrix import frmTansformationMatrix
from GUI.frmWholeBrainROI import frmWholeBrainROI
from GUI.frmProbabilisticROI import frmProbabilisticROI
from GUI.frmCombineROI import frmCombineROI
from GUI.frmManuallyDesignROI import frmManuallyDesignROI
from GUI.frmAtlasROI import frmAtlasROI
from GUI.frmRemoveRestScan import frmRemoveRestScan
from GUI.frmRemoveRestScanCross import frmRemoveRestScanCross
from GUI.frmCombineData import frmCombineData
from GUI.frmFECrossValidation import frmFECrossValidation
from GUI.frmImageInfo import frmImageInfo
from GUI.frmSelectSession import frmSelectSession
from GUI.frmFEEZCrossValidation import frmFEEZCrossValidation
from GUI.frmEzMat import frmEzMat

from Base.utility import fixstr, getDirSpaceINI, getDirSpace, setParameters3, convertDesignMatrix, fitLine
from Base.utility import strRange, strMultiRange, getSettingVersion
from Base.Setting import Setting
from Base.SettingHistory import History
from Base.Conditions import Conditions
from Base.dialogs import LoadFile, SaveFile, SelectDir
from Base.fsl import FSL


class RegistrationThread(threading.Thread):
    def __init__(self, flirt=None, arg=None, InTitle=None, files=list()):
        super(RegistrationThread, self).__init__()
        self.flirt  = flirt
        self.arg    = arg
        self.InTitle= InTitle

        # Necessary
        self.open   = False
        self.files  = files
        self.status = "Ready"
        self.isKill   = False

    def kill(self):
        self.isKill = True

    def run(self):
        import subprocess, os
        self.status = "Running"
        print("Registering " + self.InTitle + " ...")
        cmd = subprocess.Popen(self.flirt + " " + self.arg, shell=True)
        while (not self.isKill) and (cmd.poll() is None):
            pass
        cmd.kill()

        if self.isKill:
            self.status = "Failed"
            return

        isFailed = False
        for fil in self.files:
            if not os.path.isfile(fil):
                print("Cannot find " + fil + "!")
                isFailed = True
                break
        if isFailed:
            self.status = "Failed"
        else:
            self.status = "Done"
            print(self.InTitle + " - is done.")


class MainWindow(QtWidgets.QMainWindow):
    parent = None

    def __init__(self, parentin=None):
        super().__init__()
        global parent
        if parentin is not None:
            parent = parentin

    def closeEvent(self, event):
        global parent
        try:
            if parent is not None:
                parent.show()
        except:
            pass

    pass


class frmFeatureAnalysis(Ui_frmFeatureAnalysis):
    ui = Ui_frmFeatureAnalysis()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, parentin=None):
        from Base.utility import getVersion, getBuild
        global dialog, ui, parent
        ui = Ui_frmFeatureAnalysis()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        if parentin is not None:
            dialog = MainWindow(parentin)
        else:
            dialog = MainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)
        ui.tabWidget_2.setCurrentIndex(0)
        ui.tabWidget_3.setCurrentIndex(0)
        ui.tabWidget_4.setCurrentIndex(0)

        # Load Setting History
        history = History()
        histories = history.load_history()
        ui.txtSSSetting.clear()
        for history in histories:
            ui.txtSSSetting.addItem(history)
            ui.txtDISetting.addItem(history)
        ui.txtSSSetting.setCurrentText("")
        ui.txtDISetting.setCurrentText("")

        # DI Default Values for Input File
        ui.txtDIInFile.addItem(
            "$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/filtered_func_data.nii.gz")
        ui.txtDIInFile.addItem(
            "$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/std_filtered_func_data.nii.gz")

        # DI Default Values for Design Matrix
        ui.txtDIDM.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/design.mat")

        # SS Default Values for Input File
        ui.txtSSInFile.addItem(
            "$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/filtered_func_data.nii.gz")
        ui.txtSSInFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/mask.nii.gz")

        # SS Default Values for Output File
        ui.txtSSOutFile.addItem(
            "$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/std_filtered_func_data.nii.gz")
        ui.txtSSOutFile.addItem("$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/std_mask.nii.gz")

        # SS Defuilt Values of Interpolation
        ui.cbSSInter.clear()
        ui.cbSSInter.addItem("Tri-Linear", "trilinear")
        ui.cbSSInter.addItem("Nearest Neighbour", "nearestneighbour")
        ui.cbSSInter.addItem("Spline", "spline")

        # SS Default Values for Space
        ui.txtSSSpace.addItem(
            "$MAINDIR$/sub-$SUB$/func/sub-$SUB$_task-$TASK$_run-$RUN$_analyze.feat/reg/standard.nii.gz")
        try:
            spaceINI = str.rsplit(open(getDirSpaceINI()).read(), "\n")
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


        fsl = FSL()
        fsl.setting()
        if not fsl.Validate:
            msgBox = QMessageBox()
            msgBox.setText("Cannot find FSL setting!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        else:
            ui.txtFSLDIR.setText(fsl.FSLDIR)
            ui.txtFlirt.setText(fsl.flirt)


        # Unsupervised Feature Engineering
        ui.cbFEU.addItem("MatLab: Data Normalization",1)
        ui.cbFEU.addItem("MatLab: Dictionary Learning",20002)
        ui.cbFEU.addItem("MatLab: Factor Analysis",20000)
        ui.cbFEU.addItem("MatLab: Fast Independent Component Analysis (FastICA)",20001)
        ui.cbFEU.addItem("MatLab: Incremental Principal Component Analysis (IPCA)",10001)
        ui.cbFEU.addItem("MatLab: Kernel Principal Component Analysis (KPCA)",10002)
        ui.cbFEU.addItem("MatLab: Multi Region Pattern Analysis (Snapshots)", 30000)
        ui.cbFEU.addItem("MatLab: Principal Component Analysis (PCA)",10000)
        ui.cbFEU.addItem("MatLab: Sparse Principal Component Analysis (SPCA)",10003)

        # Supervised Feature Engineering
        ui.cbFES.addItem("MatLab: Linear Discriminant Analysis (LDA)",1)


        # Functional Alignment
        ui.cbFA.addItem("MatLab: Regularized Hyperalignment", 10000)

        dialog.setWindowTitle("easy fMRI feature analysis - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnSSSetting.clicked.connect(self.btnSSSetting_click)
        ui.btnDISetting.clicked.connect(self.btnDISetting_click)
        ui.btnSSSettingReload.clicked.connect(self.btnSSSettingReload_click)
        ui.btnDISettingReload.clicked.connect(self.btnDISettingReload_click)
        ui.btnSSMatCreator.clicked.connect(self.btnSSMatCreator_click)
        ui.btnSSSpace.clicked.connect(self.btnSSSpace_click)
        ui.btnSSMatFile.clicked.connect(self.btnSSMatFile_click)
        ui.btnSSRUN.clicked.connect(self.btnSSRUN_click)
        ui.btnDIRUN.clicked.connect(self.btnDIRUN_click)
        ui.btnROIWholeBrain.clicked.connect(self.btnROIWholeBrain_click)
        ui.btnROIProbabilistic.clicked.connect(self.btnROIProbabilistic_click)
        ui.btnROICombine.clicked.connect(self.btnROICombine_click)
        ui.btnROIManuallyDesign.clicked.connect(self.btnROIManuallyDesign_click)
        ui.btnROIAtlas.clicked.connect(self.btnROIAtlas_click)
        ui.btnDIOutFile.clicked.connect(self.btnDIOutFile_click)
        ui.btnDIROIFile.clicked.connect(self.btnDIROIFile_click)
        ui.btnDILabels.clicked.connect(self.btnDILabels_click)
        ui.btnDIRemoveRest.clicked.connect(self.btnDIRemoveRest_click)
        ui.btnDIRemoveRest2.clicked.connect(self.btnDIRemoveRest2_click)
        ui.btnDICombineData.clicked.connect(self.btnDICombineData_click)
        ui.btnFEURun.clicked.connect(self.btnFEU_click)
        ui.btnFESRun.clicked.connect(self.btnFES_click)
        ui.btnDIDraw.clicked.connect(self.btnDIDraw_click)
        ui.btnFECross.clicked.connect(self.btnFECross_click)
        ui.btnFARun.clicked.connect(self.btnFA_click)
        ui.btnImageInfo.clicked.connect(self.btnImageInfo_click)
        ui.btnDIConvertEzData.clicked.connect(self.btnDIConverEzData_click)
        ui.btnFECrossEzData.clicked.connect(self.btnFECrossEzData_click)


    # Exit function
    def btnClose_click(self):
        global dialog, parent
        dialog.close()

    def btnImageInfo_click(self):
        frmImageInfo.show(frmImageInfo)

    def btnSSSetting_click(self):
        global ui
        if os.path.isfile(ui.txtSSSetting.currentText()):
            currDir = os.path.dirname(ui.txtSSSetting.currentText())
        else:
            currDir = None
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
                ui.txtSSSpace.setCurrentText(setting.Analysis + ".feat/reg/standard.nii.gz")
                ui.txtSSInFile.setCurrentText(setting.Analysis + ".feat/filtered_func_data.nii.gz")
                ui.txtSSOutFile.setCurrentText(setting.Analysis + ".feat/std_filtered_func_data.nii.gz")

    def btnDISetting_click(self):
        global ui

        if os.path.isfile(ui.txtDISetting.currentText()):
            currDir = os.path.dirname(ui.txtDISetting.currentText())
        else:
            currDir = None

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
                ui.txtDISetting.setCurrentText(filename)
                ui.txtDIDIR.setText(setting.mainDIR)
                ui.txtDITask.setText(setting.Task)
                ui.txtDISubRange.setText(setting.SubRange)
                ui.txtDISubLen.setValue(setting.SubLen)
                ui.txtDISubPer.setText(setting.SubPer)
                ui.txtDIConRange.setText(setting.ConRange)
                ui.txtDIConLen.setValue(setting.ConLen)
                ui.txtDIConPer.setText(setting.ConPer)
                ui.txtDIRunRange.setText(setting.RunRange)
                ui.txtDIRunPer.setText(setting.RunPer)
                ui.txtDIRunLen.setValue(setting.RunLen)
                ui.txtDIEventDIR.setText(setting.EventFolder)
                ui.txtDIInFile.setCurrentText(setting.Analysis + ".feat/filtered_func_data.nii.gz")
                ui.txtDIDM.setCurrentText(setting.Analysis + ".feat/design.mat")

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
                    ui.txtSSSpace.setCurrentText(setting.Analysis + ".feat/reg/standard.nii.gz")
                    ui.txtSSInFile.setCurrentText(setting.Analysis + ".feat/filtered_func_data.nii.gz")
                    ui.txtSSOutFile.setCurrentText(setting.Analysis + ".feat/std_filtered_func_data.nii.gz")

        else:
            print("Setting file not found!")

    def btnDISettingReload_click(self):
        from Base.utility import getVersion
        global ui
        filename = ui.txtDISetting.currentText()
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
                    ui.txtDISetting.setCurrentText(filename)
                    ui.txtDIDIR.setText(setting.mainDIR)
                    ui.txtDITask.setText(setting.Task)
                    ui.txtDISubRange.setText(setting.SubRange)
                    ui.txtDISubLen.setValue(setting.SubLen)
                    ui.txtDISubPer.setText(setting.SubPer)
                    ui.txtDIConRange.setText(setting.ConRange)
                    ui.txtDIConLen.setValue(setting.ConLen)
                    ui.txtDIConPer.setText(setting.ConPer)
                    ui.txtDIRunRange.setText(setting.RunRange)
                    ui.txtDIRunPer.setText(setting.RunPer)
                    ui.txtDIRunLen.setValue(setting.RunLen)
                    ui.txtDIEventDIR.setText(setting.EventFolder)
                    ui.txtDIInFile.setCurrentText(setting.Analysis + ".feat/filtered_func_data.nii.gz")
                    ui.txtDIDM.setCurrentText(setting.Analysis + ".feat/design.mat")



        else:
            print("Setting file not found!")

    def btnSSMatFile_click(self):
        global ui
        filename = LoadFile("Open Transformation Matrix ...",['Matrix files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtSSMatFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSSMatFile.setText(filename)
            else:
                print("Image file not found!")

    def btnSSSpace_click(self):
        global ui
        filename = LoadFile("Open image file ...",['Image files (*.nii.gz)','All files (*.*)'],'nii.gz', \
                            os.path.dirname(ui.txtSSSpace.currentText()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSSSpace.setCurrentText(filename)
            else:
                print("Image file not found!")

    def btnSSMatCreator_click(self):
        frmTansformationMatrix.show(frmTansformationMatrix)

    def btnSSRUN_click(self):
        global ui

        msgBox = QMessageBox()
        FSLDIR = ui.txtFSLDIR.text()

        if (os.path.isfile(FSLDIR + ui.txtFlirt.text()) == False):
            msgBox.setText("Cannot find feat cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

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


        Mat = ui.txtSSMatFile.text()
        if not len(Mat):
            msgBox.setText("Please enter transformation matrix!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        Space = ui.txtSSSpace.currentText()
        if not len(Space):
            msgBox.setText("Please enter standard space!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        In = ui.txtSSInFile.currentText()
        if not len(In):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        Out = ui.txtSSOutFile.currentText()
        if not len(Out):
            msgBox.setText("Please enter output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        Flirt = ui.txtFSLDIR.text() + ui.txtFlirt.text()
        if not os.path.isfile(Flirt):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find flirt cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        print("Checking files ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                for r in RunRange[si]:
                    MatFile = setParameters3(Mat, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                             fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                             fixstr(cnt, ConLen, ui.txtSSConPer.text()))
                    if os.path.isfile(MatFile):
                        print(MatFile + " - is OKAY.")
                    else:
                        print(MatFile + " - not found!")
                        return

                    SpaceFile = setParameters3(Space, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                               fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                               fixstr(cnt, ConLen, ui.txtSSConPer.text()))
                    if os.path.isfile(SpaceFile):
                        print(SpaceFile + " - is OKAY.")
                    else:
                        print(SpaceFile + " - not found!")
                        return

                    InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                            fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                            fixstr(cnt, ConLen, ui.txtSSConPer.text()))
                    if os.path.isfile(InFile):
                        print(InFile + " - is OKAY.")
                    else:
                        print(InFile + " - not found!")
                        return

        Jobs = list()
        print("Registration ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                for r in RunRange[si]:
                    MatFile = setParameters3(Mat, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                             fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                             fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    SpaceFile = setParameters3(Space, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                               fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                               fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                            fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                            fixstr(cnt, ConLen, ui.txtSSConPer.text()))
                    InTitle = setParameters3(In, "", fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                            fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                            fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    OutFile = setParameters3(Out, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                             fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                             fixstr(cnt, ConLen, ui.txtSSConPer.text()))


                    files  = [OutFile]
                    arg    = " -in " + InFile + " -applyxfm -init " + MatFile + " -out " + OutFile + \
                                " -paddingsize 0.0 -interp " + ui.cbSSInter.currentData() + " -ref " + SpaceFile
                    thread = RegistrationThread(flirt=Flirt, arg=arg, files=files, InTitle=InTitle)
                    Jobs.append(["Registration", InTitle, thread])
                    print("Job: Registration for " + InTitle + " - is created.")

        if not len(Jobs):
            print("TASK FAILED!")
        else:
            print("TASK DONE.")
            dialog.hide()
            from GUI.frmJobs import frmJobs
            frmJobs.show(frmJobs, Jobs, dialog)


    def btnROIWholeBrain_click(self):
        frmWholeBrainROI.show(frmWholeBrainROI)

    def btnROIProbabilistic_click(self):
        frmProbabilisticROI.show(frmProbabilisticROI)

    def btnROICombine_click(self):
        frmCombineROI.show(frmCombineROI)

    def btnROIManuallyDesign_click(self):
        frmManuallyDesignROI.show(frmManuallyDesignROI)

    def btnROIAtlas_click(self):
        frmAtlasROI.show(frmAtlasROI)

    def btnFECrossEzData_click(self):
        frmFEEZCrossValidation.show(frmFEEZCrossValidation)

    def btnDIOutFile_click(self):
        global ui
        ofile = SelectDir("Select output directory", ui.txtDIOutDIR.text())

        #ofile = SaveFile("Output data file ...",['Data file (*.mat)'],'mat',\
                         #os.path.dirname(ui.txtDIOutFile.text()))
        if len(ofile):
            ui.txtDIOutDIR.setText(ofile)

    def btnDIROIFile_click(self):
        global ui
        roi_file = LoadFile('Select ROI image file ...',['ROI image (*.nii.gz)','All files (*.*)'], 'nii.gz',\
                            os.path.dirname(ui.txtDIROIFile.text()))
        if len(roi_file):
            if os.path.isfile(roi_file):
                ui.txtDIROIFile.setText(roi_file)
            else:
                print("ROI file not found!")

    def btnDILabels_click(self):
        global ui
        filename = LoadFile('Open label file ...', ['Text files (*.txt)', 'All files (*.*)'], 'txt',\
                            os.path.dirname(ui.txtDILabels.text()))
        if len(filename):
            if os.path.isfile(filename):
                ui.txtDILabels.setText(filename)
            else:
                print("File not found!")


    def btnDIRUN_click(self):
        global ui

        msgBox = QMessageBox()
        mainDIR = ui.txtDIDIR.text()
        Task = ui.txtDITask.text()
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
            SubRange = strRange(ui.txtDISubRange.text(),Unique=True)
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
            SubLen = np.int32(ui.txtDISubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is okay!")
        try:
            ConRange = strMultiRange(ui.txtDIConRange.text(),SubSize)
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
            ConLen = np.int32(ui.txtDIConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of Counter is okay!")
        try:
            RunRange = strMultiRange(ui.txtDIRunRange.text(),SubSize)
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
            RunLen = np.int32(ui.txtDIRunLen.value())
            1 / RunLen
        except:
            msgBox.setText("Length of runs must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of runs is valid")

        OutDIR = ui.txtDIOutDIR.text()
        if not len(OutDIR):
            msgBox.setText("Please enter output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        OutDIR = OutDIR.replace("$MAINDIR$", mainDIR)

        OutHDR = ui.txtDIOutHDR.text()
        OutHDR = OutHDR.replace("$TASK$", Task)
        if not len(OutHDR):
            msgBox.setText("Please enter output header file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        OutDAT = ui.txtDIOutDAT.text()
        if not len(OutDAT):
            msgBox.setText("Please enter output data file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        ROIFile = ui.txtDIROIFile.text()
        if not len(ROIFile):
            msgBox.setText("Please enter ROI file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not os.path.isfile(ROIFile):
            msgBox.setText("Cannot find ROI File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            roiHDR = nb.load(ROIFile)
            roiIMG = roiHDR.get_data()
            roiSize = np.shape(roiIMG)
            roiIND = np.where(roiIMG != 0)
        except:
            msgBox.setText("Cannot load ROI File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        print("Number of feature: ", np.shape(roiIND)[1])

        In = ui.txtDIInFile.currentText()
        if not len(In):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if ui.rbDIDynamic.isChecked() or ui.cbDIDM.isChecked():
            DM = ui.txtDIDM.currentText()
            if not len(DM):
                msgBox.setText("Please enter desgin matrix!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            try:
                Threshold = np.float(ui.txtDIThreshold.text())
            except:
                msgBox.setText("Threshold must be a number")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if (Threshold < 0) or (Threshold > 1):
                msgBox.setText("Threshold must be between 0 to 1")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            print("Threshold is valid")

        else:
            LB = ui.txtDILabels.text()
            if not len(LB):
                msgBox.setText("Please enter label files!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Subject
        if ui.cbDISubjectID.isChecked():
            if not len(ui.txtDISubjectID.text()):
                msgBox.setText("Please enter Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Task
        if ui.cbDITaskID.isChecked():
            if not len(ui.txtDITaskID.text()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Run
        if ui.cbDIRunID.isChecked():
            if not len(ui.txtDIRunID.text()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Counter
        if ui.cbDICounterID.isChecked():
            if not len(ui.txtDICounterID.text()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Label
        if ui.cbDILabelID.isChecked():
            if not len(ui.txtDILabelID.text()):
                msgBox.setText("Please enter Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Matrix Label
        if ui.cbDImLabelID.isChecked():
            if not len(ui.txtDImLabelID.text()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Data
        if ui.cbDIDataID.isChecked():
            if not len(ui.txtDIDataID.text()):
                msgBox.setText("Please enter Data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Design
        if ui.cbDIDM.isChecked():
            if not len(ui.txtDIDMID.text()):
                msgBox.setText("Please enter Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Coordinate
        if ui.cbDICoID.isChecked():
            if not len(ui.txtDICoID.text()):
                msgBox.setText("Please enter Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Condition
        if ui.cbDICondID.isChecked():
            if not len(ui.txtDICoundID.text()):
                msgBox.setText("Please enter Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Number of Scan
        if ui.cbDINScanID.isChecked():
            if not len(ui.txtDINScanID.text()):
                msgBox.setText("Please enter Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False


        print("Checking files ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                for r in RunRange[si]:
                    InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                            fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                            fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                    if os.path.isfile(InFile):
                        print(InFile + " - is OKAY.")
                    else:
                        print(InFile + " - not found!")
                        return

                    EventFolder = setParameters3(ui.txtDIEventDIR.text(), mainDIR,
                                                 fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                                 fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                                 fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                    CondFile = EventFolder + ui.txtDICondPre.text() + ".mat"
                    if os.path.isfile(CondFile):
                        print(CondFile + " - is OKAY.")
                    else:
                        print(CondFile + " - not found!")
                        return

                    if ui.rbDIDynamic.isChecked() or ui.cbDIDM.isChecked():

                        DMFile = setParameters3(DM, mainDIR, fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                            fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                            fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        if os.path.isfile(DMFile):
                            print(DMFile + " - is OKAY.")
                        else:
                            print(DMFile + " - not found!")
                            return
                    else:
                        LBFile = setParameters3(LB, mainDIR, fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                            fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                            fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        if os.path.isfile(LBFile):
                            print(LBFile + " - is OKAY.")
                        else:
                            print(LBFile + " - not found!")
                            return

        fMRISize    = None

        SubjectID   = list()
        RunID       = list()
        TaskID      = list()
        CounterID   = list()
        Y           = list()
        NScanID     = list()
        DesignID    = list()
        DataFiles   = list()
        CondID      = Conditions()
        NumberOFExtract = 0
        NumberOFALL = 0
        # RUNNING ...
        try:
            os.stat(OutDIR)
        except:
            os.makedirs(OutDIR,exist_ok=True)

        print("Extraction ...")
        for si, s in enumerate(SubRange):
            for cnt in ConRange[si]:
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in RunRange[si]:
                    X = list()
                    try:
                        InFile = setParameters3(In, mainDIR,
                                    fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                    fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                    fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        InHDR = None # Free Mem
                        InHDR = nb.load(InFile)
                        InIMG = InHDR.get_data()
                        if fMRISize is None:
                            fMRISize = np.shape(InIMG)[0:3]
                            if roiSize != fMRISize:
                                print("ROI and fMRI images must be in the same size!")
                                msgBox.setText("ROI and fMRI images must be in the same size!")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return

                        else:
                            if fMRISize != np.shape(InIMG)[0:3]:
                                print("Image size is not matched!")
                                msgBox.setText("Image size is not matched!")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return
                        NScan = np.shape(InIMG)[3]
                    except:
                        print(InFile + " - cannot load image file!")
                        return

                    print(InFile + " - is loaded.")
                    print("Number of scans: ", NScan)

                    try:
                        EventFolder = setParameters3(ui.txtDIEventDIR.text(), mainDIR,
                                                     fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                                     fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                                     fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        CondFile = EventFolder + ui.txtDICondPre.text() + ".mat"
                        CondTitle = io.loadmat(CondFile)["Cond"]
                        CondSize = len(CondTitle)
                        for condindx in range(0, CondSize):
                            CondID.add_cond(CondTitle[condindx][0][0],CondTitle[condindx][1][0])

                    except:
                        print(CondFile + " - cannot load file!")
                        return

                    print("Number of conditions: ", CondSize)

                    if ui.rbDIDynamic.isChecked() or ui.cbDIDM.isChecked():
                        try:
                            DMFile = setParameters3(DM, mainDIR, fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                                fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                                fixstr(cnt, ConLen, ui.txtDIConPer.text()))

                            DesginValues = convertDesignMatrix(DMFile, CondSize)
                            DMval = np.transpose(DesginValues)
                            print("Desing Matrix is recovered.")
                        except:
                            print(DMFile + " - cannot load file!")
                            return


                    # Session Class Labels
                    Y_Sess = list()

                    if ui.rbDIDynamic.isChecked():
                        print("Estimating class labels ...")
                        DMNew = list()
                        DMCoeff     = list()
                        for valinx in range(0, len(DMval)):
                            val = DMval[valinx]
                            val = val - np.min(val)
                            val = val / np.max(val)
                            coeff = fitLine(val)
                            val = val - coeff
                            DMCoeff.append(coeff)
                            DMNew.append(val)
                        DMNew = np.transpose(DMNew)

                        for DMLineIndx, DMLine in enumerate(DMNew):
                            MaxValIndx = np.argmax(DMLine)
                            if DMLine[MaxValIndx] < Threshold:
                                Y_Sess.append(0)
                            else:
                                Y_Sess.append(MaxValIndx + 1)
                        Y_Sess = np.int32(Y_Sess)
                    else:
                        print("Loading class labels ...")
                        try:
                            LBFile = setParameters3(LB, mainDIR, fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                            fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                            fixstr(cnt, ConLen, ui.txtDIConPer.text()))

                            Y_Sess = np.int32(open(LBFile).read().rsplit())
                        except:
                            print("Cannot read label file!")
                            return

                    if len(Y_Sess) == NScan:
                        print("Number of class labels is okay. Class labels: ", len(Y_Sess))
                    else:
                        print("Number of class labels must be equal to number of scans! Class labels: ", len(Y_Sess))
                        return

                    if np.max(Y_Sess) >= CondSize:
                        print("Number of conditions is okay. Conditions: ", np.max(Y_Sess))
                    else:
                        print("WARNING: some class labels are not found!", np.max(Y_Sess))


                    for instID, yID in enumerate(Y_Sess):
                        NumberOFALL = NumberOFALL + 1
                        if not ui.cbDIRemoveRest.isChecked() or yID != 0:
                            NumberOFExtract = NumberOFExtract + 1
                            # NScan
                            if ui.cbDINScanID.isChecked():
                                NScanID.append(instID)

                            # Subject
                            if ui.cbDISubjectID.isChecked():
                                SubjectID.append(s)

                            # Task
                            if ui.cbDITaskID.isChecked():
                                TaskID.append(ui.txtDITask.text())

                            # Run
                            if ui.cbDIRunID.isChecked():
                                RunID.append(r)

                            # Counter
                            if ui.cbDICounterID.isChecked():
                                CounterID.append(cnt)

                            # Label
                            if ui.cbDILabelID.isChecked():
                                Y.append(yID)

                            # Data
                            if ui.cbDIDataID.isChecked():
                                Snapshot = InIMG[:, :, :, instID]
                                X.append(Snapshot[roiIND])

                            if ui.cbDIDM.isChecked():
                                DesignID.append(DesginValues[instID])

                    if ui.cbDIDataID.isChecked():
                        OutDataFile = setParameters3(OutDAT, "",
                                    fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                    fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                    fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        print("Saving data " + OutDataFile + "... ")
                        DataFiles.append(OutDataFile)
                        io.savemat(OutDIR + '/' + OutDataFile, mdict={ui.txtDIDataID.text(): X},appendmat=False, do_compression=True)
                        print("Data " + OutDataFile + " is saved!")

        print("Saving Header " + OutHDR + "...")
        OutData = dict()
        OutData["imgShape"] = np.array(fMRISize)
        OutData["DataStructure"] = []
        if len(DataFiles):
            OutData["DataStructure"] = [ui.txtDIDataID.text()]
            OutData[ui.txtDIDataID.text() + "_files"] = DataFiles

        # NScan
        if ui.cbDINScanID.isChecked():
            OutData[ui.txtDINScanID.text()] = NScanID
        # Subject
        if ui.cbDISubjectID.isChecked():
            OutData[ui.txtDISubjectID.text()] = SubjectID
        # Task
        if ui.cbDITaskID.isChecked():
            OutData[ui.txtDITaskID.text()] = np.array(TaskID,dtype=object)
        # Run
        if ui.cbDIRunID.isChecked():
            OutData[ui.txtDIRunID.text()] = RunID
        # Counter
        if ui.cbDICounterID.isChecked():
            OutData[ui.txtDICounterID.text()] = CounterID
        # Label
        if ui.cbDILabelID.isChecked():
            OutData[ui.txtDILabelID.text()] = Y
        # Matrix Label
        if ui.cbDImLabelID.isChecked():
            OutData[ui.txtDImLabelID.text()] = label_binarize(Y,np.unique(Y))
        # Design
        if ui.cbDIDM.isChecked():
            OutData[ui.txtDIDMID.text()] = DesignID
        # Coordinate
        if ui.cbDICoID.isChecked():
            OutData[ui.txtDICoID.text()] = np.array(roiIND)
        # Condition
        if ui.cbDICondID.isChecked():
            OutData[ui.txtDICoundID.text()] = np.array(CondID.get_cond(),dtype=object)

        io.savemat(OutDIR + '/' + OutHDR, mdict=OutData,appendmat=False,do_compression=True)
        print("Number of all instances:", NumberOFALL)
        print("Number of selected instances:", NumberOFExtract)
        print("Number of features: ", np.shape(roiIND)[1])
        print("DONE.")
        msgBox.setText("Data Integration is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def btnDIDraw_click(self):
        global ui
        msgBox = QMessageBox()
        mainDIR = ui.txtDIDIR.text()
        Task = ui.txtDITask.text()
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
            SubRange = strRange(ui.txtDISubRange.text(),Unique=True)
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
            SubLen = np.int32(ui.txtDISubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is okay!")
        try:
            ConRange = strMultiRange(ui.txtDIConRange.text(),SubSize)
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
            ConLen = np.int32(ui.txtDIConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of Counter is okay!")
        try:
            RunRange = strMultiRange(ui.txtDIRunRange.text(),SubSize)
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
            RunLen = np.int32(ui.txtDIRunLen.value())
            1 / RunLen
        except:
            msgBox.setText("Length of runs must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of runs is valid")


        if not ui.rbDIDynamic.isChecked():
            msgBox.setText("Please select dynamic method first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Threshold = np.float(ui.txtDIThreshold.text())
        except:
            msgBox.setText("Threshold must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if (Threshold < 0) or (Threshold > 1):
            msgBox.setText("Threshold must be between 0 to 1")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        print("Threshold is valid")

        DM = ui.txtDIDM.currentText()
        if not len(DM):
            msgBox.setText("Please enter desgin matrix!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        setting = Setting()
        setting.Task = Task

        setting.SubRange    = ui.txtDISubRange.text()
        setting.SubLen      = SubLen
        setting.SubPer      = ui.txtDISubPer.text()

        setting.RunRange    = ui.txtDIRunRange.text()
        setting.RunLen      = RunLen
        setting.RunPer      = ui.txtDIRunPer.text()


        setting.ConRange     = ui.txtDIConRange.text()
        setting.ConLen      = ConLen
        setting.ConPer      = ui.txtDIConPer.text()
        sSess = frmSelectSession(None, setting=setting)

        try:
            EventFolder = setParameters3(ui.txtDIEventDIR.text(), mainDIR,
                                         fixstr(sSess.SubID, SubLen, ui.txtDISubPer.text()), \
                                         fixstr(sSess.RunID, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                         fixstr(sSess.ConID, ConLen, ui.txtDIConPer.text()))
            CondFile = EventFolder + ui.txtDICondPre.text() + ".mat"
            CondTitle = io.loadmat(CondFile)["Cond"]
            CondSize = len(CondTitle)
        except:
            print(CondFile + " - not found!")
            return

        try:
            DMFile = setParameters3(DM, mainDIR, fixstr(sSess.SubID, SubLen, ui.txtDISubPer.text()), \
                                    fixstr(sSess.RunID, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                    fixstr(sSess.ConID, ConLen, ui.txtDIConPer.text()))

            DesginValues = convertDesignMatrix(DMFile, CondSize)
            DMval = np.transpose(DesginValues)
            print("Desing Matrix is recovered.")
        except:
            print(DMFile + " - cannot load file!")
            return

        print("Estimating class labels ...")
        DMNew = list()
        DMCoeff = list()
        for valinx in range(0, len(DMval)):
            val = DMval[valinx]
            val = val - np.min(val)
            val = val / np.max(val)
            coeff = fitLine(val)
            val = val - coeff
            DMCoeff.append(coeff)
            DMNew.append(val)


        Y_Sess = list()

        for DMLineIndx, DMLine in enumerate(np.transpose(DMNew)):
            MaxValIndx = np.argmax(DMLine)
            if DMLine[MaxValIndx] < Threshold:
                Y_Sess.append(0)
            else:
                Y_Sess.append(MaxValIndx + 1)

        NumPlot = np.shape(DMNew)[0]
        NumTimePoints = np.shape(DMNew)[1]
        TimePoints = range(0,NumTimePoints)

        if not ui.cbDIDraw.isChecked():
            fig, ax = plt.subplots()

        if not ui.cbDIColor.isChecked():
            yColor = "-y"
            bColor = "-b"
            rColor = "-r"
            gColor = "-g"
            goColor = "og"
        else:
            yColor = ""
            bColor = ""
            rColor = ""
            gColor = ""
            goColor = "o"

        for pltindx in range(0,NumPlot):

            if ui.cbDIDraw.isChecked():
                fig, ax = plt.subplots()

            if ui.cbDIRest.isChecked():
                ax.plot(TimePoints, Threshold * np.ones(NumTimePoints), yColor, label="L" + str(pltindx + 1) + ":Rest")
                ax.plot(TimePoints, - 1 * Threshold * np.ones(NumTimePoints), yColor)

            if ui.cbDINorm.isChecked():
                ax.plot(TimePoints, DMNew[pltindx], bColor, label="L" + str(pltindx + 1) +":Norm (coeff= {0:.{digits}f}) ".format(DMCoeff[pltindx],digits=3))

            if ui.cbDIReal.isChecked():
                ax.plot(TimePoints, DMval[pltindx], rColor, label="L" + str(pltindx + 1) +":Real")

            if ui.cbDIClass.isChecked():
                val = DMNew[pltindx]
                val[np.where(np.array(Y_Sess) != pltindx + 1)] = None
                ax.plot(TimePoints, val, gColor, label="L" + str(pltindx + 1) +":Class")
                ax.plot(TimePoints, val, goColor)

            if ui.cbDILegend.isChecked():
                leg = ax.legend( shadow=True)
                leg.draggable()
        plt.show()

    def btnDIConverEzData_click(self):
        frmEzMat.show(frmEzMat)

    def btnDIRemoveRest_click(self):
        frmRemoveRestScan.show(frmRemoveRestScan)

    def btnDIRemoveRest2_click(self):
        frmRemoveRestScanCross.show(frmRemoveRestScanCross)

    def btnDICombineData_click(self):
        frmCombineData.show(frmCombineData)

    def btnFEU_click(self):
        FEID = ui.cbFEU.currentData()
        if FEID == 1:
            from GUI.frmFENormalization import frmFENormalization
            frmFENormalization.show(frmFENormalization)
            return
        if FEID == 10000:
            from GUI.frmFEPCA import frmFEPCA
            frmFEPCA.show(frmFEPCA)
            return
        if FEID == 10001:
            from GUI.frmFEIPCA import frmFEIPCA
            frmFEIPCA.show(frmFEIPCA)
            return
        if FEID == 10002:
            from GUI.frmFEKPCA import frmFEKPCA
            frmFEKPCA.show(frmFEKPCA)
            return
        if FEID == 10003:
            from GUI.frmFESPCA import frmFESPCA
            frmFESPCA.show(frmFESPCA)
            return
        if FEID == 20000:
            from GUI.frmFEFactorAnalysis import frmFEFactorAnalysis
            frmFEFactorAnalysis.show(frmFEFactorAnalysis)
            return
        if FEID == 20001:
            from GUI.frmFEFastICA import frmFEFastICA
            frmFEFastICA.show(frmFEFastICA)
            return
        if FEID == 20002:
            from GUI.frmFEDictionaryLearning import frmFEDictionaryLearning
            frmFEDictionaryLearning.show(frmFEDictionaryLearning)
            return
        if FEID == 30000:
            from GUI.frmFEMRPA import frmFEMRPA
            frmFEMRPA.show(frmFEMRPA)
            return

    def btnFECross_click(self):
        frmFECrossValidation.show(frmFECrossValidation)


    def btnFES_click(self):
        FEID = ui.cbFES.currentData()
        if FEID == 1:
            from GUI.frmFELDA import frmFELDA
            frmFELDA.show(frmFELDA)
            return

    def btnFA_click(self):
        FAID = ui.cbFA.currentData()

        if FAID == 10000:
            from GUI.frmFAHA import frmFAHA
            frmFAHA.show(frmFAHA)
            return

# Auto Run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmFeatureAnalysis.show(frmFeatureAnalysis)
    sys.exit(app.exec_())