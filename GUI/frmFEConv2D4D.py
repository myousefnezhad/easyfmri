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
from PyQt6.QtWidgets import *
from GUI.frmFEConv2D4DGUI import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector


class frmFEConv2D4D(Ui_frmFEConv2D4D):
    ui = Ui_frmFEConv2D4D()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFEConv2D4D()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        dialog.setWindowTitle("easy fMRI Convert 2D data to 4D - V" + getVersion() + "B" + getBuild())
        # dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        # dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
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

                    # Data
                    ui.txtData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtData.setCurrentText("data")

                        print("Data shape: ", np.shape(data["data"]))

                        try:
                            if data["dataShape"] != 2:
                                print("WARNING: data shape is not matched!")
                        except:
                            print("WARNING: cannot find dataShape variable! Integration is old version. We will assign it for output, automatically.")

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")


                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtLabel.setCurrentText("label")
                    ui.cbLabel.setChecked(HasDefualt)

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

                    # imgShape
                    ui.txtImgShape.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtImgShape.addItem(key)
                        if key == "imgShape":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtImgShape.setCurrentText("imgShape")


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
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        # InFile
        InFile = ui.txtInFile.text()
        if not len(InFile):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        if not os.path.isfile(InFile):
            msgBox.setText("Input file not found!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        InData = mainIO_load(InFile)
        OutData = dict()
        OutData["dataShape"] = 4
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinate variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coor = InData[ui.txtCol.currentText()]
            OutData[ui.txtOCol.text()] = Coor
        except:
            print("Cannot load Coordinate!")
            return
        # imgShape
        if not len(ui.txtImgShape.currentText()):
            msgBox.setText("Please enter imgShape variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            imgShape = InData[ui.txtImgShape.currentText()]
            OutData[ui.txtOImgShape.text()] = reshape_1Dvector(imgShape)
        except:
            print("Cannot load Coordinate!")
            return
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            X = InData[ui.txtData.currentText()]

            if ui.cbNormalize.isChecked():
                X = preprocessing.scale(X)
                print("Data is scaled X~N(0,1).")
        except:
            print("Cannot load data")
            return
        # Subject
        if ui.cbSubject.isChecked():
            if not len(ui.txtSubject.currentText()):
                msgBox.setText("Please enter Subject variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOSubject.text()] = reshape_1Dvector(InData[ui.txtSubject.currentText()])
        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOTask.text()] = reshape_1Dvector(InData[ui.txtTask.currentText()])
        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtORun.text()] = reshape_1Dvector(InData[ui.txtRun.currentText()])
        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOCounter.text()] = reshape_1Dvector(InData[ui.txtCounter.currentText()])
        # Label
        if ui.cbLabel.isChecked():
            if not len(ui.txtLabel.currentText()):
                    msgBox.setText("Please enter Label variable name!")
                    msgBox.setIcon(QMessageBox.Icon.Critical)
                    msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msgBox.exec()
                    return False
            OutData[ui.txtOLabel.text()] = reshape_1Dvector(InData[ui.txtLabel.currentText()])
        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOmLabel.text()] = InData[ui.txtmLabel.currentText()]
        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtODM.text()] = InData[ui.txtDM.currentText()]
        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtCond.currentText()):
                msgBox.setText("Please enter Condition variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOCond.text()] = InData[ui.txtCond.currentText()]
        # Number of Scan
        if ui.cbNScan.isChecked():
            if not len(ui.txtScan.currentText()):
                msgBox.setText("Please enter Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            OutData[ui.txtOScan.text()] = reshape_1Dvector(InData[ui.txtScan.currentText()])
        # Boxed Data
        if ui.rb4DShape2.isChecked():
            imgShape = np.array([np.max(Coor,axis=1) - np.min(Coor,axis=1) + 1])
            Coor  = np.array([Coor[0] - np.min(Coor,axis=1)[0], Coor[1] - np.min(Coor,axis=1)[1], Coor[2] - np.min(Coor,axis=1)[2]])
            OutData[ui.txtOCol.text() + "_box"] = Coor
        imgShape = imgShape[0]
        timepoints =  np.shape(X)[0]
        Xnew = list()
        for i, xi in enumerate(X):
            xi_new = np.zeros(imgShape)
            for j, (Xi, Xj, Xk) in enumerate(Coor.T):
                xi_new[Xi, Xj, Xk] = xi[j]
            Xnew.append(xi_new)
            if (i + 1) % 100 == 0:
                print("Time point {:8d} of {:8d} is reshaped!".format(i + 1, timepoints))
        print("Time point {:8d} of {:8d} is reshaped!".format(i + 1, timepoints))
        OutData[ui.txtOData.text()] = np.array(Xnew, dtype=np.float32)
        print("Data shape: ", np.shape(Xnew))
        print("Saving ...")
        mainIO_save(OutData, ui.txtOutFile.text())
        print("DONE.")
        msgBox.setText("Data is reshaped.")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFEConv2D4D.show(frmFEConv2D4D)
    sys.exit(app.exec())