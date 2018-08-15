#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QMessageBox
import os, platform
import subprocess
from PyQt5.QtWidgets import QFileDialog, QDialog

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui

import configparser as cp
import glob
import nibabel as nb
import numpy as np
import scipy.io as io
from scipy.stats import mode
from sklearn.preprocessing import label_binarize


import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt



from frmFeatureAnalysisGUI import *
from frmTransformationMatrix import frmTansformationMatrix
from frmWholeBrainROI import frmWholeBrainROI
from frmProbabilisticROI import frmProbabilisticROI
from frmCombineROI import frmCombineROI
from frmManuallyDesignROI import frmManuallyDesignROI
from frmAtlasROI import frmAtlasROI
from frmRemoveRestScan import frmRemoveRestScan
from frmCombineData import frmCombineData
from frmFECrossValidation import frmFECrossValidation


from frmSelectSession import frmSelectSession
from utility import fixstr, getDirSpaceINI, getDirSpace, setParameters3, convertDesignMatrix, fitLine
from Setting import Setting
from SettingHistory import History
from Conditions import Conditions


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
        from utility import getVersion, getBuild
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

        # FSL Parameters
        if platform.system() == "Linux":
            ui.txtFSLDIR.setText("")
            if os.path.isfile("/usr/bin/fsl5.0-flirt"):
                ui.txtFlirt.setText("/usr/bin/fsl5.0-flirt")
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
            else:
                ui.txtFlirt.setText("")


        # Unsupervised Feature Engineering
        ui.cbFEU.addItem("Data Normalization",1)
        ui.cbFEU.addItem("Dictionary Learning",20002)
        ui.cbFEU.addItem("Factor Analysis",20000)
        ui.cbFEU.addItem("Fast Independent Component Analysis (FastICA)",20001)
        ui.cbFEU.addItem("Incremental Principal Component Analysis (IPCA)",10001)
        ui.cbFEU.addItem("Kernel Principal Component Analysis (KPCA)",10002)
        ui.cbFEU.addItem("Multi Region Pattern Analysis (Snapshots)", 30000)
        ui.cbFEU.addItem("Principal Component Analysis (PCA)",10000)
        ui.cbFEU.addItem("Sparse Principal Component Analysis (SPCA)",10003)

        # Supervised Feature Engineering
        ui.cbFES.addItem("Linear Discriminant Analysis (LDA)",1)


        # Functional Alignment
        ui.cbFA.addItem("Regularized Hyperalignment", 10000)


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
        ui.btnDICombineData.clicked.connect(self.btnDICombineData_click)
        ui.btnFEURun.clicked.connect(self.btnFEU_click)
        ui.btnFESRun.clicked.connect(self.btnFES_click)
        ui.btnDIDraw.clicked.connect(self.btnDIDraw_click)
        ui.btnFECross.clicked.connect(self.btnFECross_click)
        ui.btnFARun.clicked.connect(self.btnFA_click)


    # Exit function
    def btnClose_click(self):
        global dialog, parent
        dialog.close()

    def btnSSSetting_click(self):
        from utility import getVersion
        global ui

        if os.path.isfile(ui.txtSSSetting.currentText()):
            currDir = os.path.dirname(ui.txtSSSetting.currentText())
        else:
            currDir = ""

        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open setting file ...", currDir,
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
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

            if setting.Version != getVersion():
                print("WARNING: You are using different version of Easy fMRI!!!")

            if not setting.empty:
                ui.txtSSSetting.setCurrentText(filename)
                ui.txtSSDIR.setText(setting.mainDIR)
                # ui.txtSSSpace.setCurrentText(setting.MNISpace)
                ui.txtSSTask.setText(setting.Task)
                ui.txtSSSubFrom.setValue(setting.SubFrom)
                ui.txtSSSubTo.setValue(setting.SubTo)
                ui.txtSSSubLen.setValue(setting.SubLen)
                ui.txtSSSubPer.setText(setting.SubPer)
                ui.txtSSConFrom.setValue(setting.ConFrom)
                ui.txtSSConTo.setValue(setting.ConTo)
                ui.txtSSConLen.setValue(setting.ConLen)
                ui.txtSSConPer.setText(setting.ConPer)
                ui.txtSSRunNum.setText(setting.Run)
                ui.txtSSRunPer.setText(setting.RunPer)
                ui.txtSSRunLen.setValue(setting.RunLen)

    def btnDISetting_click(self):
        from utility import getVersion
        global ui

        if os.path.isfile(ui.txtDISetting.currentText()):
            currDir = os.path.dirname(ui.txtDISetting.currentText())
        else:
            currDir = ""

        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open setting file ...", currDir,
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
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

            if setting.Version != getVersion():
                print("WARNING: You are using different version of Easy fMRI!!!")

            if not setting.empty:
                ui.txtDISetting.setCurrentText(filename)
                ui.txtDIDIR.setText(setting.mainDIR)
                # ui.txtSSSpace.setCurrentText(setting.MNISpace)
                ui.txtDITask.setText(setting.Task)
                ui.txtDISubFrom.setValue(setting.SubFrom)
                ui.txtDISubTo.setValue(setting.SubTo)
                ui.txtDISubLen.setValue(setting.SubLen)
                ui.txtDISubPer.setText(setting.SubPer)
                ui.txtDIConFrom.setValue(setting.ConFrom)
                ui.txtDIConTo.setValue(setting.ConTo)
                ui.txtDIConLen.setValue(setting.ConLen)
                ui.txtDIConPer.setText(setting.ConPer)
                ui.txtDIRunNum.setText(setting.Run)
                ui.txtDIRunPer.setText(setting.RunPer)
                ui.txtDIRunLen.setValue(setting.RunLen)

    def btnSSSettingReload_click(self):
        from utility import getVersion
        global ui
        filename = ui.txtSSSetting.currentText()
        if os.path.isfile(filename):
            if len(filename):
                setting = Setting()
                setting.Load(filename)

                if setting.Version != getVersion():
                    print("WARNING: You are using different version of Easy fMRI!!!")

                if not setting.empty:
                    ui.txtSSSetting.setCurrentText(filename)
                    ui.txtSSDIR.setText(setting.mainDIR)
                    # ui.txtSSSpace.setCurrentText(setting.MNISpace)
                    ui.txtSSTask.setText(setting.Task)
                    ui.txtSSSubFrom.setValue(setting.SubFrom)
                    ui.txtSSSubTo.setValue(setting.SubTo)
                    ui.txtSSSubLen.setValue(setting.SubLen)
                    ui.txtSSSubPer.setText(setting.SubPer)
                    ui.txtSSConFrom.setValue(setting.ConFrom)
                    ui.txtSSConTo.setValue(setting.ConTo)
                    ui.txtSSConLen.setValue(setting.ConLen)
                    ui.txtSSConPer.setText(setting.ConPer)
                    ui.txtSSRunNum.setText(setting.Run)
                    ui.txtSSRunPer.setText(setting.RunPer)
                    ui.txtSSRunLen.setValue(setting.RunLen)
        else:
            print("Setting file not found!")

    def btnDISettingReload_click(self):
        from utility import getVersion
        global ui
        filename = ui.txtDISetting.currentText()
        if os.path.isfile(filename):
            if len(filename):
                setting = Setting()
                setting.Load(filename)

                if setting.Version != getVersion():
                    print("WARNING: You are using different version of Easy fMRI!!!")

                if not setting.empty:
                    ui.txtDISetting.setCurrentText(filename)
                    ui.txtDIDIR.setText(setting.mainDIR)
                    # ui.txtSSSpace.setCurrentText(setting.MNISpace)
                    ui.txtDITask.setText(setting.Task)
                    ui.txtDISubFrom.setValue(setting.SubFrom)
                    ui.txtDISubTo.setValue(setting.SubTo)
                    ui.txtDISubLen.setValue(setting.SubLen)
                    ui.txtDISubPer.setText(setting.SubPer)
                    ui.txtDIConFrom.setValue(setting.ConFrom)
                    ui.txtDIConTo.setValue(setting.ConTo)
                    ui.txtDIConLen.setValue(setting.ConLen)
                    ui.txtDIConPer.setText(setting.ConPer)
                    ui.txtDIRunNum.setText(setting.Run)
                    ui.txtDIRunPer.setText(setting.RunPer)
                    ui.txtDIRunLen.setValue(setting.RunLen)
        else:
            print("Setting file not found!")

    def btnSSMatFile_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open image file ...", os.path.dirname(ui.txtSSMatFile.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtSSMatFile.setText(filename)
            else:
                print("Image file not found!")

    def btnSSSpace_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open space file ...", os.path.dirname(ui.txtSSSpace.currentText()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
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
            SubFrom = np.int32(ui.txtSSSubFrom.value())
            1 / SubFrom
        except:
            msgBox.setText("Subject From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubTo = np.int32(ui.txtSSSubTo.value())
            1 / SubTo
        except:
            msgBox.setText("Subject To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if SubTo < SubFrom:
            msgBox.setText("Subject To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Number of subjects is valid")
        try:
            SubLen = np.int32(ui.txtSSSubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is valid")

        try:
            ConFrom = np.int32(ui.txtSSConFrom.value())
            1 / ConFrom
        except:
            msgBox.setText("Counter From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            ConTo = np.int32(ui.txtSSConTo.value())
            1 / ConTo
        except:
            msgBox.setText("Counter To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if ConTo < ConFrom:
            msgBox.setText("Conunter To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter is valid")
        try:
            ConLen = np.int32(ui.txtSSConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of counter is valid")

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

        StrRuns = str(ui.txtSSRunNum.text()).replace("\'", " ").replace(",", " ").replace("[", "").replace("]",
                                                                                                           "").split()
        Run = []
        for srun in StrRuns:
            try:
                Run.append(np.int32(srun))
            except:
                msgBox.setText("Run must include an integer array")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if (len(Run) == 1):
            runValue = Run[0]
            Run = []
            for _ in range(int(ui.txtSSSubFrom.value()), int(ui.txtSSSubTo.value()) + 1):
                Run.append(runValue)
        else:
            if (len(Run) != (ui.txtSSSubTo.value() - ui.txtSSSubFrom.value() + 1)):
                msgBox.setText(
                    "Number of Runs must include a unique number for all subject or an array with size of number of subject, e.g. [1,2,2,1]")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        print("Number of Runs are okay.")

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
        for si, s in enumerate(range(SubFrom, SubTo + 1)):
            for cnt in range(ConFrom, ConTo + 1):
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
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

        print("Registration ...")
        for si, s in enumerate(range(SubFrom, SubTo + 1)):
            for cnt in range(ConFrom, ConTo + 1):
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    MatFile = setParameters3(Mat, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                             fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                             fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    SpaceFile = setParameters3(Space, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                               fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                               fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    InFile = setParameters3(In, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                            fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                            fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    OutFile = setParameters3(Out, mainDIR, fixstr(s, SubLen, ui.txtSSSubPer.text()), \
                                             fixstr(r, RunLen, ui.txtSSRunPer.text()), ui.txtSSTask.text(), \
                                             fixstr(cnt, ConLen, ui.txtSSConPer.text()))

                    RunScript = Flirt + " -in " + InFile + " -applyxfm -init " + MatFile + " -out " + OutFile + \
                                " -paddingsize 0.0 -interp " + ui.cbSSInter.currentData() + " -ref " + SpaceFile

                    os.system(RunScript)
                    print(OutFile + " - is created.")

        msgBox.setText("Registration is done!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

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

    def btnDIOutFile_click(self):
        global ui
        current = ui.txtDIOutFile.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        ofile = dialog.getSaveFileName(None, "Output File", current, "", "", flags)[0]
        if len(ofile):
            ui.txtDIOutFile.setText(ofile)

    def btnDIROIFile_click(self):
        global ui
        current = ui.txtDIROIFile.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        roi_file = dialog.getOpenFileName(None, "Select ROI File", current, "", "", flags)[0]
        if len(roi_file):
            if os.path.isfile(roi_file):
                ui.txtDIROIFile.setText(roi_file)
            else:
                print("ROI file not found!")

    def btnDILabels_click(self):
        global ui
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open label file ...", os.path.dirname(ui.txtDILabels.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
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
            SubFrom = np.int32(ui.txtDISubFrom.value())
            1 / SubFrom
        except:
            msgBox.setText("Subject From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubTo = np.int32(ui.txtDISubTo.value())
            1 / SubTo
        except:
            msgBox.setText("Subject To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if SubTo < SubFrom:
            msgBox.setText("Subject To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Number of subjects is valid")
        try:
            SubLen = np.int32(ui.txtDISubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is valid")

        try:
            ConFrom = np.int32(ui.txtDIConFrom.value())
            1 / ConFrom
        except:
            msgBox.setText("Counter From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            ConTo = np.int32(ui.txtDIConTo.value())
            1 / ConTo
        except:
            msgBox.setText("Counter To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if ConTo < ConFrom:
            msgBox.setText("Conunter To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter is valid")
        try:
            ConLen = np.int32(ui.txtDIConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of counter is valid")

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


        StrRuns = str(ui.txtDIRunNum.text()).replace("\'", " ").replace(",", " ").replace("[", "").replace("]",
                                                                                                           "").split()
        Run = []
        for srun in StrRuns:
            try:
                Run.append(np.int32(srun))
            except:
                msgBox.setText("Run must include an integer array")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if (len(Run) == 1):
            runValue = Run[0]
            Run = []
            for _ in range(int(ui.txtDISubFrom.value()), int(ui.txtDISubTo.value()) + 1):
                Run.append(runValue)
        else:
            if (len(Run) != (ui.txtDISubTo.value() - ui.txtDISubFrom.value() + 1)):
                msgBox.setText(
                    "Number of Runs must include a unique number for all subject or an array with size of number of subject, e.g. [1,2,2,1]")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        print("Number of Runs are okay.")

        OutFile = ui.txtDIOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter output file!")
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
            #roiShape = np.shape(roiIMG)
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
        for si, s in enumerate(range(SubFrom, SubTo + 1)):
            for cnt in range(ConFrom, ConTo + 1):
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
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
        X           = list()
        Y           = list()
        NScanID     = list()
        DesignID    = list()
        CondID      = Conditions()
        NumberOFExtract = 0
        NumberOFALL = 0


        print("Extraction ...")
        for si, s in enumerate(range(SubFrom, SubTo + 1)):
            for cnt in range(ConFrom, ConTo + 1):
                print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                # SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    try:
                        InFile = setParameters3(In, mainDIR,
                                    fixstr(s, SubLen, ui.txtDISubPer.text()), \
                                    fixstr(r, RunLen, ui.txtDIRunPer.text()), ui.txtDITask.text(), \
                                    fixstr(cnt, ConLen, ui.txtDIConPer.text()))
                        InHDR = nb.load(InFile)
                        InIMG = InHDR.get_data()
                        if fMRISize is None:
                            fMRISize = np.shape(InIMG)[0:3]
                            if roiSize != fMRISize:
                                print("ROI and fMRI images must be in the same size!")

                        else:
                            if fMRISize != np.shape(InIMG)[0:3]:
                                print("Image size is not matched!")
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


                    OutData = dict()
                    OutData["imgShape"] = fMRISize

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
                    # Data
                    if ui.cbDIDataID.isChecked():
                        OutData[ui.txtDIDataID.text()] = X
                    # Design
                    if ui.cbDIDM.isChecked():
                        OutData[ui.txtDIDMID.text()] = DesignID
                    # Coordinate
                    if ui.cbDICoID.isChecked():
                        OutData[ui.txtDICoID.text()] = roiIND
                    # Condition
                    if ui.cbDICondID.isChecked():
                        OutData[ui.txtDICoundID.text()] = np.array(CondID.get_cond(),dtype=object)

        print("Saving ...")
        io.savemat(ui.txtDIOutFile.text(), mdict=OutData)
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
            SubFrom = np.int32(ui.txtDISubFrom.value())
            1 / SubFrom
        except:
            msgBox.setText("Subject From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubTo = np.int32(ui.txtDISubTo.value())
            1 / SubTo
        except:
            msgBox.setText("Subject To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if SubTo < SubFrom:
            msgBox.setText("Subject To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Number of subjects is valid")
        try:
            SubLen = np.int32(ui.txtDISubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is valid")

        try:
            ConFrom = np.int32(ui.txtDIConFrom.value())
            1 / ConFrom
        except:
            msgBox.setText("Counter From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            ConTo = np.int32(ui.txtDIConTo.value())
            1 / ConTo
        except:
            msgBox.setText("Counter To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if ConTo < ConFrom:
            msgBox.setText("Conunter To is smaller then Subject From!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter is valid")
        try:
            ConLen = np.int32(ui.txtDIConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of counter is valid")

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


        StrRuns = str(ui.txtDIRunNum.text()).replace("\'", " ").replace(",", " ").replace("[", "").replace("]",
                                                                                                           "").split()
        Run = []
        for srun in StrRuns:
            try:
                Run.append(np.int32(srun))
            except:
                msgBox.setText("Run must include an integer array")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if (len(Run) == 1):
            runValue = Run[0]
            Run = []
            for _ in range(int(ui.txtDISubFrom.value()), int(ui.txtDISubTo.value()) + 1):
                Run.append(runValue)
        else:
            if (len(Run) != (ui.txtDISubTo.value() - ui.txtDISubFrom.value() + 1)):
                msgBox.setText(
                    "Number of Runs must include a unique number for all subject or an array with size of number of subject, e.g. [1,2,2,1]")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        print("Number of Runs are okay.")

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

        setting.SubFrom = SubFrom
        setting.SubTo = SubTo
        setting.SubLen = SubLen
        setting.SubPer = ui.txtDISubPer.text()

        setting.Run    = Run
        setting.RunLen = RunLen
        setting.RunPer = ui.txtDIRunPer.text()


        setting.ConFrom = ConFrom
        setting.ConTo = ConTo
        setting.ConLen = ConLen
        setting.ConPer = ui.txtDIConPer.text()

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



    def btnDIRemoveRest_click(self):
        frmRemoveRestScan.show(frmRemoveRestScan)

    def btnDICombineData_click(self):
        frmCombineData.show(frmCombineData)


    def btnFEU_click(self):
        FEID = ui.cbFEU.currentData()
        if FEID == 1:
            from frmFENormalization import frmFENormalization
            frmFENormalization.show(frmFENormalization)
            return
        if FEID == 10000:
            from frmFEPCA import frmFEPCA
            frmFEPCA.show(frmFEPCA)
            return
        if FEID == 10001:
            from frmFEIPCA import frmFEIPCA
            frmFEIPCA.show(frmFEIPCA)
            return
        if FEID == 10002:
            from frmFEKPCA import frmFEKPCA
            frmFEKPCA.show(frmFEKPCA)
            return
        if FEID == 10003:
            from frmFESPCA import frmFESPCA
            frmFESPCA.show(frmFESPCA)
            return
        if FEID == 20000:
            from frmFEFactorAnalysis import frmFEFactorAnalysis
            frmFEFactorAnalysis.show(frmFEFactorAnalysis)
            return
        if FEID == 20001:
            from frmFEFastICA import frmFEFastICA
            frmFEFastICA.show(frmFEFastICA)
            return
        if FEID == 20002:
            from frmFEDictionaryLearning import frmFEDictionaryLearning
            frmFEDictionaryLearning.show(frmFEDictionaryLearning)
            return
        if FEID == 30000:
            from frmFEMRPA import frmFEMRPA
            frmFEMRPA.show(frmFEMRPA)
            return

    def btnFECross_click(self):
        frmFECrossValidation.show(frmFECrossValidation)


    def btnFES_click(self):
        FEID = ui.cbFES.currentData()
        if FEID == 1:
            from frmFELDA import frmFELDA
            frmFELDA.show(frmFELDA)
            return

    def btnFA_click(self):
        FAID = ui.cbFA.currentData()

        if FAID == 10000:
            from frmFAHA import frmFAHA
            frmFAHA.show(frmFAHA)
            return





# Auto Run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmFeatureAnalysis.show(frmFeatureAnalysis)
    sys.exit(app.exec_())
