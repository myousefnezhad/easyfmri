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
import sys
import seaborn as sns
import numpy as np
from IO.mainIO import mainIO_load
from PyQt6.QtWidgets import *
from Base.utility import getVersion, getBuild, fixstr
from Base.dialogs import LoadFile
from GUI.frmFELabelAlignGUI import *


class frmFELabelAlign(Ui_frmFELabelAlign):
    ui = Ui_frmFELabelAlign()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFELabelAlign()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.txtColor.clear()
        ui.txtColor.addItem("Basic", None)
        ui.txtColor.addItem("HLS", "hls")
        ui.txtColor.addItem("HUSL", "husl")
        ui.tabWidget.setCurrentIndex(0)
        ui.tabWidget2.setCurrentIndex(0)
        dialog.setWindowTitle("easy fMRI Label Alignment Report - V" + getVersion() + "B" + getBuild())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnReport.clicked.connect(self.btnReport_click)

    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFile_click(self):
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading ...")
                    data = mainIO_load(filename)
                    Keys = data.keys()
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
                        print("Number of labels: ", np.shape(Labels)[0])
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

                    ui.tbReport.clear()
                    ui.tbReport.setRowCount(0)
                    ui.tbReport.setColumnCount(0)
                    ui.tbReport2.clear()
                    ui.tbReport2.setRowCount(0)
                    ui.tbReport2.setColumnCount(0)
                    ui.tabWidget2.setCurrentIndex(0)
                    ui.tabWidget.setCurrentIndex(2)


                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")


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

        # Label
        if not len(ui.txtLabel.currentText()):
            msgBox.setText("Please enter Label variable name!")
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
        InData = mainIO_load(InFile)

        try:
            Label = InData[ui.txtLabel.currentText()][0]
        except:
            print("Cannot load Labels!")
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
            Task = np.asarray(InData[ui.txtTask.currentText()])
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
        print("Number of data in this level is " + str(len(UniqFold)))
        ReformLabel = list()
        ReformLabelCounter = dict()
        MaxSize = None
        # Reconstruct Labels
        for foldID, fold in enumerate(GUFold):
            foldLevelLabel = Label[np.where(UnitFold == fold)]
            MaxSize = np.shape(foldLevelLabel)[0] if MaxSize is None else np.max((np.shape(foldLevelLabel)[0], MaxSize))
            foldLevelUnique, foldLevelCounter = np.unique(foldLevelLabel, return_counts=True)
            ReformLabelCounter[foldID] = dict(zip(foldLevelUnique, foldLevelCounter))
            ReformLabel.append(foldLevelLabel)

        ui.tbReport.clear()
        ui.tbReport2.clear()
        ui.tbReport.setRowCount(MaxSize)
        ui.tbReport2.setRowCount(np.shape(np.unique(Label))[0])
        ui.tbReport.setColumnCount(np.shape(GUFold)[0])
        ui.tbReport2.setColumnCount(np.shape(GUFold)[0])

        HorHdrLabel = list()
        for col_width in range(np.shape(GUFold)[0]):
            ui.tbReport.setColumnWidth(col_width, 50)
            ui.tbReport2.setColumnWidth(col_width, 50)
            HorHdrLabel.append('F' + str(col_width + 1))
        ui.tbReport.setHorizontalHeaderLabels(HorHdrLabel)
        ui.tbReport2.setHorizontalHeaderLabels(HorHdrLabel)


        # Create Color Dictionary
        colormap = sns.color_palette(ui.txtColor.currentData(), np.shape(np.unique(Label))[0])
        colordict = dict()
        for color, lbl in zip(colormap, np.unique(Label)):
            colordict[str(lbl)] = QtGui.QColor(int(255 * color[0]), int(255 * color[1]), int(255 * color[2]))

        # Draw Timepoint Lables
        TimePointLabels = list()
        for timepoint in range(MaxSize):
            TimePointLabels.append('T' + str(timepoint + 1))
        ui.tbReport.setVerticalHeaderLabels(TimePointLabels)
        # Draw Timepoint
        for col_index, col in enumerate(ReformLabel):
            for row_index, row in enumerate(col):
                item = QTableWidgetItem(str(row))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setBackground(colordict[str(row)])
                ui.tbReport.setItem(row_index, col_index, item)
        ui.tbReport.move(0, 0)
        ui.tabWidget.setCurrentIndex(2)

        # Draw Class Labels
        ClassLabels = list()
        for clsID, cls in enumerate(np.unique(Label)):
            ClassLabels.append('C' + str(cls))
            CounterList = list()
            for foldID, fold in enumerate(GUFold):
                value = ReformLabelCounter[foldID][cls]
                CounterList.append(value)
                item = QTableWidgetItem(str(value))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                ui.tbReport2.setItem(clsID, foldID, item)

            UniqueValues = np.unique(CounterList)
            colormap = sns.color_palette(ui.txtColor.currentData(), np.shape(np.unique(UniqueValues))[0])
            colordict = dict()
            for color, value in zip(colormap, np.unique(UniqueValues)):
                colordict[str(value)] = QtGui.QColor(int(255 * color[0]), int(255 * color[1]), int(255 * color[2]))
            for foldID, fold in enumerate(GUFold):
                ui.tbReport2.item(clsID, foldID).setBackground(colordict[ui.tbReport2.item(clsID, foldID).text()])





        ui.tbReport2.setVerticalHeaderLabels(ClassLabels)
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFELabelAlign.show(frmFELabelAlign)
    sys.exit(app.exec_())