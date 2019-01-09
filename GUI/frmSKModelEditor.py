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

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *

from sklearn import preprocessing

from sklearn.externals import joblib
from sklearn.metrics import accuracy_score, precision_score, average_precision_score, f1_score, recall_score, confusion_matrix


from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile
from GUI.frmSKModelEditorGUI import *
from GUI.frmDataViewer import frmDataViewer
from GUI.frmSelectRange import frmSelectRange


class frmSKModelEditor(Ui_frmSKModelEditor):
    ui = Ui_frmSKModelEditor()
    dialog = None
    data = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmSKModelEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.tabWidget.setCurrentIndex(0)

        ui.lwData.setColumnCount(4)
        ui.lwData.setHeaderLabels(['Name','Class' ,'Shape','Value'])
        ui.lwData.setColumnWidth(0,200)


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


        dialog.setWindowTitle("easy fMRI SK Classification Model Viewer - V" + getVersion() + "B" + getBuild())
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
        ui.btnTestConfusion.clicked.connect(self.btnTestConfusion_click)
        ui.btnTestLabels.clicked.connect(self.btnTestLabels_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInData_click(self):
        filename = LoadFile("Load MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtInData.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    print("Data is loading ...")
                    data = io.loadmat(filename)
                    Keys = data.keys()

                    # Test Data
                    ui.txtITeData.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtITeData.addItem(key)
                        if key == "test_data":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtITeData.setCurrentText("test_data")

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
                        Labels = data[ui.txtITeLabel.currentText()]
                        Labels = np.unique(Labels)

                        lblString = None
                        for lbl in Labels:
                            lblString = str(lbl) if lblString is None else lblString + ", " + str(lbl)
                        ui.txtClass.setText(lblString.strip())
                    ui.txtInData.setText(filename)
                    print("Data is ready.")

                except:
                    print("Cannot load data file!")
                    return



    def btnLoadFile_click(self):
        global data
        ifile = LoadFile("Load SK Classification model file ...",['Model files (*.model)'],'model',\
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
        print("Test is running ...")
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
            clf = joblib.load(InModelFile)
        except:
            msgBox.setText("Cannot load classification model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            InData = io.loadmat(InDataFile)
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
        PeL = clf.predict(TeX)


        if ui.cbAverage.isChecked():
            print("Average            Test {:5.2f}".format(accuracy_score(TeL, PeL) * 100))

        if ui.cbPrecision.isChecked():
            print("Precision          Test {:5.2f}".format(precision_score(TeL, PeL, average=ui.cbPrecisionAvg.currentData()) * 100))

        if ui.cbAPrecision.isChecked():
            print("Average Precision: Test {:5.2f}".format(average_precision_score(TeL, PeL, average=ui.cbAPrecisionAvg.currentData()) * 100))

        if ui.cbRecall.isChecked():
            print("Recall:            Test {:5.2f}".format(recall_score(TeL, PeL, average=ui.cbRecallAvg.currentData()) * 100))

        if ui.cbF1.isChecked():
            print("F1:                Test {:5.2f}".format(f1_score(TeL, PeL, average=ui.cbF1Avg.currentData()) * 100))

        print("Testing data is analyzed!")
        msgBox.setText("Testing data is analyzed!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def btnTestConfusion_click(self):
        print("Test is running ...")
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
            clf = joblib.load(InModelFile)
        except:
            msgBox.setText("Cannot load classification model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            InData = io.loadmat(InDataFile)
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
        PeL = clf.predict(TeX)
        confusion = confusion_matrix(TeL, PeL)
        print("Confusion Matrix:\n", confusion)
        frmDataViewer(confusion, VarName="Confusion Matrix", VarType="d2", D1From=0, D1To=np.shape(confusion)[0], D2From=0, D2To=np.shape(confusion)[1])


    def btnTestLabels_click(self):
        print("Test is running ...")
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
            clf = joblib.load(InModelFile)
        except:
            msgBox.setText("Cannot load classification model!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        try:
            InData = io.loadmat(InDataFile)
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
        PeL = clf.predict(TeX)
        Labels = np.transpose(np.concatenate(([TeL], [PeL])))
        print("Labels vs Predicts:\n", Labels)
        frmDataViewer(Labels, VarName="Labels vs Predicts", VarType="d2", D1From=0, D1To=np.shape(Labels)[0], D2From=0, D2To=np.shape(Labels)[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmSKModelEditor.show(frmSKModelEditor)
    sys.exit(app.exec_())