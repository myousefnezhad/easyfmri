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

import configparser as cp
import os
import platform
import subprocess
import sys, shutil
import logging
import nibabel as nb
import numpy as np
import scipy.io as io


from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QMessageBox


from Base.Setting import Setting
from Base.SettingHistory import History
from Base.fsl import FSL
from Base.tools import Tools
from Base.utility import getTimeSliceText, fixstr, setParameters3, getSettingVersion, encoding, strRange, strMultiRange, OpenReport
from Base.dialogs import SaveFile, LoadFile, SelectDir

from Preprocess.BIDS import load_BIDS

from GUI.frmEventConcatenator import frmEventConcatenator
from GUI.frmEventViewer import frmEventViewer
from GUI.frmPreprocessGUI import *
from GUI.frmRenameFile import frmRenameFile
from GUI.frmScriptEditor import frmScriptEditor
from GUI.frmfMRIConcatenator import frmfMRIConcatenator
from GUI.frmSelectSession import frmSelectSession
from GUI.frmImageInfo import frmImageInfo


from Preprocess.BrainExtractor import BrainExtractor
from Preprocess.EventGenerator import EventGenerator
from Preprocess.RunPreprocess import RunPreprocess
from Preprocess.ScriptGenerator import ScriptGenerator


logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets


def EventCode():
    return\
"""# This procedure extracts information from the event files.
# Note 1: You can write any Python 3 style codes in order to extract the information.
# Note 2: Numpy can be called by using np, e.g. np.int32()
#
# Input:
# \tEvent[] includes each line of the event files in each iteration.
# \tk shows line number in each event file --- starting from 0
# \t\tYou may use k for indexing very large design matrix rather 
# \t\tthat trial type, e.g., movie data 
# Output:
# \t1. RowStartID: denotes the first row of each files that is contained the information.
# \t   It starts from 0, and the default value is 1 (the first row is considered as the header).
# \t2. Onset: the time that each stimulus happens. Its type is float.
# \t3. Duration:  the echo time (TE). Its type is float.
# \t4. Condition: the condition title (category of stimuli). Its type is str.

# Handling headers ->
RowStartID = 1

# Skip is not zero for any row that you don't want to use it!
Skip = 0

# Extracting onset ->
# In order to handle the headers, you must use this style:
try:
    Onset = float(Event[0])
except:
    Onset = None
    Skip = 1

# Extracting echo time ->
# In order to handle the headers, you must use this style:
try:
    Duration = float(Event[1])
except:
    Duration = None
    Skip = 1

Condition = Event[2]
# This is an example of labeling based on line number for complex stimuli
#Condition = str(k%5 + 1)"""

class MainWindow(QtWidgets.QMainWindow):
    parent = None
    def __init__(self,parentin=None):
        super().__init__()
        global parent
        if parentin is not None:
            parent = parentin

    def closeEvent(self,event):
        global parent
        try:
            if parent is not None:
                parent.show()
        except:
            pass
    pass

class frmPreprocess(Ui_frmPreprocess):
    ui      = Ui_frmPreprocess()
    dialog  = None
