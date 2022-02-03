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
import logging
import numpy as np
import nibabel as nb
from PyQt6.QtWidgets import *
from GUI.frmAAAtlasGUI import *
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from sklearn.linear_model import LogisticRegression
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, roc_auc_score, f1_score, confusion_matrix
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



class frmAAAtlas(Ui_frmAAAtlas):
    ui = Ui_frmAAAtlas()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmAAAtlas()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        ui.txtEvents = api.CodeEdit(ui.tab_2)
        ui.txtEvents.setGeometry(QtCore.QRect(10, 10, 641, 200))
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



        dialog.setWindowTitle("easy fMRI Atlas based analysis - V" + getVersion() + "B" + getBuild())
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
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = 1
                        if key == "train_data":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtData.setCurrentText("data")
                    if HasDefualt == 2:
                        ui.txtData.setCurrentText("train_data")

                    # Test Data
                    ui.txtTeData.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtTeData.addItem(key)
                        if key == "data":
                            HasDefualt = 1
                        if key == "test_data":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtTeData.setCurrentText("data")
                    if HasDefualt == 2:
                        ui.txtTeData.setCurrentText("test_data")



                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = 1
                        if key == "train_label":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtLabel.setCurrentText("label")
                    if HasDefualt == 2:
                        ui.txtLabel.setCurrentText("train_label")

                    # Test Label
                    ui.txtTeLabel.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtTeLabel.addItem(key)
                        if key == "label":
                            HasDefualt = 1
                        if key == "test_label":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtTeLabel.setCurrentText("label")
                    if HasDefualt == 2:
                        ui.txtTeLabel.setCurrentText("test_label")

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
                    #ImgDAT = ImgHDR.get_data()
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
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
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
            #AtlasImg = AtlasHdr.get_data()
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
        OutData = dict()
        MappingVectorRegion = None
        CodeText = ui.txtEvents.toPlainText()
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

            # Train data
            if not len(ui.txtData.currentText()):
                msgBox.setText(f"FOLD {fold}: Please enter train data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                Xtr = InData[ui.txtData.currentText()]
                if ui.cbScale.isChecked():
                    Xtr = preprocessing.scale(Xtr)
                    print(f"FOLD {fold}: Whole of train data is scaled X~N(0,1).")
            except:
                print(f"FOLD {fold}: Cannot load train data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            # Test data
            if not len(ui.txtTeData.currentText()):
                msgBox.setText(f"FOLD {fold}: Please enter test data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                Xte = InData[ui.txtTeData.currentText()]
                if ui.cbScale.isChecked():
                    Xte = preprocessing.scale(Xte)
                    print(f"FOLD {fold}: Whole of test data is scaled X~N(0,1).")
            except:
                print(f"FOLD {fold}: Cannot load test data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            # Train Label
            if not len(ui.txtLabel.currentText()):
                    msgBox.setText(f"FOLD {fold}: Please enter Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            try:
                Ytr = InData[ui.txtLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load label")
                return

            # Test Label
            if not len(ui.txtTeLabel.currentText()):
                    msgBox.setText(f"FOLD {fold}: Please enter test Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            try:
                Yte = InData[ui.txtTeLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load test label")
                return

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
            for reg in sorted(MappingVectorRegion.keys()):
                RegIndex = MappingVectorRegion[reg]
                SubXtr = Xtr[:, RegIndex]
                SubXte = Xte[:, RegIndex]

                try:
                    allvars = dict(locals(), **globals())
                    exec(CodeText, allvars, allvars)
                    model = allvars['model']
                    model.fit(SubXtr, Ytr)
                    Pte = model.predict(SubXte)
                    acc = accuracy_score(Yte, Pte)
                    clr = classification_report(Yte, Pte)
                    cfm = confusion_matrix(Yte, Pte)
                    pre = precision_score(Yte, Pte)
                    f1  = f1_score(Yte, Pte)
                    rca = recall_score(Yte, Pte)
                except Exception as e:
                    print(f'Cannot generate model\n{e}')
                    msgBox.setText(f'Cannot generate model\n{e}')
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

                try:
                    OutData[f"Region_{reg}_accuracy_score"].append(acc)
                    OutData[f"Region_{reg}_count"] += 1
                    OutData[f"Region_{reg}_classification_report"].append(clr)
                    OutData[f"Region_{reg}_precision_score"].append(pre)
                    OutData[f"Region_{reg}_f1_score"].append(f1)
                    OutData[f"Region_{reg}_recall_score"].append(rca)
                    OutData[f"Region_{reg}_confusion_matrix"].append(cfm)
                except:
                    OutData[f"Region_{reg}_count"]  = 1
                    OutData[f"Region_{reg}_accuracy_score"] = list()
                    OutData[f"Region_{reg}_accuracy_score"].append(acc)
                    OutData[f"Region_{reg}_classification_report"] = list()
                    OutData[f"Region_{reg}_classification_report"].append(clr)
                    OutData[f"Region_{reg}_precision_score"] = list()
                    OutData[f"Region_{reg}_precision_score"].append(pre)
                    OutData[f"Region_{reg}_f1_score"] = list()
                    OutData[f"Region_{reg}_f1_score"].append(f1)
                    OutData[f"Region_{reg}_recall_score"] = list()
                    OutData[f"Region_{reg}_recall_score"].append(rca)
                    OutData[f"Region_{reg}_confusion_matrix"] = list()
                    OutData[f"Region_{reg}_confusion_matrix"].append(cfm)

                print(f"FOLD {fold}: Linear accuracy for {reg} is {acc}")

        for reg in sorted(MappingVectorRegion.keys()):
            macc = np.mean(OutData[f"Region_{reg}_accuracy_score"])
            mpre = np.mean(OutData[f"Region_{reg}_precision_score"])
            mf1  = np.mean(OutData[f"Region_{reg}_f1_score"])
            mrca = np.mean(OutData[f"Region_{reg}_recall_score"])
            mcfm = None
            for ecmf in OutData[f"Region_{reg}_confusion_matrix"]:
                mcfm = ecmf if mcfm is None else mcfm + ecmf
            mcfm = mcfm / OutData[f"Region_{reg}_count"]
            OutData[f"Region_{reg}_mean_accuracy"]  = macc
            OutData[f"Region_{reg}_mean_precision"] = mpre
            OutData[f"Region_{reg}_mean_recall"]    = mrca
            OutData[f"Region_{reg}_mean_f1"]        = mf1
            OutData[f"Region_{reg}_mean_confusion_matrix"] = mcfm
            print(f"Mean accuracy of region {reg}: {macc}")

        print("Saving ...")
        mainIO_save(OutData, ui.txtOutFile.text())
        print("DONE.")
        msgBox.setText("Wise area analysis: Atlas is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmAAAtlas.show(frmAAAtlas)
    sys.exit(app.exec_())