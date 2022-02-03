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
import nibabel as nb
import scipy.io as io
from PyQt6.QtWidgets import *
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from GUI.frmMAAtlasEnsembleGUI import *
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, average_precision_score, f1_score, recall_score, confusion_matrix, classification_report


import logging
logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets



def EventCode():
    return\
"""from sklearn.linear_model import LogisticRegression as CLS
# Uncomment this line to use Linear SVC
#from sklearn.svm import LinearSVC as CLS
model = CLS()
"""



def EventCode2():
    return\
"""from sklearn.linear_model import LogisticRegression as eCLS
# Uncomment this line to use Linear SVC
#from sklearn.svm import LinearSVC as eCLS
emodel = eCLS()
"""


class frmMAAtlasEnsemble(Ui_frmMAAtlasEnsemble):
    ui = Ui_frmMAAtlasEnsemble()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMAAtlasEnsemble()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Base
        ui.txtEvents = api.CodeEdit(ui.tab_2)
        ui.txtEvents.setGeometry(QtCore.QRect(10, 10, 790, 420))
        ui.txtEvents.setObjectName("txtEvents")
        ui.txtEvents.backend.start('backend/server.py')
        ui.txtEvents.modes.append(modes.CodeCompletionMode())
        ui.txtEvents.modes.append(modes.CaretLineHighlighterMode())
        ui.txtEvents.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtEvents.document()))
        ui.txtEvents.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtEvents.setFont(font)
        ui.txtEvents.setPlainText(EventCode(),"","")

        # Ensemble
        ui.txtEvents2 = api.CodeEdit(ui.tab_7)
        ui.txtEvents2.setGeometry(QtCore.QRect(10, 10, 790, 420))
        ui.txtEvents2.setObjectName("txtEvents")
        ui.txtEvents2.backend.start('backend/server.py')
        ui.txtEvents2.modes.append(modes.CodeCompletionMode())
        ui.txtEvents2.modes.append(modes.CaretLineHighlighterMode())
        ui.txtEvents2.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtEvents.document()))
        ui.txtEvents2.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
        font2 = QtGui.QFont()
        font2.setBold(True)
        font2.setWeight(75)
        ui.txtEvents2.setFont(font2)
        ui.txtEvents2.setPlainText(EventCode2(),"","")

        # Precision Avg
        ui.cbPrecisionAvg.addItem("weighted","weighted")
        ui.cbPrecisionAvg.addItem("micro","micro")
        ui.cbPrecisionAvg.addItem("macro","macro")
        ui.cbPrecisionAvg.addItem("binary","binary")
        ui.cbPrecisionAvg.addItem("samples","samples")
        ui.cbPrecisionAvg.addItem("None", None)

        # Average of Precistion Avg
        ui.cbAPrecisionAvg.addItem("macro","macro")
        ui.cbAPrecisionAvg.addItem("weighted","weighted")
        ui.cbAPrecisionAvg.addItem("micro","micro")
        ui.cbAPrecisionAvg.addItem("samples","samples")
        ui.cbAPrecisionAvg.addItem("None", None)

        # Recall
        ui.cbRecallAvg.addItem("weighted","weighted")
        ui.cbRecallAvg.addItem("micro","micro")
        ui.cbRecallAvg.addItem("macro","macro")
        ui.cbRecallAvg.addItem("binary","binary")
        ui.cbRecallAvg.addItem("samples","samples")
        ui.cbRecallAvg.addItem("None", None)

        # f1 score
        ui.cbF1Avg.addItem("weighted","weighted")
        ui.cbF1Avg.addItem("micro","micro")
        ui.cbF1Avg.addItem("macro","macro")
        ui.cbF1Avg.addItem("binary","binary")
        ui.cbF1Avg.addItem("samples","samples")
        ui.cbF1Avg.addItem("None", None)

        dialog.setWindowTitle("easy fMRI Atlas-based ensemble analysis: Atlas - V" + getVersion() + "B" + getBuild())
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
        ui.btnAtlas.clicked.connect(self.btnAtlas_click)
        ui.btnShowFilterContent.clicked.connect(self.btnShowFilterContent_click)

    def btnShowFilterContent_click(self):
        msgBox = QMessageBox()
        filename = ui.txtInFile.text()
        if len(filename):
            if os.path.isfile(filename):
                try:
                    InData = mainIO_load(filename)
                    if ui.cbFilterTrID.isChecked():
                        try:
                            # Check Filter ID for training
                            if not len(ui.txtFilterTrID.currentText()):
                                msgBox.setText("Please enter variable name for training filter!")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return False
                            TrF = InData[ui.txtFilterTrID.currentText()][0]
                            fstr = ""
                            fconnect = ""
                            for filter in np.unique(TrF):
                                fstr += fconnect
                                fstr += str(filter)
                                fconnect = ", "
                            print("Training Reference Content:", fstr)
                        except:
                            print("Reference filter for training is wrong!")
                            msgBox.setText("Reference filter for training is wrong!")
                            msgBox.setIcon(QMessageBox.Critical)
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                            return

                    # Ref Filter Test
                    if ui.cbFilterTeID.isChecked():
                        try:
                            # Check Filter ID for testing
                            if not len(ui.txtFilterTeID.currentText()):
                                msgBox.setText("Please enter variable name for testing filter!")
                                msgBox.setIcon(QMessageBox.Critical)
                                msgBox.setStandardButtons(QMessageBox.Ok)
                                msgBox.exec_()
                                return False
                            TeF = InData[ui.txtFilterTeID.currentText()][0]
                            fstr = ""
                            fconnect = ""
                            for filter in np.unique(TeF):
                                fstr += fconnect
                                fstr += str(filter)
                                fconnect = ", "
                            print("Testing  Reference Content:", fstr)
                        except:
                            print("Reference filter for testing is wrong!")
                            msgBox.setText("Reference filter for testing is wrong!")
                            msgBox.setIcon(QMessageBox.Critical)
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            msgBox.exec_()
                            return
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")


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

                    # Train Filter
                    ui.txtFilterTrID.clear()
                    for key in Keys:
                        ui.txtFilterTrID.addItem(key)
                    # Test Filter
                    ui.txtFilterTeID.clear()
                    for key in Keys:
                        ui.txtFilterTeID.addItem(key)


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
                    ui.txtClass.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeLabel.addItem(key)
                        if key == "test_label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeLabel.setCurrentText("test_label")
                        # set number of features
                        Labels = data[ui.txtITrLabel.currentText()]
                        Labels = np.unique(Labels)
                        for lbl in Labels:
                            ui.txtClass.append(str(lbl))

                    # FoldID
                    ui.txtFoldID.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtFoldID.addItem(key)
                        if key == "FoldID":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtFoldID.setCurrentText("FoldID")

                    ui.lbFoldID.setText("ID=" + str(data[ui.txtFoldID.currentText()][0][0]))

                    # Coordinate
                    ui.txtCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCol.setCurrentText("coordinate")

                    # ImgShape
                    ui.txtImg.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtImg.addItem(key)
                        if key == "imgShape":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtImg.setCurrentText("imgShape")
                        try:
                            print(f'Input image shape is {tuple(data["imgShape"][0])}')
                        except:
                            print("Cannot find ImgShape")


                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnAtlas_click(self):
        global ui
        roi_file = LoadFile('Select Atlas image file ...',['ROI image (*.nii.gz)','All files (*.*)'], 'nii.gz',\
                            os.path.dirname(ui.txtAtlas.text()))
        if len(roi_file):
            if os.path.isfile(roi_file):
                ui.txtAtlas.setText(roi_file)

                try:
                    ImgHDR = nb.load(roi_file)
                    ImgDAT = np.asanyarray(ImgHDR.dataobj)
                    Area = np.unique(ImgDAT)
                    Area = Area[np.where(Area != 0)[0]]
                    print(f'Regions are {Area}')
                    print(f'We consider 0 area as black space/rest; Max region ID: {np.max(Area)}, Min region ID: {np.min(Area)}')
                    print(f'Atlas shape is {np.shape(ImgDAT)}')
                except Exception as e:
                    print(f'Cannot load atlas {e}')


            else:
                print("Atlas file not found!")


    def btnOutFile_click(self):
        ofile = SaveFile("Save result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        print("Loading...")

        try:
            FoldFrom = np.int32(ui.txtFoldFrom.text())
            FoldTo   = np.int32(ui.txtFoldTo.text())
        except:
            print("Please check fold parameters!")
            return

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Atlas
        InAtlas = ui.txtAtlas.text()
        if not len(InAtlas):
            msgBox.setText("Please enter atlas file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isfile(InAtlas):
            msgBox.setText("Atlas file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            AtlasHdr = nb.load(InAtlas)
            AtlasImg = np.asanyarray(AtlasHdr.dataobj)
            AtlasShape = np.shape(AtlasImg)
            if np.shape(AtlasShape)[0] != 3:
                msgBox.setText("Atlas must be 3D image")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        except:
            msgBox.setText("Cannot load atlas file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        # Filter
        try:
            Filter = ui.txtFilter.text()
            if not len(Filter):
                Filter = None
            else:
                Filter = Filter.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split()
                Filter = np.int32(Filter)
        except:
            print("Class Filter is wrong!")
            msgBox.setText("Class filter is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return


        MappingVectorRegion = None
        CodeText  = ui.txtEvents.toPlainText()
        eCodeText = ui.txtEvents2.toPlainText()


        Fold  = list()
        accuracy = list()
        precision = list()
        average_precision = list()
        f1score = list()
        recall = list()

        accuracyTr = list()
        precisionTr = list()
        average_precisionTr = list()
        f1scoreTr = list()
        recallTr = list()

        InFileList = list()

        OutData = dict()
        OutData["ModelAnalysis"] = "Atlas-based ensemble"


        for fold in range(FoldFrom, FoldTo + 1):
            print(f"Analyzing Fold: {fold}...")
            # InFile
            InFile = ui.txtInFile.text()
            if not len(InFile):
                msgBox.setText(f"FOLD {fold}: Please enter input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            InFile = InFile.replace("$FOLD$", str(fold))
            InFileList.append(InFile)
            if not os.path.isfile(InFile):
                msgBox.setText(f"FOLD {fold}: Input file not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Load InData
            try:
                InData = mainIO_load(InFile)
            except:
                print(f"FOLD {fold}: Cannot load file: {InFile}")
                return False

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

            try:
                TrX = InData[ui.txtITrData.currentText()]
            except:
                print(f"FOLD {fold}: Cannot load train data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            try:
                TeX = InData[ui.txtITeData.currentText()]
            except:
                print(f"FOLD {fold}: Cannot load test data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False


            try:
                TrL = InData[ui.txtITrLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load label")
                return


            try:
                TeL = InData[ui.txtITeLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load test label")
                return



            # Ref Filter Train
            if ui.cbFilterTrID.isChecked():
                try:
                    # Create content structure for training
                    TrFilterContent = ui.txtFilterTrContent.text()
                    TrFilterContent = TrFilterContent.replace(" ", "")
                    if not len(TrFilterContent):
                        print("Reference filter for training is wrong!")
                        msgBox.setText("Reference filter for training is wrong!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return
                    else:
                        TrFilterContent = TrFilterContent.replace("\'", " ").replace(",", " ").replace("[", "").replace(
                            "]", "").split()
                        TrFilterContent = np.int32(TrFilterContent)
                    # Check Filter ID for training
                    if not len(ui.txtFilterTrID.currentText()):
                        msgBox.setText("Please enter variable name for training filter!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return False
                    TrF = InData[ui.txtFilterTrID.currentText()][0]

                    if np.shape(TrX)[0] != np.shape(TrF)[0] or np.shape(TrL)[0] != np.shape(TrF)[0]:
                        print("Shape of reference for training must be the same as data and label")
                        msgBox.setText("Shape of reference for training must be the same as data and label")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return

                except:
                    print("Reference filter for training is wrong!")
                    msgBox.setText("Reference filter for training is wrong!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                # Remove training set
                try:
                    print("Removing training set based on reference. Data shape: ", np.shape(TrX), "Label shape: ", np.shape(TrL))
                    for content in TrFilterContent:
                        contIndex = np.where(TrF == content)[0]
                        TrL = np.delete(TrL, contIndex, axis=0)
                        TrX = np.delete(TrX, contIndex, axis=0)
                        TrF = np.delete(TrF, contIndex, axis=0)
                        print("  Content", content, "is removed from training set. Data shape: ", np.shape(TrX), "Label shape: ", np.shape(TrL))
                except Exception as e:
                    print("Cannot filter the training set based on Reference")
                    print(str(e))
                    msgBox.setText("Cannot filter the training set based on Reference")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return

            # Ref Filter Test
            if ui.cbFilterTeID.isChecked():
                try:
                    # Create content structure for testing
                    TeFilterContent = ui.txtFilterTeContent.text()
                    TeFilterContent = TeFilterContent.replace(" ", "")
                    if not len(TeFilterContent):
                        print("Reference filter for testing is wrong!")
                        msgBox.setText("Reference filter for testing is wrong!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return
                    else:
                        TeFilterContent = TeFilterContent.replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split()
                        TeFilterContent = np.int32(TeFilterContent)
                    # Check Filter ID for testing
                    if not len(ui.txtFilterTeID.currentText()):
                        msgBox.setText("Please enter variable name for testing filter!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return False
                    TeF = InData[ui.txtFilterTeID.currentText()][0]

                    if np.shape(TeX)[0] != np.shape(TeF)[0] or np.shape(TeL)[0] != np.shape(TeF)[0]:
                        print("Shape of reference for testing must be the same as data and label")
                        msgBox.setText("Shape of reference for testing must be the same as data and label")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return

                except:
                    print("Reference filter for testing is wrong!")
                    msgBox.setText("Reference filter for testing is wrong!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                # Remove testing set
                try:
                    print("Removing testing set based on reference. Data shape: ", np.shape(TeX), "Label shape: ", np.shape(TeL))
                    for content in TeFilterContent:
                        contIndex = np.where(TeF == content)[0]
                        TeL = np.delete(TeL, contIndex, axis=0)
                        TeX = np.delete(TeX, contIndex, axis=0)
                        TeF = np.delete(TeF, contIndex, axis=0)
                        print("  Content", content, "is removed from testing set. Data shape: ", np.shape(TeX), "Label shape: ", np.shape(TeL))
                except Exception as e:
                    print("Cannot filter the testing set based on Reference")
                    print(str(e))
                    msgBox.setText("Cannot filter the testing set based on Reference")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return



            try:
                if Filter is not None:
                    for fil in Filter:
                        # Remove Training Set
                        labelIndx = np.where(TrL == fil)[0]
                        TrL = np.delete(TrL, labelIndx, axis=0)
                        TrX = np.delete(TrX, labelIndx, axis=0)
                        # Remove Testing Set
                        labelIndx = np.where(TeL == fil)[0]
                        TeL = np.delete(TeL, labelIndx, axis=0)
                        TeX = np.delete(TeX, labelIndx, axis=0)
                        print("Class ID = " + str(fil) + " is removed from data.")

                if ui.cbScale.isChecked():
                    TrX = preprocessing.scale(TrX)
                    TeX = preprocessing.scale(TeX)
                    print("Whole of data is scaled Train~N(0,1) and Test~N(0,1).")
            except:
                print("Cannot load data or label")
                return

            # FoldID
            if not len(ui.txtFoldID.currentText()):
                msgBox.setText("Please enter FoldID variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                currFID = InData[ui.txtFoldID.currentText()][0][0]
                Fold.append(currFID)
            except:
                print("Cannot load Fold ID!")
                return


            # Creating Mapping Dictionary for Atlas
            if MappingVectorRegion is None:
                # Coordinate
                if not len(ui.txtCol.currentText()):
                    msgBox.setText("Please enter Condition variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    Coord = np.transpose(InData[ui.txtCol.currentText()])
                except:
                    print("Cannot load coordinate")
                    return
                # imgShape
                if not len(ui.txtImg.currentText()):
                    msgBox.setText("Please enter Image Shape variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    DataShape = tuple(InData[ui.txtImg.currentText()][0])
                except:
                    print("Cannot load data image shape")
                    return

                # Check shape
                if AtlasShape[0] != DataShape[0] or AtlasShape[1] != DataShape[1] or AtlasShape[2] != DataShape[2]:
                    print(f'Atlas and data must have the same shape.\nAtlas: {AtlasShape} vs. Data: {DataShape}')
                    msgBox.setText(f'Atlas and data must have the same shape.\nAtlas: {AtlasShape} vs. Data: {DataShape}')
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

                print("Mapping 2D vector space to 3D region area...")
                MappingVectorRegion = dict()
                for cooIdx, coo in enumerate(Coord):
                    reg = AtlasImg[coo[0], coo[1], coo[2]]
                    if reg == 0:
                        print(f'{tuple(coo)} is belong to black area.')
                    else:
                        try:
                            MappingVectorRegion[str(reg)].append(cooIdx)
                        except:
                            MappingVectorRegion[str(reg)] = list()
                            MappingVectorRegion[str(reg)].append(cooIdx)
                        print(f'{tuple(coo)}:{cooIdx} is belong to region {reg}')



            print(f"FOLD {fold}: analyzing regions...")
            baseTrX = list()
            baseTeX = list()

            for reg in sorted(MappingVectorRegion.keys()):
                RegIndex = MappingVectorRegion[reg]
                SubXtr = TrX[:, RegIndex]
                SubXte = TeX[:, RegIndex]
                try:
                    allvars = dict(locals(), **globals())
                    exec(CodeText, allvars, allvars)
                    model = allvars['model']
                    model.fit(SubXtr, TrL)
                    baseTrX.append(model.predict(SubXtr))
                    TeP = model.predict(SubXte)
                    baseTeX.append(TeP)
                    bacc = accuracy_score(TeL, TeP)
                except Exception as e:
                    print(f'Cannot generate model\n{e}')
                    msgBox.setText(f'Cannot generate model\n{e}')
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                print(f"FOLD {fold}: Linear accuracy for {reg} is {bacc}")


            baseTrX = np.transpose(baseTrX)
            baseTeX = np.transpose(baseTeX)

            try:
                print(f"FOLD {fold}: Creating ensemble model ...")
                allvars = dict(locals(), **globals())
                exec(eCodeText, allvars, allvars)
                emodel = allvars['emodel']
                emodel.fit(baseTrX, TrL)
                PrL = emodel.predict(baseTrX)
                PeL = emodel.predict(baseTeX)
            except Exception as e:
                print(f"Cannot generate the final model\n{e}")
                msgBox.setText(f"Cannot generate the final model\n{e}")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False


            if ui.cbAverage.isChecked():
                acc     = accuracy_score(TeL, PeL)
                accTr   = accuracy_score(TrL, PrL)
                accuracy.append(acc)
                accuracyTr.append(accTr)
                print("FoldID = {:d}, Average            Train {:5.2f} Test {:5.2f}".format(currFID, accTr*100, acc*100))

            if ui.cbPrecision.isChecked():
                pre     = precision_score(TeL, PeL, average=ui.cbPrecisionAvg.currentData())
                preTr   = precision_score(TrL, PrL, average=ui.cbPrecisionAvg.currentData())
                precision.append(pre)
                precisionTr.append(preTr)
                print("FoldID = {:d}, Precision          Train {:5.2f} Test {:5.2f}".format(currFID, preTr*100, pre*100))

            if ui.cbAPrecision.isChecked():
                prA     = average_precision_score(TeL, PeL, average=ui.cbAPrecisionAvg.currentData())
                prATr   = average_precision_score(TrL, PrL, average=ui.cbAPrecisionAvg.currentData())
                average_precision.append(prA)
                average_precisionTr.append(prATr)
                print("FoldID = {:d}, Average Precision: Train {:5.2f} Test {:5.2f}".format(currFID, prATr*100, prA*100))

            if ui.cbRecall.isChecked():
                rec     = recall_score(TeL, PeL, average=ui.cbRecallAvg.currentData())
                recTr   = recall_score(TrL, PrL, average=ui.cbRecallAvg.currentData())
                recall.append(rec)
                recallTr.append(recTr)
                print("FoldID = {:d}, Recall:            Train {:5.2f} Test {:5.2f}".format(currFID, recTr*100, rec*100))

            if ui.cbF1.isChecked():
                f1      = f1_score(TeL, PeL, average=ui.cbF1Avg.currentData())
                f1Tr    = f1_score(TrL, PrL, average=ui.cbF1Avg.currentData())
                f1score.append(f1)
                f1scoreTr.append(f1Tr)
                print("FoldID = {:d}, F1:                Train {:5.2f} Test {:5.2f}".format(currFID, f1Tr*100, f1*100))

            print("FoldID = " + str(currFID) + " is analyzed!")


        if ui.cbAverage.isChecked():
            OutData["FoldAccuracy"] = accuracy
            MeanAcc = np.mean(accuracy)
            OutData["MeanTestAccuracy"] = MeanAcc
            STDAcc  = np.std(accuracy)
            OutData["StdTestAccuracy"] = STDAcc
            MeanAccTr = np.mean(accuracyTr)
            OutData["MeanTrainAccuracy"] = MeanAccTr
            STDAccTr  = np.std(accuracyTr)
            OutData["StdTrainAccuracy"] = STDAccTr
            print("Accuracy:         Train {:5.2f} +/- {:4.2f} Test {:5.2f} +/- {:4.2f}".format(MeanAccTr*100, STDAccTr, MeanAcc*100, STDAcc))

        if ui.cbPrecision.isChecked():
            OutData["ModePrecision"] = ui.cbPrecisionAvg.currentText()
            OutData["FoldPrecision"] = precision
            MeanPre = np.mean(precision)
            OutData["MeanTrainPrecision"] = MeanPre
            STDPre  = np.std(precision)
            OutData["StdTrainPrecision"] = STDPre
            MeanPreTr = np.mean(precisionTr)
            OutData["MeanTestPrecision"] = MeanPreTr
            STDPreTr  = np.std(precisionTr)
            OutData["StdTestPrecision"] = STDPreTr
            print("Precision:        Train {:5.2f} +/- {:4.2f} Test {:5.2f} +/- {:4.2f}".format(MeanPreTr*100, STDPreTr, MeanPre*100, STDPre))

        if ui.cbAPrecision.isChecked():
            OutData["ModeAveragePrecision"] = ui.cbAPrecisionAvg.currentText()
            OutData["FoldAveragePrecision"] = average_precision
            MeanAPre = np.mean(average_precision)
            OutData["MeanTrainAveragePrecision"] = MeanAPre
            STDAPre  = np.std(average_precision)
            OutData["StdTestAveragePrecision"] = STDAPre
            MeanAPreTr = np.mean(average_precisionTr)
            OutData["MeanTrainAveragePrecision"] = MeanAPreTr
            STDAPreTr  = np.std(average_precisionTr)
            OutData["StdTrainAveragePrecision"] = STDAPreTr
            print("AveragePrecision: Train {:5.2f} +/- {:4.2f} Test {:5.2f} +/- {:4.2f}".format(MeanAPreTr*100, STDAPreTr, MeanAPre*100, STDAPre))

        if ui.cbRecall.isChecked():
            OutData["ModeRecall"] = ui.cbRecallAvg.currentText()
            OutData["FoldRecall"] = recall
            MeanRec = np.mean(recall)
            OutData["MeanTestRecall"] = MeanRec
            STDRec  = np.std(recall)
            OutData["StdTestRecall"] = STDRec
            MeanRecTr = np.mean(recallTr)
            OutData["MeanTrainRecall"] = MeanRecTr
            STDRecTr  = np.std(recallTr)
            OutData["StdTrainRecall"] = STDRecTr
            print("Recall:           Train {:5.2f} +/- {:4.2f} Test {:5.2f} +/- {:4.2f}".format(MeanRecTr*100, STDRecTr, MeanRec*100, STDRec))

        if ui.cbF1.isChecked():
            OutData["ModeF1"] = ui.cbF1Avg.currentText()
            OutData["FoldF1"] = f1score
            MeanF1 = np.mean(f1score)
            OutData["MeanTestF1"] = MeanF1
            STDF1  = np.std(f1score)
            OutData["StdTestF1"] = STDF1
            MeanF1Tr = np.mean(f1scoreTr)
            OutData["MeanTrainF1"] = MeanF1Tr
            STDF1Tr  = np.std(f1scoreTr)
            OutData["StdTrainF1"] = STDF1Tr
            print("F1:               Train {:5.2f} +/- {:4.2f} Test {:5.2f} +/- {:4.2f}".format(MeanF1Tr*100, STDF1Tr, MeanF1*100, STDF1))

        OutData["InputFiles"] = InFileList



        print("Saving ...")
        mainIO_save(OutData, ui.txtOutFile.text())
        print("DONE.")
        msgBox.setText("Atlas-based ensemble analysis is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMAAtlasEnsemble.show(frmMAAtlasEnsemble)
    sys.exit(app.exec_())