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

from sklearn import preprocessing
from sklearn.metrics import accuracy_score
# Python 3.8: Support both old and new joblib
try:
    from sklearn.externals import joblib
except:
    import joblib
from IO.mainIO import mainIO_load
from sklearn.metrics import normalized_mutual_info_score, adjusted_mutual_info_score, adjusted_rand_score
from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile
from GUI.frmSKCModelEditorGUI import *
from GUI.frmDataViewer import frmDataViewer
from GUI.frmSelectRange import frmSelectRange


class frmSKCModelEditor(Ui_frmSKCModelEditor):
    ui = Ui_frmSKCModelEditor()
    dialog = None
    data = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmSKCModelEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.tabWidget.setCurrentIndex(0)

        ui.lwData.setColumnCount(4)
        ui.lwData.setHeaderLabels(['Name','Class' ,'Shape','Value'])
        ui.lwData.setColumnWidth(0,200)

        dialog.setWindowTitle("easy fMRI SK Clustering Model Viewer - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnLoadFile_click)
        ui.btnInData.clicked.connect(self.btnInData_click)
        ui.btnValue.clicked.connect(self.btnValue_click)
        ui.lwData.doubleClicked.connect(self.btnValue_click)
        ui.btnTest.clicked.connect(self.btnTest_click)

    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInData_click(self):
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                             os.path.dirname(ui.txtInData.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = mainIO_load(filename)
                    Keys = data.keys()

                    # Test Data
                    ui.txtITeData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeData.addItem(key)
                        if key == "data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeData.setCurrentText("data")

                    # Test Label
                    ui.txtClass.clear()
                    ui.txtITeLabel.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeLabel.addItem(key)
                        if key == "label":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeLabel.setCurrentText("label")
                        # set number of features
                        Labels = data[ui.txtITeLabel.currentText()]
                        Labels = np.unique(Labels)
                        lblString = ""
                        for lbl in Labels:
                            lblString = lblString + "  " + str(lbl)
                        ui.txtClass.setText(lblString.strip())
                    ui.txtInData.setText(filename)

                except:
                    print("Cannot load data file!")
                    return



    def btnLoadFile_click(self):
        global data
        ifile =  LoadFile("Load SK Clustering model file ...",['Model files (*.model)'],'model',\
                             os.path.dirname(ui.txtInData.text()))
        if len(ifile):
            if os.path.isfile(ifile):
                try:
                    clf = joblib.load(ifile)
                    data = clf.__getstate__()
                except:
                    print("Cannot load model file!")
                    return
                ui.lwData.clear()
                for key in data:
                    item = QtWidgets.QTreeWidgetItem()
                    value = data[key]
                    valueType = str(type(value)).strip().replace("<class \'","").replace("\'>","").replace("numpy.","")
                    valueShape = np.shape(value)

                    if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                            valueType.replace("32", "").replace("64", "").lower() == "float" or \
                            valueType.replace("32", "").replace("64", "").lower() == "double":
                        valueShape = 1
                    elif valueType.lower() == "str":
                        valueShape = len(value)
                    elif valueType.lower() == "bool" or valueType.lower() == "nonetype":
                        valueShape = 1
                    elif valueType.lower() == "ndarray":
                        if valueShape[0] == 1:
                            valueShape = np.shape(value)

                    item.setText(0,str(key).strip())
                    item.setText(1,valueType)
                    item.setText(2,str(valueShape).replace("(","").replace(")",""))
                    item.setText(3, str(value).replace("\n", ""))

                    ui.lwData.addTopLevelItem(item)
                ui.txtInFile.setText(ifile)

    def btnValue_click(self):
        global data
        msgBox = QMessageBox()
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)

        value = data[varName]
        valueType = str(type(value)).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
        valueShape = np.shape(value)

        if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                        valueType.replace("32", "").replace("64", "").lower() == "float" or \
                        valueType.replace("32", "").replace("64", "").lower() == "double":
            valueShape = 1
        elif valueType.lower() == "str":
            valueShape = len(value)
        elif valueType.lower() == "bool" or valueType.lower() == "nonetype":
            valueShape = 1
        elif valueType.lower() == "ndarray":
            if valueShape[0] == 1:
                valueShape = np.shape(value)

        frmDataV = frmDataViewer()

        if valueShape == 1:
            frmDataV = frmDataViewer(str(value), VarName=varName, VarType="num")
        else:
            if valueType == "str" or valueType == "bool":
                if not len(np.shape(value)):
                    frmDataV = frmDataViewer(str(value), VarName=varName, VarType="str")
                else:
                    frmDataV = frmDataViewer(value, VarName=varName, VarType="str_arr")
            else:
                if len(np.shape(value)) == 1:
                    frmSelectR = frmSelectRange(None,Mode="d1",D1From=0,D1To=np.shape(value)[0])
                    frmSelectR.show()
                    frmSelectR.hide()
                    if frmSelectR.PASS:
                        frmDataV = frmDataViewer(value, VarName=varName, VarType="d1",\
                                                 D1From=frmSelectR.D1From, D1To=frmSelectR.D1To)
                elif  len(np.shape(value)) == 2:
                    frmSelectR = frmSelectRange(None,Mode="d2",D1From=0,D1To=np.shape(value)[0],\
                                                D2From=0,D2To=np.shape(value)[1])
                    frmSelectR.show()
                    frmSelectR.hide()
                    if frmSelectR.PASS:
                        frmDataV = frmDataViewer(value, VarName=varName, VarType="d2",\
                                                 D1From=frmSelectR.D1From, D1To=frmSelectR.D1To,\
                                                 D2From=frmSelectR.D2From, D2To=frmSelectR.D2To)
                else:
                    print("Object data is not supported!")
                    return
        frmDataV.show()

    def btnTest_click(self):
        msgBox = QMessageBox()

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

        # InModel
        InModelFile = ui.txtInFile.text()
        if not len(InModelFile):
            msgBox.setText("Please enter model file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isfile(InModelFile):
            msgBox.setText("Model file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # InData
        InDataFile = ui.txtInData.text()
        if not len(InDataFile):
            msgBox.setText("Please enter data file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isfile(InDataFile):
            msgBox.setText("data file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Data
        if not len(ui.txtITeData.currentText()):
            msgBox.setText("Please enter Input Test Data variable name!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        # Label
        if not len(ui.txtITeLabel.currentText()):
                msgBox.setText("Please enter Test Input Label variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

        try:
            cls = joblib.load(InModelFile)
        except:
            msgBox.setText("Cannot load classification model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            InData = mainIO_load(InDataFile)
        except:
            print("cannot load data file!")
            msgBox.setText("cannot load data file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        TeX = InData[ui.txtITeData.currentText()]
        TeL = InData[ui.txtITeLabel.currentText()][0]

        try:
            if Filter is not None:
                for fil in Filter:
                    # Remove Testing Set
                    labelIndx = np.where(TeL == fil)[0]
                    TeL = np.delete(TeL, labelIndx, axis=0)
                    TeX = np.delete(TeX, labelIndx, axis=0)
                    print("Class ID = " + str(fil) + " is removed from data.")

            if ui.cbScale.isChecked():
                TeX = preprocessing.scale(TeX)
                print("Whole of data is scaled Train~N(0,1) and Test~N(0,1).")
        except:
            print("Cannot load data or label")
            return

        print("Run testing ...")
        PeL = cls.predict(TeX)

        if ui.cbAverage.isChecked():
            print("Average                             {:5.2f}".format(accuracy_score(TeL, PeL) * 100))

        if ui.cbNMI.isChecked():
            print("Normalized Mutual Information (NMI) {:7.6f}".format(normalized_mutual_info_score(TeL, PeL)))

        if ui.cbRIA.isChecked():
            print("Rand Index Adjusted (RIA)           {:7.6f}".format(adjusted_rand_score(TeL, PeL)))

        if ui.cbAMI.isChecked():
            print("Adjusted Mutual Information (AMI)   {:7.6f}".format(adjusted_mutual_info_score(TeL, PeL)))

        print("Data is analyzed!")
        msgBox.setText("Data is analyzed!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmSKCModelEditor.show(frmSKCModelEditor)
    sys.exit(app.exec_())