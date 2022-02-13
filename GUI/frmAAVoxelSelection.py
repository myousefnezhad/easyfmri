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
import time
import numpy as np
import nibabel as nb
from PyQt6.QtWidgets import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmAAVoxelSelectionGUI import *
from GUI.frmAAVoxel import *
from scipy.stats import  pearsonr
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector
# Plot
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


class frmAAVoxelSelection(Ui_frmAAVoxelSelection):
    ui = Ui_frmAAVoxelSelection()
    dialog = None
    data = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        global data
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
        ui.vwSele.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwSele.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        ui.vwAvai.clear()
        ui.vwAvai.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwAvai.setColumnWidth(0, 120)
        ui.vwAvai.setColumnWidth(1, 100)
        ui.vwAvai.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwAvai.setSortingEnabled(True)
        ui.vwAvai.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwAvai.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        data = None

        dialog.setWindowTitle("easy fMRI Voxel-based analysis: Voxel Selection - V" + getVersion() + "B" + getBuild())
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
        ui.btnAnFile.clicked.connect(self.btnAnalysisFile_click)
        ui.btnAcc.clicked.connect(self.btnTSelect_click)
        ui.btnMask.clicked.connect(self.btnASelect_click)
        ui.btnAdd.clicked.connect(self.btnAddItems_click)
        ui.btnRemove.clicked.connect(self.btnRemoveItems_click)
        ui.btnAvaiSA.clicked.connect(self.btnAvaiSA_click)
        ui.btnAvaiDS.clicked.connect(self.btnAvaiDS_click)
        ui.btnSeleSA.clicked.connect(self.btnSeleSA_click)
        ui.btnSeleDS.clicked.connect(self.btnSeleDS_click)
        ui.btnAvaiR.clicked.connect(self.btnAvaiR_click)
        ui.btnSeleR.clicked.connect(self.btnSeleR_click)
        ui.btnAvaiP.clicked.connect(self.btnAvaiP_click)
        ui.btnSeleP.clicked.connect(self.btnSeleP_click)
        ui.btnVBA.clicked.connect(self.btnVBA_click)
        ui.btnVBATemp.clicked.connect(self.btnVBATemp_click)


    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnAvaiSA_click(self):
        ui.vwAvai.selectAll()

    def btnAvaiDS_click(self):
        ui.vwAvai.clearSelection()

    def btnSeleSA_click(self):
        ui.vwSele.selectAll()

    def btnSeleDS_click(self):
        ui.vwSele.clearSelection()

    def btnVBA_click(self):
        try:
            frmAAVoxel.show(frmAAVoxel)
        except Exception as e:
            print(str(e))

    def btnVBATemp_click(self):
        global data
        msgBox = QMessageBox()
        if data is None:
            print("Please load dataset first")
            msgBox.setText("Please load dataset first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coord = np.transpose(data[ui.txtCol.currentText()])
        except:
            print("Cannot load data")
            return
        # Clear Views
        ui.vwSele.clear()
        ui.vwSele.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwSele.setColumnWidth(0, 120)
        ui.vwSele.setColumnWidth(1, 100)
        ui.vwSele.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwSele.setSortingEnabled(True)
        ui.vwSele.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwSele.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        ui.vwAvai.clear()
        ui.vwAvai.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwAvai.setColumnWidth(0, 120)
        ui.vwAvai.setColumnWidth(1, 100)
        ui.vwAvai.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwAvai.setSortingEnabled(True)
        ui.vwAvai.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwAvai.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # Draw
        ui.vwAvai.setRowCount(np.shape(Coord)[0])
        ui.vwAvai.setRowCount(np.shape(Coord)[0])
        for rowId, coo in enumerate(Coord):
            try:
                item = QTableWidgetItem('{:5};{:5};{:5}'.format(coo[0], coo[1], coo[2]))
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                ui.vwAvai.setItem(rowId, 0, item)
                item = QTableWidgetItem('None')
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                ui.vwAvai.setItem(rowId, 1, item)
            except:
                print(f'Item: {rowId} cannot add to the list --- format error')
        print(f"We have added {np.shape(Coord)[0]} items")
        ui.tabWidget.setCurrentIndex(1)



    def btnAvaiP_click(self):
        global data
        msgBox = QMessageBox()
        if ui.vwAvai.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if data is None:
            print("Please load dataset first")
            msgBox.setText("Please load dataset first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwAvai.selectionModel().selectedRows()) < 1:
            print("You have to select at least an item first")
            msgBox.setText("You have to select at least an item first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwAvai.selectionModel().selectedRows()) > 9:
            print("You have to select at most 9 items")
            msgBox.setText("You have to select at most 9 items")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            X = data[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coord = data[ui.txtCol.currentText()]
        except:
            print("Cannot load data")
            return
        # Make dict of Coord indexes
        dCoord = {}
        for cooInd, coo in enumerate(np.transpose(Coord)):
            dCoord[tuple(coo)] = cooInd
        # Finding selected coordinates
        indxList = list()
        for selectID in sorted(ui.vwAvai.selectionModel().selectedRows()):
            try:
                itemString = str(ui.vwAvai.item(selectID.row(), 0).text()).split(";")
                item = (int(itemString[0]), int(itemString[1]), int(itemString[2]))
                indxList.append([dCoord[item], ui.vwAvai.item(selectID.row(), 0).text()])
            except:
                print("Cannot load data")
                return
        plotSize = np.shape(indxList)[0]
        plotSize *= 100
        plotSize += 10
        plt.xlabel("Time Points")
        for rowID, (idx, cooID) in enumerate(indxList):
            x = X[:, idx]
            plt.subplot(plotSize + rowID + 1)
            plt.plot(x, 'b.')
            plt.ylabel(cooID)
            plt.xlabel("Time Points")
        plt.show()



    def btnSeleP_click(self):
        global data
        msgBox = QMessageBox()
        if ui.vwSele.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if data is None:
            print("Please load dataset first")
            msgBox.setText("Please load dataset first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwSele.selectionModel().selectedRows()) < 1:
            print("You have to select at least an item first")
            msgBox.setText("You have to select at least an item first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwSele.selectionModel().selectedRows()) > 9:
            print("You have to select at most 9 items")
            msgBox.setText("You have to select at most 9 items")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            X = data[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coord = data[ui.txtCol.currentText()]
        except:
            print("Cannot load data")
            return
        # Make dict of Coord indexes
        dCoord = {}
        for cooInd, coo in enumerate(np.transpose(Coord)):
            dCoord[tuple(coo)] = cooInd
        # Finding selected coordinates
        indxList = list()
        for selectID in sorted(ui.vwSele.selectionModel().selectedRows()):
            try:
                itemString = str(ui.vwSele.item(selectID.row(), 0).text()).split(";")
                item = (int(itemString[0]), int(itemString[1]), int(itemString[2]))
                indxList.append([dCoord[item], ui.vwSele.item(selectID.row(), 0).text()])
            except:
                print("Cannot load data")
                return
        plotSize = np.shape(indxList)[0]
        plotSize *= 100
        plotSize += 10
        plt.xlabel("Time Points")
        for rowID, (idx, cooID) in enumerate(indxList):
            x = X[:, idx]
            plt.subplot(plotSize + rowID + 1)
            plt.plot(x, 'b.')
            plt.ylabel(cooID)
            plt.xlabel("Time Points")
        plt.show()




    def btnAvaiR_click(self):
        global data
        msgBox = QMessageBox()
        if ui.vwAvai.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if data is None:
            print("Please load dataset first")
            msgBox.setText("Please load dataset first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwAvai.selectionModel().selectedRows()) != 2:
            print("You have to select only 2 rows for correlation analysis")
            msgBox.setText("You have to select only 2 rows for correlation analysis")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        try:
            X = data[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coord = data[ui.txtCol.currentText()]
        except:
            print("Cannot load data")
            return
        # Make dict of Coord indexes
        dCoord = {}
        for cooInd, coo in enumerate(np.transpose(Coord)):
            dCoord[tuple(coo)] = cooInd
        # Finding selected coordinates
        indxList = list()
        for selectID in sorted(ui.vwAvai.selectionModel().selectedRows()):
            try:
                itemString = str(ui.vwAvai.item(selectID.row(), 0).text()).split(";")
                item = (int(itemString[0]), int(itemString[1]), int(itemString[2]))
                indxList.append([dCoord[item], ui.vwAvai.item(selectID.row(), 0).text()])
            except:
                print("Cannot load data")
                return
        # Time Point Values for selected coordinates
        x1 = X[:, indxList[0][0]]
        x2 = X[:, indxList[1][0]]
        R, pValue = pearsonr(x1, x2)
        print(f"Pearson correlation: {R} 2-tailed p-value: {pValue}")
        #TODO: change instance color based on labels
        plt.plot(x1, x2, 'b.')
        plt.xlabel(indxList[0][1])
        plt.ylabel(indxList[1][1])
        plt.show()


    def btnSeleR_click(self):
        global data
        msgBox = QMessageBox()
        if ui.vwSele.rowCount() == 0:
            print("Please load voxel analysis first")
            msgBox.setText("Please load voxel analysis first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if data is None:
            print("Please load dataset first")
            msgBox.setText("Please load dataset first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if len(ui.vwSele.selectionModel().selectedRows()) != 2:
            print("You have to select only 2 rows for correlation analysis")
            msgBox.setText("You have to select only 2 rows for correlation analysis")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        try:
            X = data[ui.txtData.currentText()]
        except:
            print("Cannot load data")
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            Coord = data[ui.txtCol.currentText()]
        except:
            print("Cannot load data")
            return
        # Make dict of Coord indexes
        dCoord = {}
        for cooInd, coo in enumerate(np.transpose(Coord)):
            dCoord[tuple(coo)] = cooInd
        # Finding selected coordinates
        indxList = list()
        for selectID in sorted(ui.vwSele.selectionModel().selectedRows()):
            try:
                itemString = str(ui.vwSele.item(selectID.row(), 0).text()).split(";")
                item = (int(itemString[0]), int(itemString[1]), int(itemString[2]))
                indxList.append([dCoord[item], ui.vwSele.item(selectID.row(), 0).text()])
            except:
                print("Cannot load data")
                return
        # Time Point Values for selected coordinates
        x1 = X[:, indxList[0][0]]
        x2 = X[:, indxList[1][0]]
        R, pValue = pearsonr(x1, x2)
        print(f"Pearson correlation: {R} 2-tailed p-value: {pValue}")
        #TODO: change instance color based on labels
        plt.plot(x1, x2, 'b.')
        plt.xlabel(indxList[0][1])
        plt.ylabel(indxList[1][1])
        plt.show()




    def btnInFile_click(self):
        global data
        data = None
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading...")
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
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtAnFile.text()))
        # Load File
        dat = None
        try:
            dat = mainIO_load(filename)
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
        ui.vwSele.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwSele.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        ui.vwAvai.clear()
        ui.vwAvai.setColumnCount(2)
        ui.vwSele.setRowCount(0)
        ui.vwAvai.setColumnWidth(0, 120)
        ui.vwAvai.setColumnWidth(1, 100)
        ui.vwAvai.setHorizontalHeaderLabels(['Coordinate', 'Accuracy'])
        ui.vwAvai.setSortingEnabled(True)
        ui.vwAvai.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        ui.vwAvai.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # Draw
        ui.vwAvai.setRowCount(np.shape(results)[0])
        ui.vwAvai.setRowCount(np.shape(results)[0])
        for rowId, (coo, acc) in enumerate(results):
            try:
                item = QTableWidgetItem('{:5};{:5};{:5}'.format(coo[0][0], coo[0][1], coo[0][2]))
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                ui.vwAvai.setItem(rowId, 0, item)
                item = QTableWidgetItem('{:8f}'.format(acc[0][0] * 100))
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        try:
            T = np.float(ui.txtAcc.text())
        except:
            print("Accuracy rate must be a number")
            msgBox.setText("Accuracy rate must be a number")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        if T <= 0 or T > 100:
            print("Accuracy rate must be between 0 and 100")
            msgBox.setText("Accuracy rate must be between 0 and 100")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        global data
        data = None
        msgBox = QMessageBox()
        if ui.vwSele.rowCount() == 0:
            print("Please select some voxel first")
            msgBox.setText("Please select some voxel first")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
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
        print("Loading...")
        InData = mainIO_load(InFile)
        OutData = dict()
        OutData["imgShape"] = reshape_1Dvector(InData["imgShape"])
        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Label variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return
        try:
            OutData[ui.txtOLabel.text()] = reshape_1Dvector(InData[ui.txtLabel.currentText()])
        except:
            print("Cannot load Label ID")
            return
        # Subject
        if ui.cbSubject.isChecked():
            if not len(ui.txtSubject.currentText()):
                msgBox.setText("Please enter Subject variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            try:
                OutData[ui.txtOSubject.text()] = reshape_1Dvector(InData[ui.txtSubject.currentText()])
            except:
                print("Cannot load Subject ID")
                return
        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            try:
                OutData[ui.txtOTask.text()] = reshape_1Dvector(InData[ui.txtTask.currentText()])
            except:
                print("Cannot load Task ID")
                return
        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            try:
                OutData[ui.txtORun.text()] = reshape_1Dvector(InData[ui.txtRun.currentText()])
            except:
                print("Cannot load Run ID")
                return
        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            try:
                OutData[ui.txtOCounter.text()] = reshape_1Dvector(InData[ui.txtCounter.currentText()])
            except:
                print("Cannot load Counter ID")
                return
        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
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
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
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
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
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
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            try:
                OutData[ui.txtOScan.text()] = reshape_1Dvector(InData[ui.txtScan.currentText()])
            except:
                print("Cannot load NumScan ID")
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
        except:
            print("Cannot load data")
            return
        # Coordinate
        if not len(ui.txtCol.currentText()):
            msgBox.setText("Please enter Coordinator variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
        mainIO_save(OutData, ui.txtOutFile.text())
        print("DONE.")
        msgBox.setText("Data with new ROI is created.")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmAAVoxelSelection.show(frmAAVoxelSelection)
    sys.exit(app.exec())