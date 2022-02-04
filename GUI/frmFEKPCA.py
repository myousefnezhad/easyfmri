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
import numpy as np
from PyQt5.QtWidgets import *
from GUI.frmFEKPCAGUI import *
from sklearn import preprocessing
from Base.dialogs import LoadFile, SaveFile
from sklearn.decomposition import KernelPCA
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector


class frmFEKPCA(Ui_frmFEKPCA):
    ui = Ui_frmFEKPCA()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmFEKPCA()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        # Kenel List
        ui.cbKernel.addItem("linear")
        ui.cbKernel.addItem("poly")
        ui.cbKernel.addItem("rbf")
        ui.cbKernel.addItem("sigmoid")
        ui.cbKernel.addItem("cosine")


        dialog.setWindowTitle("easy fMRI Kernel Principal Component Analysis (PCA) - V" + getVersion() + "B" + getBuild())
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
                    XShape = np.shape(data[ui.txtData.currentText()])
                    ui.txtNumFea.setMaximum(1)
                    ui.txtNumFea.setMaximum(XShape[1])
                    ui.txtNumFea.setValue(XShape[1])
                    ui.lblFeaNum.setText("1 ... " + str(XShape[1]))

                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")

    def btnOutFile_click(self):
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        # Kernel
        Kernel = ui.cbKernel.currentText()
        # Gamma
        try:
            Gamma = np.float(ui.txtGamma.text())
        except:
            msgBox.setText("Gamma is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Degree
        try:
            Degree = np.int32(ui.txtDegree.text())
        except:
            msgBox.setText("Degree is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Coef0
        try:
            Coef0 = np.float(ui.txtCoef0.text())
        except:
            msgBox.setText("Coef0 is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Alpha
        try:
            Alpha = np.int32(ui.txtAlpha.text())
        except:
            msgBox.setText("Alpha is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Tol
        try:
            Tol = np.float(ui.txtTole.text())
        except:
            msgBox.setText("Tolerance is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # MaxIte
        try:
            MaxIter = np.int32(ui.txtMaxIter.text())
        except:
            msgBox.setText("Maximum number of iterations is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if MaxIter <= 0:
            MaxIter = None
        # Number of Job
        try:
            NJob = np.int32(ui.txtJobs.text())
        except:
            msgBox.setText("The number of parallel jobs is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if NJob < -1 or NJob == 0:
            msgBox.setText("The number of parallel jobs must be -1 or greater than 0!")
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
        InData = mainIO_load(InFile)
        OutData = dict()
        OutData["imgShape"] = reshape_1Dvector(InData["imgShape"])
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            X = InData[ui.txtData.currentText()]

            if ui.cbScale.isChecked() and (not ui.rbScale.isChecked()):
                X = preprocessing.scale(X)
                print("Whole of data is scaled X~N(0,1).")
        except:
            print("Cannot load data")
            return
        try:
            NumFea = np.int32(ui.txtNumFea.text())
        except:
            msgBox.setText("Number of features is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if NumFea < 1:
            msgBox.setText("Number of features must be greater than zero!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if NumFea > np.shape(X)[1]:
            msgBox.setText("Number of features is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        # Subject
        if not len(ui.txtSubject.currentText()):
            msgBox.setText("Please enter Subject variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            Subject = InData[ui.txtSubject.currentText()]
            OutData[ui.txtOSubject.text()] = reshape_1Dvector(Subject)
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
        OutData[ui.txtOLabel.text()] = reshape_1Dvector(InData[ui.txtLabel.currentText()])
        # Task
        if ui.cbTask.isChecked():
            if not len(ui.txtTask.currentText()):
                msgBox.setText("Please enter Task variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOTask.text()] = reshape_1Dvector(InData[ui.txtTask.currentText()])
        # Run
        if ui.cbRun.isChecked():
            if not len(ui.txtRun.currentText()):
                msgBox.setText("Please enter Run variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtORun.text()] = reshape_1Dvector(InData[ui.txtRun.currentText()])
        # Counter
        if ui.cbCounter.isChecked():
            if not len(ui.txtCounter.currentText()):
                msgBox.setText("Please enter Counter variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            OutData[ui.txtOCounter.text()] = reshape_1Dvector(InData[ui.txtCounter.currentText()])
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
            OutData[ui.txtOScan.text()] = reshape_1Dvector(InData[ui.txtScan.currentText()])
        Models = dict()
        Models["Name"] = "KPCA"
        if ui.rbALScale.isChecked():
            print("Partition data to subject level ...")
            SubjectUniq = np.unique(Subject)
            X_Sub = list()
            for subj in SubjectUniq:
                if ui.cbScale.isChecked() and ui.rbScale.isChecked():
                    X_Sub.append(preprocessing.scale(X[np.where(Subject == subj)[1], :]))
                    print("Data in subject level is scaled, X_" + str(subj) + "~N(0,1).")
                else:
                    X_Sub.append(X[np.where(Subject == subj)[1],:])
                print("Subject ", subj, " is extracted from data.")
            print("Running KPCA in subject level ...")
            X_Sub_PCA = list()
            lenPCA    = len(X_Sub)
            for xsubindx, xsub in enumerate(X_Sub):
                model = KernelPCA(n_components=NumFea,kernel=Kernel,gamma=Gamma,degree=Degree,\
                                  coef0=Coef0, alpha=Alpha, tol=Tol, max_iter=MaxIter, n_jobs=NJob)
                X_Sub_PCA.append(model.fit_transform(xsub))
                Models["Model" + str(xsubindx + 1)] = str(model.get_params(deep=True))
                print("KPCA: ", xsubindx + 1, " of ", lenPCA, " is done.")
            print("Data integration ... ")
            X_new = None
            for xsubindx, xsub in enumerate(X_Sub_PCA):
                X_new = np.concatenate((X_new, xsub)) if X_new is not None else xsub
                print("Integration: ", xsubindx + 1, " of ", lenPCA, " is done.")
            OutData[ui.txtOData.text()] = X_new
        else:
            print("Running KPCA ...")
            model = KernelPCA(n_components=NumFea,kernel=Kernel,gamma=Gamma,degree=Degree,\
                            coef0=Coef0, alpha=Alpha, tol=Tol, max_iter=MaxIter, n_jobs=NJob)
            OutData[ui.txtOData.text()] = model.fit_transform(X)
            Models["Model"] = str(model.get_params(deep=True))
        OutData["ModelParameter"] = Models
        print("Saving ...")
        mainIO_save(OutData, ui.txtOutFile.text())
        print("DONE.")
        msgBox.setText("Kernel PCA is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmFEKPCA.show(frmFEKPCA)
    sys.exit(app.exec_())