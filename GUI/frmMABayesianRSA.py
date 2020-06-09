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
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
import sklearn.linear_model as linmdl
from RSA.BRSA.brsa import BRSA, GBRSA, prior_GP_var_inv_gamma, prior_GP_var_half_cauchy
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild, SimilarityMatrixBetweenClass
from GUI.frmMABayesianRSAGUI import *


import logging
logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets




def OptimizationCode():
    return\
"""# Please refer to follwoing link for the other options:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html

optimizer='L-BFGS-B'            
minimize_options={'gtol': 1e-4, 'disp': False, 'maxiter': 6}
"""



# Plot
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage



class frmMABayesianRSA(Ui_frmMABayesianRSA):
    ui = Ui_frmMABayesianRSA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMABayesianRSA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Method
        ui.cbMethod.addItem("Bayesian RSA","brsa")
        ui.cbMethod.addItem("Group Bayesian RSA","gbrsa")

        # Nureg Method
        ui.cbNuregMethod.addItem("PCA", "PCA")
        ui.cbNuregMethod.addItem("ICA", "ICA")
        ui.cbNuregMethod.addItem("Factor Analysis", "FA")
        ui.cbNuregMethod.addItem("Sparse PCA", "SPCA")

        # Tau2Prior
        ui.cbTau2Prior.addItem("Gamma", prior_GP_var_inv_gamma)
        ui.cbTau2Prior.addItem("Half Cauchy", prior_GP_var_half_cauchy)

        # SNR_prior
        ui.cbSNRPrior.addItem("Exponential", "exp")
        ui.cbSNRPrior.addItem("Log Norm", "lognorm")
        ui.cbSNRPrior.addItem("Uniform", "unif")

        # Base
        ui.txtEvents = api.CodeEdit(ui.tab_7)
        ui.txtEvents.setGeometry(QtCore.QRect(10, 10, 700, 500))
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
        ui.txtEvents.setPlainText(OptimizationCode(),"","")

        dialog.setWindowTitle("easy fMRI Bayesian RSA - V" + getVersion() + "B" + getBuild())
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

                    # Coordinate
                    ui.txtCoord.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCoord.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCoord.setCurrentText("coordinate")

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
        if not ui.cbCov.isChecked() and not ui.cbCorr.isChecked():
            msgBox.setText("At least, you must select one metric!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        Method          = ui.cbMethod.currentData()
        NuregMethod     = ui.cbNuregMethod.currentData()
        Tau2Prior       = ui.cbTau2Prior.currentData()
        SNRPrior        = ui.cbSNRPrior.currentData()

        GPS             = ui.cbGBS.isChecked()
        GPI             = ui.cbGPI.isChecked()
        BaselineSingle  = ui.cbBaselineSingle.isChecked()
        AutoNuisance    = ui.cbAutoNuisance.isChecked()
        NuregZscore     = ui.cbNuregZscore.isChecked()


        try:
            miter = np.int(ui.txtMaxIter.text())
            assert miter >= 1, None
        except:
            msgBox.setText("Max Iteration is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            iiter = np.int(ui.txtInitIter.text())
            assert iiter >= 1, None
        except:
            msgBox.setText("Init Iteration is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Speed = np.int(ui.txtAnnealSpeed.text())
            assert Speed >= 1, None
        except:
            msgBox.setText("Anneal speed is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            rank = np.int(ui.txtRank.text())
            assert rank >= 0, None
            if rank == 0:
                rank = None
        except:
            msgBox.setText("Rank is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            NumReg = np.int(ui.txtNumReg.text())
            assert NumReg >= 0, None
            if NumReg == 0:
                NumReg = None
        except:
            msgBox.setText("Number of Reg is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SNRBin = np.int(ui.txtSNRBins.text())
            assert SNRBin > 0, None
        except:
            msgBox.setText("SNR bin is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            rhoBin = np.int(ui.txtRhoBins.text())
            assert rhoBin > 0, None
        except:
            msgBox.setText("Rho bin is wrong!")
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
            eta = np.float(ui.txtEta.text())
        except:
            msgBox.setText("Eta is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            LogSRange = np.float(ui.txtLogSRange.text())
        except:
            msgBox.setText("LogS range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SpaceSmoothRange = np.float(ui.txtSpaceSmoothRange.text())
            if SpaceSmoothRange == 0:
                SpaceSmoothRange = None
        except:
            msgBox.setText("Space Smooth Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            IntenSmoothRange = np.float(ui.txtIntenSmoothRange.text())
            if IntenSmoothRange == 0:
                IntenSmoothRange = None
        except:
            msgBox.setText("Inten Smooth Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Tau = np.float(ui.txtTauRange.text())
        except:
            msgBox.setText("Eta is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        try:
            CodeText  = ui.txtEvents.toPlainText()
            allvars = dict(locals(), **globals())
            exec(CodeText, allvars, allvars)
            Optimizer = allvars['optimizer']
            MinimizeOptions = allvars['minimize_options']
        except Exception as e:
            msgBox.setText("Optimizer is wrong!\n" + str(e))
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
        InData = io.loadmat(InFile)

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
            Intensity = np.mean(X, axis=0)
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
            TaskTitle = InData[ui.txtTask.currentText()][0]
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
            #RegLi       =  np.insert(Design[Index], 0, 1, axis=1)
            RegLi       =  Design[Index]

            try:
                if Method == "brsa":
                    model = BRSA(n_iter=miter, rank=rank, auto_nuisance=AutoNuisance,
                                 n_nureg=NumReg, nureg_zscore=NuregZscore, nureg_method=NuregMethod,
                                 baseline_single=BaselineSingle, GP_space=GPS, GP_inten=GPI,
                                 space_smooth_range=SpaceSmoothRange, inten_smooth_range=IntenSmoothRange,
                                 tau_range=Tau,
                                 tau2_prior=Tau2Prior, eta=eta, init_iter=iiter, anneal_speed=Speed, tol=tol,
                                 optimizer=Optimizer, minimize_options=MinimizeOptions)
                    model.fit(XLi, RegLi, coords=Coord, inten=Intensity)
                else:
                    model = GBRSA(n_iter=miter, rank=rank, auto_nuisance=AutoNuisance,
                                  n_nureg=NumReg, nureg_zscore=NuregZscore, nureg_method=NuregMethod,
                                  baseline_single=BaselineSingle, tol=tol, anneal_speed=Speed,
                                  SNR_prior=SNRPrior, logS_range=LogSRange, SNR_bins=SNRBin, rho_bins=rhoBin,
                                  optimizer=Optimizer, minimize_options=MinimizeOptions)
                    model.fit(XLi, RegLi)
            except Exception as e:
                msgBox.setText(str(e))
                print(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

            BetaLi = model.beta_
            Beta = BetaLi if Beta is None else Beta + BetaLi

            print("Calculating MSE for level %d ..." % (foldID + 1))
            MSE = mean_squared_error(XLi, np.matmul(RegLi, BetaLi))
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
        io.savemat(OutFile,mdict=OutData,do_compression=True)
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
    frmMABayesianRSA.show(frmMABayesianRSA)
    sys.exit(app.exec_())