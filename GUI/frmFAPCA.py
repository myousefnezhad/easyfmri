#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn.decomposition import KernelPCA, PCA, IncrementalPCA
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmFAPCAGUI import *


class frmFAPCA(Ui_frmFAPCA):
    ui = Ui_frmFAPCA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFAPCA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        # Kenel List
        ui.cbKernel.addItem("linear")
        ui.cbKernel.addItem("poly")
        ui.cbKernel.addItem("rbf")
        ui.cbKernel.addItem("sigmoid")
        ui.cbKernel.addItem("cosine")

        # Method
        ui.cbMethod.addItem("PCA")
        ui.cbMethod.addItem("Kernel PCA")
        ui.cbMethod.addItem("Incremental PCA")


        dialog.setWindowTitle("easy fMRI PCA Functional Alignment - V" + getVersion() + "B" + getBuild())
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
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename)
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

                    # Test Subject
                    ui.txtITeSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeSubject.addItem(key)
                        if key == "test_subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeSubject.setCurrentText("test_subject")

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
                    data = io.loadmat(filename)
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
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()

        # Batch
        try:
            Batch = np.int32(ui.txtBatch.text())
        except:
            msgBox.setText("Size of batch is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if Batch == 0:
            Batch = None

        # Kernel
        Kernel = ui.cbKernel.currentText()
        # Method
        Method = ui.cbMethod.currentText()

        # Gamma
        try:
            Gamma = np.float(ui.txtGamma.text())
        except:
            msgBox.setText("Gamma is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Degree
        try:
            Degree = np.int32(ui.txtDegree.text())
        except:
            msgBox.setText("Degree is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Coef0
        try:
            Coef0 = np.float(ui.txtCoef0.text())
        except:
            msgBox.setText("Coef0 is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Alpha
        try:
            Alpha = np.int32(ui.txtAlpha.text())
        except:
            msgBox.setText("Alpha is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Tol
        try:
            Tol = np.float(ui.txtTole.text())
        except:
            msgBox.setText("Tolerance is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # MaxIte
        try:
            MaxIter = np.int32(ui.txtMaxIter.text())
        except:
            msgBox.setText("Maximum number of iterations is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if MaxIter <= 0:
            MaxIter = None

        # Number of Job
        try:
            NJob = np.int32(ui.txtJobs.text())
        except:
            msgBox.setText("The number of parallel jobs is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if NJob < -1 or NJob == 0:
            msgBox.setText("The number of parallel jobs must be -1 or greater than 0!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        TrFoldErr = list()
        TeFoldErr = list()

        try:
            FoldFrom = np.int32(ui.txtFoldFrom.text())
            FoldTo   = np.int32(ui.txtFoldTo.text())
        except:
            print("Please check fold parameters!")
            return

        if FoldTo < FoldFrom:
            print("Please check fold parameters!")
            return

        for fold_all in range(FoldFrom, FoldTo+1):

            # OutFile
            OutFile = ui.txtOutFile.text()
            OutFile = OutFile.replace("$FOLD$", str(fold_all))
            if not len(OutFile):
                msgBox.setText("Please enter out file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            # InFile
            InFile = ui.txtInFile.text()
            InFile = InFile.replace("$FOLD$", str(fold_all))
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

            InData = io.loadmat(InFile)
            OutData = dict()
            OutData["imgShape"] = InData["imgShape"]

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

            if NumFea > np.shape(XTe)[1]:
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
                OutData[ui.txtOTrLabel.text()] = InData[ui.txtITrLabel.currentText()]
                OutData[ui.txtOTeLabel.text()] = InData[ui.txtITeLabel.currentText()]
            except:
                print("Cannot load labels!")

            # Subject
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
                TrSubject = InData[ui.txtITrSubject.currentText()]
                OutData[ui.txtOTrSubject.text()] = TrSubject
                TeSubject = InData[ui.txtITeSubject.currentText()]
                OutData[ui.txtOTeSubject.text()] = TeSubject
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
                    TrTask = InData[ui.txtITrTask.currentText()]
                    OutData[ui.txtOTrTask.text()] = TrTask
                    TeTask = InData[ui.txtITeTask.currentText()]
                    OutData[ui.txtOTeTask.text()] = TeTask
                    TrTaskIndex = TrTask.copy()
                    for tasindx, tas in enumerate(np.unique(TrTask)):
                        TrTaskIndex[TrTask == tas] = tasindx + 1
                    TeTaskIndex = TeTask.copy()
                    for tasindx, tas in enumerate(np.unique(TeTask)):
                        TeTaskIndex[TeTask == tas] = tasindx + 1
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
                    TrRun = InData[ui.txtITrRun.currentText()]
                    OutData[ui.txtOTrRun.text()] = TrRun
                    TeRun = InData[ui.txtITeRun.currentText()]
                    OutData[ui.txtOTeRun.text()] = TeRun
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
                    TrCounter = InData[ui.txtITrCounter.currentText()]
                    OutData[ui.txtOTrCounter.text()] = TrCounter
                    TeCounter = InData[ui.txtITeCounter.currentText()]
                    OutData[ui.txtOTeCounter.text()] = TeCounter
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
                    OutData[ui.txtOFoldID.text()] = InData[ui.txtFoldID.currentText()]
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
                    OutData[ui.txtOTrScan.text()] = InData[ui.txtITrScan.currentText()]
                    OutData[ui.txtOTeScan.text()] = InData[ui.txtITeScan.currentText()]
                except:
                    print("Cannot load NScan!")
                    return


            if Method == "PCA":
                model = PCA(n_components=NumFea,copy=False,tol=Tol)
            elif Method == "Kernel PCA":
                model = KernelPCA(n_components=NumFea,kernel=Kernel,gamma=Gamma,degree=Degree,\
                              coef0=Coef0, alpha=Alpha, tol=Tol, max_iter=MaxIter, n_jobs=NJob,copy_X=False)
            else:
                model = IncrementalPCA(n_components=NumFea,copy=False,batch_size=Batch)

            print("Running PCA Functional Alignment on Training Data ...")
            OutData[ui.txtOTrData.text()] = model.fit_transform(XTr)
            print("Running PCA Functional Alignment on Testing Data ...")
            OutData[ui.txtOTeData.text()] = model.fit_transform(XTe)

            HAParam = dict()
            HAParam["Method"]   = Method
            HAParam["NumFea"]   = NumFea
            HAParam["Kernel"]   = Kernel
            OutData["FunctionalAlignment"] = HAParam

            print("Saving ...")
            io.savemat(OutFile, mdict=OutData)
            print("Fold " + str(fold_all) + " is DONE: " + OutFile)

        print("PCA Functional Alignment is done.")
        msgBox.setText("PCA Functional Alignment is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFAPCA.show(frmFAPCA)
    sys.exit(app.exec_())