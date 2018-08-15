#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.metrics import normalized_mutual_info_score, adjusted_mutual_info_score, adjusted_rand_score
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild
from GUI.frmMAAgglomerativeGUI import *


class frmMAAgglomerative(Ui_frmMAAgglomerative):
    ui = Ui_frmMAAgglomerative()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmMAAgglomerative()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        # compute_full_tree
        ui.cbTree.addItem("Auto", "auto")
        ui.cbTree.addItem("True", True)
        ui.cbTree.addItem("False", False)

        # Affinity
        ui.cbAffinity.addItem("Euclidean", "euclidean")
        ui.cbAffinity.addItem("L1 Norm","l1")
        ui.cbAffinity.addItem("L2 Norm","l2")
        ui.cbAffinity.addItem("Manhattan","manhattan")
        ui.cbAffinity.addItem("Cosine", "cosine")
        ui.cbAffinity.addItem("Precomputed","precomputed")

        # Linkage
        ui.cbLinkage.addItem("Ward","ward")
        ui.cbLinkage.addItem("Complete","complete")
        ui.cbLinkage.addItem("Average","average")


        dialog.setWindowTitle("easy fMRI Agglomerative Clustering - V" + getVersion() + "B" + getBuild())
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
        msgBox = QMessageBox()

        # Linkage
        Linkage = ui.cbLinkage.currentData()
        # Affinity
        Affinity = ui.cbAffinity.currentData()
        # Tree
        Tree = ui.cbTree.currentData()

        # NCluster
        try:
            NCluster = np.int32(ui.txtNCluster.text())
        except:
            msgBox.setText("Number of Cluster is wrong!")
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
        OutData["ModelAnalysis"] = "Agglomerative"

        # OutModel
        OutModel = ui.txtOutModel.text()
        if not len(OutModel):
            OutModel = None

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

        InData = io.loadmat(InFile)
        # Data
        if not len(ui.txtData.currentText()):
            msgBox.setText("Please enter Input Train Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Label
        if not len(ui.txtLabel.currentText()):
                msgBox.setText("Please enter Train Input Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
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
            cls = AgglomerativeClustering(n_clusters=NCluster,affinity=Affinity,compute_full_tree=Tree,linkage=Linkage)
            print("Run Clustering ...")
            PeL = cls.fit_predict(X)
        except Exception as e:
            print(e)
            msgBox = QMessageBox()
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

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
        io.savemat(OutFile, mdict=OutData)
        print("DONE.")
        msgBox.setText("Agglomerative Clustering is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmMAAgglomerative.show(frmMAAgglomerative)
    sys.exit(app.exec_())