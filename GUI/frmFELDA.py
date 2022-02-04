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
import numpy as np
from PyQt5.QtWidgets import *
from GUI.frmFELDAGUI import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


class frmFELDA(Ui_frmFELDA):
    ui = Ui_frmFELDA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFELDA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        ui.cbSolver.addItem("Singular Value Decomposition", "svd")
        ui.cbSolver.addItem("Least Squares", "lsqr")
        ui.cbSolver.addItem("Eigenvalue Decomposition", "eigen")

        dialog.setWindowTitle("easy fMRI Linear Discriminant Analysis (LDA) - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnOutFile.clicked.connect(self.btnOutFile_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFile_click(self):
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtInFile.text()))

        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = mainIO_load(filename)
                    Keys = data.keys()

                    # Train Data
                    ui.txtITrData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrData.addItem(key)
                        if key == "train_data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrData.setCurrentText("train_data")

                    # Test Data
                    ui.txtITeData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeData.addItem(key)
                        if key == "test_data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeData.setCurrentText("test_data")

                    # Train Label
                    ui.txtITrLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrLabel.addItem(key)
                        if key == "train_label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrLabel.setCurrentText("train_label")

                    # Test Label
                    ui.txtITeLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeLabel.addItem(key)
                        if key == "test_label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeLabel.setCurrentText("test_label")

                    # Train mLabel
                    ui.txtITrmLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrmLabel.addItem(key)
                        if key == "train_mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrmLabel.setCurrentText("train_mlabel")
                    ui.cbmLabel.setChecked(HasDefualt)

                    # Test mLabel
                    ui.txtITemLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITemLabel.addItem(key)
                        if key == "test_mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITemLabel.setCurrentText("test_mlabel")
                    if ui.cbmLabel.isChecked():
                        ui.cbmLabel.setChecked(HasDefualt)

                    # Coordinate
                    ui.txtCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCol.setCurrentText("coordinate")
                    ui.cbCol.setChecked(HasDefualt)

                    # Train Design
                    ui.txtITrDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrDM.addItem(key)
                        if key == "train_design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrDM.setCurrentText("train_design")
                    ui.cbDM.setChecked(HasDefualt)

                    # Test Design
                    ui.txtITeDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeDM.addItem(key)
                        if key == "test_design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeDM.setCurrentText("test_design")
                    if ui.cbDM.isChecked():
                        ui.cbDM.setChecked(HasDefualt)

                    # Train Subject
                    ui.txtITrSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrSubject.addItem(key)
                        if key == "train_subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrSubject.setCurrentText("train_subject")
                    ui.cbSubject.setChecked(HasDefualt)

                    # Test Subject
                    ui.txtITeSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeSubject.addItem(key)
                        if key == "test_subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeSubject.setCurrentText("test_subject")
                    if ui.cbSubject.isChecked():
                        ui.cbSubject.setChecked(HasDefualt)

                    # Train Task
                    ui.txtITrTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrTask.addItem(key)
                        if key == "train_task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrTask.setCurrentText("train_task")
                    ui.cbTask.setChecked(HasDefualt)

                    # Test Task
                    ui.txtITeTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeTask.addItem(key)
                        if key == "test_task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeTask.setCurrentText("test_task")
                    if ui.cbTask.isChecked():
                        ui.cbTask.setChecked(HasDefualt)


                    # Train Run
                    ui.txtITrRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrRun.addItem(key)
                        if key == "train_run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrRun.setCurrentText("train_run")
                    ui.cbRun.setChecked(HasDefualt)

                    # Test Run
                    ui.txtITeRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeRun.addItem(key)
                        if key == "test_run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeRun.setCurrentText("test_run")
                    if ui.cbRun.isChecked():
                        ui.cbRun.setChecked(HasDefualt)

                    # Train Counter
                    ui.txtITrCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrCounter.addItem(key)
                        if key == "train_counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrCounter.setCurrentText("train_counter")
                    ui.cbCounter.setChecked(HasDefualt)

                    # Test Counter
                    ui.txtITeCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeCounter.addItem(key)
                        if key == "test_counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeCounter.setCurrentText("test_counter")
                    if ui.cbCounter.isChecked():
                        ui.cbCounter.setChecked(HasDefualt)

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")
                    ui.cbCond.setChecked(HasDefualt)

                    # Train NScan
                    ui.txtITrScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITrScan.addItem(key)
                        if key == "train_nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITrScan.setCurrentText("train_nscan")
                    ui.cbNScan.setChecked(HasDefualt)

                    # Test NScan
                    ui.txtITeScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeScan.addItem(key)
                        if key == "test_nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeScan.setCurrentText("test_nscan")
                    if ui.cbNScan.isChecked():
                        ui.cbNScan.setChecked(HasDefualt)

                    # FoldID
                    ui.txtFoldID.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFoldID.addItem(key)
                        if key == "FoldID":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFoldID.setCurrentText("FoldID")
                    ui.cbFoldID.setChecked(HasDefualt)

                    # FoldInfo
                    ui.txtFoldInfo.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFoldInfo.addItem(key)
                        if key == "FoldInfo":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFoldInfo.setCurrentText("FoldInfo")
                    ui.cbFoldInfo.setChecked(HasDefualt)


                    # set number of features
                    XShape = np.shape(data[ui.txtITrData.currentText()])
                    ui.txtNumFea.setMaximum(1)
                    ui.txtNumFea.setMaximum(XShape[1])
                    ui.txtNumFea.setValue(XShape[1])
                    ui.lblFeaNum.setText("1 ... " + str(XShape[1]))
                    if ui.cbFoldID.isChecked():
                        ui.lbFoldID.setText("ID=" + str(data[ui.txtFoldID.currentText()][0][0]))


                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        try:
            FoldFrom = np.int32(ui.txtFoldFrom.text())
            FoldTo   = np.int32(ui.txtFoldTo.text())
        except:
            print("Please check fold parameters!")
            return

        if FoldTo < FoldFrom:
            print("Please check fold parameters!")
            return

        for fold in range(FoldFrom, FoldTo+1):
            # Tol
            try:
                Tol = np.float(ui.txtTole.text())
            except:
                msgBox.setText("Tolerance is wrong!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Solver
            Solver = ui.cbSolver.currentData()
            # OutFile
            OutFile = ui.txtOutFile.text()
            OutFile = OutFile.replace("$FOLD$", str(fold))
            if not len(OutFile):
                msgBox.setText("Please enter out file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # InFile
            InFile = ui.txtInFile.text()
            InFile = InFile.replace("$FOLD$", str(fold))
            if not len(InFile):
                msgBox.setText("Please enter input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not os.path.isfile(InFile):
                msgBox.setText("Input file not found!\n"+InFile)
                print(InFile + " - not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            InData = mainIO_load(InFile)
            OutData = dict()
            OutData["imgShape"] = reshape_1Dvector(InData["imgShape"])
            # Data
            if not len(ui.txtITrData.currentText()):
                msgBox.setText("Please enter Input Train Data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtITeData.currentText()):
                msgBox.setText("Please enter Input Test Data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOTrData.text()):
                msgBox.setText("Please enter Output Train Data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOTeData.text()):
                msgBox.setText("Please enter Output Test Data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                XTr = InData[ui.txtITrData.currentText()]
                XTe = InData[ui.txtITeData.currentText()]
                if ui.cbScale.isChecked():
                    XTr = preprocessing.scale(XTr)
                    XTe = preprocessing.scale(XTe)
                    print("Whole of data is scaled X~N(0,1).")
            except:
                print("Cannot load data")
                return
            # NComponent
            try:
                NumFea = np.int32(ui.txtNumFea.text())
            except:
                msgBox.setText("Number of features is wrong!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if NumFea < 1:
                msgBox.setText("Number of features must be greater than zero!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if NumFea > np.shape(XTr)[1]:
                msgBox.setText("Number of features is wrong!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Label
            if not len(ui.txtITrLabel.currentText()):
                    msgBox.setText("Please enter Train Input Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            if not len(ui.txtITeLabel.currentText()):
                    msgBox.setText("Please enter Test Input Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            if not len(ui.txtOTrLabel.text()):
                    msgBox.setText("Please enter Train Output Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            if not len(ui.txtOTeLabel.text()):
                    msgBox.setText("Please enter Test Output Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            try:
                YTr = InData[ui.txtITrLabel.currentText()][0]
                YTe = InData[ui.txtITeLabel.currentText()][0]
                OutData[ui.txtOTrLabel.text()] = reshape_1Dvector(YTr)
                OutData[ui.txtOTeLabel.text()] = reshape_1Dvector(YTe)
            except:
                print("Cannot load labels!")
            # Subject
            if ui.cbSubject.isChecked():
                if not len(ui.txtITrSubject.currentText()):
                    msgBox.setText("Please enter Train Input Subject variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeSubject.currentText()):
                    msgBox.setText("Please enter Test Input Subject variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrSubject.text()):
                    msgBox.setText("Please enter Train Output Subject variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeSubject.text()):
                    msgBox.setText("Please enter Test Output Subject variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrSubject.text()] = reshape_1Dvector(InData[ui.txtITrSubject.currentText()])
                    OutData[ui.txtOTeSubject.text()] = reshape_1Dvector(InData[ui.txtITeSubject.currentText()])
                except:
                    print("Cannot load Subject IDs")
                    return
            # Task
            if ui.cbTask.isChecked():
                if not len(ui.txtITrTask.currentText()):
                    msgBox.setText("Please enter Input Train Task variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeTask.currentText()):
                    msgBox.setText("Please enter Input Test Task variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrTask.text()):
                    msgBox.setText("Please enter Output Train Task variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeTask.text()):
                    msgBox.setText("Please enter Output Test Task variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrTask.text()] = reshape_1Dvector(InData[ui.txtITrTask.currentText()])
                    OutData[ui.txtOTeTask.text()] = reshape_1Dvector(InData[ui.txtITeTask.currentText()])
                except:
                    print("Cannot load Tasks!")
                    return
            # Run
            if ui.cbRun.isChecked():
                if not len(ui.txtITrRun.currentText()):
                    msgBox.setText("Please enter Train Input Run variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeRun.currentText()):
                    msgBox.setText("Please enter Test Input Run variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrRun.text()):
                    msgBox.setText("Please enter Train Output Run variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeRun.text()):
                    msgBox.setText("Please enter Test Output Run variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrRun.text()] = reshape_1Dvector(InData[ui.txtITrRun.currentText()])
                    OutData[ui.txtOTeRun.text()] = reshape_1Dvector(InData[ui.txtITeRun.currentText()])
                except:
                    print("Cannot load Runs!")
                    return
            # Counter
            if ui.cbCounter.isChecked():
                if not len(ui.txtITrCounter.currentText()):
                    msgBox.setText("Please enter Train Input Counter variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeCounter.currentText()):
                    msgBox.setText("Please enter Test Input Counter variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrCounter.text()):
                    msgBox.setText("Please enter Train Output Counter variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeCounter.text()):
                    msgBox.setText("Please enter Test Output Counter variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrCounter.text()] = reshape_1Dvector(InData[ui.txtITrCounter.currentText()])
                    OutData[ui.txtOTeCounter.text()] = reshape_1Dvector(InData[ui.txtITeCounter.currentText()])
                except:
                    print("Cannot load Counters!")
                    return
            # Matrix Label
            if ui.cbmLabel.isChecked():
                if not len(ui.txtITrmLabel.currentText()):
                    msgBox.setText("Please enter Train Input Matrix Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITemLabel.currentText()):
                    msgBox.setText("Please enter Test Input Matrix Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrmLabel.text()):
                    msgBox.setText("Please enter Train Output Matrix Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTemLabel.text()):
                    msgBox.setText("Please enter Test Output Matrix Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrmLabel.text()] = InData[ui.txtITrmLabel.currentText()]
                    OutData[ui.txtOTemLabel.text()] = InData[ui.txtITemLabel.currentText()]
                except:
                    print("Cannot load matrix lables!")
                    return
            # Design
            if ui.cbDM.isChecked():
                if not len(ui.txtITrDM.currentText()):
                    msgBox.setText("Please enter Train Input Design Matrix variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeDM.currentText()):
                    msgBox.setText("Please enter Test Input Design Matrix variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrDM.text()):
                    msgBox.setText("Please enter Train Output Design Matrix variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeDM.text()):
                    msgBox.setText("Please enter Test Output Design Matrix variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrDM.text()] = InData[ui.txtITrDM.currentText()]
                    OutData[ui.txtOTeDM.text()] = InData[ui.txtITeDM.currentText()]
                except:
                    print("Cannot load design matrices!")
                    return
            # Coordinate
            if ui.cbCol.isChecked():
                if not len(ui.txtCol.currentText()):
                    msgBox.setText("Please enter Coordinator variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOCol.text()):
                    msgBox.setText("Please enter Coordinator variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOCol.text()] = InData[ui.txtCol.currentText()]
                except:
                    print("Cannot load coordinator!")
                    return
            # Condition
            if ui.cbCond.isChecked():
                if not len(ui.txtCond.currentText()):
                    msgBox.setText("Please enter Condition variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOCond.text()):
                    msgBox.setText("Please enter Condition variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOCond.text()] = InData[ui.txtCond.currentText()]
                except:
                    print("Cannot load conditions!")
                    return
            # FoldID
            if ui.cbFoldID.isChecked():
                if not len(ui.txtFoldID.currentText()):
                    msgBox.setText("Please enter FoldID variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOFoldID.text()):
                    msgBox.setText("Please enter FoldID variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOFoldID.text()] = reshape_1Dvector(InData[ui.txtFoldID.currentText()])
                except:
                    print("Cannot load Fold ID!")
                    return
            # FoldInfo
            if ui.cbFoldInfo.isChecked():
                if not len(ui.txtFoldInfo.currentText()):
                    msgBox.setText("Please enter FoldInfo variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOFoldInfo.text()):
                    msgBox.setText("Please enter FoldInfo variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOFoldInfo.text()] = InData[ui.txtFoldInfo.currentText()]
                except:
                    print("Cannot load Fold Info!")
                    return
                pass
            # Number of Scan
            if ui.cbNScan.isChecked():
                if not len(ui.txtITrScan.currentText()):
                    msgBox.setText("Please enter Number of Scan variable name for Input Train!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtITeScan.currentText()):
                    msgBox.setText("Please enter Number of Scan variable name for Input Test!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTrScan.text()):
                    msgBox.setText("Please enter Number of Scan variable name for Output Train!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if not len(ui.txtOTeScan.text()):
                    msgBox.setText("Please enter Number of Scan variable name for Output Test!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    OutData[ui.txtOTrScan.text()] = reshape_1Dvector(InData[ui.txtITrScan.currentText()])
                    OutData[ui.txtOTeScan.text()] = reshape_1Dvector(InData[ui.txtITeScan.currentText()])
                except:
                    print("Cannot load NScan!")
                    return
            print("Running LDA:")
            model = LDA(n_components=NumFea,solver=Solver,tol=Tol)
            print("Training ...")
            XTr_New = model.fit_transform(XTr,YTr)
            OutData[ui.txtOTrData.text()] = XTr_New
            print("Testing ...")
            XTe_New = model.transform(XTe)
            OutData[ui.txtOTeData.text()] = XTe_New
            print("Saving ...")
            mainIO_save(OutData, OutFile)
            print("Fold " + str(fold) + " is DONE: " + OutFile)
        print("LDA is done.")
        msgBox.setText("LDA is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFELDA.show(frmFELDA)
    sys.exit(app.exec_())