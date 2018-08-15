#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from Base.Conditions import Conditions
from PyQt5.QtWidgets import *
from sklearn.preprocessing import label_binarize
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmRemoveRestScanCrossGUI import *


class frmRemoveRestScanCross(Ui_frmRemoveRestScanCross):
    ui = Ui_frmRemoveRestScanCross()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmRemoveRestScanCross()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)



        dialog.setWindowTitle("easy fMRI remove rest scans (after cross validation) - V" + getVersion() + "B" + getBuild())
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
        ui.btnReadClassName.clicked.connect(self.btnLoadCondition_click)


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
                        if key == "train_data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtData.setCurrentText("train_data")

                    ui.txtTData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTData.addItem(key)
                        if key == "test_data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTData.setCurrentText("test_data")

                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "train_label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtLabel.setCurrentText("train_label")

                    ui.txtTLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTLabel.addItem(key)
                        if key == "test_label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTLabel.setCurrentText("test_label")

                    # mLabel
                    ui.txtmLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtmLabel.addItem(key)
                        if key == "train_mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtmLabel.setCurrentText("train_mlabel")
                    ui.cbmLabel.setChecked(HasDefualt)

                    ui.txtTmLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTmLabel.addItem(key)
                        if key == "test_mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTmLabel.setCurrentText("test_mlabel")
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

                    # Design
                    ui.txtDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtDM.addItem(key)
                        if key == "train_design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtDM.setCurrentText("train_design")
                    ui.cbDM.setChecked(HasDefualt)

                    ui.txtTDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTDM.addItem(key)
                        if key == "test_design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTDM.setCurrentText("test_design")
                    if ui.cbDM.isChecked():
                        ui.cbDM.setChecked(HasDefualt)

                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "train_subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("train_subject")
                    ui.cbSubject.setChecked(HasDefualt)

                    ui.txtTSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTSubject.addItem(key)
                        if key == "test_subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTSubject.setCurrentText("test_subject")
                    if ui.cbSubject.isChecked():
                        ui.cbSubject.setChecked(HasDefualt)

                    # Task
                    ui.txtTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "train_task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("train_task")
                    ui.cbTask.setChecked(HasDefualt)

                    ui.txtTTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTTask.addItem(key)
                        if key == "test_task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTTask.setCurrentText("test_task")
                    if ui.cbTask.isChecked:
                        ui.cbTask.setChecked(HasDefualt)

                    # Run
                    ui.txtRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "train_run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("train_run")
                    ui.cbRun.setChecked(HasDefualt)

                    ui.txtTRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTRun.addItem(key)
                        if key == "test_run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTRun.setCurrentText("test_run")
                    if ui.cbRun.isChecked:
                        ui.cbRun.setChecked(HasDefualt)

                    # Counter
                    ui.txtCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "train_counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("train_counter")
                    ui.cbCounter.setChecked(HasDefualt)

                    # Counter
                    ui.txtTCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTCounter.addItem(key)
                        if key == "test_counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTCounter.setCurrentText("test_counter")
                    if ui.cbCounter.isChecked():
                        ui.cbCounter.setChecked(HasDefualt)

                    # FoldID
                    ui.txtFoldID.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFoldID.addItem(key)
                        if key == "FoldID":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFoldID.setCurrentText("FoldID")
                        ui.lbFoldID.setText("ID=" + str(data["FoldID"][0][0]))

                    # FoldInfo
                    ui.txtFoldInfo.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFoldInfo.addItem(key)
                        if key == "FoldInfo":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFoldInfo.setCurrentText("FoldInfo")



                    # Condition
                    ui.txtCond.clear()
                    ui.txtClassName.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")
                        try:
                            Cond = data[ui.txtCond.currentText()]
                        finally:
                            try:
                                ui.txtClassName.addItem("")
                                for condition in Cond:
                                    ui.txtClassName.addItem(condition[0][0])
                            except:
                                ui.txtClassName.clear()
                                pass

                    ui.cbCond.setChecked(HasDefualt)

                    # NScan
                    ui.txtNScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtNScan.addItem(key)
                        if key == "train_nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtNScan.setCurrentText("train_nscan")
                    ui.cbNScan.setChecked(HasDefualt)

                    ui.txtTNScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTNScan.addItem(key)
                        if key == "test_nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTNScan.setCurrentText("test_nscan")
                    if ui.cbNScan.isChecked():
                        ui.cbNScan.setChecked(HasDefualt)

                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnLoadCondition_click(self):
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

        InData = io.loadmat(InFile)
        try:
            Cond = InData[ui.txtCond.currentText()]
        except:
            msgBox.setText("Cannot find Condition ID!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        ui.txtClassName.clear()
        ui.txtClassName.addItem("")
        for condition in Cond:
            ui.txtClassName.addItem(condition[0][0])





    def btnOutFile_click(self):
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)


    def btnConvert_click(self):

        msgBox = QMessageBox()

        # Subject
        if ui.cbSubject.isChecked():
            if not len(ui.txtSubject.currentText()):
                msgBox.setText("Please enter Train Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTSubject.currentText()):
                msgBox.setText("Please enter Test Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Train Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTTask.currentText()):
                msgBox.setText("Please enter Test Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Train Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTRun.currentText()):
                msgBox.setText("Please enter Test Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Train Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTCounter.currentText()):
                msgBox.setText("Please enter Test Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Label
        if not len(ui.txtLabel.currentText()):
            msgBox.setText("Please enter Train Label variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.txtTLabel.currentText()):
            msgBox.setText("Please enter Test Label variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Train Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTmLabel.currentText()):
                msgBox.setText("Please enter Test Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Train Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.txtTData.currentText()):
            msgBox.setText("Please enter Test Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter Train Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTDM.currentText()):
                msgBox.setText("Please enter Test Design Matrix variable name!")
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
            if not len(ui.txtNScan.currentText()):
                msgBox.setText("Please enter Train Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtTNScan.currentText()):
                msgBox.setText("Please enter Test Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        if ui.cbFoldID.isChecked():
            if not len(ui.txtFoldID.currentText()):
                msgBox.setText("Please enter Fold ID variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        if ui.cbFoldInfo.isChecked():
            if not len(ui.txtFoldInfo.currentText()):
                msgBox.setText("Please enter Fold Info variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            ClassID = np.int32(ui.txtClassID.text())
        except:
            msgBox.setText("Class ID is wrong!")
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

        InData = io.loadmat(InFile)
        OutData = dict()
        OutData["imgShape"] = InData["imgShape"]

        if ui.cbFoldID.isChecked():
            OutData[ui.txtFoldID.currentText()] = InData[ui.txtFoldID.currentText()]

        if ui.cbFoldInfo.isChecked():
            OutData[ui.txtFoldInfo.currentText()] = InData[ui.txtFoldInfo.currentText()]

        # Condition
        if ui.cbCond.isChecked():
            try:
                Cond = InData[ui.txtCond.currentText()]
                New_Condition = Conditions()
                for condition in Cond:
                    if condition[0][0] != ui.txtClassName.currentText():
                        New_Condition.add_cond(condition[0][0],condition[1][0])

                OutData[ui.txtCond.currentText()] = np.array(New_Condition.get_cond(),dtype=object)
            except Exception as e:
                print(e)
                print("Cannot load Condition ID!")
                return


        try:
            Y = InData[ui.txtLabel.currentText()]
            YT = InData[ui.txtTLabel.currentText()]
        except:
            print("Cannot load class labels!")
            return

        if not len(np.where(Y == ClassID)[0]):
            msgBox.setText("Train Data: There is no label with this Class ID!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(np.where(YT == ClassID)[0]):
            msgBox.setText("Test Data: There is no label with this Class ID!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        NoneZeroArea = np.where(Y != ClassID)
        New_Y = Y[NoneZeroArea]
        OutData[ui.txtLabel.currentText()] = New_Y

        NoneZeroAreaT = np.where(YT != ClassID)
        New_YT = YT[NoneZeroAreaT]
        OutData[ui.txtTLabel.currentText()] = New_YT


        try:
            X  = InData[ui.txtData.currentText()]
            XT = InData[ui.txtTData.currentText()]
        except:
            print("Cannot load data")
            return
        OutData[ui.txtData.currentText()]  = X[NoneZeroArea[1]]
        OutData[ui.txtTData.currentText()] = XT[NoneZeroAreaT[1]]

        # Subject
        if ui.cbSubject.isChecked():
            try:
                Subject = InData[ui.txtSubject.currentText()]
                OutData[ui.txtSubject.currentText()] = Subject[NoneZeroArea]

                SubjectT = InData[ui.txtTSubject.currentText()]
                OutData[ui.txtTSubject.currentText()] = SubjectT[NoneZeroAreaT]

            except:
                print("Cannot load Subject ID!")
                return

        # Task
        if ui.cbTask.isChecked():
            try:
                Task = InData[ui.txtTask.currentText()]
                OutData[ui.txtTask.currentText()] = np.array(Task[NoneZeroArea],dtype=object)

                TaskT = InData[ui.txtTTask.currentText()]
                OutData[ui.txtTTask.currentText()] = np.array(TaskT[NoneZeroAreaT],dtype=object)
            except:
                print("Cannot load Task ID!")
                return

        # Run
        if ui.cbRun.isChecked():
            try:
                Run = InData[ui.txtRun.currentText()]
                OutData[ui.txtRun.currentText()] = Run[NoneZeroArea]

                RunT = InData[ui.txtTRun.currentText()]
                OutData[ui.txtTRun.currentText()] = RunT[NoneZeroAreaT]
            except:
                print("Cannot load Run ID!")
                return

        # Counter
        if ui.cbCounter.isChecked():
            try:
                Counter = InData[ui.txtCounter.currentText()]
                OutData[ui.txtCounter.currentText()] = Counter[NoneZeroArea]

                CounterT = InData[ui.txtTCounter.currentText()]
                OutData[ui.txtTCounter.currentText()] = CounterT[NoneZeroAreaT]
            except:
                print("Cannot load Counter ID!")
                return

        # Matrix Label
        if ui.cbmLabel.isChecked():
            try:
                OutData[ui.txtmLabel.currentText()] = label_binarize(New_Y,np.unique(New_Y))
                OutData[ui.txtTmLabel.currentText()] = label_binarize(New_YT,np.unique(New_YT))
            except:
                print("Cannot load Matrix Label ID!")
                return

        # Design
        if ui.cbDM.isChecked():
            try:
                DM = InData[ui.txtDM.currentText()]
                OutData[ui.txtDM.currentText()] = DM[NoneZeroArea[1]]

                DMT = InData[ui.txtTDM.currentText()]
                OutData[ui.txtTDM.currentText()] = DMT[NoneZeroAreaT[1]]
            except:
                print("Cannot load Design Matrix ID!")
                return

        # Coordinate
        if ui.cbCol.isChecked():
            try:
                OutData[ui.txtCol.currentText()] = InData[ui.txtCol.currentText()]
            except:
                print("Cannot load Coordinate ID!")
                return

        # NScan
        if ui.cbNScan.isChecked():
            try:
                NScan = InData[ui.txtNScan.currentText()]
                OutData[ui.txtNScan.currentText()] = NScan[NoneZeroArea]
                NScanT = InData[ui.txtTNScan.currentText()]
                OutData[ui.txtTNScan.currentText()] = NScanT[NoneZeroAreaT]
            except:
                print("Cannot load NScan ID!")
                return



        print("Saving ...")
        io.savemat(ui.txtOutFile.text(), mdict=OutData)
        print("Train: Number of selected instances: ", np.shape(NoneZeroArea)[1])
        print("Train: Number of all instances: ", np.shape(Y)[1])
        print("Test: Number of selected instances: ", np.shape(NoneZeroAreaT)[1])
        print("Test: Number of all instances: ", np.shape(YT)[1])
        print("DONE.")
        msgBox.setText("Rest scans are removed.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmRemoveRestScanCross.show(frmRemoveRestScanCross)
    sys.exit(app.exec_())