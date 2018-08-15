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
from GUI.frmCombineDataGUI import *


class frmCombineData(Ui_frmCombineData):
    ui = Ui_frmCombineData()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmCombineData()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)



        dialog.setWindowTitle("easy fMRI combine data - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFFile.clicked.connect(self.btnInFFile_click)
        ui.btnInSFile.clicked.connect(self.btnInSFile_click)
        ui.btnOutFile.clicked.connect(self.btnOutFile_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)



    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    # Data
                    ui.txtFData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFData.setCurrentText("data")

                    # Label
                    ui.txtFLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFLabel.setCurrentText("label")


                    # Coordinate
                    ui.txtFCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFCol.setCurrentText("coordinate")

                    # Design
                    ui.txtFDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFDM.addItem(key)
                        if key == "design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFDM.setCurrentText("design")

                    # Subject
                    ui.txtFSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFSubject.setCurrentText("subject")

                    # Task
                    ui.txtFTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFTask.setCurrentText("task")

                    # Run
                    ui.txtFRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFRun.setCurrentText("run")

                    # Counter
                    ui.txtFCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFCounter.setCurrentText("counter")

                    # Condition
                    ui.txtFCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFCond.setCurrentText("condition")


                    # NScan
                    ui.txtFScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFScan.addItem(key)
                        if key == "nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFScan.setCurrentText("nscan")


                    ui.txtInFFile.setText(filename)
                except:
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")


    def btnInSFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInSFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    # Data
                    ui.txtSData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSData.setCurrentText("data")

                    # Label
                    ui.txtSLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSLabel.setCurrentText("label")


                    # Coordinate
                    ui.txtSCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSCol.setCurrentText("coordinate")

                    # Design
                    ui.txtSDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSDM.addItem(key)
                        if key == "design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSDM.setCurrentText("design")

                    # Subject
                    ui.txtSSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSSubject.setCurrentText("subject")

                    # Task
                    ui.txtSTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSTask.setCurrentText("task")

                    # Run
                    ui.txtSRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSRun.setCurrentText("run")

                    # Counter
                    ui.txtSCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSCounter.setCurrentText("counter")

                    # Condition
                    ui.txtSCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSCond.setCurrentText("condition")


                    # NScan
                    ui.txtSScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSScan.addItem(key)
                        if key == "nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSScan.setCurrentText("nscan")


                    ui.txtInSFile.setText(filename)
                except:
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

        InFFile = ui.txtInFFile.text()
        if not len(InFFile):
            msgBox.setText("Please select the first input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        elif not os.path.isfile(InFFile):
            msgBox.setText("The first input file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        InSFile = ui.txtInSFile.text()
        if not len(InSFile):
            msgBox.setText("Please select the second input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        elif not os.path.isfile(InSFile):
            msgBox.setText("The second input file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please select the output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not ui.cbCondUnion.isChecked():
            if not len(ui.txtFCondPre.text()):
                msgBox.setText("Please enter the condition prefix!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # if not len(ui.txtSCondPre.text()):
            #     msgBox.setText("Please enter the condition prefix!")
            #     msgBox.setIcon(QMessageBox.Critical)
            #     msgBox.setStandardButtons(QMessageBox.Ok)
            #     msgBox.exec_()
            #     return False
            # if not len(ui.txtOCondPre.text()):
            #     msgBox.setText("Please enter the condition prefix!")
            #     msgBox.setIcon(QMessageBox.Critical)
            #     msgBox.setStandardButtons(QMessageBox.Ok)
            #     msgBox.exec_()
            #     return False

        InFData = io.loadmat(InFFile)
        InSData = io.loadmat(InSFile)
        OutData = dict()


        # Data
        if not len(ui.txtFData.currentText()):
            msgBox.setText("Please enter First Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.txtSData.currentText()):
            msgBox.setText("Please enter Second Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.txtOData.text()):
            msgBox.setText("Please enter Out Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            InFX = InFData[ui.txtFData.currentText()]
        except:
            print("Cannot load data from the first file!")
            return

        try:
            InSX = InSData[ui.txtSData.currentText()]
        except:
            print("Cannot load data from the second file!")
            return

        if np.shape(InFX)[1] != np.shape(InSX)[1]:
            print("Both data files must have the same size!")
            return

        # fMRI Size
        InterfMRISize = InFData["imgShape"][0] - InSData["imgShape"][0]
        if  (np.max(InterfMRISize) != 0) or (np.min(InterfMRISize) != 0):
            print("Both data files must extract from the same size fMRI images!")
            return

        OutData["imgShape"] = InFData["imgShape"]

        # Coordinate
        if ui.cbCol.isChecked():
            if not len(ui.txtFCol.currentText()):
                msgBox.setText("Please enter First Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSCol.currentText()):
                msgBox.setText("Please enter Second Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOCoI.text()):
                msgBox.setText("Please enter Out Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                InFCol = np.array(InFData[ui.txtFCol.currentText()])
            except:
                print("Cannot load coordinate in the first file!")
                return
            try:
                InSCol = np.array(InSData[ui.txtSCol.currentText()])
            except:
                print("Cannot load coordinate in the second file!")
                return

            SubCol = InFCol - InSCol
            if (np.max(SubCol) != 0) or (np.min(SubCol) != 0):
                msgBox.setText("Coordinates are not matched!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            OutData[ui.txtOCoI.text()] = InFData[ui.txtFCol.currentText()]

        OutData[ui.txtOData.text()] = np.concatenate((InFX,InSX))


        # Label
        if not len(ui.txtFLabel.currentText()):
                msgBox.setText("Please enter First Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if not len(ui.txtSLabel.currentText()):
                msgBox.setText("Please enter Second Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if not len(ui.txtOLabel.text()):
                msgBox.setText("Please enter Out Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        try:
            InFL = InFData[ui.txtFLabel.currentText()]
            InSL = InSData[ui.txtSLabel.currentText()]

            InFLUniq = np.unique(InFL)
            InSLUniq = np.unique(InSL)
            if not ui.cbRelabeling.isChecked():
                OutData[ui.txtOLabel.text()] = np.concatenate((InFL, InSL), 1)[0]
                InSLUniqNew = InSLUniq.copy()
            else:

                InSLUniqNew  = InSLUniq + np.max(InFLUniq) + 1

                InSLNew = InSL.copy()
                for lblinx, lbl in enumerate(InSLUniq):
                    InSLNew[np.where(InSL == lbl)] = InSLUniqNew[lblinx]

                OutData[ui.txtOLabel.text()] = np.concatenate((InFL, InSLNew), 1)[0]

        except:
            print("Cannot combine Labels!")
            return

        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtOmLabel.text()):
                msgBox.setText("Please enter Out Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOmLabel.text()] = label_binarize(OutData[ui.txtOLabel.text()],np.unique(OutData[ui.txtOLabel.text()]))



        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtFCond.currentText()):
                msgBox.setText("Please enter First Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSCond.currentText()):
                msgBox.setText("Please enter Second Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOCond.text()):
                msgBox.setText("Please enter Out Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if ui.cbCondUnion.isChecked():
                OutData[ui.txtOCond.text()] = np.concatenate((InFData[ui.txtFCond.currentText()], InSData[ui.txtSCond.currentText()]))
            else:
                NewCond = Conditions()
                InFCond = InFData[ui.txtFCond.currentText()]
                for cond in InFCond:
                    NewCond.add_cond(str.replace(cond[0][0], ui.txtFCondPre.text(), ui.txtOCondPre.text()),cond[1][0])


                InSCond = InSData[ui.txtSCond.currentText()]
                for cond in InSCond:
                    condID = np.int32(str.replace(cond[0][0],ui.txtSCondPre.text() + "_",""))
                    condIDNew = InSLUniqNew[np.where(InSLUniq == condID)][0]
                    NewCond.add_cond(ui.txtOCondPre.text() + "_" + str(condIDNew), cond[1][0])

                OutData[ui.txtOCond.text()] = np.array(NewCond.get_cond(),dtype=object)


        # Subject
        if ui.cbSubject.isChecked():
            if not len(ui.txtFSubject.currentText()):
                msgBox.setText("Please enter First Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSSubject.currentText()):
                msgBox.setText("Please enter Second Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOSubject.text()):
                msgBox.setText("Please enter Out Subject variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOSubject.text()] = np.concatenate((InFData[ui.txtFSubject.currentText()],InSData[ui.txtSSubject.currentText()]),1)[0]
            except:
                print("Cannot combine Subject IDs!")
                return

        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtFTask.currentText()):
                msgBox.setText("Please enter First Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSTask.currentText()):
                msgBox.setText("Please enter Second Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOTask.text()):
                msgBox.setText("Please enter Out Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOTask.text()] = np.concatenate((InFData[ui.txtFTask.currentText()],InSData[ui.txtSTask.currentText()]),1)[0]
            except:
                print("Cannot combine Task IDs!")
                return

        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtFRun.currentText()):
                msgBox.setText("Please enter First Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSRun.currentText()):
                msgBox.setText("Please enter Second Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtORun.text()):
                msgBox.setText("Please enter Out Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtORun.text()] = np.concatenate((InFData[ui.txtFRun.currentText()],InSData[ui.txtSRun.currentText()]),1)[0]
            except:
                print("Cannot combine Run IDs!")
                return

        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtFCounter.currentText()):
                msgBox.setText("Please enter First Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSCounter.currentText()):
                msgBox.setText("Please enter Second Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtOCounter.text()):
                msgBox.setText("Please enter Out Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOCounter.text()] = np.concatenate((InFData[ui.txtFCounter.currentText()],InSData[ui.txtSCounter.currentText()]),1)[0]
            except:
                print("Cannot combine Counter IDs!")
                return

        # Number of Scan
        if ui.cbNScan.isChecked():
            if not len(ui.txtFScan.currentText()):
                msgBox.setText("Please enter First NScan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if ui.cbNScan.isChecked():
            if not len(ui.txtSScan.currentText()):
                msgBox.setText("Please enter Second NScan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if ui.cbNScan.isChecked():
            if not len(ui.txtOScan.text()):
                msgBox.setText("Please enter Out NScan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        try:
            OutData[ui.txtOScan.text()] = np.concatenate((InFData[ui.txtFScan.currentText()], InSData[ui.txtSScan.currentText()]), 1)[0]
        except:
            print("Cannot combine Counter IDs!")
            return

        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtFDM.currentText()):
                msgBox.setText("Please enter First Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtSDM.currentText()):
                msgBox.setText("Please enter Second Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            if not len(ui.txtODM.text()):
                msgBox.setText("Please enter Out Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtODM.text()] = np.concatenate((InFData[ui.txtFDM.currentText()],InSData[ui.txtSDM.currentText()]))
            except:
                print("Cannot combine Design Matrices!")
                return



        print("Saving ...")
        io.savemat(ui.txtOutFile.text(), mdict=OutData)
        print("DONE.")
        msgBox.setText("Datasets are combined.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmCombineData.show(frmCombineData)
    sys.exit(app.exec_())