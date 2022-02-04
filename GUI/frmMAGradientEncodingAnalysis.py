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
import torch
import matplotlib
import numpy as np
from RSA.GrRSA import GrRSA
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector
from GUI.frmMAGradientEncodingAnalysisGUI import *
from Base.Conditions import reshape_condition_cell
from Base.utility import getVersion, getBuild, SimilarityMatrixBetweenClass



# Plot
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def MethodTitle(str):
    if   str == 'ridge':
        return 'Ridge Regression'
    elif str == 'ln1':
        return 'Least Norm 1'
    elif str == 'ln2':
        return 'Least Norm 2'
    elif str == 'ln12':
        return 'Least Norms 1, 2'
    elif str == 'linear':
        return 'Linear Model'
    elif str == 'lasso':
        return 'LASSO'
    elif str == 'elastic':
        return 'Elastic Net'
    return ''


class frmMAGradientEncodingAnalysis(Ui_frmMAGradientEncodingAnalysis):
    ui = Ui_frmMAGradientEncodingAnalysis()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMAGradientEncodingAnalysis()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        # Method
        ui.cbMethod.addItem('Linear Model' , 'linear')
        ui.cbMethod.addItem('Ridge Regression','ridge')
        ui.cbMethod.addItem('LASSO' , 'lasso')
        ui.cbMethod.addItem('Elastic Net', 'elastic')
        ui.cbMethod.addItem('Least Norm 1','ln1')
        ui.cbMethod.addItem('Least Norm 2', 'ln2')
        ui.cbMethod.addItem('Least Norms 1, 2' , 'ln12')


        # LOSS Type
        ui.cbLossType.addItem('Mean Square Error', 'mse')
        ui.cbLossType.addItem('Soft Margin Loss', 'soft')
        ui.cbLossType.addItem('Norm', 'norm')
        ui.cbLossType.addItem('Mean', 'mean')

        # Optimization
        ui.cbOptim.addItem('Adam', 'adam')
        ui.cbOptim.addItem('SGD', 'sgd')

        # Device
        ui.cbDevice.addItem("Auto", torch.cuda.is_available())
        ui.cbDevice.addItem("Just CPU", False)


        dialog.setWindowTitle("easy fMRI Gradient Encoding Analysis (Session Level) - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnRef.clicked.connect(self.btnRefresh_click)
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
                        print("Labels: ", Labels)
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

                    # Subject
                    ui.txtSubject.clear()
                    ui.txtSubjectVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")
                        print("Number of subjects: ", np.shape(np.unique(data["subject"]))[0])
                        values = np.unique(data["subject"])
                        for val in values:
                            ui.txtSubjectVal.addItem(str(val))

                    # Run
                    ui.txtRun.clear()
                    ui.txtRunVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("run")
                        values = np.unique(data["run"])
                        for val in values:
                            ui.txtRunVal.addItem(str(val))

                    # Counter
                    ui.txtCounter.clear()
                    ui.txtCounterVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("counter")
                        values = np.unique(data["counter"])
                        for val in values:
                            ui.txtCounterVal.addItem(str(val))

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")

                    # Task
                    ui.txtTask.clear()
                    ui.txtTaskVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")
                        values = np.unique(np.asarray(data["task"]))
                        for val in values:
                            ui.txtTaskVal.addItem(str(reshape_condition_cell(val)))

                    ui.txtInFile.setText(filename)
                    print("DONE.")
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")


    def btnRefresh_click(self):
        filename = ui.txtInFile.text()
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

                    # Subject
                    ui.txtSubject.clear()
                    ui.txtSubjectVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")
                        values = np.unique(data["subject"])
                        for val in values:
                            ui.txtSubjectVal.addItem(str(val))

                    # Run
                    ui.txtRun.clear()
                    ui.txtRunVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("run")
                        values = np.unique(data["run"])
                        for val in values:
                            ui.txtRunVal.addItem(str(val))

                    # Counter
                    ui.txtCounter.clear()
                    ui.txtCounterVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("counter")
                        values = np.unique(data["counter"])
                        for val in values:
                            ui.txtCounterVal.addItem(str(val))

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")

                    # Task
                    ui.txtTask.clear()
                    ui.txtTaskVal.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")
                        values = np.unique(data["task"])
                        for val in values:
                            ui.txtTaskVal.addItem(str(reshape_condition_cell(val)))

                    ui.txtInFile.setText(filename)
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
        msgBox      = QMessageBox()
        tStart      = time.time()
        Method      = ui.cbMethod.currentData()
        LossType    = ui.cbLossType.currentData()
        Optim       = ui.cbOptim.currentData()

        try:
            Epoch = np.int32(ui.txtIter.text())
        except:
            msgBox.setText("Number of iteration is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            BatchSize = np.int32(ui.txtBatch.text())
        except:
            msgBox.setText("Number of batch is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            ReportStep = np.int32(ui.txtReportStep.text())
        except:
            msgBox.setText("Number of Report Step is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            LearningRate = np.float32(ui.txtRate.text())
        except:
            msgBox.setText("Number of Report Step is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            LassoAlpha = np.float32(ui.txtLParam.text())
        except:
            msgBox.setText("Number of Lasso Parameter is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        try:
            ElasticLambda1 = np.float32(ui.txtEL1.text())
        except:
            msgBox.setText("Number of Elastic Lambda 1 is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            ElasticAlpha = np.float32(ui.txtEL2.text())
        except:
            msgBox.setText("Number of Elastic Lambda 2 is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            RidgeReg = np.float32(ui.txtRRP.text())
        except:
            msgBox.setText("Number of Ridge Regression Parameter is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if not ui.cbCov.isChecked() and not ui.cbCorr.isChecked():
            msgBox.setText("At least, you must select one metric!")
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
        # Task Val
        if not len(ui.txtTaskVal.currentText()):
                msgBox.setText("Please enter Task value!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            TaskIDTitle = ui.txtTaskVal.currentText()
        except:
            msgBox.setText("Task value is wrong!")
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

        for ttlinx, ttl in enumerate(TaskTitleUnique):
            if TaskIDTitle == ttl:
                TaskID = ttlinx + 1
                break

        OutData["Task"] = TaskIDTitle

        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Subject Val
        if not len(ui.txtSubjectVal.currentText()):
            msgBox.setText("Please enter Subject value!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubID = np.int32(ui.txtSubjectVal.currentText())
        except:
            msgBox.setText("Subject value is wrong!")
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
        OutData["SubjectID"] = SubID

        # Run
        if not len(ui.txtRun.currentText()):
            msgBox.setText("Please enter Run variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Run Val
        if not len(ui.txtRunVal.currentText()):
            msgBox.setText("Please enter Run value!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            RunID = np.int32(ui.txtRunVal.currentText())
        except:
            msgBox.setText("Run value is wrong!")
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
        OutData["RunID"] = RunID

        # Counter
        if not len(ui.txtCounter.currentText()):
            msgBox.setText("Please enter Counter variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Counter Val
        if not len(ui.txtCounterVal.currentText()):
            msgBox.setText("Please enter Counter value!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            ConID = np.int32(ui.txtCounterVal.currentText())
        except:
            msgBox.setText("Counter value is wrong!")
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
        OutData["CounterID"] = ConID


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

        # Select Task
        TaskIndex = np.where(Task == TaskID)
        Design  = Design[TaskIndex,:][0]
        X       = X[TaskIndex,:][0]
        L       = L[TaskIndex]
        Sub     = Sub[TaskIndex]
        Run     = Run[TaskIndex]
        Con     = Con[TaskIndex]
        # Select Subject
        SubIndex = np.where(Sub == SubID)
        Design  = Design[SubIndex,:][0]
        X       = X[SubIndex,:][0]
        L       = L[SubIndex]
        Run     = Run[SubIndex]
        Con     = Con[SubIndex]
        # Select Counter
        ConIndex = np.where(Con == ConID)
        Design  = Design[ConIndex,:][0]
        X       = X[ConIndex,:][0]
        L       = L[ConIndex]
        Run     = Run[ConIndex]
        # Select Run
        RunIndex = np.where(Run == RunID)
        Design  = Design[RunIndex,:][0]
        X       = X[RunIndex,:][0]
        L       = L[RunIndex]           # This will only use in supervised methods
        LUnique = np.unique(L)
        LNum    = np.shape(LUnique)[0]
        OutData["Label"] = LUnique
        OutData["ModelAnalysis"] = "PyTorch.Session.Gradient.RSA." + ui.cbMethod.currentText()


        if np.shape(X)[0] == 0:
            msgBox.setText("The selected data is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.cbScale.isChecked():
            X = preprocessing.scale(X)
            print("Data is scaled to N(0,1).")
        print("Running Gradient RSA ...")
        # RSA Method
        OutData['Method'] = dict()
        OutData['Method']['Method']         = Method
        OutData['Method']['LossType']       = LossType
        OutData['Method']['Optimization']   = Optim
        OutData['Method']['LearningRate']   = LearningRate
        OutData['Method']['Epoch']          = Epoch
        OutData['Method']['BatchSize']      = BatchSize
        OutData['Method']['ReportStep']     = ReportStep
        OutData['Method']['RidgeAlpha']     = RidgeReg
        OutData['Method']['ElaticLambda1']  = ElasticLambda1
        OutData['Method']['ElaticAlpha']    = ElasticAlpha
        OutData['Method']['LassoAlpha']     = LassoAlpha
        OutData['Method']['Verbose']        = ui.cbVerbose.isChecked()

        rsa = GrRSA(method=Method,loss_type=LossType, optim=Optim, learning_rate=LearningRate, epoch=Epoch, \
                    batch_size=BatchSize, report_step=ReportStep, ridge_param=RidgeReg, elstnet_l1_ratio=ElasticLambda1,\
                    elstnet_alpha=ElasticAlpha, lasso_alpha=LassoAlpha, verbose=ui.cbVerbose.isChecked(),\
                    gpu_enable=ui.cbDevice.currentData(),normalization=False)



        Betas, Eps, loss_vec, MSE, Performacne, _ = rsa.fit(data_vals=X, design_vals=Design)
        OutData["LossVec"] = loss_vec
        OutData["MSE"] = MSE
        OutData["Performance"] = Performacne
        print("MSE: ", OutData["MSE"])

        if ui.cbBeta.isChecked():
            OutData["Betas"]  = Betas
            OutData["Eps"]    = Eps
        # Calculate Results
        if ui.cbCorr.isChecked():
            print("Calculating Correlation ...")
            Corr = np.corrcoef(Betas)
            corClass = SimilarityMatrixBetweenClass(Corr)
            OutData["Correlation"]      = Corr
            OutData["Correlation_min"]  = corClass.min()
            OutData["Correlation_max"]  = corClass.max()
            OutData["Correlation_std"]  = corClass.std()
            OutData["Correlation_mean"] = corClass.mean()

        if ui.cbCov.isChecked():
            print("Calculating Covariance ...")
            Cov = np.cov(Betas)
            covClass = SimilarityMatrixBetweenClass(Cov)
            OutData["Covariance"]       = Cov
            OutData["Covariance_min"]   = covClass.min()
            OutData["Covariance_max"]   = covClass.max()
            OutData["Covariance_std"]   = covClass.std()
            OutData["Covariance_mean"]  = covClass.mean()


        # Calculating Distance Matrix
        dis = np.zeros((np.shape(Betas)[0], np.shape(Betas)[0]))

        for i in range(np.shape(Betas)[0]):
            for j in range(i + 1, np.shape(Betas)[0]):
                dis[i, j] = 1 - np.dot(Betas[i, :], Betas[j, :].T)
                dis[j, i] = dis[i, j]
        OutData["DistanceMatrix"] = dis
        Z = linkage(dis)
        OutData["Linkage"] = Z


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
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=45)
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize)
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
                    plt.title('Correlation (' + ui.cbMethod.currentText() + \
                               ')\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
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
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=45)
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize)
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
                    plt.title('Covariance (' + ui.cbMethod.currentText() + \
                               ')\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))

                plt.show()

            fig3 = plt.figure(figsize=(25, 10), )
            if len(ui.txtTitleDen.text()):
                plt.title(ui.txtTitleDen.text())
            else:
                plt.title('Similarity Analysis (' + ui.cbMethod.currentText() + \
                          ')\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
            dn = dendrogram(Z, labels=labels, leaf_font_size=FontSize, color_threshold=1)
            plt.show()

        print("DONE.")
        msgBox.setText("Gradient Representational Similarity Analysis (RSA) is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnRedraw_click(self):
        msgBox = QMessageBox()

        ofile = LoadFile("Load result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))

        FontSize = ui.txtFontSize.value()

        if len(ofile):
            try:
                Res     = mainIO_load(ofile)
                LUnique = reshape_1Dvector(Res["Label"])[0]
                LNum    = np.shape(LUnique)[0]
                SubID   = Res["SubjectID"]
                ConID   = Res["CounterID"]
                RunID   = Res["RunID"]
                TaskIDTitle = reshape_condition_cell(Res["Task"])
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
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=45)
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize)
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
                    plt.title('Gradient RSA: Correlation\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
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
                ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=45)
                ax.set_yticklabels(labels, minor=False, fontsize=FontSize)
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
                    plt.title('Gradient RSA: Covariance\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
                plt.show()

            fig3 = plt.figure(figsize=(25, 10), )
            dn = dendrogram(Res["Linkage"], labels=labels, leaf_font_size=FontSize, color_threshold=1)
            if len(ui.txtTitleDen.text()):
                plt.title(ui.txtTitleDen.text())
            else:
                plt.title('Gradient RSA: Similarity Analysis\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
            plt.show()

    # def btnRedraw_clickq(self):
    #     msgBox = QMessageBox()
    #
    #     ofile = LoadFile("Load result file ...", ['Result files (*.ezx *.mat)'], 'ezx',\
    #                          os.path.dirname(ui.txtOutFile.text()))
    #     if len(ofile):
    #         try:
    #             Res     = mainIO_load(ofile)
    #             LUnique = Res["Label"][0]
    #             LNum    = np.shape(LUnique)[0]
    #             SubID   = Res["SubjectID"]
    #             ConID   = Res["CounterID"]
    #             RunID   = Res["RunID"]
    #             TaskIDTitle = Res["Task"][0]
    #         except:
    #             print("Cannot load result file!")
    #             msgBox.setText("Cannot load result file!")
    #             msgBox.setIcon(QMessageBox.Critical)
    #             msgBox.setStandardButtons(QMessageBox.Ok)
    #             msgBox.exec_()
    #             return False
    #
    #         if ui.cbCorr.isChecked():
    #             try:
    #                 Corr = Res["Correlation"]
    #             except:
    #                 print("Cannot load Correlation variable!")
    #                 msgBox.setText("Cannot load Correlation variable!")
    #                 msgBox.setIcon(QMessageBox.Critical)
    #                 msgBox.setStandardButtons(QMessageBox.Ok)
    #                 msgBox.exec_()
    #                 return False
    #             fig1 = plt.figure(num=None, figsize=(5, 5), dpi=100)
    #             plt.pcolor(Corr, vmin=-0.1, vmax=1)
    #             plt.xlim([0, LNum])
    #             plt.ylim([0, LNum])
    #             plt.colorbar()
    #             ax = plt.gca()
    #             ax.set_aspect(1)
    #             plt.title('Correlation (' + MethodTitle(str(Res['Method']['Type'][0][0][0])) + \
    #                       ')\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
    #             plt.show()
    #
    #
    #         if ui.cbCov.isChecked():
    #             try:
    #                 Cov = Res["Covariance"]
    #             except:
    #                 print("Cannot load Covariance variable!")
    #                 msgBox.setText("Cannot load Covariance variable!")
    #                 msgBox.setIcon(QMessageBox.Critical)
    #                 msgBox.setStandardButtons(QMessageBox.Ok)
    #                 msgBox.exec_()
    #                 return False
    #             fig2 = plt.figure(num=None, figsize=(5, 5), dpi=100)
    #             plt.pcolor(Cov)
    #             plt.xlim([0, LNum])
    #             plt.ylim([0, LNum])
    #             plt.colorbar()
    #             ax = plt.gca()
    #             ax.set_aspect(1)
    #             plt.title('Covariance (' + MethodTitle(str(Res['Method']['Type'][0][0][0])) + \
    #                       ')\nTask: %s\nSub: %d, Counter: %d, Run: %d' % (TaskIDTitle, SubID, ConID, RunID))
    #             plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMAGradientEncodingAnalysis.show(frmMAGradientEncodingAnalysis)
    sys.exit(app.exec_())