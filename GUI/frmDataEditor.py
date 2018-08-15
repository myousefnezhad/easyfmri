#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from PyQt5.QtWidgets import *

from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile
from GUI.frmDataEditorGUI import *
from GUI.frmDataViewer import frmDataViewer
from GUI.frmSelectRange import frmSelectRange


class frmDataEditor(Ui_frmDataEditor):
    ui = Ui_frmDataEditor()
    dialog = None
    data = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmDataEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.lwData.setColumnCount(4)
        ui.lwData.setHeaderLabels(['Name','Class','Shape','Value'])
        ui.lwData.setColumnWidth(0,200)

        dialog.setWindowTitle("easy fMRI Data Viewer - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnLoadFile_click)
        ui.btnValue.clicked.connect(self.btnValue_click)
        ui.lwData.doubleClicked.connect(self.btnValue_click)

    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnLoadFile_click(self):
        global data
        ifile = LoadFile("Open data files ...",\
                         ['Data files (*.mat *.ezdata *.ezmat)', 'MatLab files (*.mat)','EasyData files (*.ezdata)', \
                          'EasyMat (*.ezmat)', 'All files (*.*)'],'mat')
        if len(ifile):
            if os.path.isfile(ifile):
                try:
                    data = io.loadmat(ifile)
                except:
                    print("Cannot load file!")
                    return
                ui.lwData.clear()
                for key in data:
                    if key == "__header__":
                        pass
                    elif key == "__version__":
                        pass
                    elif key == "__globals__":
                        pass
                    else:
                        item = QtWidgets.QTreeWidgetItem()
                        value = data[key]
                        valueType = str(type(value[0][0])).strip().replace("<class \'","").replace("\'>","").replace("numpy.","")
                        valueShape = np.shape(value)

                        if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                                valueType.replace("32", "").replace("64", "").lower() == "float" or \
                                valueType.replace("32", "").replace("64", "").lower() == "double":
                            if valueShape == (1,1):
                                value = value[0,0]
                                valueShape = 1
                            elif valueShape[0] == 1:
                                value = value[0]
                                valueShape = valueShape[1]
                        if valueType.lower() == "str":
                            if valueShape == (1,):
                                value = value[0]
                                valueShape = len(value)
                        if valueType.lower() == "void":
                            if valueShape == (1,1):
                                value = value[0,0]
                                valueType = "complex"
                                valueShape = np.shape(value)
                        if valueType.lower() == "ndarray":
                            if valueShape[0] == 1:
                                value = value[0]
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
        valueType = str(type(value[0][0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
        valueShape = np.shape(value)

        if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                        valueType.replace("32", "").replace("64", "").lower() == "float" or \
                        valueType.replace("32", "").replace("64", "").lower() == "double":
            if valueShape == (1, 1):
                value = value[0, 0]
                valueShape = 1
            elif valueShape[0] == 1:
                value = value[0]
                valueShape = valueShape[1]
        if valueType.lower() == "str":
            if valueShape == (1,):
                value = value[0]
                valueShape = len(value)
        if valueType.lower() == "void":
            if valueShape == (1, 1):
                value = value[0, 0]
                valueType = "complex"
                valueShape = np.shape(value)
        if valueType.lower() == "ndarray":
            if valueShape[0] == 1:
                value = value[0]
                valueShape = np.shape(value)

        frmDataV = frmDataViewer()

        if valueShape == 1:
            frmDataV = frmDataViewer(str(value), VarName=varName, VarType="num")
        else:
            if valueType == "str":
                if not len(np.shape(value)):
                    frmDataV = frmDataViewer(value, VarName=varName, VarType="str")
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmDataEditor.show(frmDataEditor)
    sys.exit(app.exec_())