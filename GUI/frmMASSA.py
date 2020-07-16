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
import torch
import numpy as np
from RSA.SSA import SSA
from Base.draw import DrawRSA
from PyQt5.QtWidgets import *
from GUI.frmMASSAGUI import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from sklearn.preprocessing import label_binarize
from Base.Conditions import reshape_condition_cell
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector
from Base.utility import getVersion, getBuild, SimilarityMatrixBetweenClass

# Plot
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage



class frmMASSA(Ui_frmMASSA):
    ui = Ui_frmMASSA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMASSA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Method
        ui.cbGPU.addItem("Auto", torch.cuda.is_available())
        ui.cbGPU.addItem("Only CPU", False)

        # Linkage Method
        ui.cbLMethod.addItem("Single", "single")
        ui.cbLMethod.addItem("Complete", "complete")
        ui.cbLMethod.addItem("Average", "average")
        ui.cbLMethod.addItem("Weighted", "weighted")
        ui.cbLMethod.addItem("Centroid", "centroid")
        ui.cbLMethod.addItem("Median", "median")
        ui.cbLMethod.addItem("Ward", "ward")

        # Linkage Meric
        ui.cbLMetric.addItem("Euclidean", "euclidean")
        ui.cbLMetric.addItem("Cityblock", "cityblock")
        ui.cbLMetric.addItem("Sqeuclidean", "sqeuclidean")
        ui.cbLMetric.addItem("Correlation", "correlation")
        ui.cbLMetric.addItem("Cosine", "cosine")

        dialog.setWindowTitle("easy fMRI Shared Similarity Analysis (SSA) - V" + getVersion() + "B" + getBuild())
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
        ui.btnRedraw.clicked.connect(self.btnRedraw_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


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
                        ui.lblFea.setText("[0 ... " + str(np.shape(data["data"])[1]) + "]")
                        ui.txtNumFea.setMaximum(np.shape(data["data"])[1])
                        ui.txtNumFea.setMinimum(0)

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

                    # Design
                    ui.txtCoordinate.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCoordinate.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCoordinate.setCurrentText("coordinate")

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")

                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")

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

                    # Task
                    ui.txtTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")

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


        if not ui.cbCov.isChecked() and not ui.cbCorr.isChecked():
            msgBox.setText("At least, you must select one metric!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Method
        gpu      = ui.cbGPU.currentData()
        Verbose  = ui.cbVerbose.isChecked()

        try:
            gamma = np.float(ui.txtGamma.text())
        except:
            msgBox.setText("Gamma is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Iter = np.int(ui.txtIter.text())
        except:
            msgBox.setText("Max Iteration is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            NumFea = ui.txtNumFea.value()
        except:
            msgBox.setText("Number of features is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if NumFea <= 0:
            NumFea = None

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


        if not len(ui.txtSharedSpace.text()):
            msgBox.setText("Please enter Shared Space variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtSharedVoxelSpace.text()):
            msgBox.setText("Please enter Shared Voxel Space variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtViewSpaces.text()):
            msgBox.setText("Please enter View Space variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.txtTransformMats.text()):
            msgBox.setText("Please enter Transform Matrices variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        print("Loading ...")
        InData = mainIO_load(InFile)
        OutData["imgShape"] = reshape_1Dvector(InData["imgShape"])

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

        # Coordinate
        if not len(ui.txtCoordinate.currentText()):
            msgBox.setText("Please enter Input Coordinate variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Coordinate = InData[ui.txtCoordinate.currentText()]
            OutData["coordinate"] = Coordinate
        except:
            msgBox.setText("Coordinate value is wrong!")
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
            OutData["condition"] = Cond
            labels = list()
            for con in Cond:
                labels.append(reshape_condition_cell(con[1]))
            OutData["labels"] = labels

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
            if ui.cbScale.isChecked() and not ui.rbScale.isChecked():
                X = preprocessing.scale(X)
                print("Whole of data is scaled X~N(0,1).")
        except:
            print("Cannot load data or label")
            return

        # Task
        if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        try:
            TaskTitle = np.array(InData[ui.txtTask.currentText()][0])
        except:
            msgBox.setText("Task variable name is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        TaskTitleUnique = np.unique(TaskTitle)
        Task = np.zeros(np.shape(TaskTitle))

        for ttinx, tt in enumerate(TaskTitle):
            for ttlinx, ttl in enumerate(TaskTitleUnique):
                if tt[0] == ttl:
                    Task[ttinx] = ttlinx + 1
                    break

        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Sub = InData[ui.txtSubject.currentText()][0]
        except:
            msgBox.setText("Subject variable name is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Run
        if not len(ui.txtRun.currentText()):
            msgBox.setText("Please enter Run variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Run = InData[ui.txtRun.currentText()][0]
        except:
            msgBox.setText("Run variable name is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Counter
        if not len(ui.txtCounter.currentText()):
            msgBox.setText("Please enter Counter variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Con = InData[ui.txtCounter.currentText()][0]
        except:
            msgBox.setText("Counter variable name is wrong!")
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
                Task = np.delete(Task, labelIndx, axis=0)
                Sub = np.delete(Sub, labelIndx, axis=0)
                Run = np.delete(Run, labelIndx, axis=0)
                Con = np.delete(Con, labelIndx, axis=0)
                print("Class ID = " + str(fil) + " is removed from data.")

        try:
            Unit = np.int32(ui.txtUnit.text())
        except:
            msgBox.setText("Unit for the test set must be a number!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if Unit < 1:
            msgBox.setText("Unit for the test set must be greater than zero!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        print("Calculating Levels ...")
        GroupFold = None
        FoldStr = ""
        if ui.cbFSubject.isChecked():
            if not ui.rbFRun.isChecked():
                GroupFold = [Sub]
                FoldStr = "Subject"
            else:
                GroupFold = np.concatenate(([Sub],[Run]))
                FoldStr = "Subject+Run"

        if ui.cbFTask.isChecked():
            GroupFold = np.concatenate((GroupFold,[Task])) if GroupFold is not None else [Task]
            FoldStr = FoldStr + "+Task"

        if ui.cbFCounter.isChecked():
            GroupFold = np.concatenate((GroupFold,[Con])) if GroupFold is not None else [Con]
            FoldStr = FoldStr + "+Counter"

        if FoldStr == "":
            FoldStr = "Whole-Data"
            GUFold = [1]
            ListFold = [1]
            UniqFold = [1]
            GroupFold = [1]
            UnitFold = np.ones((1, np.shape(X)[0]))
        else:
            GroupFold = np.transpose(GroupFold)
            UniqFold = np.array(list(set(tuple(i) for i in GroupFold.tolist())))
            FoldIDs = np.arange(len(UniqFold)) + 1

            if len(UniqFold) <= Unit:
                msgBox.setText("Unit must be smaller than all possible levels! Number of all levels is: " + str(len(UniqFold)))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            if np.mod(len(UniqFold),Unit):
                msgBox.setText("Unit must be divorceable to all possible levels! Number of all levels is: " + str(len(UniqFold)))
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


        FoldInfo = dict()
        FoldInfo["Unit"]    = Unit
        FoldInfo["Group"]   = GroupFold
        FoldInfo["Order"]   = FoldStr
        FoldInfo["List"]    = ListFold
        FoldInfo["Unique"]  = UniqFold
        FoldInfo["Folds"]   = UnitFold

        OutData["FoldInfo"] = FoldInfo
        OutData["ModelAnalysis"] = "SSA"
        print("Number of all levels is: " + str(len(UniqFold)))

        Xi = list()
        Yi = list()


        for foldID, fold in enumerate(GUFold):
            print("Extracting view " + str(foldID + 1)," of ", str(len(UniqFold)) , " ...")
            Index = np.where(UnitFold == fold)
            # Whole-Data
            if FoldStr == "Whole-Data" and np.shape(Index)[0]:
                Index = [Index[1]]

            Xi.append(X[Index])
            yyi = label_binarize(L[Index], np.unique(L))

            # Adopt it for binary labels (just two class SSA comparison)
            if np.shape(yyi)[1] == 1:
                yyi_inv = yyi.copy()
                yyi_inv[np.where(yyi_inv == 0)] = 2
                yyi_inv -= 1
                yyi = np.concatenate((yyi, yyi_inv), axis=1)
            Yi.append(yyi)

        try:
            ssa  = SSA(gamma=gamma, gpu=gpu)
            Beta = ssa.run(X=Xi, Y=Yi, Dim=NumFea, verbose=Verbose, Iteration=Iter, ShowError=ui.cbError.isChecked())
            if ui.cbError.isChecked():
                if ssa.LostVec is not None:
                    OutData["LossVec"] = ssa.LostVec
                    OutData["Error"]   = ssa.Loss

        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        OutData["AlgorithmRuntime"]            = ssa.Runtime
        OutData[ui.txtSharedSpace.text()]      = Beta
        OutData[ui.txtSharedVoxelSpace.text()] = ssa.getSharedVoxelSpace()
        OutData[ui.txtTransformMats.text()]    = ssa.getTransformMats()
        if ui.cbViewSpace.isChecked():
            for viewID, view in enumerate(ssa.getSubjectSpace()):
                OutData[ui.txtViewSpaces.text() + "_View" + str(viewID + 1)]  = np.transpose(view)
        else:
            OutData[ui.txtViewSpaces.text()] = ssa.getSubjectSpace()

        print("Calculating Distance Matrix ...")
        dis = np.zeros((np.shape(Beta)[0], np.shape(Beta)[0]))
        for i in range(np.shape(Beta)[0]):
            for j in range(i + 1, np.shape(Beta)[0]):
                dis[i, j] = 1 - np.dot(Beta[i, :], Beta[j, :].T)
                dis[j, i] = dis[i, j]
        # dis = dis - np.min(dis)
        # dis = dis / np.max(dis)
        OutData["DistanceMatrix"]       = dis
        print("Applying linkage ...")
        Z = linkage(dis, method=ui.cbLMethod.currentData(), metric=ui.cbLMetric.currentData(), optimal_ordering=ui.cbLOrder.isChecked())
        OutData["Linkage"]              = Z


        if ui.cbCov.isChecked():
            Cov = np.cov(Beta)
            covClass = SimilarityMatrixBetweenClass(Cov)
            OutData["Covariance"]       = Cov
            OutData["Covariance_min"]   = covClass.min()
            OutData["Covariance_max"]   = covClass.max()
            OutData["Covariance_std"]   = covClass.std()
            OutData["Covariance_mean"]  = covClass.mean()
        if ui.cbCorr.isChecked():
            Corr = np.corrcoef(Beta)
            corClass = SimilarityMatrixBetweenClass(Corr)
            OutData["Correlation"]      = Corr
            OutData["Correlation_min"]  = corClass.min()
            OutData["Correlation_max"]  = corClass.max()
            OutData["Correlation_std"]  = corClass.std()
            OutData["Correlation_mean"] = corClass.mean()

        OutData["Runtime"] = time.time() - tStart
        print("Runtime: ", OutData["Runtime"])
        print("Algorithm Runtime: ", OutData["AlgorithmRuntime"])

        print("Saving results ...")
        mainIO_save(OutData, OutFile)
        print("Output is saved.")

        if ui.cbDiagram.isChecked():
            drawrsa = DrawRSA()

            if ui.cbCorr.isChecked():
                drawrsa.ShowFigure(Corr, labels, ui.txtTitleCorr.text(), FontSize, ui.txtXRotation.value(), ui.txtYRotation.value())

            if ui.cbCov.isChecked():
                drawrsa.ShowFigure(Cov, labels,ui.txtTitleCov.text(), FontSize, ui.txtXRotation.value(), ui.txtYRotation.value())

            drawrsa.ShowDend(Z, labels, ui.txtTitleDen.text(), FontSize, ui.txtXRotation.value())

        print("DONE.")
        msgBox.setText("Shared Similarity Analysis (SSA) is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnRedraw_click(self):
        msgBox = QMessageBox()

        ofile = LoadFile("Save result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))

        FontSize = ui.txtFontSize.value()

        if len(ofile):
            try:
                Res = mainIO_load(ofile)
            except:
                print("Cannot load result file!")
                msgBox.setText("Cannot load result file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            # Load Variables
            try:
                labels  = list(Res["labels"])
                Z       = Res["Linkage"]
                if ui.cbCorr.isChecked():
                    Corr    = Res["Correlation"]
                if ui.cbCov.isChecked():
                    Cov     = Res["Covariance"]
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            drawrsa = DrawRSA()

            if ui.cbCorr.isChecked():
                drawrsa.ShowFigure(Corr, labels, ui.txtTitleCorr.text(), FontSize, ui.txtXRotation.value(), ui.txtYRotation.value())

            if ui.cbCov.isChecked():
                drawrsa.ShowFigure(Cov, labels,ui.txtTitleCov.text(), FontSize, ui.txtXRotation.value(), ui.txtYRotation.value())

            drawrsa.ShowDend(Z, labels, ui.txtTitleDen.text(), FontSize, ui.txtXRotation.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMASSA.show(frmMASSA)
    sys.exit(app.exec_())