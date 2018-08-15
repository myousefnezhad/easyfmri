#!/usr/bin/env python3
import os
import sys

import nibabel as nb
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from Base.SettingHistory import History
from Base.utility import getVersion, getBuild, getSettingVersion, strMultiRange, strRange, fixstr, setParameters3
from Base.dialogs import LoadFile, SaveFile
from Base.Setting import Setting

from GUI.frmFEEZCrossValidationGUI import *


class frmFEEZCrossValidation(Ui_frmFEEZCrossValidation):
    ui = Ui_frmFEEZCrossValidation()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        global OutSize, currentFile, currentSize
        ui = Ui_frmFEEZCrossValidation()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        dialog.setWindowTitle("easy fMRI Cross Validation on EzData - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnReload.clicked.connect(self.btnReload_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)


    def btnClose_click(self):
        global dialog
        dialog.close()
        pass


    def btnInFile_click(self):
        filename = LoadFile("Load EzData file ...",['EzData files (*.ezdata)'],'ezdata',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename,appendmat=False)
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

                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")


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

                    try:
                        ui.txtDISubLen.setValue(np.int32(data["Integration"]["SubLen"][0][0]))
                    except:
                        print("Cannot load Subject Length!")

                    try:
                        ui.txtDIRunLen.setValue(np.int32(data["Integration"]["RunLen"][0][0]))
                    except:
                        print("Cannot load Run Length!")

                    try:
                        ui.txtDIConLen.setValue(np.int32(data["Integration"]["ConLen"][0][0]))
                    except:
                        print("Cannot load Counter Length!")

                    try:
                        ui.txtDISubPer.setText(data["Integration"]["SubPer"][0][0][0])
                    except:
                        print("Cannot load Subject Perfix!")

                    try:
                        ui.txtDIRunPer.setText(data["Integration"]["RunPer"][0][0][0])
                    except:
                        print("Cannot load Run Perfix!")

                    try:
                        ui.txtDIConPer.setText(data["Integration"]["ConPer"][0][0][0])
                    except:
                        print("Cannot load Counter Perfix!")

                    try:
                        ui.txtDIOutDAT.setText(data["Integration"]["OutData"][0][0][0])
                    except:
                        print("Cannot load out data format!")

                    # Data Files
                    ui.txtDataFiles.clear()
                    try:
                        HasDefualt = False
                        dstr = data["Integration"]["DataStructure"][0][0]
                        for st in dstr:
                            ui.txtData.addItem(st + "_files")
                            if len(st):
                                HasDefualt = True
                        if HasDefualt:
                            ui.txtData.setCurrentText(dstr[0] + "_files")
                            try:
                                for dfile in data["Integration"][dstr[0] + "_files"][0][0]:
                                    ui.txtDataFiles.append(dfile)
                            except:
                                print("Cannot load data files!")
                                ui.lblDataStr.setText("Data Structure: NO DATA FILE!")
                        ui.lblDataStr.setText("Data Structure: DETECT")
                    except:
                        ui.lblDataStr.setText("Data Structure: NOT FOUND!")
                        print("Cannot find Data Structure!")
                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnReload_click(self):
        msgBox = QMessageBox()

        filename = ui.txtInFile.text()
        if not len(filename):
            msgBox.setText("ROI and fMRI images must be in the same size!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if os.path.isfile(filename):
            try:
                data = io.loadmat(filename)
                ui.txtDataFiles.clear()
                for dfile in data["Integration"][ui.txtData.currentText()][0][0]:
                    ui.txtDataFiles.append(dfile)
                ui.lblDataStr.setText("Data Structure: DETECT")
                print("Data files are reloaded")
            except:
                ui.lblDataStr.setText("Data Structure: NO DATA FILE!")
                print("Cannot load data files!")


    def btnConvert_click(self):
        msgBox = QMessageBox()

        DataFiles = ui.txtDataFiles.toPlainText()
        if not len(DataFiles):
            print("WARNING: Please load data files!")
            msgBox.setText("Please load data files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        OutDataFormat = ui.txtDIOutDAT.text()
        if not len(OutDataFormat):
            msgBox.setText("Please enter output data format!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

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
            RunLen = np.int32(ui.txtDIRunLen.value())
            1 / RunLen
        except:
            msgBox.setText("Length of runs must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of runs is valid")

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

        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        TrainVal = ui.txtTrain.text()
        if not len(TrainVal):
            msgBox.setText("Please enter train perfix!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        TestVal = ui.txtTest.text()
        if not len(TestVal):
            msgBox.setText("Please enter test perfix!")
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
            InData = io.loadmat(InFile,appendmat=False)
        except:
            print("Cannot load data file!")
            msgBox.setText("Cannot load data file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        try:
            DataFiles = InData["Integration"][ui.txtData.currentText()][0][0]
        except:
            print("Cannot load data files!")
            msgBox.setText("Cannot load data files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        # Subject
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
        if not len(ui.txtTask.currentText()):
            msgBox.setText("Please enter Task variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Task = InData[ui.txtTask.currentText()]
            TaskIndex = Task.copy()
            TaskList = list()
            for tasindx, tas in enumerate(np.unique(Task)):
                TaskIndex[Task == tas] = tasindx + 1
                TaskList.append([tasindx + 1, tas])
        except:
            print("Cannot load Task ID")
            return

        # Run
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

        print("Checking data files ...")
        DataStream  = np.transpose(np.concatenate((TaskIndex, Subject, Counter, Run)))
        DataStrUniq =  list(np.transpose(np.array(list(set(tuple(i) for i in DataStream.tolist())))))
        DataTasks = list()
        for taskid in DataStrUniq[0]:
            for taskls in TaskList:
                if taskls[0] == taskid:
                    DataTasks.append(taskls[1])
        DataStrUniq = np.transpose(DataStrUniq)
        DataTasks   = np.transpose(DataTasks)
        for datindx, dat in enumerate(DataStrUniq):
            SubID = dat[1]
            CouID = dat[2]
            RunID = dat[3]
            TaskID  = DataTasks[0][datindx]
            dfile = setParameters3(OutDataFormat,"",fixstr(SubID,SubLen,ui.txtDISubPer.text()),\
                                   fixstr(RunID,RunLen,ui.txtDIRunPer.text()),TaskID,\
                                   fixstr(CouID,ConLen,ui.txtDIConPer.text()))
            if dfile in DataFiles:
                print(dfile + " is okay.")
            else:
                print(dfile + " is not found!")
                msgBox.setText(dfile + " is not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

        print("Calculating Folds ...")
        GroupFold = np.transpose(DataStrUniq.copy())
        FoldStr = ""
        if not ui.cbFSubject.isChecked():
            GroupFold[1] = -1
            GroupFold[3] = -1
        else:
            if not ui.rbFRun.isChecked():
                GroupFold[3] = -1
                FoldStr = "Subject"
            else:
                FoldStr = "Subject+Run"

        if not ui.cbFTask.isChecked():
            GroupFold[0] = -1
        else:
            FoldStr = FoldStr + "+Task"

        if not ui.cbFCounter.isChecked():
            GroupFold[2] = -1
        else:
            FoldStr = FoldStr + "+Counter"

        GroupFold = np.transpose(GroupFold)
        UniqFold = np.array(list(set(tuple(i) for i in GroupFold.tolist())))

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

        FoldIDs = np.arange(len(UniqFold)) + 1
        if not Unit == 1:
            FoldIDs = np.int32((FoldIDs - 0.1) / Unit) + 1

        DataStructure = list(InData["Integration"]["DataStructure"][0][0])
        try:
            FoldCounter = np.int32(InData["FoldCounter"][0][0]) + 1
        except:
            FoldCounter = 1

        FoldInfo = dict()
        FoldInfo["Unit"]     = Unit
        FoldInfo["Group"]    = GroupFold
        FoldInfo["Order"]    = FoldStr
        FoldInfo["Unique"]   = UniqFold
        FoldInfo["FoldID"]   = FoldIDs
        FoldInfo["TrainVal"] = TrainVal
        FoldInfo["TestVal"]  = TestVal

        GUFold = np.unique(FoldIDs)
        print("Number of all folds is: " + str(len(UniqFold)))

        for foldID, fold in enumerate(GUFold):
            print("Generating Fold " + str(foldID + 1)," of ", str(len(np.unique(FoldIDs))) , " ...")
            Train_Info = UniqFold[FoldIDs != fold]
            Test_Info  = UniqFold[FoldIDs == fold]

            currentTrainList = list()
            currentTestList  = list()
            if not ui.cbFSubject.isChecked():
                if ui.cbFTask.isChecked() and not ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])

                elif not ui.cbFTask.isChecked() and ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[2] == datastr[2]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[2] == datastr[2]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                else:
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0] and trinf[2] == datastr[2]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0] and teinf[2] == datastr[2]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])

            elif not ui.rbFRun.isChecked():
                if not ui.cbFTask.isChecked() and not ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[1] == datastr[1]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[1] == datastr[1]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                elif ui.cbFTask.isChecked() and not ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0] and trinf[1] == datastr[1]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0] and teinf[1] == datastr[1]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                elif not ui.cbFTask.isChecked() and ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[1] == datastr[1] and trinf[2] == datastr[2]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[1] == datastr[1] and teinf[2] == datastr[2]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                else:
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0] and trinf[1] == datastr[1] and trinf[2] == datastr[2]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0] and teinf[1] == datastr[1] and teinf[2] == datastr[2]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
            else:
                if not ui.cbFTask.isChecked() and not ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[1] == datastr[1] and trinf[3] == datastr[3]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[1] == datastr[1] and teinf[3] == datastr[3]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                elif ui.cbFTask.isChecked() and not ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0] and trinf[1] == datastr[1] and trinf[3] == datastr[3]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0] and teinf[1] == datastr[1] and teinf[3] == datastr[3]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])

                elif not ui.cbFTask.isChecked() and ui.cbFCounter.isChecked():
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[1] == datastr[1] and trinf[2] == datastr[2] and trinf[3] == datastr[3]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[1] == datastr[1] and teinf[2] == datastr[2] and teinf[3] == datastr[3]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])
                else:
                    for trinf in Train_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if trinf[0] == datastr[0] and trinf[1] == datastr[1] and trinf[2] == datastr[2] and trinf[3] == datastr[3]:
                                currentTrainList.append([datastr,DataTasks[0][datastrindx]])
                    for teinf in Test_Info:
                        for datastrindx, datastr in enumerate(DataStrUniq):
                            if teinf[0] == datastr[0] and teinf[1] == datastr[1] and teinf[2] == datastr[2] and trinf[3] == datastr[3]:
                                currentTestList.append([datastr,DataTasks[0][datastrindx]])

            if not len(DataStrUniq) == len(currentTestList) + len(currentTrainList):
                print("WARNING: There are some confilcts between test set and train set!", len(DataStrUniq), \
                      " is not ", len(currentTestList), " + ", len(currentTrainList))

            currTrainFiles = list()
            currTestFiles = list()
            for currTrain in currentTrainList:
                dfile = setParameters3(OutDataFormat, "", fixstr(currTrain[0][1], SubLen, ui.txtDISubPer.text()), \
                                       fixstr(currTrain[0][3], RunLen, ui.txtDIRunPer.text()), currTrain[1], \
                                       fixstr(currTrain[0][2], ConLen, ui.txtDIConPer.text()))
                currTrainFiles.append(dfile)

            for currTest in currentTestList:
                dfile = setParameters3(OutDataFormat, "", fixstr(currTest[0][1], SubLen, ui.txtDISubPer.text()), \
                                       fixstr(currTest[0][3], RunLen, ui.txtDIRunPer.text()), currTest[1], \
                                       fixstr(currTest[0][2], ConLen, ui.txtDIConPer.text()))
                currTestFiles.append(dfile)

            currTrainVal = TrainVal.replace("$FOLD$",str(fold))
            currTestVal = TestVal.replace("$FOLD$",str(fold))
            DataStructure.append(currTrainVal)
            DataStructure.append(currTestVal)
            FoldInfo[currTrainVal + "_files"] = np.array(currTrainFiles, dtype=object)
            FoldInfo[currTestVal  + "_files"] = np.array(currTestFiles,  dtype=object)

        FoldInfo["DataStructure"] = np.array(DataStructure,dtype=object)
        InData["FoldInfo" + str(FoldCounter)] = FoldInfo
        #InData["DataFold"] = np.array(DataStructure,dtype=object)
        InData["FoldCounter"] = FoldCounter

        print("Saving ...")

        io.savemat(InFile, InData, appendmat=False, do_compression=True)
        print("DONE.")
        print("Cross validation is done.")
        msgBox.setText("Cross validation is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFEEZCrossValidation.show(frmFEEZCrossValidation)
    sys.exit(app.exec_())