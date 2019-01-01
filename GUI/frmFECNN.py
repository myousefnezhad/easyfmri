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
import torch
import time
import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile, SaveFile
from GUI.frmFECNNGUI import *
from GUI.frmCNNDialog import frmConv, frmAF, frmPool
from Network.CNN import CNN
from Base.utility import Str2Bool

def convertKernel(kerstr):
    ker = str.lower(kerstr).replace('[', '').replace(']', '').replace(')', '').replace('(', '').replace(';', ',').split(',')
    if len(ker) == 1:
        return int(ker[0])
    elif len(ker) == 3:
        return (int(ker[0]), int(ker[1]), int(ker[2]))
    else:
        raise Exception("Kernel format is wrong: " + kerstr)

def createModel(table):
    if table.rowCount() <= 0:
        return None
    model = list()
    for i in range(table.rowCount()):
        if   table.item(i, 0).text() == "conv3":
           model.append([table.item(i, 0).text(), int(table.item(i, 1).text()), convertKernel(table.item(i, 2).text()),\
                         int(table.item(i, 3).text()), int(table.item(i, 4).text()), int(table.item(i, 5).text()), \
                         int(table.item(i, 6).text()), Str2Bool(table.item(i, 7).text())])
        elif table.item(i, 0).text() == "max3" or table.item(i, 0).text() == "avg3":
            model.append([table.item(i, 0).text(), int(table.item(i, 2).text())])
        elif table.item(i, 0).text() == "afun":
            model.append([table.item(i, 0).text(), table.item(i, 2).text()])
        else:
            raise Exception("Unsupported module: " + table.item(i, 0).text())
    return model



