#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn.preprocessing import label_binarize
from Base.dialogs import LoadFile, SelectDir
from Base.utility import getVersion, getBuild
from GUI.frmFECrossValidationGUI import *


class frmFECrossValidation(Ui_frmFECrossValidation):
    ui = Ui_frmFECrossValidation()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFECrossValidation()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        dialog.setWindowTitle("easy fMRI Cross Validation - V" + getVersion() + "B" + getBuild())
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

                    # Data
                    ui.txtData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtData.setCurrentText("data")

                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtLabel.setCurrentText("label")

                    # mLabel
                    ui.txtmLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtmLabel.addItem(key)
                        if key == "mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtmLabel.setCurrentText("mlabel")
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

                    # Design
                    ui.txtDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtDM.addItem(key)
                        if key == "design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtDM.setCurrentText("design")
                    ui.cbDM.setChecked(HasDefualt)

                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")
                    ui.cbSubject.setChecked(HasDefualt)


                    # Task
                    ui.txtTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")
                    ui.cbTask.setChecked(HasDefualt)

                    # Run
                    ui.txtRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("run")
                    ui.cbRun.setChecked(HasDefualt)

                    # Counter
                    ui.txtCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("counter")
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

                    # NScan
                    ui.txtScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtScan.addItem(key)
                        if key == "nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtScan.setCurrentText("nscan")
                    ui.cbNScan.setChecked(HasDefualt)

                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        directory = SelectDir("Open Output Directory",ui.txtOutDIR.text())
        if len(directory):
            ui.txtOutDIR.setText(directory)

    def btnConvert_click(self):
        msgBox = QMessageBox()


        if not ui.cbFSubject.isChecked():
            if not ui.cbFTask.isChecked():
                if not ui.cbFCounter.isChecked():
                    msgBox.setText("You must at least select one Fold Level!")
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

        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Coordinate
        if ui.cbCol.isChecked():
            if not len(ui.txtCol.currentText()):
                msgBox.setText("Please enter Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtCond.currentText()):
                msgBox.setText("Please enter Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Number of Scan
        if ui.cbNScan.isChecked():
            if not len(ui.txtScan.currentText()):
                msgBox.setText("Please enter Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Subject Condition
        if ui.cbFSubject.isChecked():
            if not ui.cbSubject.isChecked():
                msgBox.setText("For using task as a fold level, you have to enable task filed in input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Run Condition
            if ui.rbFRun.isChecked():
                if not ui.cbRun.isChecked():
                    msgBox.setText("For using run as a fold level, you have to enable run filed in input file!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False


        # Task Condition
        if not ui.cbTask.isChecked():
            if ui.cbFTask.isChecked():
                msgBox.setText("For using task as a fold level, you have to enable task filed in input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Counter
        if not ui.cbCounter.isChecked():
            if ui.cbFCounter.isChecked():
                msgBox.setText("For using counter as a fold level, you have to enable counter filed in input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # OutDIR
        OutDIR = ui.txtOutDIR.text()
        if not len(OutDIR):
            msgBox.setText("Please enter out directory!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not os.path.isdir(OutDIR):
            msgBox.setText("Output directory not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        # Out Files
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

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

        try:
            InData = io.loadmat(InFile)
        except:
            print("Cannot load data file!")
            return


        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            X = InData[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return

        # Subject
        if ui.cbSubject.isChecked():
            if not len(ui.txtSubject.currentText()):
                msgBox.setText("Please enter Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            Subject = InData[ui.txtSubject.currentText()]
        except:
            print("Cannot load Subject ID")
            return

        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            Task = InData[ui.txtTask.currentText()]
            TaskIndex = Task.copy()
            for tasindx, tas in enumerate(np.unique(Task)):
                TaskIndex[Task == tas] = tasindx + 1
        except:
            print("Cannot load Task ID")
            return

        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            Run = InData[ui.txtRun.currentText()]
        except:
            print("Cannot load Run ID")
            return

        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            Counter = InData[ui.txtCounter.currentText()]
        except:
            print("Cannot load Counter ID")
            return


        try:
            Unit = np.int32(ui.txtUnit.text())
        except:
            msgBox.setText("Unit for the test set must be a number!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if Unit < 1:
            msgBox.setText("Unit for the test set must be greater than zero!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        print("Calculating Folds ...")
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

        print("Number of all folds is: " + str(len(UniqFold)))
        for foldID, fold in enumerate(GUFold):
            print("Saving Fold " + str(foldID + 1)," of ", str(len(UniqFold)) , " ...")

            OutData = dict()
            OutData["imgShape"] = InData["imgShape"]

            OutData["FoldInfo"] = FoldInfo
            OutData["FoldID"]     = fold

            TestIndex = np.where(UnitFold == fold)
            TrainIndex = np.where(UnitFold != fold)


            OutData[ui.txtTrain.text() + ui.txtOData.text()] = X[TrainIndex]
            OutData[ui.txtTest.text()  + ui.txtOData.text()] = X[TestIndex]

            # Subject
            if ui.cbSubject.isChecked():
                OutData[ui.txtTrain.text() + ui.txtOSubject.text()] = Subject[0,TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtOSubject.text()] = Subject[0,TestIndex]

            # Task
            if ui.cbTask.isChecked():
                OutData[ui.txtTrain.text() + ui.txtOTask.text()] = Task[0,TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtOTask.text()] = Task[0,TestIndex]

            # Run
            if ui.cbRun.isChecked():
                OutData[ui.txtTrain.text() + ui.txtORun.text()] = Run[0,TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtORun.text()] = Run[0,TestIndex]

            # Counter
            if ui.cbCounter.isChecked():
                OutData[ui.txtTrain.text() + ui.txtOCounter.text()] = Counter[0,TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtOCounter.text()] = Counter[0,TestIndex]

            # Label
            Label = InData[ui.txtLabel.currentText()]
            TrainLabel = Label[0, TrainIndex]
            TestLabel  = Label[0, TestIndex]
            OutData[ui.txtTrain.text() + ui.txtOLabel.text()] = TrainLabel
            OutData[ui.txtTest.text()  + ui.txtOLabel.text()] = TestLabel

            # m Label
            if ui.cbmLabel.isChecked():
                OutData[ui.txtTrain.text() + ui.txtOmLabel.text()] = label_binarize(TrainLabel[0], np.unique(TrainLabel))
                OutData[ui.txtTest.text()  + ui.txtOmLabel.text()] = label_binarize(TestLabel[0], np.unique(TestLabel))

            # DM
            if ui.cbDM.isChecked():
                DM = InData[ui.txtDM.currentText()]
                OutData[ui.txtTrain.text() + ui.txtODM.text()] = DM[TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtODM.text()] = DM[TestIndex]

            # NScan
            if ui.cbNScan.isChecked():
                NScan = InData[ui.txtScan.currentText()]
                OutData[ui.txtTrain.text() + ui.txtOScan.text()] = NScan[0, TrainIndex]
                OutData[ui.txtTest.text()  + ui.txtOScan.text()] = NScan[0, TestIndex]

            # Coordination
            if ui.cbCol.isChecked():
                OutData[ui.txtCol.currentText()]  = InData[ui.txtOCol.text()]

            # Condition
            if ui.cbCond.isChecked():
                OutData[ui.txtCond.currentText()] = InData[ui.txtOCond.text()]


            OutFileUpdate = str.replace(OutFile,"$FOLD$", str(foldID + 1))
            io.savemat(OutDIR + OutFileUpdate, mdict=OutData)


        print("Cross validation is done.")
        msgBox.setText("Cross validation is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFECrossValidation.show(frmFECrossValidation)
    sys.exit(app.exec_())