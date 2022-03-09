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
import logging
import matplotlib
import numpy as np
import nibabel as nb
from nilearn import plotting
from PyQt6.QtWidgets import *
from sklearn import preprocessing
from GUI.frmMAClassicNetworkGUI import *
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save
from Base.Conditions import reshape_condition_cell
from Visualization.Connectome import PlotConnectome
from Network.DistanceNetwork import ClassicNetworkAnalysis

# Plot
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from Base.codeEditor import codeEditor


def MetricCode():
    return\
"""# This function returns distance between vectors 'a' and 'b'
# By default, it is the Pearson correlation

import scipy.stats as stats
import numpy as np 

def metric(a, b):
    return np.abs(stats.pearsonr(a, b)[0]) 
"""

def IntegrationCode():
    return\
"""# This function generates a vector from matrix 'a'
# By default, it calculate row mean of the matrix 'a'

import numpy as np

def integration(a): 
    #return np.min(a, axis=1)
    #return np.max(a, axis=1)
    return np.mean(a, axis=1)
"""


class frmMAClassicNetwork(Ui_frmMAClassicNetwork):
    ui = Ui_frmMAClassicNetwork()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMAClassicNetwork()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Metric
        cEditor2 = codeEditor(ui)
        ui.txtMetric = cEditor2.Obj
        cEditor2.setObjectName("txtMetric")
        cEditor2.setText(MetricCode())
        layout2 = QHBoxLayout(ui.Code2)
        layout2.addWidget(cEditor2.Obj)

        # Integration
        cEditor = codeEditor(ui)
        ui.txtIntegration = cEditor.Obj
        cEditor.setObjectName("txtIntegration")
        cEditor.setText(IntegrationCode())
        layout = QHBoxLayout(ui.Code)
        layout.addWidget(cEditor.Obj)

        dialog.setWindowTitle("easy fMRI Classic Network Analysis - V" + getVersion() + "B" + getBuild())
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
        ui.btnAtlasFile.clicked.connect(self.btnAtlasFile_click)

        ui.btnRedraw.clicked.connect(self.btnRedraw_click)


    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnAtlasFile_click(self):
        global ui
        roi_file = LoadFile('Select Atlas image file ...',['ROI image (*.nii.gz)','All files (*.*)'], 'nii.gz',\
                            os.path.dirname(ui.txtAtlasFile.text()))
        if len(roi_file):
            if os.path.isfile(roi_file):
                ui.txtAtlasFile.setText(roi_file)

                try:
                    ImgHDR = nb.load(roi_file)
                    ImgDAT = np.asanyarray(ImgHDR.dataobj)
                    Area = np.unique(ImgDAT)
                    ui.lblRegion.setText(f"Number of regions: {len(Area)}")
                    for a in Area:
                        ui.txtRegionList.append(str(a))
                    Area = Area[np.where(Area != 0)[0]]
                    print(f'Regions are {Area}')
                    print(f'We consider 0 area as black space/rest; Max region ID: {np.max(Area)}, Min region ID: {np.min(Area)}')
                    print(f'Atlas shape is {np.shape(ImgDAT)}')
                except Exception as e:
                    print(f'Cannot load atlas {e}')


            else:
                print("Atlas file not found!")


    def btnInFile_click(self):
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading ...")
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
                        print("Labels:")
                        print(Labels)
                        ui.txtClass.clear()
                        for lbl in Labels:
                            ui.txtClass.append(str(lbl))

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")

                    # Coordinate
                    ui.txtCoord.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCoord.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCoord.setCurrentText("coordinate")

                    ui.lblImgShape.setText("imgShape: " + str(data["imgShape"][0]))

                    ui.txtInFile.setText(filename)
                    print("DONE.")

                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        ofile = SaveFile("Save result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)


    def btnConvert_click(self):
        msgBox = QMessageBox()
        tStart = time.time()
        try:
            Threshold = np.float(ui.txtThre.text())
            assert Threshold <= 1
            assert Threshold >= 0
        except:
            msgBox.setText("Threshold is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            EdgeThreshold = np.float(ui.txtEdgeThre.text())
            assert EdgeThreshold <= 1
            assert EdgeThreshold >= 0
        except:
            msgBox.setText("Edge threshold is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        try:
            MetricCode  = ui.txtMetric.toPlainText()
            allvars = dict(locals(), **globals())
            exec(MetricCode, allvars, allvars)
            Metric = allvars['metric']
        except Exception as e:
            msgBox.setText("Metric is wrong!\n" + str(e))
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        try:
            IntegrationCode  = ui.txtIntegration.toPlainText()
            allvars = dict(locals(), **globals())
            exec(IntegrationCode, allvars, allvars)
            Integration = allvars['integration']
        except Exception as e:
            msgBox.setText("Integration is wrong!\n" + str(e))
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        AtlasPath = ui.txtAtlasPath.text()

        # Filter
        try:
            Filter = ui.txtFilter.text()
            if not len(Filter):
                Filter = None
            else:
                Filter = Filter.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split()
                Filter = np.int32(Filter)
        except:
            print("Filter is wrong!")
            return

        # Region Filter
        try:
            RegionFilter = ui.txtRegions.text()
            if not len(RegionFilter):
                RegionFilter = []
            else:
                RegionFilter = RegionFilter.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split()
                RegionFilter = np.int32(RegionFilter)
        except:
            print("Region filter is wrong!")
            return

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        OutData = dict()

        # AtlasFile
        AtlasFile = ui.txtAtlasFile.text()
        if not len(AtlasFile):
            msgBox.setText("Please enter atlas file!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        if not os.path.isfile(AtlasFile):
            msgBox.setText("Atlas file not found!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        try:
            AtlasHDR    = nb.load(AtlasFile)
            AtlasImg    = np.asanyarray(AtlasHDR.dataobj)
            AtlasReg    = np.unique(AtlasImg)

            if not 0 in RegionFilter:
                AtlasReg    = AtlasReg[np.where(AtlasReg != 0)[0]]
                print("Region 0 is considered as rest mode!")
            AtlasShape = np.shape(AtlasImg)
        except:
            msgBox.setText("Cannot load atlas file!")
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

        try:
            print("Loading ...")
            InData = mainIO_load(InFile)
            imgShape = InData["imgShape"][0]
        except:
            print("Cannot load data!")
            return

        try:
            assert imgShape[0] == AtlasShape[0]
            assert imgShape[1] == AtlasShape[1]
            assert imgShape[2] == AtlasShape[2]
        except:
            msgBox.setText("Input file (" + str(imgShape).replace("]", "").replace("[", "") + ") and Atlas file " + str(AtlasShape).replace(",", "") + " must have the same shape!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Input Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Train Label variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False

        # Condition
        try:
            if not len(ui.txtCond.currentText()):
                Cond = 0
            else:
                Cond = InData[ui.txtCond.currentText()]
                OutData[ui.txtCond.currentText()] = Cond
                labels = list()
                for con in Cond:
                    labels.append(reshape_condition_cell(con[1]))
                labels = np.array(labels)
        except:
            msgBox.setText("Condition value is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        try:
            X = InData[ui.txtData.currentText()]
            L = InData[ui.txtLabel.currentText()][0]
            if ui.cbScale.isChecked():
                X = preprocessing.scale(X)
                print("Whole of data is scaled X~N(0,1).")
        except:
            print("Cannot load data or label")
            return

        try:
            if len(ui.txtCoord.currentText()):
                Coord = np.transpose(InData[ui.txtCoord.currentText()])
            else:
                Coord = None
        except:
            msgBox.setText("Coordinate variable is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False


        if Filter is not None:
            for fil in Filter:
                # Remove Training Set
                labelIndx = np.where(L == fil)[0]
                X = np.delete(X, labelIndx, axis=0)
                L = np.delete(L, labelIndx, axis=0)
                print("Class ID = " + str(fil) + " is removed from data.")

        Net, ThrNet, ActiveRegions, A, ACoord, listL = ClassicNetworkAnalysis(X=X, L=L, Coord=Coord,
                                                                       Integration=Integration,
                                                                       Metric=Metric,
                                                                       AtlasImg=AtlasImg,
                                                                       affine=AtlasHDR.affine,
                                                                       KeepRegions=RegionFilter,
                                                                       AtlasPath=AtlasPath,
                                                                       Threshold=Threshold)
        Out = {}
        Out["Networks"] = Net
        Out["ThresholdNetworks"] = ThrNet
        Out["ActiveRegions"] = ActiveRegions
        Out["Atlas"] = A
        Out["Atlas_parcellation"] = ACoord
        Out["Atlas_affine"] =  AtlasHDR.affine
        Out["condition"] = Cond
        Out["labels"] = listL
        Out["RunTime"] = time.time() - tStart
        print("Runtime (s): %f" % (Out["RunTime"]))
        print("Saving results ...")
        mainIO_save(Out, OutFile)
        print("Output is saved.")
        if ui.cbDiagram.isChecked():
            for nnIndex, (nn, tnn) in enumerate(zip(Net, ThrNet)):
                try:
                    Title = f"Label: {reshape_condition_cell(Cond[nnIndex][1])}"
                except:
                    Title = f"Label: {nnIndex}"
                PlotConnectome(tnn, ACoord, Title, EdgeThreshold)
                fig = plt.figure()
                plt.imshow(np.transpose(nn))
                plt.title(Title)
            plt.show()
        print("DONE.")
        msgBox.setText("Network analysis is done.")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()





    def btnRedraw_click(self):
        msgBox = QMessageBox()
        try:
            EdgeThreshold = np.float(ui.txtEdgeThre.text())
            assert EdgeThreshold <= 1
            assert EdgeThreshold >= 0
        except:
            msgBox.setText("Edge threshold is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False
        ofile = LoadFile("Load result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
                         os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            Out = {}
            try:
                Out = mainIO_load(ofile)
            except:
                print("Cannot load result file!")
                msgBox.setText("Cannot load result file!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False
            Net = Out["Networks"]
            ThrNet = Out["ThresholdNetworks"]
            ACoord = Out["Atlas_parcellation"]
            for nnIndex, (nn, tnn) in enumerate(zip(Net, ThrNet)):
                try:
                    Cond = Out["condition"]
                    Title = f"Label: {reshape_condition_cell(Cond[nnIndex][1])}"
                except:
                    Title = f"Label: {nnIndex}"
                PlotConnectome(tnn, ACoord, Title, EdgeThreshold)
                fig = plt.figure()
                plt.imshow(np.transpose(nn))
                plt.title(Title)
            plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMAClassicNetwork.show(frmMAClassicNetwork)
    sys.exit(app.exec())