# This function is run when the main form start
# and initiate the default parameters.
    def show(self,parentin=None):
        from Base.utility import getVersion, getBuild, getDirSpaceINI, getDirSpace
        global dialog, ui, parent
        ui = Ui_frmPreprocess()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        if parentin is not None:
            dialog = MainWindow(parentin)
        else:
            dialog = MainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        self.set_history(self)

        tools = Tools()
        tools.combo(ui.cbTools)

        ui.cbMode.addItem("Full Analysis")
        ui.cbMode.addItem("Only Preprocessing")

        ui.txtEvents.setText(EventCode())
        ui.tabWidget.setCurrentIndex(0)
        ui.tabWidget_2.setCurrentIndex(0)
        ui.cbSliceTime.addItem("None")
        ui.cbSliceTime.addItem("Regular up (1, 2, ..., n)")
        ui.cbSliceTime.addItem("Regular down (n, n-1, ..., 1)")
        ui.cbSliceTime.addItem("Interleaved (2, 4, 6, ...), (1, 3, 5, ...)")

        ui.txtEvents = api.CodeEdit(ui.tab_3)
        ui.txtEvents.setGeometry(QtCore.QRect(10, 10, 641, 451))
        ui.txtEvents.setObjectName("txtEvents")

        ui.txtEvents.backend.start('backend/server.py')

        ui.txtEvents.modes.append(modes.CodeCompletionMode())
        ui.txtEvents.modes.append(modes.CaretLineHighlighterMode())
        ui.txtEvents.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtEvents.document()))
        #ui.txtEvents.panels.append(panels.SearchAndReplacePanel(), api.Panel.Position.TOP)
        ui.txtEvents.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtEvents.setFont(font)
        ui.txtEvents.setPlainText(EventCode(),"","")

        try:
            spaceINI = str.rsplit(open(getDirSpaceINI()).read(),"\n")
            for space in spaceINI:
                if len(space):
                    ui.txtMNI.addItem(getDirSpace() + space)

            ui.txtMNI.setCurrentIndex(1)

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
            ui.txtFeat.setText(fsl.feat)
            ui.txtFeat_gui.setText(fsl.FeatGUI)
            ui.txtbetcmd.setText(fsl.bet)
            ui.txtfslcmd.setText(fsl.fsl)



        dialog.setWindowTitle("easy fMRI preprocessing - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

# This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnDIR.clicked.connect(self.btnDIR_click)
        ui.btnTest.clicked.connect(self.btnTest_click)
        ui.btnSave.clicked.connect(self.btnSave_click)
        ui.btnLoad.clicked.connect(self.btnLoad_click)
        ui.btnLoadHistory.clicked.connect(self.btnLoadHistory_click)
        ui.btnClearAllHistory.clicked.connect(self.btnClearAllHistory_click)
        ui.btnRemoveHistory.clicked.connect(self.btnRemoveHistory_click)
        ui.lwHistory.itemDoubleClicked.connect(self.btnLoadHistory_click)
        ui.btnExtractor.clicked.connect(self.btnBrainExtractor_click)
        ui.btnEvent.clicked.connect(self.btnEventGenerator_click)
        ui.btnPreprocessScripts.clicked.connect(self.btnPreprocessingScript_click)
        ui.btnPreprocess.clicked.connect(self.btn_RunProcess_click)
        ui.btnReadTask.clicked.connect(self.btnTaskRead_click)
        ui.btnEstimate.clicked.connect(self.btn_ViewParameters_click)
        ui.btnEventTest.clicked.connect(self.btnEventExtractor_click)
        ui.btnFilesRename.clicked.connect(self.btnGroupRenameFile_click)
        ui.btnScriptEditor.clicked.connect(self.btnGroupScriptEditor_click)
        ui.btnReportViewer.clicked.connect(self.btnReportViewer_onclick)
        ui.btnVerify.clicked.connect(self.btnVerify_click)
        ui.btnDelete.clicked.connect(self.btnDelete_click)
        ui.btnTools.clicked.connect(self.btnTools_click)
        ui.cbMode.currentIndexChanged.connect(self.cbMode_change)
        ui.btnfslcmd.clicked.connect(self.btnfslcmd_click)
        ui.btnfsleyescmd.clicked.connect(self.btnfsleyescmd_click)

# Open FSL GUI
    def btnfslcmd_click(self):
        try:
            fsl = FSL()
            fsl.setting()
            if not fsl.Validate:
                msgBox = QMessageBox()
                msgBox.setText("Cannot find FSL setting!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
            else:
                CMD = fsl.FSLDIR if len(fsl.FSLDIR) else ""            
                CMD += fsl.fsl
                if len(CMD):
                    print(f"Running {CMD} ...")
                    subprocess.Popen([CMD, ""])
        except Exception as e:
            print(e)

# Open FSL Eyes GUI
    def btnfsleyescmd_click(self):
        try:
            fsl = FSL()
            fsl.setting()
            if not fsl.Validate:
                msgBox = QMessageBox()
                msgBox.setText("Cannot find FSL setting!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
            else:
                CMD = fsl.FSLDIR if len(fsl.FSLDIR) else ""            
                CMD += fsl.fsleyes
                if len(CMD):
                    print(f"Running {CMD} ...")
                    subprocess.Popen([CMD, ui.txtMNI.currentText()])
        except Exception as e:
            print(e)


# Read history from file and visualized in the History tab
    def set_history(self):
        global ui
        history = History()
        histories = history.load_history()
        ui.lwHistory.clear()
        for hist in histories:
            item = QtWidgets.QListWidgetItem(hist)
            ui.lwHistory.addItem(item)

# Exit function
    def btnClose_click(self):
        global dialog, parent
        dialog.close()

    def btnTools_click(self):
        tools = Tools()
        tools.run(ui.cbTools.currentData())


    def cbMode_change(self):
        currInx = ui.cbMode.currentIndex()
        if (currInx == 0):
            ui.txtEvents.setEnabled(True)
            ui.btnEvent.setEnabled(True)
            ui.btnEventTest.setEnabled(True)
        else:
            ui.txtEvents.setEnabled(False)
            ui.btnEvent.setEnabled(False)
            ui.btnEventTest.setEnabled(False)



# This is the main directory in the Directory tab
    def btnDIR_click(self):
        import glob
        global ui
        directory = SelectDir("Open Main Directory", ui.txtDIR.text())
        if len(directory):
            if os.path.isdir(directory) == False:
                ui.txtDIR.setText("")
            else:
                ui.txtDIR.setText(directory)

                ui.txtTask.clear()
                TaskFiles = glob.glob(directory + "/task-*.json")

                combined = None
                for file in TaskFiles:
                    task = str(file).replace(directory,"")
                    task = str(task).replace("/","")
                    task = str(task).replace("-","")
                    task = str(task).replace("_","")
                    task = str(task).replace(".","")
                    task = str(task).replace("task","",1)
                    task = str(task).replace("json","")
                    task = str(task).replace("bold","")
                    if len(task):
                        ui.txtTask.addItem(task)
                        combined = task if combined is None else combined + ", " + task                
                if combined is not None:
                    ui.txtTask.addItem(f"[{combined}]")


# This function read the basic features from datasets, i.e. TR, Voxel size, etc.
    def btnTaskRead_click(self):
        global ui
        if ui.txtTask.currentText() == "":
            msgBox = QMessageBox()
            msgBox.setText("Please enter the task name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        setting             = Setting()
        setting.Task        = ui.txtTask.currentText()
        setting.SubRange    = ui.txtSubRange.text()
        setting.SubLen      = ui.txtSubLen.text()
        setting.SubPer      = ui.txtSubPer.text()
        setting.ConRange    = ui.txtConRange.text()
        setting.ConLen      = ui.txtConLen.text()
        setting.ConPer      = ui.txtConPer.text()
        setting.RunRange    = ui.txtRunRange.text()
        setting.RunLen      = ui.txtRunLen.text()
        setting.RunPer      = ui.txtRunPer.text()

        sSess = frmSelectSession(None, setting=setting)
        if not sSess.PASS:
            return

        directory = ui.txtDIR.text()
        if len(directory):
            ui.txtDIR.setText(directory)
            FirstFile =  setParameters3(ui.txtBOLD.text(),directory, sSess.SubID, sSess.RunID, sSess.TaskID, sSess.ConID)
            #print(FirstFile)
            if not os.path.isfile(FirstFile):
                msgBox = QMessageBox()
                msgBox.setText("Cannot find the BOLD data for the first subject, please check the parameters")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            try:
                BoldHDR = nb.load(FirstFile)
                ui.txtTR.setText(str(float(BoldHDR.header.get_zooms()[3])))
                Voxels = BoldHDR.header.get_zooms()[0:3]
                ui.txtVoxel.setText("Voxel Size: " + str(Voxels))

                msgBox = QMessageBox()
                msgBox.setText(f"Basic information is read from BOLD file from:\nTask: {sSess.TaskID}\nSubject: {sSess.SubID}\nCounter {sSess.ConID}\nRun: {sSess.RunID}" + \
                                "\n\nTR: " + ui.txtTR.text() + "\nData Shape: " + str(BoldHDR.header.get_data_shape()) +\
                                " \n" + ui.txtVoxel.text() +\
                                "\n\n\nYou can manually change these parameters in the Basic tab!")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
            except:
                msgBox = QMessageBox()
                msgBox.setText("Cannot read file. Please check parameters!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                pass

    def btnTest_click(self):
        global ui
        setting = Setting()
        if setting.checkValue(ui):
            msgBox = QMessageBox()
            msgBox.setText("It is okay")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def btnSave_click(self):
        global ui
        SettingFileName = ui.txtSetting.text()
        setting = Setting()
        if not setting.checkValue(ui):
            print("TEST: It is failed")
        else:
            print("TEST: It is okay")
            OpenDialog = False

            if not len(SettingFileName):
                OpenDialog = True
            else:
                msgBox = QMessageBox()
                reply = msgBox.question(msgBox, 'Save as ...', 'Do you want to save settting in the same file?'
                                                   , QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.No:
                    OpenDialog = True


            if OpenDialog:
                filename = SaveFile("Save setting file ...",['Easy fMRI setting files (*.ez)'],'ez',\
                                    setting.mainDIR, "setting-" + setting.Task + ".ez")
                if len(filename):
                    SettingFileName = filename
                else:
                    SettingFileName = ""

            if len(SettingFileName):
                try:
                    os.remove(SettingFileName)
                except:
                    pass

                config = cp.ConfigParser()
                config.read(SettingFileName)
                config['DEFAULT']['ver']        = setting.Version
                config['DEFAULT']['mode']       = str(setting.Mode)
                config['DEFAULT']['maindir']    = setting.mainDIR
                config['DEFAULT']['mni_space']  = setting.MNISpace
                config['DEFAULT']['task']       = setting.Task
                config['DEFAULT']['sub_range']  = str(setting.SubRange)
                config['DEFAULT']['sub_len']    = str(setting.SubLen)
                config['DEFAULT']['sub_perfix'] = setting.SubPer
                config['DEFAULT']['con_range']  = str(setting.ConRange)
                config['DEFAULT']['con_len']    = str(setting.ConLen)
                config['DEFAULT']['con_perfix'] = setting.ConPer
                config['DEFAULT']['run_range']  = setting.RunRange
                config['DEFAULT']['run_len']    = str(setting.RunLen)
                config['DEFAULT']['run_perfix'] = setting.RunPer
                config['DEFAULT']['bold']       = setting.BOLD
                config['DEFAULT']['onset']      = setting.Onset
                config['DEFAULT']['anat_dir']   = setting.AnatDIR
                config['DEFAULT']['bet']        = setting.BET
                config['DEFAULT']['bet_pdf']    = setting.BETPDF
                config['DEFAULT']['analysis']   = setting.Analysis
                config['DEFAULT']['script']     = setting.Script
                config['DEFAULT']['event_dir']  = setting.EventFolder
                config['DEFAULT']['cond_per']   = setting.CondPre
                config['DEFAULT']['TR']         = str(setting.TR)
                config['DEFAULT']['FWHM']       = str(setting.FWHM)
                config['DEFAULT']['deletevol']  = str(setting.DeleteVol)
                config['DEFAULT']['totalvol']   = str(setting.TotalVol)
                config['DEFAULT']['timeslice']  = str(setting.TimeSlice)
                config['DEFAULT']['highpass']   = str(setting.HighPass)
                config['DEFAULT']['denl']       = str(setting.DENL)
                config['DEFAULT']['dets']       = str(setting.DETS)
                config['DEFAULT']['dezt']       = str(setting.DEZT)
                config['DEFAULT']['ctzt']       = str(setting.CTZT)
                config['DEFAULT']['ctpt']       = str(setting.CTPT)
                config['DEFAULT']['motion']     = str(setting.Motion)
                config['DEFAULT']['anat']       = str(setting.Anat)
                config.add_section("CODE")
                config['CODE']['event_code']   = encoding(setting.EventCodes)

                with open(SettingFileName, 'w') as configfile:
                    config.write(configfile)
                ui.txtSetting.setText(SettingFileName)
                ui.btnExtractor.setEnabled(setting.Anat)

                history = History()
                history.add_history(SettingFileName)
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)

                print("Saved setting in ",SettingFileName)

    def btnLoad_click(self):
        from Base.utility import getVersion
        #global ui
        filename = LoadFile("Open setting file ...", ['Easy fMRI setting files (*.ez)'], 'ez', currentDirectory=ui.txtDIR.text())
        if len(filename):
            setting = Setting()
            setting.Load(filename)

            if setting.Version != getVersion():
                if np.double(setting.Version) < np.double(getSettingVersion()):
                    print("WARNING: You are using different version of Easy fMRI!!!")
                    msgBox = QMessageBox()
                    msgBox.setText("This version of setting is not supported!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return

            if not setting.empty:
                ui.txtSetting.setText(filename)
                ui.txtDIR.setText(setting.mainDIR)
                ui.cbMode.setCurrentIndex(setting.Mode)
                ui.txtMNI.setCurrentText(setting.MNISpace)
                ui.txtTask.setCurrentText(setting.Task)
                ui.txtBOLD.setText(setting.BOLD)
                ui.txtOnset.setText(setting.Onset)
                ui.txtAnat.setText(setting.AnatDIR)
                ui.txtBET.setText(setting.BET)
                ui.txtBETPDF.setText(setting.BETPDF)
                ui.txtEventDIR.setText(setting.EventFolder)
                ui.txtCondPre.setText(setting.CondPre)
                ui.txtSubRange.setText(setting.SubRange)
                ui.txtSubLen.setValue(setting.SubLen)
                ui.txtSubPer.setText(setting.SubPer)
                ui.txtConRange.setText(setting.ConRange)
                ui.txtConLen.setValue(setting.ConLen)
                ui.txtConPer.setText(setting.ConPer)
                ui.txtRunRange.setText(setting.RunRange)
                ui.txtRunPer.setText(setting.RunPer)
                ui.txtRunLen.setValue(setting.RunLen)
                ui.txtAnalysis.setText(setting.Analysis)
                ui.txtScript.setText(setting.Script)
                ui.txtTR.setText(str(setting.TR))
                ui.txtFWHM.setText(str(setting.FWHM))
                ui.txtTotalVol.setValue(setting.TotalVol)
                ui.txtDeleteVol.setValue(setting.DeleteVol)
                ui.txtHighPass.setText(str(setting.HighPass))
                ui.txtDENL.setText(str(setting.DENL))
                ui.txtDETS.setText(str(setting.DETS))
                ui.txtDEZT.setText(str(setting.DEZT))
                ui.txtCTZT.setText(str(setting.CTZT))
                ui.txtCTPT.setText(str(setting.CTPT))
                try:
                    ui.txtEvents.setPlainText(setting.EventCodes,"","")
                except:
                    ui.txtEvents.setText(setting.EventCodes)
                Title = getTimeSliceText(setting.TimeSlice)
                if Title is None:
                    print("Time Slice loading error!")
                else:
                    ui.cbSliceTime.setCurrentText(Title)
                ui.cbMotionCorrection.setChecked(setting.Motion)
                ui.cbRegAnat.setChecked(setting.Anat)
                ui.txtVoxel.setText("Voxel Size: None")
                ui.btnExtractor.setEnabled(setting.Anat)

                history = History()
                history.add_history(filename)
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)

    def btnLoadHistory_click(self):
        from Base.utility import getVersion
        global ui
        try:
            filename = ui.lwHistory.selectedItems()[0].text()
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
                    ui.txtSetting.setText(filename)
                    ui.txtDIR.setText(setting.mainDIR)
                    ui.cbMode.setCurrentIndex(setting.Mode)
                    ui.txtMNI.setCurrentText(setting.MNISpace)
                    ui.txtTask.setCurrentText(setting.Task)
                    ui.txtBOLD.setText(setting.BOLD)
                    ui.txtOnset.setText(setting.Onset)
                    ui.txtAnat.setText(setting.AnatDIR)
                    ui.txtBET.setText(setting.BET)
                    ui.txtBETPDF.setText(setting.BETPDF)
                    ui.txtEventDIR.setText(setting.EventFolder)
                    ui.txtCondPre.setText(setting.CondPre)
                    ui.txtSubRange.setText(setting.SubRange)
                    ui.txtSubLen.setValue(setting.SubLen)
                    ui.txtSubPer.setText(setting.SubPer)
                    ui.txtConRange.setText(setting.ConRange)
                    ui.txtConLen.setValue(setting.ConLen)
                    ui.txtConPer.setText(setting.ConPer)
                    ui.txtRunRange.setText(setting.RunRange)
                    ui.txtRunPer.setText(setting.RunPer)
                    ui.txtRunLen.setValue(setting.RunLen)
                    ui.txtAnalysis.setText(setting.Analysis)
                    ui.txtScript.setText(setting.Script)
                    ui.txtTR.setText(str(setting.TR))
                    ui.txtFWHM.setText(str(setting.FWHM))
                    ui.txtTotalVol.setValue(setting.TotalVol)
                    ui.txtDeleteVol.setValue(setting.DeleteVol)
                    ui.txtHighPass.setText(str(setting.HighPass))
                    ui.txtDENL.setText(str(setting.DENL))
                    ui.txtDETS.setText(str(setting.DETS))
                    ui.txtDEZT.setText(str(setting.DEZT))
                    ui.txtCTZT.setText(str(setting.CTZT))
                    ui.txtCTPT.setText(str(setting.CTPT))
                    try:
                        ui.txtEvents.setPlainText(setting.EventCodes,"","")
                    except:
                        ui.txtEvents.setText(setting.EventCodes)
                    Title = getTimeSliceText(setting.TimeSlice)
                    if Title is None:
                        print("Time Slice loading error!")
                    else:
                        ui.cbSliceTime.setCurrentText(Title)
                    ui.cbMotionCorrection.setChecked(setting.Motion)
                    ui.cbRegAnat.setChecked(setting.Anat)
                    ui.btnExtractor.setEnabled(setting.Anat)
                    ui.tabWidget.setCurrentIndex(4)
        except:
            return

    def btnClearAllHistory_click(self):
        global ui
        history = History()
        history.clear_history()
        ui.lwHistory.clear()


    def btnRemoveHistory_click(self):
        global ui
        try:
            filename = ui.lwHistory.selectedItems()[0].text()
            if len(filename):
                history = History()
                history.del_history(str(filename).replace("\n",""))
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)
        except:
            return

    def btnBrainExtractor_click(self):
        global ui
        setting = Setting()
        isChange = setting.checkGUI(ui,ui.txtSetting.text())
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                brainExtractor = BrainExtractor()
                Status, Jobs = brainExtractor.run(ui.txtSetting.text(), ui.txtFSLDIR.text() + ui.txtbetcmd.text())
                if (not Status) or (Jobs is None):
                    print("TASK FAILED!")
                else:
                    print("TASK DONE.")
                    dialog.hide()
                    from GUI.frmJobs import frmJobs
                    frmJobs.show(frmJobs, Jobs, dialog)


    def btnEventGenerator_click(self):
            global ui
            setting = Setting()
            isChange = setting.checkGUI(ui, ui.txtSetting.text())
            if isChange == None:
                msgBox = QMessageBox()
                if len(ui.txtSetting.text()):
                    msgBox.setText("Please verify parameters")
                else:
                    msgBox.setText("You must save setting first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                if isChange == True:
                    msgBox = QMessageBox()
                    msgBox.setText("Parameters are changed. Please save them first!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                else:
                    eventGenerator = EventGenerator()
                    eventGenerator.run(ui.txtSetting.text())
                    #,setting.OnsetRID,setting.DurationRID,setting.ConditionRID,setting.DontReadFist)
                    print("TASK FINISHED!")
                    msgBox = QMessageBox()
                    msgBox.setText("All events are generated!")
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return

    def btnPreprocessingScript_click(self):
        global ui
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(),checkGeneratedFiles=True)
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                scriptGenerator = ScriptGenerator()
                if ui.cbMode.currentIndex() == 0 or setting.Mode == 0:
                    scriptGenerator.run(ui.txtSetting.text())
                else:
                    scriptGenerator.runbase(ui.txtSetting.text())
                print("TASK FINISHED!")
                msgBox = QMessageBox()
                msgBox.setText("All Script are generated!")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
        pass


    def btn_RunProcess_click(self):
        global ui, dialog
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(),checkGeneratedFiles=True)
        if isChange is None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                SubID=None
                ConID=None
                RunID=None
                TaskID=None
                if ui.cbJustRun.checkState():
                    sSess = frmSelectSession(None, setting=setting)
                    if sSess.PASS:
                        SubID = sSess.SubID
                        ConID = sSess.ConID
                        RunID = sSess.RunID
                        TaskID= sSess.TaskID
                    else:
                        return

                runPreprocess = RunPreprocess()
                if not runPreprocess.Check(ui.txtSetting.text(),ui.cbJustRun.checkState(),SubID,RunID,ConID,TaskID):
                    msgBox = QMessageBox()
                    msgBox.setText("Script(s) are not found!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                else:
                    feat = ui.txtFSLDIR.text() + ui.txtFeat.text()
                    Status, Jobs = runPreprocess.Run(ui.txtSetting.text(),ui.cbJustRun.checkState(),\
                                                    ui.cbRemoveOlds.checkState(),feat,SubID,RunID,ConID,TaskID)

                    if (not Status) or (Jobs is None):
                        print("TASK FAILED!")
                    else:
                        print("TASK DONE.")
                        dialog.hide()
                        from GUI.frmJobs import frmJobs
                        frmJobs.show(frmJobs, Jobs, dialog)
                    return

    def btn_ViewParameters_click(self):
        global ui, dialog
        Feat_gui = ui.txtFSLDIR.text() + ui.txtFeat_gui.text()
        if not os.path.isfile(Feat_gui):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find Feat_gui cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(), checkGeneratedFiles=True)
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                sSess = frmSelectSession(None,setting=setting)
                if sSess.PASS:
                    ScriptAdd = setParameters3(setting.Script,setting.mainDIR,sSess.SubID,sSess.RunID, sSess.TaskID, sSess.ConID)
                    subprocess.Popen([Feat_gui, ScriptAdd])
        return


    def btnEventExtractor_click(self):
        global ui
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text())
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                sSess = frmSelectSession(None, setting=setting)
                if sSess.PASS:
                    EventAddr = setParameters3(setting.Onset, setting.mainDIR, sSess.SubID, sSess.RunID, sSess.TaskID, sSess.ConID)

                    if not os.path.isfile(EventAddr):
                        print(EventAddr, " - file not find!")
                        return
                    else:
                        file = open(EventAddr, "r")
                        lines = file.readlines()
                        file.close()
                        GenEvents = list()

                        for k in range(0, len(lines)):
                            Event = lines[k].rsplit()
                            try:
                                allvars = dict(locals(), **globals())
                                exec(setting.EventCodes, allvars, allvars)

                            except Exception as e:
                                print("Event codes generated following error:")
                                print(e)
                                msgBox = QMessageBox()
                                msgBox.setText(str(e))
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return
                            try:
                                RowStartID = allvars['RowStartID']
                            except:
                                print("Cannot find RowStartID variable in event code")
                                msgBox = QMessageBox()
                                msgBox.setText("Cannot find RowStartID variable in event code")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return
                            try:
                                Condition = allvars['Condition']
                            except:
                                print("Cannot find Condition variable in event code")
                                msgBox = QMessageBox()
                                msgBox.setText("Cannot find Condition variable in event code")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return
                            try:
                                Onset = allvars['Onset']
                            except:
                                print("Cannot find Onset variable in event code")
                                msgBox = QMessageBox()
                                msgBox.setText("Cannot find Onset variable in event code")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return
                            try:
                                Duration = allvars['Duration']
                            except:
                                print("Cannot find Duration variable in event code")
                                msgBox = QMessageBox()
                                msgBox.setText("Cannot find Duration variable in event code")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return

                            try:
                                Skip = int(allvars["Skip"])
                            except:
                                print("Cannot find Skip variable in event code")
                                msgBox = QMessageBox()
                                msgBox.setText("Cannot find Skip variable in event code")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return

                            if RowStartID <= k and Skip == 0:
                                GenEvents.append([Onset,Duration,Condition])

                    EventViewer = frmEventViewer(Events=GenEvents,StartRow=RowStartID,SubID=sSess.SubID,\
                                                RowID=sSess.RunID, Task=sSess.TaskID)
        pass

    def btnGroupRenameFile_click(self):
        global ui
        frmRenameFile.show(frmRenameFile,SubRange=ui.txtSubRange.text(),SubLen=ui.txtSubLen.value(),\
                            SubPer=ui.txtSubPer.text(),ConRange=ui.txtConRange.text(),ConLen=ui.txtConLen.value(),\
                            ConPer=ui.txtConPer.text(),RunRange=ui.txtRunRange.text(),RunLen=ui.txtRunLen.value(),\
                            RunPer=ui.txtRunPer.text(),Task=ui.txtTask.currentText(),DIR=ui.txtDIR.text())

    def btnGroupScriptEditor_click(self):
        global ui
        frmScriptEditor.show(frmScriptEditor,SubRange=ui.txtSubRange.text(),SubLen=ui.txtSubLen.value(),\
                            SubPer=ui.txtSubPer.text(),ConRange=ui.txtConRange.text(),ConLen=ui.txtConLen.value(),\
                            ConPer=ui.txtConPer.text(),RunRange=ui.txtRunRange.text(),RunLen=ui.txtRunLen.value(),\
                            RunPer=ui.txtRunPer.text(),Task=ui.txtTask.currentText(),DIR=ui.txtDIR.text())


    def btnReportViewer_onclick(self):
        import webbrowser
        global ui, dialog
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(),checkGeneratedFiles=True)
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                runPreprocess = RunPreprocess()
                if not runPreprocess.Check(ui.txtSetting.text(),False):
                    msgBox = QMessageBox()
                    msgBox.setText("Script(s) are not found!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                else:
                    sSess = frmSelectSession(None, setting=setting)
                    if sSess.PASS:
                        AnalysisFile = setParameters3(setting.Analysis, setting.mainDIR, sSess.SubID, sSess.RunID, sSess.TaskID, sSess.ConID)
                        AnalysisAdd =  AnalysisFile + ".feat/report.html"
                        if not os.path.isfile(AnalysisAdd):
                            print(AnalysisAdd + " - not found!")
                        else:
                            webbrowser.open_new("file://" + AnalysisAdd)
                    return

    def btnVerify_click(self):
        global ui
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text())
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                ofile = SaveFile("Save log file",["Log file (*.txt)"],"txt")
                if len(ofile):

                    # Subjects = strRange(setting.SubRange, Unique=True)
                    # if Subjects is None:
                    #     print("Cannot load Subject Range!")
                    #     return False
                    # SubSize = len(Subjects)

                    # Counters = strMultiRange(setting.ConRange, SubSize)
                    # if Counters is None:
                    #     print("Cannot load Counter Range!")
                    #     return False

                    # Runs = strMultiRange(setting.RunRange, SubSize)
                    # if Runs is None:
                    #     print("Cannot load Run Range!")
                    #     return False

                    bids = load_BIDS(setting)
                    Log = 20*"#" + " easy fMRI - Files Verification " + 20*"#" + "\n"

                    for (_, t, _, s, _, c, runs) in bids:

                    # for si, s in enumerate(Subjects):
                    #     for cnt in Counters[si]:

                        # Anatomical Files
                        Log = Log + "\t" + 10*"#" + "\tSubject: " + s + " Counter: " + c + "\t" + 10*"#" + "\n"
                        # MRI Files
                        if ui.cbVMRI.isChecked():
                            file = setParameters3(setting.AnatDIR, setting.mainDIR, s, "", t, c)

                            if os.path.isfile(file):
                                Log = Log + "OKAY: MRI FILE,\t" + file + "\n"
                            else:
                                Log = Log + "NOT FOUND: MRI FILE,\t" + file + "\n"

                        if ui.cbVBet.isChecked():
                            file = setParameters3(setting.BET, setting.mainDIR, s, "", t, c)

                            if os.path.isfile(file):
                                Log = Log + "OKAY: BET FILE,\t" + file + "\n"
                            else:
                                Log = Log + "NOT FOUND: BET FILE,\t" + file + "\n"

                            file = setParameters3(setting.BETPDF, setting.mainDIR, s, "", t, c)

                            if os.path.isfile(file):
                                Log = Log + "OKAY: PDF FILE,\t" + file + "\n"
                            else:
                                Log = Log + "NOT FOUND: PDF FILE,\t" + file + "\n"
                        # Check run based files
                        for r in runs:
                            Log = Log + "\t\t" + 5 * "#" + "\tSubject: " + s + " Counter: " + c + \
                                    " Run: " + r + "\t" + 5 * "#" + "\n"

                            # Image
                            if ui.cbVImage.isChecked():
                                file = setParameters3(setting.BOLD, setting.mainDIR, s, r, t, c)
                                
                                if os.path.isfile(file):
                                    Log = Log + "OKAY: IMAGE FILE,\t" + file + "\n"
                                else:
                                    Log = Log + "NOT FOUND: IMAGE FILE,\t" + file + "\n"


                            # Event
                            if ui.cbVImage.isChecked():
                                file = setParameters3(setting.Onset,setting.mainDIR, s, r, t, c)
                                if os.path.isfile(file):
                                    Log = Log + "OKAY: EVENT FILE,\t" + file + "\n"
                                else:
                                    Log = Log + "NOT FOUND: EVENT FILE,\t" + file + "\n"

                            # ExEvent
                            if ui.cbVExEvent.isChecked():
                                dir = setParameters3(setting.EventFolder,setting.mainDIR, s, r, t, c)

                                if os.path.isdir(dir):
                                    Log = Log + "OKAY: EVENT DIR,\t" + dir + "\n"
                                    file = dir + setting.CondPre + ".mat"
                                    if os.path.isfile(file):
                                        Log = Log + "OKAY: MAT FILE,\t" + file + "\n"
                                        try:
                                            cond = io.loadmat(file)["Cond"]
                                            Log = Log + "\t\t" + 2 * "#" + "\tSubject: " + s + " Counter: " + c + " Run: " + r + \
                                                    " Number of conditions: " + str(len(cond)) + "\t" + 5 * "#" + "\n"
                                        except:
                                            Log = Log + "NOT LOAD: MAT FILE,\t" + file + "\n"
                                        for cnd in cond:
                                            file = dir + cnd[0][0] + ".tab"
                                            if os.path.isfile(file):
                                                Log = Log + "OKAY: TAB FILE,\t" + file + "\n"
                                            else:
                                                Log = Log + "NOT FOUND: TAB FILE,\t" + file + "\n"
                                    else:
                                        Log = Log + "NOT FOUND: MAT FILE,\t" + file + "\n"

                                else:
                                    Log = Log + "NOT FOUND: EVENT DIR,\t" + dir + "\n"

                            # Script
                            if ui.cbVScript.isChecked():
                                file = setParameters3(setting.Script, setting.mainDIR, s, r, t, c)
                                if os.path.isfile(file):
                                    Log = Log + "OKAY: SCRIPT,\t" + file + "\n"
                                else:
                                    Log = Log + "NOT FOUND: SCRIPT,\t" + file + "\n"

                            # Output
                            if ui.cbVOutput.isChecked():
                                dir = setParameters3(setting.Analysis, setting.mainDIR, s, r, t, c) + ".feat"
                                if os.path.isdir(dir):
                                    Log = Log + "OKAY: ANALYZE,\t" + dir + "\n"
                                    files = str(ui.txtVOutput.toPlainText()).split()
                                    for file in files:
                                        if len(file):
                                            if os.path.isfile(dir + "/" + file):
                                                Log = Log + "OKAY: OUTPUT,\t" + dir +  "/" + file + "\n"
                                            else:
                                                Log = Log + "NOT FOUND: OUTPUT,\t" + dir + "/" + file + "\n"
                                else:
                                    Log = Log + "NOT FOUND: ANALYZE,\t" + dir + "\n"
                            Log = Log + "\n"
                        Log = Log + "\n\n\n\n"
                    fileHandle = open(ofile, "w")
                    fileHandle.write(Log)
                    fileHandle.close()
                    print("Log file is saved: ", ofile)
                    OpenReport(ofile)


    def btnDelete_click(self):
        global ui
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text())
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                strDel = ""
                if ui.cbDelSmoke.isChecked():
                    strDel = "SMOKED::"
                msgBox = QMessageBox()
                reply = msgBox.question(msgBox, strDel + 'DELETING OUTPUT FILES ...', strDel + 'Do you want to DELETE output files?'
                                        , QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    bids = load_BIDS(setting)
                    print("Deleting Files ...")
                    for (_, t, _, s, _, c, runs) in bids:
                        # Anatomical Files
                        if ui.cbVBet.isChecked():
                            file = setParameters3(setting.BET, setting.mainDIR, s, "", t, c)
                            if os.path.isfile(file):
                                try:
                                    if not ui.cbDelSmoke.isChecked():
                                        os.remove(file)
                                    print(strDel + "DELETE: BET FILE,\t" + file)
                                except:
                                    print("CANNOT DELETE: BET FILE,\t" + file)
                            else:
                                print("NOT FOUND: BET FILE,\t" + file)
                            file = setParameters3(setting.BETPDF, setting.mainDIR, s, "", t, c)
                            if os.path.isfile(file):
                                try:
                                    if not ui.cbDelSmoke.isChecked():
                                        os.remove(file)
                                    print(strDel + "DELETE: PDF FILE,\t" + file)
                                except:
                                    print("NOT DELETE: PDF FILE,\t" + file)
                            else:
                                print("NOT FOUND: PDF FILE,\t" + file)
                        # Check run based files
                        for r in runs:
                            # ExEvent
                            if ui.cbVExEvent.isChecked():
                                dir = setParameters3(setting.EventFolder,setting.mainDIR, s, r, t, c)
                                if os.path.isdir(dir):
                                    try:
                                        if not ui.cbDelSmoke.isChecked():
                                            shutil.rmtree(dir)
                                        print(strDel + "DELETE: EVENT DIR,\t" + dir)
                                    except:
                                        print("CANNOT DELETE: EVENT DIR,\t" + dir)
                                else:
                                    print("NOT FOUND: EVENT DIR,\t" + dir)
                            # Script
                            if ui.cbVScript.isChecked():
                                file = setParameters3(setting.Script,setting.mainDIR, s, r, t, c)
                                if os.path.isfile(file):
                                    try:
                                        if not ui.cbDelSmoke.isChecked():
                                            os.remove(file)
                                        print(strDel + "DELETE: SCRIPT,\t" + file)
                                    except:
                                        print("CANNOT DELETE: SCRIPT,\t" + file)
                                else:
                                    print("NOT FOUND: SCRIPT,\t" + file)
                            # Output
                            if ui.cbVOutput.isChecked():
                                dir = setParameters3(setting.Analysis,setting.mainDIR, s, r, t, c) + ".feat"
                                if os.path.isdir(dir):
                                    try:
                                        if not ui.cbDelSmoke.isChecked():
                                            shutil.rmtree(dir)
                                        print(strDel + "DELETE: ANALYZE DIR,\t" + dir)
                                    except:
                                        print("CANNOT DELETE: ANALYZE DIR,\t" + dir)
                                else:
                                    print("NOT FOUND: ANALYZE DIR,\t" + dir)
                    print("Task is done.")
                    msgBox.setText("All available output files are deleted!")
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()


# Auto Run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmPreprocess.show(frmPreprocess)
    sys.exit(app.exec_())