class frmFECNN(Ui_frmFECNN):
    ui = Ui_frmFECNN()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFECNN()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)

        ui.tbModel.setRowCount(0)
        ui.tbModel.setColumnCount(8)
        ui.tbModel.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        ui.tbModel.setHorizontalHeaderLabels(['Type', 'Out', 'Kernel', 'Stride', 'Padding', 'Dilation', 'Groups', 'Bias'])
        ui.tbModel.setColumnWidth(0, 80)
        ui.tbModel.setColumnWidth(1, 50)
        ui.tbModel.setColumnWidth(2, 100)
        ui.tbModel.setColumnWidth(3, 60)
        ui.tbModel.setColumnWidth(4, 80)
        ui.tbModel.setColumnWidth(5, 80)
        ui.tbModel.setColumnWidth(6, 80)
        ui.tbModel.setColumnWidth(8, 80)

        dialog.setWindowTitle("easy fMRI Convolutional Neural Network (CNN) - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnOutFile.clicked.connect(self.btnOutFile_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)
        ui.btnAddPool.clicked.connect(self.btnAddPool_click)
        ui.btnAddAF.clicked.connect(self.btnAddAF_click)
        ui.btnAddConv.clicked.connect(self.btnAddConv_click)
        ui.btnDelete.clicked.connect(self.btnDelete_click)
        ui.btnUp.clicked.connect(self.btnUp_click)
        ui.btnDown.clicked.connect(self.btnDown_click)
        ui.btnSaveNet.clicked.connect(self.btnSaveNet_click)
        ui.btnLoadNet.clicked.connect(self.btnLoadNet_click)
        ui.btnClearNet.clicked.connect(self.btnClearNet_click)


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

                    # mLabel
                    ui.txtmLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtmLabel.addItem(key)
                        if key == "mlabel":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtmLabel.setCurrentText("mlabel")
                    ui.cbmLabel.setChecked(HasDefualt)

                    # Coordinate
                    ui.txtCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCol.setCurrentText("coordinate")
                    ui.cbCol.setChecked(HasDefualt)

                    # Design
                    ui.txtDM.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtDM.addItem(key)
                        if key == "design":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtDM.setCurrentText("design")
                    ui.cbDM.setChecked(HasDefualt)

                    # Subject
                    ui.txtSubject.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtSubject.addItem(key)
                        if key == "subject":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtSubject.setCurrentText("subject")


                    # Task
                    ui.txtTask.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtTask.addItem(key)
                        if key == "task":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtTask.setCurrentText("task")
                    ui.cbTask.setChecked(HasDefualt)

                    # Run
                    ui.txtRun.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtRun.addItem(key)
                        if key == "run":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtRun.setCurrentText("run")
                    ui.cbRun.setChecked(HasDefualt)

                    # Counter
                    ui.txtCounter.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCounter.addItem(key)
                        if key == "counter":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCounter.setCurrentText("counter")
                    ui.cbCounter.setChecked(HasDefualt)

                    # Condition
                    ui.txtCond.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCond.addItem(key)
                        if key == "condition":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCond.setCurrentText("condition")
                    ui.cbCond.setChecked(HasDefualt)

                    # NScan
                    ui.txtScan.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtScan.addItem(key)
                        if key == "nscan":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtScan.setCurrentText("nscan")
                    ui.cbNScan.setChecked(HasDefualt)

                    # set number of features
                    data = io.loadmat(filename)
                    XShape = np.shape(data[ui.txtData.currentText()])

                    print("Data shape: ", XShape)

                    if len(XShape) != 4:
                        msgBox = QMessageBox()
                        msgBox.setText("This method just supports 4D datasets!")
                        msgBox.setIcon(QMessageBox.Warning)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                    else:
                        print("Data shape is okay.")

                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()


        try:
            Threshold = np.float64(ui.txtThreshold.text())
        except:
            msgBox.setText("Standard deviation threshold value is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            net_model = createModel(ui.tbModel)
        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if net_model is None:
            msgBox.setText("Please create a network model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
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

        if ui.rbScale.isChecked() == True and ui.rbALScale.isChecked() == False:
            msgBox.setText("Subject Level Normalization is just available for Subject Level Analysis!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        InData = io.loadmat(InFile)
        OutData = dict()
        OutData["imgShape"] = InData["imgShape"]

        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            X = InData[ui.txtData.currentText()]

            if ui.cbScale.isChecked() and (not ui.rbScale.isChecked()):
                X = X - X.mean()
                X = X / X.std()
                print("Whole of data is scaled X~N(0,1).")
        except:
            print("Cannot load data")
            return

        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            Subject = InData[ui.txtSubject.currentText()]
            OutData[ui.txtOSubject.text()] = Subject
        except:
            print("Cannot load Subject ID")
            return

        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        OutData[ui.txtOLabel.text()] = InData[ui.txtLabel.currentText()]


        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOTask.text()] = InData[ui.txtTask.currentText()]

        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtORun.text()] = InData[ui.txtRun.currentText()]


        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOCounter.text()] = InData[ui.txtCounter.currentText()]

        # Matrix Label
        if ui.cbmLabel.isChecked():
            if not len(ui.txtmLabel.currentText()):
                msgBox.setText("Please enter Matrix Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOmLabel.text()] = InData[ui.txtmLabel.currentText()]

        # Design
        if ui.cbDM.isChecked():
            if not len(ui.txtDM.currentText()):
                msgBox.setText("Please enter Design Matrix variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtODM.text()] = InData[ui.txtDM.currentText()]

        # Coordinate
        if ui.cbCol.isChecked():
            if not len(ui.txtCol.currentText()):
                msgBox.setText("Please enter Coordinator variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOCol.text()] = InData[ui.txtCol.currentText()]

        # Condition
        if ui.cbCond.isChecked():
            if not len(ui.txtCond.currentText()):
                msgBox.setText("Please enter Condition variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOCond.text()] = InData[ui.txtCond.currentText()]

        # Number of Scan
        if ui.cbNScan.isChecked():
            if not len(ui.txtScan.currentText()):
                msgBox.setText("Please enter Number of Scan variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOScan.text()] = InData[ui.txtScan.currentText()]

        if ui.rbALScale.isChecked():
            print("Partition data to subject level ...")
            SubjectUniq = np.unique(Subject)
            X_Sub = list()
            for subj in SubjectUniq:
                if ui.cbScale.isChecked() and ui.rbScale.isChecked():
                    extractXsub = X[np.where(Subject == subj)[1], :]
                    extractXsub = extractXsub - extractXsub.mean()
                    extractXsub = extractXsub / extractXsub.std()
                    X_Sub.append(extractXsub)
                    print("Data in subject level is scaled, X_" + str(subj) + "~N(0,1).")
                else:
                    X_Sub.append(X[np.where(Subject == subj)[1],:])
                print("Subject ", subj, " is extracted from data.")
            print("Running CNN in subject level ...")
            X_Sub_PCA = list()
            lenPCA    = len(X_Sub)

            for xsubindx, xsub in enumerate(X_Sub):
                net = CNN(net_model)
                if ui.rbMat.isChecked():
                    xsub_tran = net.tonumpy(net.vectorize(net(torch.Tensor(np.expand_dims(xsub, axis=1)))))
                else:
                    xsub_tran = net.tonumpy(net(torch.Tensor(np.expand_dims(xsub,axis=1))))
                X_Sub_PCA.append(xsub_tran)
                print("CNN: ", xsubindx + 1, " of ", lenPCA, " is done. Shape: " + str(np.shape(xsub_tran)))

            print("Data integration ... ")
            X_new = None
            for xsubindx, xsub in enumerate(X_Sub_PCA):
                X_new = np.concatenate((X_new, xsub)) if X_new is not None else xsub
                print("Integration: ", xsubindx + 1, " of ", lenPCA, " is done.")
            if not ui.rbMat.isChecked():
                X_new = X_new[:,0,:,:,:]

            # Apply Thresholding
            print("Data shape before thresholding: ", np.shape(X_new))
            X_new_th = X_new
            if ui.rbMat.isChecked() and ui.cbThreshold.isChecked():
                index = np.where(np.std(X_new, axis=0) >= Threshold)
                X_new_index = X_new[:, index]
                print("Standard deviation thresholding ...")
                X_new_th = None
                for xx_new in X_new_index:
                    X_new_th = xx_new if X_new_th is None else np.concatenate((X_new_th, xx_new), axis=0)

            # Apply Normalization
            if ui.rbMat.isChecked() and ui.cbOutNormal.isChecked():
                X_new_th = X_new_th - np.mean(X_new_th)
                X_new_th = X_new_th / np.std(X_new_th)
                print("Output data is normalized!")

            OutData[ui.txtOData.text()] = X_new_th
        else:
            print("Running CNN ...")
            net = CNN(net_model)
            if ui.rbMat.isChecked():
                X_new = net.tonumpy(net.vectorize(net(torch.Tensor(np.expand_dims(X, axis=1)))))
            else:
                X_new = net.tonumpy(net(torch.Tensor(np.expand_dims(X, axis=1))))
            print("CNN is done. Shape: " + str(np.shape(X_new)))

            # Apply Thresholding
            print("Data shape before thresholding: ", np.shape(X_new))
            X_new_th = X_new
            if ui.rbMat.isChecked() and ui.cbThreshold.isChecked():
                index = np.where(np.std(X_new, axis=0) >= Threshold)
                X_new_index = X_new[:, index]
                print("Standard deviation thresholding ...")
                X_new_th = None
                for xx_new in X_new_index:
                    X_new_th = xx_new if X_new_th is None else np.concatenate((X_new_th, xx_new), axis=0)

            # Apply Normalization
            if ui.rbMat.isChecked() and ui.cbOutNormal.isChecked():
                X_new_th = X_new_th - np.mean(X_new_th)
                X_new_th = X_new_th / np.std(X_new_th)
                print("Output data is normalized!")

            OutData[ui.txtOData.text()] = X_new_th

        print("Saving ...")
        print("Final data shape: ", np.shape(OutData[ui.txtOData.text()]))
        io.savemat(ui.txtOutFile.text(), mdict=OutData)
        print("DONE.")
        msgBox.setText("CNN is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnAddPool_click(self):
        frmpool = frmPool()
        if frmpool.isAdd:
            id = ui.tbModel.rowCount()
            ui.tbModel.insertRow(id)
            typeItm = QTableWidgetItem(frmpool.pool)
            typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 0, typeItm)
            keneItm = QTableWidgetItem(str(frmpool.kernel))
            keneItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 2, keneItm)

    def btnAddAF_click(self):
        frmaf = frmAF()
        if frmaf.isAdd:
            id = ui.tbModel.rowCount()
            ui.tbModel.insertRow(id)
            typeItm = QTableWidgetItem("afun")
            typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 0, typeItm)
            FunItm = QTableWidgetItem(frmaf.func)
            FunItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 2, FunItm)


    def btnAddConv_click(self):
        frmconv = frmConv()
        if frmconv.isAdd:
            id = ui.tbModel.rowCount()
            ui.tbModel.insertRow(id)
            typeItm = QTableWidgetItem("conv3")
            typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 0, typeItm)

            OutItm = QTableWidgetItem(str(frmconv.Channel))
            typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 1, OutItm)

            KerItm = QTableWidgetItem(frmconv.Kernel)
            KerItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 2, KerItm)

            StrItm = QTableWidgetItem(str(frmconv.Stride))
            StrItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 3, StrItm)

            PadItm = QTableWidgetItem(str(frmconv.Padding))
            PadItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 4, PadItm)

            DilItm = QTableWidgetItem(str(frmconv.Dilation))
            DilItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 5, DilItm)

            GrpItm = QTableWidgetItem(str(frmconv.Groups))
            GrpItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 6, GrpItm)

            BiaItm = QTableWidgetItem(str(frmconv.Bias))
            BiaItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            ui.tbModel.setItem(id, 7, BiaItm)

    def btnDelete_click(self):
        currentRowID = ui.tbModel.currentRow()
        if currentRowID >= 0:
            ui.tbModel.removeRow(currentRowID)


    def btnUp_click(self):
        row = ui.tbModel.currentRow()
        column = ui.tbModel.currentColumn()
        if row > 0:
            ui.tbModel.insertRow(row - 1)
            for i in range(ui.tbModel.columnCount()):
                ui.tbModel.setItem(row - 1, i, ui.tbModel.takeItem(row + 1, i))
                ui.tbModel.setCurrentCell(row-1,column)
            ui.tbModel.removeRow(row+1)


    def btnDown_click(self):
        row = ui.tbModel.currentRow()
        column = ui.tbModel.currentColumn()
        if row < ui.tbModel.rowCount() - 1:
            ui.tbModel.insertRow(row + 2)
            for i in range(ui.tbModel.columnCount()):
               ui.tbModel.setItem(row + 2, i, ui.tbModel.takeItem(row, i))
               ui.tbModel.setCurrentCell(row + 2, column)
            ui.tbModel.removeRow(row)

    def btnSaveNet_click(self):
        msgBox = QMessageBox()
        try:
            net_model = createModel(ui.tbModel)
        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if net_model is None:
            msgBox.setText("Please create a network model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            ofile = SaveFile("Save network model ...",['Model files (*.model)'],'model', os.path.dirname(ui.txtOutFile.text()))
            if len(ofile):
                net = CNN(net_model)
                net.save(ofile)
                print("Model is saved!")
        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


    def btnClearNet_click(self):
        ui.tbModel.clear()
        ui.tbModel.setRowCount(0)
        ui.tbModel.setHorizontalHeaderLabels(['Type', 'Out', 'Kernel', 'Stride', 'Padding', 'Dilation', 'Groups', 'Bias'])
        ui.tbModel.setColumnWidth(0, 80)
        ui.tbModel.setColumnWidth(1, 50)
        ui.tbModel.setColumnWidth(2, 100)
        ui.tbModel.setColumnWidth(3, 60)
        ui.tbModel.setColumnWidth(4, 80)
        ui.tbModel.setColumnWidth(5, 80)
        ui.tbModel.setColumnWidth(6, 80)
        ui.tbModel.setColumnWidth(8, 80)


    def btnLoadNet_click(self):
        ifile = LoadFile("Load network model ...",['Model files (*.model)'],'model', os.path.dirname(ui.txtOutFile.text()))
        if len(ifile):
            net = CNN(ifile)
            ui.tbModel.clear()
            ui.tbModel.setRowCount(0)
            ui.tbModel.setHorizontalHeaderLabels(
                ['Type', 'Out', 'Kernel', 'Stride', 'Padding', 'Dilation', 'Groups', 'Bias'])

            try:

                for moduleID, module in enumerate(net.model):
                    if   module[0] == "conv3":
                        id = ui.tbModel.rowCount()
                        ui.tbModel.insertRow(id)
                        typeItm = QTableWidgetItem(module[0])
                        typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 0, typeItm)

                        OutItm = QTableWidgetItem(str(module[1]))
                        typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 1, OutItm)

                        KerItm = QTableWidgetItem(str(module[2]))
                        KerItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 2, KerItm)

                        StrItm = QTableWidgetItem(str(module[3]))
                        StrItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 3, StrItm)

                        PadItm = QTableWidgetItem(str(module[4]))
                        PadItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 4, PadItm)

                        DilItm = QTableWidgetItem(str(module[5]))
                        DilItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 5, DilItm)

                        GrpItm = QTableWidgetItem(str(module[6]))
                        GrpItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 6, GrpItm)


                        BiaItm = QTableWidgetItem(str(bool(module[7])))
                        BiaItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 7, BiaItm)

                    elif module[0] == "afun":
                        id = ui.tbModel.rowCount()
                        ui.tbModel.insertRow(id)
                        typeItm = QTableWidgetItem(module[0])
                        typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 0, typeItm)
                        FunItm = QTableWidgetItem(module[1])
                        FunItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 2, FunItm)

                    elif module[0] == "max3" or module[0] == "avg3":
                        id = ui.tbModel.rowCount()
                        ui.tbModel.insertRow(id)
                        typeItm = QTableWidgetItem(module[0])
                        typeItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 0, typeItm)
                        keneItm = QTableWidgetItem(str(module[1]))
                        keneItm.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        ui.tbModel.setItem(id, 2, keneItm)

                    else:
                        raise  Exception("Error in loading modules! ID = " + str(moduleID))
            except Exception as e:
                msgBox = QMessageBox()
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFECNN.show(frmFECNN)
    sys.exit(app.exec_())