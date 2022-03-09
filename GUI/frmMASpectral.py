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
from PyQt6.QtWidgets import *
from sklearn import preprocessing
from GUI.frmMASpectralGUI import *
from sklearn.metrics import accuracy_score
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from IO.mainIO import mainIO_load, mainIO_save
from sklearn.cluster import SpectralClustering
from sklearn.metrics import normalized_mutual_info_score, adjusted_mutual_info_score, adjusted_rand_score
# Python 3.8: Support both old and new joblib
try:
    from sklearn.externals import joblib
except:
    import joblib

class frmMASpectral(Ui_frmMASpectral):
    ui = Ui_frmMASpectral()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMASpectral()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        # Init
        ui.cbESolver.addItem("None",None)
        ui.cbESolver.addItem("arpack","arpack")
        ui.cbESolver.addItem("lobpcg","lobpcg")
        ui.cbESolver.addItem("AMG (need pyamg)","amg")

        # Pre
        ui.cbAffinity.addItem("RBF", "rbf")
        ui.cbAffinity.addItem("Nearest Neighbors","nearest_neighbors")
        ui.cbAffinity.addItem("Precomputed","precomputed")

        # Alg
        ui.cbAssignLabels.addItem("KMeans","kmeans")
        ui.cbAssignLabels.addItem("Discretize","discretize")


        dialog.setWindowTitle("easy fMRI Spectral Clustering - V" + getVersion() + "B" + getBuild())
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
        ui.btnOutModel.clicked.connect(self.btnOutModel_click)
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

                    # Train Data
                    ui.txtData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtData.setCurrentText("data")

                    # Train Label
                    ui.txtLabel.clear()
                    ui.txtClass.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtLabel.setCurrentText("label")
                        # set number of features
                        Labels = data[ui.txtLabel.currentText()]
                        Labels = np.unique(Labels)
                        ui.txtClass.clear()
                        for lbl in Labels:
                            ui.txtClass.append(str(lbl))

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

    def btnOutModel_click(self):
        ofile = SaveFile("Save SK model file ...",['Model files (*.model)'],'model',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutModel.setText(ofile)


    def btnConvert_click(self):
        msgBox = QMessageBox()

        # ESolver
        ESolver = ui.cbESolver.currentData()
        # Affinity
        Affinity = ui.cbAffinity.currentData()
        # AssignLabels
        AssignLabels = ui.cbAssignLabels.currentData()

        # NCluster
        try:
            NCluster = np.int32(ui.txtNCluster.text())
        except:
            msgBox.setText("Number of Cluster is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # NInit
        try:
            NInit = np.int32(ui.txtNInit.text())
        except:
            msgBox.setText("Number of init is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # NJobs
        try:
            NJobs = np.int(ui.txtNJobs.text())
        except:
            msgBox.setText("Number of Jobs is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Degree
        try:
            Degree = np.float(ui.txtDegree.text())
        except:
            msgBox.setText("Degree is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Tol
        try:
            Tol = np.float(ui.txtTole.text())
        except:
            msgBox.setText("Eigen Tolerance is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # NNeighbors
        try:
            NNeighbors = np.int32(ui.txtNNeighbors.text())
        except:
            msgBox.setText("Number of Neighbors is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Gamma
        try:
            Gamma = np.float(ui.txtGamma.text())
        except:
            msgBox.setText("Gamma is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Coef0
        try:
            Coef0 = np.float(ui.txtCoef0.text())
        except:
            msgBox.setText("Coef0 is wrong!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False


        OutData = dict()
        OutData["ModelAnalysis"] = "Spectral"

        # OutModel
        OutModel = ui.txtOutModel.text()
        if not len(OutModel):
            OutModel = None

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

        InData = mainIO_load(InFile)
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Input Train Data variable name!")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Train Input Label variable name!")
                msgBox.setIcon(QMessageBox.Icon.Critical)
                msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
                msgBox.exec()
                return False

        X = InData[ui.txtData.currentText()]
        L = InData[ui.txtLabel.currentText()][0]

        try:
            if Filter is not None:
                for fil in Filter:
                    # Remove Training Set
                    labelIndx = np.where(L == fil)[0]
                    L = np.delete(L, labelIndx, axis=0)
                    X = np.delete(X, labelIndx, axis=0)
                    print("Class ID = " + str(fil) + " is removed from data.")

            if ui.cbScale.isChecked():
                X = preprocessing.scale(X)
                print("Whole of data is scaled to N(0,1).")
        except:
            print("Cannot load data or label")
            return
        try:
            cls = SpectralClustering(n_clusters=NCluster,eigen_solver=ESolver,n_init=NInit,gamma=Gamma,affinity=Affinity,\
                                     n_neighbors=NNeighbors,eigen_tol=Tol,assign_labels=AssignLabels,degree=Degree,\
                                     coef0=Coef0,n_jobs=NJobs)

            print("Run Clustering ...")
            PeL = cls.fit_predict(X)
        except Exception as e:
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return False

        OutData["predict"] = PeL

        if OutModel is not None:
            joblib.dump(cls, OutModel)
            print("Model is saved: " + OutModel)


        if ui.cbAverage.isChecked():
            acc = accuracy_score(L, PeL)
            OutData["Accuracy"] = acc
            print("Average                             {:5.2f}".format(acc * 100))

        if ui.cbNMI.isChecked():
            NMI = normalized_mutual_info_score(L, PeL)
            OutData["NMI"] = NMI
            print("Normalized Mutual Information (NMI) {:7.6f}".format(NMI))

        if ui.cbRIA.isChecked():
            RIA = adjusted_rand_score(L, PeL)
            OutData["RIA"] = RIA
            print("Rand Index Adjusted (RIA)           {:7.6f}".format(RIA))

        if ui.cbAMI.isChecked():
            AMI = adjusted_mutual_info_score(L, PeL)
            OutData["AMI"] = AMI
            print("Adjusted Mutual Information (AMI)   {:7.6f}".format(AMI))

        print("Saving ...")
        mainIO_save(OutData, OutFile)
        print("DONE.")
        msgBox.setText("Spectral Clustering is done.")
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMASpectral.show(frmMASpectral)
    sys.exit(app.exec())