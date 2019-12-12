# Copyright (c) 2014--2019 Muhammad Yousefnezhad
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

from MVPA.GPUSVM import GPUSVM
from sklearn.metrics import accuracy_score, precision_score, average_precision_score, f1_score, recall_score, confusion_matrix, classification_report
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from sklearn import preprocessing
from GUI.frmMAGPUSVMGUI import *

# Plot
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

class frmMASVM(Ui_frmMAGPUSVM):
    ui = Ui_frmMAGPUSVM()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMAGPUSVM()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

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

        # Optimization
        ui.cbOptim.addItem("SGD", 'sgd')
        ui.cbOptim.addItem("Adam", "adam")

        # Kernel
        ui.cbKernel.addItem("Linear", "linear")
        ui.cbKernel.addItem("RBF", "rbf")

        dialog.setWindowTitle("easy fMRI GPU Support Vector Classification - V" + getVersion() + "B" + getBuild())

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
        ui.btnOutModel.clicked.connect(self.btnOutModel_click)
        ui.btnOutSim.clicked.connect(self.btnOutSim_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)
        ui.btnRedraw.clicked.connect(self.btnRedraw_click)
        ui.btnShowFilterContent.clicked.connect(self.btnShowFilterContent_click)

    def btnShowFilterContent_click(self):
        msgBox = QMessageBox()
        filename = ui.txtInFile.text()
        if len(filename):
            if os.path.isfile(filename):
                try:
                    InData = io.loadmat(filename)
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
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                            os.path.dirname(ui.txtInFile.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = io.loadmat(filename)
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

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")

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


                    ui.txtInFile.setText(filename)
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

    def btnOutModel_click(self):
        ofile = SaveFile("Save SK model file ...",['Model files (*.model)'],'model',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutModel.setText(ofile)

    def btnOutSim_click(self):
        ofile = SaveFile("Save data file ...",['data files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutSim.setText(ofile)


    def btnConvert_click(self):
        tme = time.time()
        msgBox = QMessageBox()

        try:
            FoldFrom = np.int32(ui.txtFoldFrom.text())
            FoldTo   = np.int32(ui.txtFoldTo.text())
        except:
            print("Please check fold parameters!")
            return

        if FoldTo < FoldFrom:
            print("Please check fold parameters!")
            return

        # Similarity Analysis
        SimFile = ui.txtOutSim.text()
        if not len(SimFile):
            SimFile = None

        # Verbose
        verbose = ui.cbVerbose.isChecked()

        # Norm 2
        Norm2 = ui.cbNorm2.isChecked()

        # Norm 1
        Norm1 = ui.cbNorm1.isChecked()

        # Kernel
        kernel = ui.cbKernel.currentData()


        # Gamma
        try:
            Gamma = float(ui.txtGamma.text())
            assert Gamma >= 0
        except:
            msgBox.setText("Gamma is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if Gamma == 0:
            Gamma = None

        # Degree
        try:
            Degree = int(ui.txtDegree.text())
            assert Degree > 0
        except:
            msgBox.setText("Degree is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # C
        try:
            C = np.float(ui.txtC.text())
        except:
            msgBox.setText("C is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # epoch
        try:
            epoch = np.int32(ui.txtEpoch.text())
        except:
            msgBox.setText("Epoch is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # batch
        try:
            batch = np.int32(ui.txtBatch.text())
        except:
            msgBox.setText("Batch size is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # lr
        try:
            lr = np.float(ui.txtRate.text())
        except:
            msgBox.setText("Learning Rate is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Percentage Rate
        try:
            perrate = np.float(ui.txtPer.text())
        except:
            msgBox.setText("C is wrong!")
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
            print("Class filter is wrong!")
            msgBox.setText("Class filter is wrong!")
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
        OutData["ModelAnalysis"] = "GPUSVM"

        SimData = dict()
        SimW    = None



        for fold in range(FoldFrom, FoldTo + 1):
            # OutModel
            OutModel = ui.txtOutModel.text()
            if not len(OutModel):
                OutModel = None
            else:
                OutModel = OutModel.replace("$FOLD$", str(fold))

            # InFile
            InFile = ui.txtInFile.text()
            InFile = InFile.replace("$FOLD$", str(fold))
            InFileList.append(InFile)
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

            InData = io.loadmat(InFile)
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
                SimData["labels"] = labels
            except:
                msgBox.setText("Condition value is wrong!")
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

            FontSize = ui.txtFontSize.value()

            TrX = InData[ui.txtITrData.currentText()]
            TeX = InData[ui.txtITeData.currentText()]
            TrL = InData[ui.txtITrLabel.currentText()][0]
            TeL = InData[ui.txtITeLabel.currentText()][0]

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
            try:
                clf = GPUSVM(epoch=epoch, batchsize=batch, learningrate=lr, C=C, normalization=False, \
                             optim=ui.cbOptim.currentData(), kernel=kernel, gamma=Gamma, degree=Degree)
                print("FoldID = " + str(currFID) + " is training ...")
                clf.train(X=TrX, Y=TrL, verbose=verbose, enable_norm2=Norm2, enable_norm1=Norm1, per_iteration=perrate)
                PrL = clf.TrainPredict

                if SimFile is not None:
                    simMat = np.dot(clf.parameters()["W"], np.transpose(clf.parameters()["W"]))
                    SimData["Sim" + str(fold)] = simMat
                    SimW = simMat if SimW is None else SimW + simMat


                if OutModel is not None:
                    clf.save(OutModel)
                    print("FoldID = " + str(currFID) + " Model is saved: " + OutModel)

                print("FoldID = " + str(currFID) + " is testing ...")
                clf.test(X=TeX, Y=TeL, verbose=verbose)
                PeL = clf.TestPredict

                OutData["fold" + str(currFID) + "_confusion_matrix"]      = confusion_matrix(TeL, PeL, np.unique(TeL))
                OutData["fold" + str(currFID) + "_classification_report"] = classification_report(TeL, PeL)
                print(OutData["fold" + str(currFID) + "_classification_report"])

            except Exception as e:
                print(e)
                msgBox = QMessageBox()
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

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
        OutData["Runtime"] = time.time() - tme
        print("Runtime: ", OutData["Runtime"])
        print("Saving ...")
        io.savemat(OutFile, mdict=OutData)

        if SimFile is not None:
            Cov = SimW - np.min(SimW) / (np.max(SimW) - np.min(SimW))
            SimData["SimMat"] = Cov
            Z = linkage(SimData["SimMat"])
            # Normalization Z
            zMin = np.min(Z[:, 2])
            zMax = np.max(Z[:, 2]) - zMin
            for zZ, _ in enumerate(Z):
                Z[zZ, 2] = (Z[zZ, 2] - zMin) / zMax
                Z[zZ, 2] += 0.1
            SimData["Linkage"] = Z
            io.savemat(SimFile, mdict=SimData)

            if ui.cbSimMatrix.isChecked():
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
                    plt.title('Similarity Analysis')
                plt.show()

            if ui.cbSimDend.isChecked():
                fig3 = plt.figure(figsize=(25, 10), )
                if len(ui.txtTitleDen.text()):
                    plt.title(ui.txtTitleDen.text())
                else:            #zMin -= 0.01

                    plt.title('Similarity Analysis')
                dn = dendrogram(Z, labels=labels, leaf_font_size=FontSize, color_threshold=1, count_sort=True, distance_sort=True)
                plt.show()

        print("DONE.")
        msgBox.setText("GPU Support Vector Classification is done.")
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

            # Condition
            if not len(ui.txtCond.currentText()):
                try:
                    labels = Res["labels"]
                except:
                    msgBox.setText("Cannot load labels!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

            # Z
            if not len(ui.txtCond.currentText()):
                try:
                    Z = Res["Linkage"]
                except:
                    msgBox.setText("Cannot load labels!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

            # SimMat
            if not len(ui.txtCond.currentText()):
                try:
                    Cov = Res["SimMat"]
                except:
                    msgBox.setText("Cannot load labels!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False

            if ui.cbSimMatrix.isChecked():
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
                    plt.title('Similarity Analysis')
                plt.show()

            if ui.cbSimDend.isChecked():
                fig3 = plt.figure(figsize=(25, 10), )
                dn = dendrogram(Res["Linkage"], labels=labels, leaf_font_size=FontSize, color_threshold=1)
                if len(ui.txtTitleDen.text()):
                    plt.title(ui.txtTitleDen.text())
                else:
                    plt.title('Similarity Analysis')
                plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMASVM.show(frmMASVM)
    sys.exit(app.exec_())