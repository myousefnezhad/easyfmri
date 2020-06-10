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
from sklearn.metrics import mean_squared_error
import sklearn.linear_model as linmdl
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild, SimilarityMatrixBetweenClass
from GUI.frmMANetworkGUI import *

# Plot
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

import logging
logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets


def MetricCode():
    return\
"""import scipy.stats as stats 

metric = stats.pearsonr 
"""

def IntegrationCode():
    return\
"""import numpy as np

#integration = np.max
#integration = np.min
integration = np.mean
"""


class frmMANetwork(Ui_frmMANetwork):
    ui = Ui_frmMANetwork()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMANetwork()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        # Metric
        ui.txtMetric = api.CodeEdit(ui.tab_5)
        ui.txtMetric.setGeometry(QtCore.QRect(10, 10, 700, 350))
        ui.txtMetric.setObjectName("txtEvents")
        ui.txtMetric.backend.start('backend/server.py')
        ui.txtMetric.modes.append(modes.CodeCompletionMode())
        ui.txtMetric.modes.append(modes.CaretLineHighlighterMode())
        ui.txtMetric.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtMetric.document()))
        ui.txtMetric.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtMetric.setFont(font)
        ui.txtMetric.setPlainText(MetricCode(),"","")

        # Integration
        ui.txtIntegration = api.CodeEdit(ui.tab_3)
        ui.txtIntegration.setGeometry(QtCore.QRect(10, 10, 700, 350))
        ui.txtIntegration.setObjectName("txtEvents")
        ui.txtIntegration.backend.start('backend/server.py')
        ui.txtIntegration.modes.append(modes.CodeCompletionMode())
        ui.txtIntegration.modes.append(modes.CaretLineHighlighterMode())
        ui.txtIntegration.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtIntegration.document()))
        ui.txtIntegration.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtIntegration.setFont(font)
        ui.txtIntegration.setPlainText(IntegrationCode(),"","")










        dialog.setWindowTitle("easy fMRI Network Analysis - V" + getVersion() + "B" + getBuild())
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
                    ImgDAT = ImgHDR.get_data()
                    Area = np.unique(ImgDAT)
                    Area = Area[np.where(Area != 0)[0]]
                    print(f'Regions are {Area}')
                    print(f'We consider 0 area as black space/rest; Max region ID: {np.max(Area)}, Min region ID: {np.min(Area)}')
                    print(f'Atlas shape is {np.shape(ImgDAT)}')
                except Exception as e:
                    print(f'Cannot load atlas {e}')


            else:
                print("Atlas file not found!")


    def btnInFile_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Loading ...")
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
        ofile = SaveFile("Save result file ...",['Result files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)


    def btnConvert_click(self):
        msgBox = QMessageBox()
        tStart = time.time()

        try:
            Threshold = np.float(ui.txtThre.text())
        except:
            msgBox.setText("Threshold is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            MetricCode  = ui.txtMetric.toPlainText()
            allvars = dict(locals(), **globals())
            exec(MetricCode, allvars, allvars)
            Metric = allvars['metric']
        except Exception as e:
            msgBox.setText("Metric is wrong!\n" + str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            IntegrationCode  = ui.txtIntegration.toPlainText()
            allvars = dict(locals(), **globals())
            exec(IntegrationCode, allvars, allvars)
            Integration = allvars['integration']
        except Exception as e:
            msgBox.setText("Integration is wrong!\n" + str(e))
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
            print("Filter is wrong!")
            return

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        OutData = dict()

        # AtlasFile
        AtlasFile = ui.txtAtlasFile.text()
        if not len(AtlasFile):
            msgBox.setText("Please enter atlas file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isfile(AtlasFile):
            msgBox.setText("Atlas file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            AtlasHDR    = nb.load(AtlasFile)
            AtlasImg    = AtlasHDR.get_data() # numpy.asanyarray(img.dataobj)
            AtlasReg    = np.unique(AtlasImg)
            AtlasReg    = AtlasReg[np.where(AtlasReg != 0)[0]]
            AtlasShape  = np.shape(AtlasImg)
        except:
            msgBox.setText("Cannot load atlas file!")
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
            print("Loading ...")
            InData = io.loadmat(InFile)
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
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Input Data variable name!")
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

        # Condition
        if not len(ui.txtCond.currentText()):
            msgBox.setText("Please enter Condition variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Cond = InData[ui.txtCond.currentText()]
            OutData[ui.txtCond.currentText()] = Cond
            labels = list()
            for con in Cond:
                labels.append(con[1][0])
            labels = np.array(labels)
        except:
            msgBox.setText("Condition value is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        FontSize = ui.txtFontSize.value()

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
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if Filter is not None:
            for fil in Filter:
                # Remove Training Set
                labelIndx = np.where(L == fil)[0]
                X = np.delete(X, labelIndx, axis=0)
                L = np.delete(L, labelIndx, axis=0)
                print("Class ID = " + str(fil) + " is removed from data.")


        Out = {}


        listL = np.unique(L)
        print(f"List of labels {listL}")
        # Generate RegMap
        RegionMap = {}
        for cooIdx, coo in enumerate(Coord):
            reg = AtlasImg[coo[0], coo[1], coo[2]]
            if reg != 0:
                try:
                    RegionMap[reg].append(cooIdx)
                except:
                    RegionMap[reg] = list()
                    RegionMap[reg].append(cooIdx)

        AtlasRegNum = len(RegionMap.keys())
        print(f"Number of regions: {AtlasRegNum}")
        print("Region map is generated!")
        # Reshape data over label
        XR = list()
        for ll in listL:
            xl = X[np.where(L == ll)[0], :]
            xri = list()
            for regID in sorted(RegionMap.keys()):
                xlr = xl[:, RegionMap[regID]]
                xlri = Integration(xlr, axis=1)
                xri.append(xlri)
                print(f"Label: {ll}, Region {regID} is done.")
            XR.append(np.transpose(xri))
        NetworkNum = np.shape(XR)[0]
        print(f"Number of networks: {NetworkNum}")
        # Generate Network
        Net = np.zeros((NetworkNum, AtlasRegNum, AtlasRegNum))
        for nn, xxr in enumerate(XR):
            for i in range(AtlasRegNum):
                for j in range(i + 1, AtlasRegNum):
                    Net[nn, i, j] = Metric(xxr[:, i], xxr[:, j])[0]
                    Net[nn, j, i] = Net[nn, i, j]
                    print(f"Label: {nn}, Network: {i} vs {j} is compared.")
        NetMaxValue = np.max(Net[:])
        print(f"Network maximum value: {NetMaxValue}")
        NetThreshold = Threshold * NetMaxValue
        print(f"Network Threshold: {NetThreshold}")
        Out["Networks"] = Net
        # Threshold
        for nn, _ in enumerate(XR):
            for i in range(AtlasRegNum):
                for j in range(i + 1, AtlasRegNum):
                    if Net[nn, i, j] < NetThreshold:
                        Net[nn, i, j] = 0
                        Net[nn, j, i] = 0
                        print(f"Label: {nn}, Network: {i} vs {j} is thresholded.")
        Out["ThresholdNetworks"] = Net
        # Active Region
        ActiveRegions = list()
        for regIndx, regID in enumerate(sorted(RegionMap.keys())):
            IsZero = True
            for nn, _ in enumerate(XR):
                if sum(Net[nn, regIndx, :]) != 0:
                    IsZero = False
                    break
            if not IsZero:
                ActiveRegions.append(regID)
        print(f"Number of active regions: {np.shape(ActiveRegions)[0]}")
        print(f"Active Regions: {ActiveRegions}")
        Out["ActiveRegions"] = ActiveRegions


















        #
        #
        #
        #
        #
        # for foldID, fold in enumerate(GUFold):
        #     print("Analyzing level " + str(foldID + 1)," of ", str(len(UniqFold)) , " ...")
        #     Index = np.where(UnitFold == fold)
        #     # Whole-Data
        #     if FoldStr == "Whole-Data" and np.shape(Index)[0]:
        #         Index = [Index[1]]
        #     XLi      = X[Index]
        #     if ui.cbScale.isChecked() and ui.rbScale.isChecked():
        #         XLi = preprocessing.scale(XLi)
        #         print("Whole of data is scaled X%d~N(0,1)." % (foldID + 1))
        #     RegLi       =  np.insert(Design[Index], 0, 1, axis=1)
        #
        #     if method == "ols":
        #         model = linmdl.LinearRegression(fit_intercept=fit, normalize=normalize, n_jobs=njob)
        #     elif method == "ridge":
        #         model = linmdl.Ridge(alpha=alpha, fit_intercept=fit, normalize=normalize, max_iter=iter, tol=tol,
        #                              solver=solver)
        #     elif method == "lasso":
        #         model = linmdl.Lasso(alpha=alpha, fit_intercept=fit, normalize=normalize, max_iter=iter, tol=tol,
        #                              selection=selection)
        #     elif method == "elast":
        #         model = linmdl.ElasticNet(alpha=alpha, l1_ratio=l1, fit_intercept=fit, normalize=normalize, \
        #                                   max_iter=iter, tol=tol, selection=selection)
        #     model.fit(RegLi, XLi)
        #     BetaLi = np.transpose(model.coef_)[1:, :]
        #     Beta = BetaLi if Beta is None else Beta + BetaLi
        #
        #     print("Calculating MSE for level %d ..." % (foldID + 1))
        #     MSE = mean_squared_error(XLi, np.matmul(Design[Index], BetaLi))
        #     print("MSE%d: %f" % (foldID + 1, MSE))
        #     OutData["MSE" + str(foldID)] = MSE
        #     AMSE.append(MSE)
        #     if ui.cbBeta.isChecked():
        #         OutData["BetaL" + str(foldID + 1)] = BetaLi
        #     # Calculate Results
        #     if ui.cbCorr.isChecked():
        #         print("Calculating Correlation for level %d ..." % (foldID + 1))
        #         CorrLi = np.corrcoef(BetaLi)
        #         OutData["Corr" + str(foldID + 1)] = CorrLi
        #         if Corr is None:
        #             Corr = CorrLi.copy()
        #         else:
        #             if ui.rbAvg.isChecked():
        #                 Corr = np.add(Corr, CorrLi)
        #             elif ui.rbMin.isChecked():
        #                 Corr = np.minimum(Corr, CorrLi)
        #             else:
        #                 Corr = np.maximum(Corr, CorrLi)
        #     if ui.cbCov.isChecked():
        #         print("Calculating Covariance for level %d ..." % (foldID + 1))
        #         CovLi = np.cov(BetaLi)
        #         OutData["Cov" + str(foldID + 1)]  = CovLi
        #         if Cov is None:
        #             Cov = CovLi.copy()
        #         else:
        #             if ui.rbAvg.isChecked():
        #                 Cov = np.add(Cov, CovLi)
        #             elif ui.rbMin.isChecked():
        #                 Cov = np.minimum(Cov, CovLi)
        #             else:
        #                 Cov = np.maximum(Cov, CovLi)
        #
        # CoEff = len(UniqFold) - 1 if len(UniqFold) > 2 else 1
        # if ui.cbCov.isChecked():
        #     if ui.rbAvg.isChecked():
        #         Cov = Cov / CoEff
        #     covClass = SimilarityMatrixBetweenClass(Cov)
        #     OutData["Covariance"]       = Cov
        #     OutData["Covariance_min"]   = covClass.min()
        #     OutData["Covariance_max"]   = covClass.max()
        #     OutData["Covariance_std"]   = covClass.std()
        #     OutData["Covariance_mean"]  = covClass.mean()
        # if ui.cbCorr.isChecked():
        #     if ui.rbAvg.isChecked():
        #         Corr = Corr / CoEff
        #     corClass = SimilarityMatrixBetweenClass(Corr)
        #     OutData["Correlation"]      = Corr
        #     OutData["Correlation_min"]  = corClass.min()
        #     OutData["Correlation_max"]  = corClass.max()
        #     OutData["Correlation_std"]  = corClass.std()
        #     OutData["Correlation_mean"] = corClass.mean()
        #
        #
        # # Calculating Distance Matrix
        # dis = np.zeros((np.shape(Beta)[0], np.shape(Beta)[0]))
        #
        # for i in range(np.shape(Beta)[0]):
        #     for j in range(i + 1, np.shape(Beta)[0]):
        #         dis[i, j] = 1 - np.dot(Beta[i, :], Beta[j, :].T)
        #         dis[j, i] = dis[i, j]
        # OutData["DistanceMatrix"] = dis
        # Z = linkage(dis)
        # OutData["Linkage"] = Z
        #
        # OutData["MSE"] = np.mean(AMSE)
        # print("Average MSE: %f" % (OutData["MSE"]))
        # OutData["RunTime"] = time.time() - tStart
        # print("Runtime (s): %f" % (OutData["RunTime"]))
        # print("Saving results ...")
        # io.savemat(OutFile,mdict=OutData,do_compression=True)
        # print("Output is saved.")
        #
        #
        # if ui.cbDiagram.isChecked():
        #     if ui.cbCorr.isChecked():
        #         NumData = np.shape(Corr)[0]
        #         fig1 = plt.figure(num=None, figsize=(NumData, NumData), dpi=100)
        #         plt.pcolor(Corr, vmin=np.min(Corr), vmax=np.max(Corr))
        #         plt.xlim([0, NumData])
        #         plt.ylim([0, NumData])
        #         cbar = plt.colorbar()
        #         cbar.ax.tick_params(labelsize=FontSize)
        #         ax = plt.gca()
        #         ax.invert_yaxis()
        #         ax.set_aspect(1)
        #
        #         ax.set_yticks(np.arange(NumData) + 0.5, minor=False)
        #         ax.set_xticks(np.arange(NumData) + 0.5, minor=False)
        #         ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtXRotation.value())
        #         ax.set_yticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtYRotation.value())
        #         ax.grid(False)
        #         ax.set_aspect(1)
        #         ax.set_frame_on(False)
        #         for t in ax.xaxis.get_major_ticks():
        #             t.tick1On = False
        #             t.tick2On = False
        #         for t in ax.yaxis.get_major_ticks():
        #             t.tick1On = False
        #             t.tick2On = False
        #
        #         if len(ui.txtTitleCorr.text()):
        #             plt.title(ui.txtTitleCorr.text())
        #         else:
        #             plt.title('Group RSA: Correlation\nLevel: ' + FoldStr)
        #         plt.show()
        #
        #
        #     if ui.cbCov.isChecked():
        #         NumData = np.shape(Cov)[0]
        #         fig2 = plt.figure(num=None, figsize=(NumData, NumData), dpi=100)
        #         plt.pcolor(Cov, vmin=np.min(Cov), vmax=np.max(Cov))
        #         plt.xlim([0, NumData])
        #         plt.ylim([0, NumData])
        #         cbar = plt.colorbar()
        #         cbar.ax.tick_params(labelsize=FontSize)
        #         ax = plt.gca()
        #         ax.invert_yaxis()
        #         ax.set_aspect(1)
        #
        #         ax.set_yticks(np.arange(NumData) + 0.5, minor=False)
        #         ax.set_xticks(np.arange(NumData) + 0.5, minor=False)
        #         ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtXRotation.value())
        #         ax.set_yticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtYRotation.value())
        #         ax.grid(False)
        #         ax.set_aspect(1)
        #         ax.set_frame_on(False)
        #         for t in ax.xaxis.get_major_ticks():
        #             t.tick1On = False
        #             t.tick2On = False
        #         for t in ax.yaxis.get_major_ticks():
        #             t.tick1On = False
        #             t.tick2On = False
        #         if len(ui.txtTitleCov.text()):
        #             plt.title(ui.txtTitleCov.text())
        #         else:
        #             plt.title('Group RSA: Covariance\nLevel: ' + FoldStr)
        #         plt.show()
        #
        #     fig3 = plt.figure(figsize=(25, 10), )
        #     if len(ui.txtTitleDen.text()):
        #         plt.title(ui.txtTitleDen.text())
        #     else:
        #         plt.title('Group MP Gradient RSA: Similarity Analysis\nLevel: ' + FoldStr)
        #
        #     dn = dendrogram(Z, labels=labels, leaf_font_size=FontSize, color_threshold=1, leaf_rotation=ui.txtXRotation.value())
        #     plt.show()


        print("DONE.")
        msgBox.setText("Network analysis is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnRedraw_click(self):
        msgBox = QMessageBox()

        ofile = LoadFile("Save result file ...",['Result files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))

        FontSize = ui.txtFontSize.value()

        if len(ofile):
            try:
                Res     = io.loadmat(ofile)
            except:
                print("Cannot load result file!")
                msgBox.setText("Cannot load result file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False


            HasDefaultCond = False
            # Condition
            if not len(ui.txtCond.currentText()):
                try:
                    Cond = Res["condition"]
                    HasDefaultCond = True
                except:
                    msgBox.setText("Please enter Condition variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

            if not HasDefaultCond:
                try:
                    Cond = Res[ui.txtCond.currentText()]
                except:
                    msgBox.setText("Condition value is wrong!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False


            labels = list()
            for con in Cond:
                labels.append(con[1][0])
            labels = np.array(labels)



            if ui.cbCorr.isChecked():
                try:
                    Corr = Res["Correlation"]
                except:
                    print("Cannot load Correlation variable!")
                    msgBox.setText("Cannot load Correlation variable!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                NumData = np.shape(Corr)[0]
                fig1 = plt.figure(num=None, figsize=(NumData, NumData), dpi=100)
                plt.pcolor(Corr, vmin=np.min(Corr), vmax=np.max(Corr))
                plt.xlim([0, NumData])
                plt.ylim([0, NumData])
                cbar = plt.colorbar()
                cbar.ax.tick_params(labelsize=FontSize)
                ax = plt.gca()
                ax.invert_yaxis()
                ax.set_aspect(1)

                ax.set_yticks(np.arange(NumData) + 0.5, minor=False)
                ax.set_xticks(np.arange(NumData) + 0.5, minor=False)
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtXRotation.value())
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtYRotation.value())
                ax.grid(False)
                ax.set_aspect(1)
                ax.set_frame_on(False)
                for t in ax.xaxis.get_major_ticks():
                    t.tick1On = False
                    t.tick2On = False
                for t in ax.yaxis.get_major_ticks():
                    t.tick1On = False
                    t.tick2On = False

                if len(ui.txtTitleCov.text()):
                    plt.title(ui.txtTitleCov.text())
                else:
                    plt.title('Group RSA: Correlation\nLevel: ' + str(Res["FoldInfo"]["Order"][0][0][0]))
                plt.show()


            if ui.cbCov.isChecked():
                try:
                    Cov = Res["Covariance"]
                except:
                    print("Cannot load Covariance variable!")
                    msgBox.setText("Cannot load Covariance variable!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                NumData = np.shape(Cov)[0]
                fig2 = plt.figure(num=None, figsize=(NumData, NumData), dpi=100)
                plt.pcolor(Cov, vmin=np.min(Cov), vmax=np.max(Cov))
                plt.xlim([0, NumData])
                plt.ylim([0, NumData])
                cbar = plt.colorbar()
                cbar.ax.tick_params(labelsize=FontSize)
                ax = plt.gca()
                ax.invert_yaxis()
                ax.set_aspect(1)

                ax.set_yticks(np.arange(NumData) + 0.5, minor=False)
                ax.set_xticks(np.arange(NumData) + 0.5, minor=False)
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtXRotation.value())
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize, rotation=ui.txtYRotation.value())
                ax.grid(False)
                ax.set_aspect(1)
                ax.set_frame_on(False)
                for t in ax.xaxis.get_major_ticks():
                    t.tick1On = False
                    t.tick2On = False
                for t in ax.yaxis.get_major_ticks():
                    t.tick1On = False
                    t.tick2On = False
                if len(ui.txtTitleCorr.text()):
                    plt.title(ui.txtTitleCorr.text())
                else:
                    plt.title('Group RSA: Covariance\nLevel: ' + str(Res["FoldInfo"]["Order"][0][0][0]))
                plt.show()

            fig3 = plt.figure(figsize=(25, 10), )
            dn = dendrogram(Res["Linkage"], labels=labels, leaf_font_size=FontSize, color_threshold=1, leaf_rotation=ui.txtXRotation.value())
            if len(ui.txtTitleDen.text()):
                plt.title(ui.txtTitleDen.text())
            else:
                plt.title('Group MP Gradient RSA: Similarity Analysis\nLevel: ' + str(Res["FoldInfo"]["Order"][0][0][0]))
            plt.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMANetwork.show(frmMANetwork)
    sys.exit(app.exec_())