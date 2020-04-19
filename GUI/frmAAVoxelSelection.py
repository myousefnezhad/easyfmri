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
import nibabel as nb
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmAAVoxelSelectionGUI import *

class frmAAVoxelSelection(Ui_frmAAVoxelSelection):
    ui = Ui_frmAAVoxelSelection()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmAAVoxelSelection()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Clear Views
        ui.vwSele.clear()
        ui.vwSele.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwSele.setColumnWidth(0, 120)
        ui.vwSele.setColumnWidth(1, 100)
        ui.vwSele.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwSele.setSortingEnabled(True)
        ui.vwSele.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        ui.vwSele.setSelectionBehavior(QAbstractItemView.SelectRows)

        ui.vwAvai.clear()
        ui.vwAvai.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwAvai.setColumnWidth(0, 120)
        ui.vwAvai.setColumnWidth(1, 100)
        ui.vwAvai.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwAvai.setSortingEnabled(True)
        ui.vwAvai.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        ui.vwAvai.setSelectionBehavior(QAbstractItemView.SelectRows)


        dialog.setWindowTitle("easy fMRI Voxel-based analysis: Voxel Selection - V" + getVersion() + "B" + getBuild())
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
        ui.btnAnFile.clicked.connect(self.btnAnalysisFile_click)
        ui.btnAcc.clicked.connect(self.btnTSelect_click)
        ui.btnMask.clicked.connect(self.btnASelect_click)
        ui.btnAdd.clicked.connect(self.btnAddItems_click)
        ui.btnRemove.clicked.connect(self.btnRemoveItems_click)


    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnInFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))

        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading...")
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
                    ui.tabWidget.setCurrentIndex(0)
                    print("DONE!")
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")




    def btnAnalysisFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtAnFile.text()))
        # Load File
        dat = None
        try:
            dat = io.loadmat(filename)
        except:
            print("Cannot load Analysis file!")
            return
        # Load Result
        results = None
        try:
            results = dat["results"]
        except:
            print("Cannot find results field --- i.e., 2D matrix including coordinates and accuracy")
            return
        # Clear Views
        ui.vwSele.clear()
        ui.vwSele.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwSele.setColumnWidth(0, 120)
        ui.vwSele.setColumnWidth(1, 100)
        ui.vwSele.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwSele.setSortingEnabled(True)
        ui.vwSele.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        ui.vwSele.setSelectionBehavior(QAbstractItemView.SelectRows)
        ui.vwAvai.clear()
        ui.vwAvai.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwAvai.setColumnWidth(0, 120)
        ui.vwAvai.setColumnWidth(1, 100)
        ui.vwAvai.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwAvai.setSortingEnabled(True)
        ui.vwAvai.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        ui.vwAvai.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Draw
        ui.vwAvai.setRowCount(np.shape(results)[0])
        ui.vwAvai.setRowCount(np.shape(results)[0])
        for rowId, (coo, acc) in enumerate(results):
            try:
                item = QTableWidgetItem('{:5};{:5};{:5}'.format(coo[0, 0], coo[0, 1], coo[0, 2]))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                ui.vwAvai.setItem(rowId, 0, item)
                item = QTableWidgetItem('{:8f}'.format(acc[0][0] * 100))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                ui.vwAvai.setItem(rowId, 1, item)


            except:
                print(f'Item: {rowId} cannot add to the list --- format error')
        print(f"We have added {np.shape(results)[0]} items")
        ui.txtAnFile.setText(filename)
        ui.tabWidget.setCurrentIndex(1)





    def btnAddItems_click(self):
        msgBox = QMessageBox()
        if ui.vwAvai.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        rowList = list()
        for selectID in sorted(ui.vwAvai.selectionModel().selectedRows()):
            rowList.append(selectID.row())
            newItemID = ui.vwSele.rowCount()
            ui.vwSele.setRowCount(ui.vwSele.rowCount() + 1)
            ui.vwSele.setItem(newItemID, 0, QTableWidgetItem(ui.vwAvai.item(selectID.row(), 0).text()))
            ui.vwSele.setItem(newItemID, 1, QTableWidgetItem(ui.vwAvai.item(selectID.row(), 1).text()))
        for rowID in sorted(rowList, reverse=True):
            ui.vwAvai.removeRow(rowID)
        print(f'{np.shape(rowList)[0]} voxels are selected.')





    def btnRemoveItems_click(self):
        msgBox = QMessageBox()
        if ui.vwSele.rowCount() == 0:
            print("Please select some voxel first")
            msgBox.setText("Please select some voxel first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        rowList = list()
        for selectID in sorted(ui.vwSele.selectionModel().selectedRows()):
            rowList.append(selectID.row())
            newItemID = ui.vwAvai.rowCount()
            ui.vwAvai.setRowCount(ui.vwAvai.rowCount() + 1)
            ui.vwAvai.setItem(newItemID, 0, QTableWidgetItem(ui.vwSele.item(selectID.row(), 0).text()))
            ui.vwAvai.setItem(newItemID, 1, QTableWidgetItem(ui.vwSele.item(selectID.row(), 1).text()))
        for rowID in sorted(rowList, reverse=True):
            ui.vwSele.removeRow(rowID)
        print(f'{np.shape(rowList)[0]} voxels are removed.')





    def btnASelect_click(self):
        msgBox = QMessageBox()
        if ui.vwAvai.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        roi_file = LoadFile('Select Atlas image file ...',['ROI image (*.nii.gz)','All files (*.*)'], 'nii.gz', "")
        if not len(roi_file) or not os.path.isfile(roi_file):
            print("Cannot load image file!")
            return
        try:
            atlas_hdr = nb.load(roi_file)
            atlas = atlas_hdr.get_data()
        except:
            print("Cannot load image file!")
            msgBox.setText("Cannot load image file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        rowList = list()
        for rowID in range(ui.vwAvai.rowCount()):
            try:
                cooString = str(ui.vwAvai.item(rowID, 0).text()).split(";")
                cooX = int(cooString[0])
                cooY = int(cooString[1])
                cooZ = int(cooString[2])
                if atlas[cooX, cooY, cooZ] != 0:
                    rowList.append(rowID)
                    newItemID = ui.vwSele.rowCount()
                    ui.vwSele.setRowCount(ui.vwSele.rowCount() + 1)
                    ui.vwSele.setItem(newItemID, 0, QTableWidgetItem(ui.vwAvai.item(rowID, 0).text()))
                    ui.vwSele.setItem(newItemID, 1, QTableWidgetItem(ui.vwAvai.item(rowID, 1).text()))
            except:
                print(f"Cannot locate {cooX}, {cooY}, {cooZ} in atlas file!\nIt seems that the size of atlas and data are not matched!")

        for rowID in sorted(rowList, reverse=True):
            ui.vwAvai.removeRow(rowID)
        print(f'{np.shape(rowList)[0]} voxels are selected.')
        print(f'Atlas file: {roi_file}')







    def btnTSelect_click(self):
        msgBox = QMessageBox()
        if ui.vwAvai.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        try:
            T = np.float(ui.txtAcc.text())
        except:
            print("Accuracy rate must be a number")
            msgBox.setText("Accuracy rate must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if T <= 0 or T > 100:
            print("Accuracy rate must be between 0 and 100")
            msgBox.setText("Accuracy rate must be between 0 and 100")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        rowList = list()
        for rowID in range(ui.vwAvai.rowCount()):
            if float(ui.vwAvai.item(rowID, 1).text()) >= T:
                rowList.append(rowID)
                newItemID = ui.vwSele.rowCount()
                ui.vwSele.setRowCount(ui.vwSele.rowCount() + 1)
                ui.vwSele.setItem(newItemID, 0, QTableWidgetItem(ui.vwAvai.item(rowID, 0).text()))
                ui.vwSele.setItem(newItemID, 1, QTableWidgetItem(ui.vwAvai.item(rowID, 1).text()))
        for rowID in sorted(rowList, reverse=True):
            ui.vwAvai.removeRow(rowID)
        print(f'{np.shape(rowList)[0]} is selected.')


    def btnOutFile_click(self):
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        if ui.vwSele.rowCount() == 0:
            print("Please select some voxel first")
            msgBox.setText("Please select some voxel first")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        # OutFile
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
        print("Loading...")
        InData = io.loadmat(InFile)
        OutData = dict()
        OutData["imgShape"] = InData["imgShape"]

        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
        try:
            OutData[ui.txtOLabel.text()] = InData[ui.txtLabel.currentText()]
        except:
            print("Cannot load Label ID")
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
                OutData[ui.txtOSubject.text()] = InData[ui.txtSubject.currentText()]
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
                OutData[ui.txtOTask.text()] = InData[ui.txtTask.currentText()]
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
                OutData[ui.txtORun.text()] = InData[ui.txtRun.currentText()]
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
                OutData[ui.txtOCounter.text()] = InData[ui.txtCounter.currentText()]
            except:
                print("Cannot load Counter ID")
                return
        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOmLabel.text()] = InData[ui.txtmLabel.currentText()]
            except:
                print("Cannot load Matrix Label ID")
                return
        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtODM.text()] = InData[ui.txtDM.currentText()]
            except:
                print("Cannot load Design ID")
                return
        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtCond.currentText()):
                msgBox.setText("Please enter Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOCond.text()] = InData[ui.txtCond.currentText()]
            except:
                print("Cannot load Condition ID")
                return
        # Number of Scan
        if ui.cbNScan.isChecked():
            if not len(ui.txtScan.currentText()):
                msgBox.setText("Please enter Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                OutData[ui.txtOScan.text()] = InData[ui.txtScan.currentText()]
            except:
                print("Cannot load NumScan ID")
                return
        # Data
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
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Coord = InData[ui.txtCol.currentText()]
        except:
            print("Cannot load data")
            return

        # Make dict of Coord indexes
        dCoord = {}
        for cooInd, coo in enumerate(np.transpose(Coord)):
            dCoord[tuple(coo)] = cooInd
        # Find selected indexes
        VoxelID = list()
        NewCoord = list()
        for rowID in range(ui.vwSele.rowCount()):
            itemString = str(ui.vwSele.item(rowID, 0).text()).split(";")
            item = (int(itemString[0]), int(itemString[1]), int(itemString[2]))
            try:
                VoxelID.append(dCoord[item])
                NewCoord.append(item)
            except:
                print(f"WARNING: Cannot find selected coordinate: {item}")
        OutData[ui.txtOCol.text()] = np.transpose(NewCoord)
        OutData[ui.txtOData.text()] = X[:, VoxelID]
        print("Saving ...")
        io.savemat(ui.txtOutFile.text(), mdict=OutData)
        print("DONE.")
        msgBox.setText("Data with new ROI is created.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmAAVoxelSelection.show(frmAAVoxelSelection)
    sys.exit(app.exec_())