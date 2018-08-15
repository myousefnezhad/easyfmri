#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *


from Base.utility import getVersion, getBuild, fixstr
from Base.dialogs import LoadFile, SaveFile

from GUI.frmFETempAlignGUI import *


import logging
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

Condition = Event[2]"""

class frmFETempAlign(Ui_frmFETempAlign):
    ui = Ui_frmFETempAlign()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFETempAlign()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)
        # ui.txtCon = api.CodeEdit(ui.tab_4)
        # ui.txtCon.setGeometry(QtCore.QRect(11, 16, 671, 411))
        # ui.txtCon.setObjectName("txtCon")
        # ui.txtCon.backend.start('backend/server.py')
        #
        # ui.txtCon.modes.append(modes.CodeCompletionMode())
        # ui.txtCon.modes.append(modes.CaretLineHighlighterMode())
        # ui.txtCon.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtCon.document()))
        # ui.txtCon.panels.append(panels.SearchAndReplacePanel(), api.Panel.Position.TOP)
        # ui.txtCon.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
        #
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # ui.txtCon.setFont(font)
        # ui.txtCon.setPlainText(EventCode(),"","")

        dialog.setWindowTitle("easy fMRI Temporal Alignment Report - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnReport.clicked.connect(self.btnReport_click)
        # ui.btnOutFile.clicked.connect(self.btnOutFile_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading ...")
                    ui.txtReport.clear()
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    # Data
                    ui.txtData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtData.setCurrentText("data")
                        print("Data Shape: ", np.shape(data["data"]))
                        ui.txtReport.append("Data Shape: " + str(np.shape(data["data"])))


                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtLabel.setCurrentText("label")
                        Labels = data[ui.txtLabel.currentText()]
                        Labels = np.unique(Labels)
                        ui.txtReport.append("Number of labels: " + str(np.shape(Labels)[0]))
                        print("Number of labels: ", np.shape(Labels)[0])
                        ui.txtReport.append("Labels: " + str(Labels))
                        print("Labels: ", Labels)


                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")
                        print("Number of subjects: ", np.shape(np.unique(data["subject"]))[0])
                        ui.txtReport.append("Number of subjects: " + str(np.shape(np.unique(data["subject"]))[0]))


                    # Task
                    ui.txtTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")

                    # Run
                    ui.txtRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("run")


                    # Counter
                    ui.txtCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("counter")


                    ui.txtInFile.setText(filename)

                    ui.tabWidget.setCurrentIndex(2)

                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    # def btnOutFile_click(self):
    #     ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
    #                          os.path.dirname(ui.txtOutFile.text()))
    #     if len(ofile):
    #         ui.txtOutFile.setText(ofile)

    def btnReport_click(self):
        msgBox = QMessageBox()

        # InFile
        InFile = ui.txtInFile.text()
        if not len(InFile):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not os.path.isfile(InFile):
            msgBox.setText("Input file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Run
        if not len(ui.txtRun.currentText()):
            msgBox.setText("Please enter Run variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Task
        if not len(ui.txtTask.currentText()):
            msgBox.setText("Please enter Task variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Counter
        if not len(ui.txtCounter.currentText()):
            msgBox.setText("Please enter Counter variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        print("Loading data ...")
        InData = io.loadmat(InFile)

        try:
            X = InData[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return

        try:
            Subject = InData[ui.txtSubject.currentText()]
        except:
            print("Cannot load Subject ID")
            return

        try:
            Run = InData[ui.txtRun.currentText()]
        except:
            print("Cannot load Run ID")
            return

        try:
            Counter = InData[ui.txtCounter.currentText()]
        except:
            print("Cannot load Counter ID")
            return

        try:
            Task = InData[ui.txtTask.currentText()]

            TaskIndex = Task.copy()
            for tasindx, tas in enumerate(np.unique(Task)):
                TaskIndex[Task == tas] = tasindx + 1

        except:
            print("Cannot load Subject ID")
            return

        Unit = 1

        print("Calculating Alignment Level ...")
        GroupFold = None
        FoldStr = ""
        if ui.cbFSubject.isChecked():
            if not ui.rbFRun.isChecked():
                GroupFold = Subject
                FoldStr = "Subject"
            else:
                GroupFold = np.concatenate((Subject,Run))
                FoldStr = "Subject+Run"

        if ui.cbFTask.isChecked():
            GroupFold = np.concatenate((GroupFold,TaskIndex)) if GroupFold is not None else TaskIndex
            FoldStr = FoldStr + "+Task"

        if ui.cbFCounter.isChecked():
            GroupFold = np.concatenate((GroupFold,Counter)) if GroupFold is not None else Counter
            FoldStr = FoldStr + "+Counter"

        GroupFold = np.transpose(GroupFold)

        UniqFold = np.array(list(set(tuple(i) for i in GroupFold.tolist())))

        FoldIDs = np.arange(len(UniqFold)) + 1

        if len(UniqFold) <= Unit:
            msgBox.setText("Unit for the test set must be smaller than all possible folds! Number of all folds is: " + str(len(UniqFold)))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if np.mod(len(UniqFold),Unit):
            msgBox.setText("Unit for the test set must be divorceable to all possible folds! Number of all folds is: " + str(len(UniqFold)))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        ListFold = list()
        for gfold in GroupFold:
            for ufoldindx, ufold in enumerate(UniqFold):
                if (ufold == gfold).all():
                    currentID = FoldIDs[ufoldindx]
                    break
            ListFold.append(currentID)

        ListFold = np.int32(ListFold)
        if Unit == 1:
            UnitFold = np.int32(ListFold)
        else:
            UnitFold = np.int32((ListFold - 0.1) / Unit) + 1

        FoldInfo = dict()
        FoldInfo["Unit"]    = Unit
        FoldInfo["Group"]   = GroupFold
        FoldInfo["Order"]   = FoldStr
        FoldInfo["List"]    = ListFold
        FoldInfo["Unique"]  = UniqFold
        FoldInfo["Folds"]   = UnitFold

        GUFold = np.unique(UnitFold)

        ui.txtReport.clear()

        print("Number of data in this level is " + str(len(UniqFold)))

        ui.txtReport.append("Number of data in this level is " + str(len(UniqFold)))

        FoldSizeStr = str(len(UniqFold))
        FirstShape = None


        for foldID, fold in enumerate(GUFold):
            Shape = np.shape(X[np.where(UnitFold == fold)])
            str2 = ""
            if FirstShape is None:
                FirstShape = Shape
            elif Shape != FirstShape:
                str2 = " - Problem"
            print("Shape of " +  fixstr(foldID + 1,len(FoldSizeStr)) + "-th data of " + FoldSizeStr + " is " + str(Shape) + str2)
            ui.txtReport.append("Shape of " + fixstr(foldID + 1,len(FoldSizeStr)) + "-th data of " + FoldSizeStr + " is " + str(Shape) + str2)

        ui.tabWidget.setCurrentIndex(2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFETempAlign.show(frmFETempAlign)
    sys.exit(app.exec_())