# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys
import time
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn.decomposition import KernelPCA, PCA, IncrementalPCA
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmTAIntersecGUI import *


class frmTAIntersec(Ui_frmTAInterSec):
    ui = Ui_frmTAInterSec()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmTAInterSec()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)

        self.set_events(self)

        ui.tabWidget.setCurrentIndex(0)

        dialog.setWindowTitle("easy fMRI Temporal Alignment with Intersection strategy- V" + getVersion() + "B" + getBuild())
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
                    print("Loading ...")
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    ui.txtClassList.clear()

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
                        for lbl in Labels:
                            ui.txtClassList.append(str(lbl))



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
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
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

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter input Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtOData.text()):
            msgBox.setText("Please enter output Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Label
        if not len(ui.txtLabel.currentText()):
            msgBox.setText("Please enter input Label variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtOLabel.text()):
            msgBox.setText("Please enter output Label variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter input Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtOSubject.text()):
            msgBox.setText("Please enter output Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Run
        if not len(ui.txtRun.currentText()):
            msgBox.setText("Please enter input Run variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtORun.text()):
            msgBox.setText("Please enter output Run variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Counter
        if not len(ui.txtCounter.currentText()):
            msgBox.setText("Please enter input Counter variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtOCounter.text()):
            msgBox.setText("Please enter output Counter variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Task
        if not len(ui.txtTask.currentText()):
            msgBox.setText("Please enter input Task variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtOTask.text()):
            msgBox.setText("Please enter output Task variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # mLabel
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter input mLabel variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if not len(ui.txtOmLabel.text()):
                msgBox.setText("Please enter output mLabel variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Coordinate
        if ui.cbCol.isChecked():
            if not len(ui.txtCol.currentText()):
                msgBox.setText("Please enter input Coordinate variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if not len(ui.txtOCol.text()):
                msgBox.setText("Please enter output Coordinate variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter input Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if not len(ui.txtODM.text()):
                msgBox.setText("Please enter output Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtCond.currentText()):
                msgBox.setText("Please enter input Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if not len(ui.txtOCond.text()):
                msgBox.setText("Please enter output Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # NScan
        if ui.cbNScan.isChecked():
            if not len(ui.txtScan.currentText()):
                msgBox.setText("Please enter input Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if not len(ui.txtOScan.text()):
                msgBox.setText("Please enter output Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Creating label filters
        try:
            ClassListString = str.split(str.strip(ui.txtFLabels.toPlainText()), "\n")
            ClassList = list()
            if len(ClassListString):
                for classstr in ClassListString:
                    if len(classstr):
                        ClassList.append(int(classstr))

                print("Label filter is ", ClassList)
        except:
            print("Cannot load label filter")
            msgBox.setText("Cannot load label filter!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Creating Fold filter
        try:
            FoldString = str.split(str.strip(ui.txtFFold.toPlainText()), "\n")
            FoldFilterList = list()
            if len(FoldString):
                for foldstr in FoldString:
                    if len(foldstr):
                        FoldFilterList.append(int(foldstr))

                print("Fold filter is ", FoldFilterList)
        except:
            print("Cannot load fold filter")
            msgBox.setText("Cannot load fold filter!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        InData = io.loadmat(InFile)
        OutData = dict()
        OutData["imgShape"] = InData["imgShape"]

        # Data
        try:
            X = InData[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return
        # Label
        try:
            Label = InData[ui.txtLabel.currentText()][0]
        except:
            print("Cannot load Labels!")
            return
        # Subject
        try:
            Subject = InData[ui.txtSubject.currentText()]
        except:
            print("Cannot load Subject ID")
            return
        # Run
        try:
            Run = InData[ui.txtRun.currentText()]
        except:
            print("Cannot load Run ID")
            return
        # Counter
        try:
            Counter = InData[ui.txtCounter.currentText()]
        except:
            print("Cannot load Counter ID")
            return
        # Task
        try:
            Task = InData[ui.txtTask.currentText()]

            TaskIndex = Task.copy()
            for tasindx, tas in enumerate(np.unique(Task)):
                TaskIndex[Task == tas] = tasindx + 1
        except:
            print("Cannot load Task ID")
            return
        # mLabel
        mLabel = None
        try:
            if ui.cbmLabel.isChecked():
                mLabel = InData[ui.txtmLabel.currentText()]
        except:
            print("Cannot load mLabel ID")
            return
        # Coordinate
        try:
            if ui.cbCol.isChecked():
                OutData[ui.txtOCol.text()] = InData[ui.txtCol.currentText()]
        except:
            print("Cannot load Coordinate ID")
            return
        # Design Matrix
        DM = None
        try:
            if ui.cbDM.isChecked():
                DM = InData[ui.txtDM.currentText()]
        except:
            print("Cannot load Design Matrix ID")
            return
        # Condition
        try:
            if ui.cbCond.isChecked():
                OutData[ui.txtOCond.text()] = InData[ui.txtCond.currentText()]
        except:
            print("Cannot load Condition ID")
            return
        # NScan
        Scan = None
        try:
            if ui.cbNScan.isChecked():
                Scan = InData[ui.txtScan.currentText()]
        except:
            print("Cannot load NScan ID")
            return


        # Apply filter
        print("Filtering labels from data ...")

        for lbl in ClassList:
            # Remove Training Set
            labelIndx = np.where(Label == lbl)[0]
            X       = np.delete(X, labelIndx, axis=0)
            Label   = np.delete(Label, labelIndx)
            Subject = np.delete(Subject, labelIndx, axis=1)
            Run     = np.delete(Run, labelIndx, axis=1)
            Task    = np.delete(Task, labelIndx, axis=1)
            Counter = np.delete(Counter, labelIndx, axis=1)
            mLabel  = np.delete(mLabel, labelIndx, axis=0) if mLabel is not None else None
            DM      = np.delete(DM, labelIndx, axis=0) if DM is not None else None
            Scan    = np.delete(Scan, labelIndx, axis=1) if Scan is not None else None
            print("Label %d is filtered!"%(lbl))

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
        GUFold = np.unique(UnitFold)
        print("Number of data in this level is " + str(len(UniqFold)))
        # Filtering folds
        print("Applying fold filter ...")
        for foldfilter in FoldFilterList:
            IndexFold = np.where(UnitFold != foldfilter)
            X       = X[IndexFold, :][0]
            Label   = Label[IndexFold]
            Subject = Subject[:, IndexFold][0]
            Run     = Run[:, IndexFold][0]
            Task    = Task[:, IndexFold][0]
            Counter = Counter[:, IndexFold][0]
            mLabel  = mLabel[IndexFold, :][0] if mLabel is not None else None
            DM      = DM[IndexFold, :][0] if DM is not None else None
            Scan    = Scan[:, IndexFold][0] if Scan is not None else None
            UnitFold = UnitFold[IndexFold]
            print("Fold %d is filtered!"%(foldfilter))
        # Reconstruct Labels
        print("Reforming labels based on folds ...")
        LabelCounter = dict()
        for lbl in np.unique(Label):
            LabelCounter[lbl] = None
        for foldID, fold in enumerate(GUFold):
            foldLevelLabel = Label[np.where(UnitFold == fold)]
            foldLevelUnique, foldLevelCounter = np.unique(foldLevelLabel, return_counts=True)
            for flu, flc in zip(foldLevelUnique, foldLevelCounter):
                LabelCounter[flu] = np.min((LabelCounter[flu], flc)) if LabelCounter[flu] is not None else flc
        if ui.cbBalence.isChecked():
            MinAllLabelCounter = None
            for lbl in np.unique(Label):
                MinAllLabelCounter = LabelCounter[lbl] if MinAllLabelCounter is None else np.min((MinAllLabelCounter, LabelCounter[lbl]))
            for lbl in np.unique(Label):
                LabelCounter[lbl] = MinAllLabelCounter
        # Report Label Threshold
        for lbl in np.unique(Label):
            print("Class ID: {:6d}, \t Selected Timepoints: {:10d}".format(lbl, LabelCounter[lbl]))
        # Make free space memory
        del InData

        XOut        = None
        LabelOut    = None
        SubjectOut  = None
        RunOut      = None
        TaskOut     = None
        CounterOut  = None
        mLabelOut   = None
        DMOut       = None
        ScanOut     = None

        for foldID, fold in enumerate(GUFold):
            IndexFold = np.where(UnitFold == fold)
            SX       = X[IndexFold, :][0]
            SLabel   = Label[IndexFold]
            SSubject = Subject[:, IndexFold][0][0]
            SRun     = Run[:, IndexFold][0][0]
            STask    = Task[:, IndexFold][0][0]
            SCounter = Counter[:, IndexFold][0][0]
            if ui.cbmLabel.isChecked():
                SmLabel  = mLabel[IndexFold, :][0] if mLabel is not None else None
            if ui.cbDM.isChecked():
                SDM      = DM[IndexFold, :][0] if DM is not None else None
            if ui.cbNScan.isChecked():
                SScan    = Scan[:, IndexFold][0][0] if Scan is not None else None

            for lbl in np.unique(Label):
                IndexLabel = np.where(SLabel == lbl)
                IndexLabel = IndexLabel[0][:LabelCounter[lbl]]
                XOut        = SX[IndexLabel, :] if XOut is None else np.concatenate((XOut, SX[IndexLabel, :]), axis=0)
                LabelOut    = SLabel[IndexLabel] if LabelOut is None else np.concatenate((LabelOut, SLabel[IndexLabel]), axis=0)
                SubjectOut  = SSubject[IndexLabel] if SubjectOut is None else np.concatenate((SubjectOut, SSubject[IndexLabel]), axis=0)
                RunOut      = SRun[IndexLabel] if RunOut is None else np.concatenate((RunOut, SRun[IndexLabel]), axis=0)
                TaskOut     = STask[IndexLabel] if TaskOut is None else np.concatenate((TaskOut, STask[IndexLabel]), axis=0)
                CounterOut  = SCounter[IndexLabel] if CounterOut is None else np.concatenate((CounterOut, SCounter[IndexLabel]), axis=0)
                if ui.cbmLabel.isChecked():
                    mLabelOut   = SmLabel[IndexLabel, :] if mLabelOut is None else np.concatenate((mLabelOut, SmLabel[IndexLabel, :]), axis=0)
                if ui.cbDM.isChecked():
                    DMOut       = SDM[IndexLabel, :] if DMOut is None else np.concatenate((DMOut, SDM[IndexLabel, :]), axis=0)
                if ui.cbNScan.isChecked():
                    ScanOut     = SScan[IndexLabel] if ScanOut is None else np.concatenate((ScanOut, SScan[IndexLabel]), axis=0)

                print("Data belong to fold {:6} and label {:6d} is collected.".format(fold, lbl))

        OutData[ui.txtOData.text()]     = XOut
        OutData[ui.txtOLabel.text()]    = LabelOut
        OutData[ui.txtOSubject.text()]  = SubjectOut
        OutData[ui.txtORun.text()]      = RunOut
        OutData[ui.txtOTask.text()]     = TaskOut
        OutData[ui.txtOCounter.text()]  = CounterOut

        if ui.cbmLabel.isChecked():
            OutData[ui.txtOmLabel.text()]   = mLabelOut
        if ui.cbDM.isChecked():
            OutData[ui.txtODM.text()]       = DMOut
        if ui.cbNScan.isChecked():
            OutData[ui.txtOScan.text()]     = ScanOut

        print("Saving ...")
        io.savemat(OutFile, mdict=OutData, do_compression=True)
        print("Temporal Alignment is done.")
        msgBox.setText("Temporal Alignment is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmTAIntersec.show(frmTAIntersec)
    sys.exit(app.exec_())