#!/usr/bin/env python3
import os
import sys
import time
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *

from MVPA.GPUSVM import GPUSVM
from sklearn.metrics import accuracy_score, precision_score, average_precision_score, f1_score, recall_score
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from sklearn import preprocessing
from GUI.frmMAGPUSVMGUI import *



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
        ui.btnConvert.clicked.connect(self.btnConvert_click)

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

        # Verbose
        verbose = ui.cbVerbose.isChecked()

        # Penalty
        penalty = ui.cbPenalty.isChecked()

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

            TrX = InData[ui.txtITrData.currentText()]
            TeX = InData[ui.txtITeData.currentText()]
            TrL = InData[ui.txtITrLabel.currentText()][0]
            TeL = InData[ui.txtITeLabel.currentText()][0]

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
                clf = GPUSVM(epoch=epoch, batchsize=batch, learningrate=lr, C=C, \
                             normalization=False, optim=ui.cbOptim.currentData())
                print("FoldID = " + str(currFID) + " is training ...")
                clf.train(TrX, TrL)
                PrL = clf.TrainPredict
                if OutModel is not None:
                    clf.save(OutModel)
                    print("FoldID = " + str(currFID) + " Model is saved: " + OutModel)

                print("FoldID = " + str(currFID) + " is testing ...")
                clf.test(TeX, TeL)
                PeL = clf.TestPredict

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
        print("DONE.")
        msgBox.setText("GPU Support Vector Classification is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMASVM.show(frmMASVM)
    sys.exit(app.exec_())