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
import matplotlib
import numpy as np
from PyQt5.QtWidgets import *
from GUI.frmMARSAGUI import *
from sklearn import preprocessing
import sklearn.linear_model as linmdl
from Base.dialogs import LoadFile, SaveFile
from sklearn.metrics import mean_squared_error
from IO.mainIO import mainIO_load, mainIO_save
from Base.Conditions import reshape_condition_cell
from scipy.cluster.hierarchy import dendrogram, linkage
from Base.utility import getVersion, getBuild, SimilarityMatrixBetweenClass


# Plot
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt



class frmMARSA(Ui_frmMARSA):
    ui = Ui_frmMARSA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMARSA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Method
        ui.cbMethod.addItem("Ridge Regression","ridge")
        ui.cbMethod.addItem("Ordinary Least Squares","ols")
        ui.cbMethod.addItem("LASSO","lasso")
        ui.cbMethod.addItem("Elastic Net","elast")

        # Selection
        ui.cbSelection.addItem("cyclic")
        ui.cbSelection.addItem("random")

        # Solver {‘auto’, ‘svd’, ‘cholesky’, ‘lsqr’, ‘sparse_cg’, ‘sag’, ‘saga’}
        ui.cbSolver.addItem("auto")
        ui.cbSolver.addItem("svd")
        ui.cbSolver.addItem("cholesky")
        ui.cbSolver.addItem("lsqr")
        ui.cbSolver.addItem("sparse_cg")
        ui.cbSolver.addItem("sag")
        ui.cbSolver.addItem("saga")


        dialog.setWindowTitle("easy fMRI RSA (Group Level) - V" + getVersion() + "B" + getBuild())
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
                    ui.txtDesign.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtDesign.addItem(key)
                        if key == "design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtDesign.setCurrentText("design")

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
        method      = ui.cbMethod.currentData()

        # Solver
        solver      = ui.cbSolver.currentText()

        # Selection
        selection   = ui.cbSelection.currentText()

        # Fit
        fit         = ui.cbFit.isChecked()

        # normalize
        normalize   = ui.cbNormalize.isChecked()

        try:
            alpha = np.float(ui.txtAlpha.text())
        except:
            msgBox.setText("Alpha is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        try:
            iter = np.int(ui.txtMaxIter.text())
        except:
            msgBox.setText("Max Iteration is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        try:
            tol = np.float(ui.txtTole.text())
        except:
            msgBox.setText("Tolerance is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            l1 = np.float(ui.txtL1.text())
        except:
            msgBox.setText("L1 is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            njob = np.float(ui.txtJobs.text())
        except:
            msgBox.setText("Number of jobs is wrong!")
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
        print("Loading ...")
        InData = mainIO_load(InFile)

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

        # Design
        if not len(ui.txtDesign.currentText()):
            msgBox.setText("Please enter Input Design variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Design = InData[ui.txtDesign.currentText()]
        except:
            msgBox.setText("Design value is wrong!")
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
                labels.append(reshape_condition_cell(con[1]))

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
                Design = np.delete(Design, labelIndx, axis=0)
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
        OutData["ModelAnalysis"] = "SK.Group.RSA." + ui.cbMethod.currentText()


        print("Number of all levels is: " + str(len(UniqFold)))

        Cov = None
        Corr = None
        AMSE = list()
        Beta = None

        for foldID, fold in enumerate(GUFold):
            print("Analyzing level " + str(foldID + 1)," of ", str(len(UniqFold)) , " ...")
            Index = np.where(UnitFold == fold)
            # Whole-Data
            if FoldStr == "Whole-Data" and np.shape(Index)[0]:
                Index = [Index[1]]
            XLi      = X[Index]
            if ui.cbScale.isChecked() and ui.rbScale.isChecked():
                XLi = preprocessing.scale(XLi)
                print("Whole of data is scaled X%d~N(0,1)." % (foldID + 1))
            RegLi       =  np.insert(Design[Index], 0, 1, axis=1)

            if method == "ols":
                model = linmdl.LinearRegression(fit_intercept=fit, normalize=normalize, n_jobs=njob)
            elif method == "ridge":
                model = linmdl.Ridge(alpha=alpha, fit_intercept=fit, normalize=normalize, max_iter=iter, tol=tol,
                                     solver=solver)
            elif method == "lasso":
                model = linmdl.Lasso(alpha=alpha, fit_intercept=fit, normalize=normalize, max_iter=iter, tol=tol,
                                     selection=selection)
            elif method == "elast":
                model = linmdl.ElasticNet(alpha=alpha, l1_ratio=l1, fit_intercept=fit, normalize=normalize, \
                                          max_iter=iter, tol=tol, selection=selection)
            model.fit(RegLi, XLi)
            BetaLi = np.transpose(model.coef_)[1:, :]
            Beta = BetaLi if Beta is None else Beta + BetaLi

            print("Calculating MSE for level %d ..." % (foldID + 1))
            MSE = mean_squared_error(XLi, np.matmul(Design[Index], BetaLi))
            print("MSE%d: %f" % (foldID + 1, MSE))
            OutData["MSE" + str(foldID)] = MSE
            AMSE.append(MSE)
            if ui.cbBeta.isChecked():
                OutData["BetaL" + str(foldID + 1)] = BetaLi
            # Calculate Results
            if ui.cbCorr.isChecked():
                print("Calculating Correlation for level %d ..." % (foldID + 1))
                CorrLi = np.corrcoef(BetaLi)
                OutData["Corr" + str(foldID + 1)] = CorrLi
                if Corr is None:
                    Corr = CorrLi.copy()
                else:
                    if ui.rbAvg.isChecked():
                        Corr = np.add(Corr, CorrLi)
                    elif ui.rbMin.isChecked():
                        Corr = np.minimum(Corr, CorrLi)
                    else:
                        Corr = np.maximum(Corr, CorrLi)
            if ui.cbCov.isChecked():
                print("Calculating Covariance for level %d ..." % (foldID + 1))
                CovLi = np.cov(BetaLi)
                OutData["Cov" + str(foldID + 1)]  = CovLi
                if Cov is None:
                    Cov = CovLi.copy()
                else:
                    if ui.rbAvg.isChecked():
                        Cov = np.add(Cov, CovLi)
                    elif ui.rbMin.isChecked():
                        Cov = np.minimum(Cov, CovLi)
                    else:
                        Cov = np.maximum(Cov, CovLi)

        CoEff = len(UniqFold) - 1 if len(UniqFold) > 2 else 1
        if ui.cbCov.isChecked():
            if ui.rbAvg.isChecked():
                Cov = Cov / CoEff
            covClass = SimilarityMatrixBetweenClass(Cov)
            OutData["Covariance"]       = Cov
            OutData["Covariance_min"]   = covClass.min()
            OutData["Covariance_max"]   = covClass.max()
            OutData["Covariance_std"]   = covClass.std()
            OutData["Covariance_mean"]  = covClass.mean()
        if ui.cbCorr.isChecked():
            if ui.rbAvg.isChecked():
                Corr = Corr / CoEff
            corClass = SimilarityMatrixBetweenClass(Corr)
            OutData["Correlation"]      = Corr
            OutData["Correlation_min"]  = corClass.min()
            OutData["Correlation_max"]  = corClass.max()
            OutData["Correlation_std"]  = corClass.std()
            OutData["Correlation_mean"] = corClass.mean()


        # Calculating Distance Matrix
        dis = np.zeros((np.shape(Beta)[0], np.shape(Beta)[0]))

        for i in range(np.shape(Beta)[0]):
            for j in range(i + 1, np.shape(Beta)[0]):
                dis[i, j] = 1 - np.dot(Beta[i, :], Beta[j, :].T)
                dis[j, i] = dis[i, j]
        OutData["DistanceMatrix"] = dis
        Z = linkage(dis)
        OutData["Linkage"] = Z

        OutData["MSE"] = np.mean(AMSE)
        print("Average MSE: %f" % (OutData["MSE"]))
        OutData["RunTime"] = time.time() - tStart
        print("Runtime (s): %f" % (OutData["RunTime"]))
        print("Saving results ...")
        mainIO_save(OutData, OutFile)
        print("Output is saved.")


        if ui.cbDiagram.isChecked():
            if ui.cbCorr.isChecked():
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

                if len(ui.txtTitleCorr.text()):
                    plt.title(ui.txtTitleCorr.text())
                else:
                    plt.title('Group RSA: Correlation\nLevel: ' + FoldStr)
                plt.show()


            if ui.cbCov.isChecked():
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
                if len(ui.txtTitleCov.text()):
                    plt.title(ui.txtTitleCov.text())
                else:
                    plt.title('Group RSA: Covariance\nLevel: ' + FoldStr)
                plt.show()

            fig3 = plt.figure(figsize=(25, 10), )
            if len(ui.txtTitleDen.text()):
                plt.title(ui.txtTitleDen.text())
            else:
                plt.title('Group MP Gradient RSA: Similarity Analysis\nLevel: ' + FoldStr)

            dn = dendrogram(Z, labels=labels, leaf_font_size=FontSize, color_threshold=1, leaf_rotation=ui.txtXRotation.value())
            plt.show()


        print("DONE.")
        msgBox.setText("Group Representational Similarity Analysis (RSA) is done.")
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
                Res     = mainIO_load(ofile)
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
                labels.append(reshape_condition_cell(con[1]))



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
    frmMARSA.show(frmMARSA)
    sys.exit(app.exec_())