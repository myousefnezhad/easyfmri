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
import queue
import numpy as np
from sklearn import preprocessing
from IO.mainIO import mainIO_load, mainIO_save, can_do_compression
from dir import getDIR
from PyQt5.QtWidgets import *
from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile, SaveFile
from GUI.frmDataEditorGUI import *
from GUI.frmDataViewer import frmDataViewer
from GUI.frmSelectRange import frmSelectRange
from GUI.frmSelectXRange import frmSelectXRange

import logging
logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels



def DefaultCode():
    return """# This is a template for writing any code in Python 3 style
# You can access to the data information as follows 
# "data" as the variable in a dictionary format
# "root" as the current location in a queue format
import os
import sys
import numpy as np
import nibabel as nb
import scipy as sp

# Example 1: Print Variable Names
#print([key for key in data.keys()])
# Example 2: Print Current Location
#print(list(root.queue)) 
"""




class frmDataEditor(Ui_frmDataEditor):
    ui = Ui_frmDataEditor()
    dialog = None
    data = None
    currentFile = None
    root = queue.Queue()
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, filename=None, pwd=None):
        global dialog
        global ui
        global data
        global root
        global currentFile
        ui = Ui_frmDataEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.lwData.setColumnCount(4)
        ui.lwData.setHeaderLabels(['Name','Class','Shape','Value'])
        ui.lwData.setColumnWidth(0,200)
        dialog.setWindowTitle("easy fMRI Data Editor - V" + getVersion() + "B" + getBuild())
        ui.tabWidget.setCurrentIndex(0)
        ui.tabWidget2.setCurrentIndex(0)
        layout = QHBoxLayout(ui.Code)
        ui.txtCode = api.CodeEdit(ui.Code)
        layout.addWidget(ui.txtCode)
        ui.txtCode.setObjectName("txtCode")
        ui.txtCode.backend.start(getDIR() + '/backend/server.py')

        ui.txtCode.modes.append(modes.CodeCompletionMode())
        ui.txtCode.modes.append(modes.CaretLineHighlighterMode())
        ui.txtCode.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtCode.document()))
        #ui.txtCode.panels.append(panels.SearchAndReplacePanel(), api.Panel.Position.TOP)
        ui.txtCode.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)

        ui.lblCodeFile.setText("New File")
        currentFile = None

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtCode.setFont(font)
        ui.txtCode.setPlainText(DefaultCode(),"","")

        root = queue.Queue()
        data = None
        if filename is not None:
           if os.path.isfile(filename):
               self.OpenFile(self, filename)
           elif pwd is not None:
               if os.path.isfile(pwd + "/" + filename):
                     self.OpenFile(self, pwd + "/" + filename)
               else:
                   print("Data file cannot find!")
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.actionExit.triggered.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnLoadFile_click)
        ui.btnMerge.clicked.connect(self.btnMerge_click)
        ui.btnValue.clicked.connect(self.btnValue_click)
        ui.lwData.doubleClicked.connect(self.btnValue_click)
        ui.btnBack.clicked.connect(self.btnBack_click)
        ui.btnIn.clicked.connect(self.btnIn_click)
        ui.btnRefresh.clicked.connect(self.btnRefresh_click)
        ui.btnTranspose.clicked.connect(self.btnTranspose_click)
        ui.btnRename.clicked.connect(self.btnRename_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)
        ui.btnScale.clicked.connect(self.btnScale_click)
        ui.btnSave.clicked.connect(self.btnSave_click)
        ui.btnSaveAs.clicked.connect(self.btnSaveAs_click)
        ui.btnClone.clicked.connect(self.btnClone_click)
        ui.btnReshape.clicked.connect(self.btnReshape_click)
        ui.btnSelectPart.clicked.connect(self.btnSelectPart_click)
        ui.btnVConcat.clicked.connect(self.btnVConcat_click)
        ui.btnHConcat.clicked.connect(self.btnHConcat_click)
        ui.btnCConcat.clicked.connect(self.btnCConcat_click)
        ui.btnConcat.clicked.connect(self.btnConcat_click)
        # Code Section
        ui.btnRun.clicked.connect(self.btnRun_click)
        ui.btnNewCode.clicked.connect(self.btnNewCode_click)
        ui.btnSaveCode.clicked.connect(self.btnSaveCode_click)
        ui.btnOpenCode.clicked.connect(self.btnOpenCode_click)

    def OpenFile(self, ifile):
        global data
        global root
        if len(ifile):
            if os.path.isfile(ifile):
                try:
                    data = mainIO_load(ifile)
                    assert data is not None
                except:
                    print("Cannot load file!")
                    return
                root = queue.Queue()
                frmDataEditor.DrawData(self)
                ui.txtInFile.setText(ifile)
                print(ifile + " is loaded!")
                ui.btnSave.setEnabled(False)



    def getCurrentVar(self):
        global data
        global root
        try:
            dat = data
            if root.empty():
                ui.btnBack.setEnabled(False)
                status = "/"
            else:
                ui.btnBack.setEnabled(True)
                for r in list(root.queue):
                    if str(type(dat[r[0]])) == "<class 'numpy.ndarray'>":
                        dat2 = dict()
                        for key in dat[r[0]].dtype.descr:
                            if key[0] == "":
                                dat2[""] = dat[r[0]][r[1]]
                            else:
                                dat2[key[0]] = dat[r[0]][key[0]]
                        dat = dat2
                    else:
                        dat = data[r[0]]
                status = ""
                for st in list(root.queue):

                    if len(status):
                        status += " / "
                    status += "<" + str(st[0]).replace("[","").replace("]","").replace(","," / ") + ">"
        except:
            print("Cannot load complex variable!")
            status = "/"
            dat = data
            root = queue.Queue()
        return dat, status

    def getCurrentPointer(self):
        global data
        global root
        try:
            dat = data
            if not root.empty():
                for r in list(root.queue):
                    if not len(r[0]):
                        dat = dat[r[1]]
                    else:
                        dat = dat[r[0]]
        except:
            print("Cannot find pointer!")
            return None
        return dat


    def DrawData(self):
        global data
        global root

        if root.empty():
            ui.btnBack.setEnabled(False)
        else:
            ui.btnBack.setEnabled(True)

        dat, status = frmDataEditor.getCurrentVar(self)
        ui.statusbar.showMessage(status)
        ui.lwData.clear()
        for key in dat:
            if key == "__header__":
                pass
            elif key == "__version__":
                pass
            elif key == "__globals__":
                pass
            else:
                item = QtWidgets.QTreeWidgetItem()
                value = dat[key]
                try:
                    valueType = str(type(value[0][0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
                except:
                    try:
                        valueType = str(type(value[0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
                    except:
                        valueType = str(type(value)).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
                valueShape = np.shape(value)
                if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                        valueType.replace("32", "").replace("64", "").lower() == "float" or \
                        valueType.replace("32", "").replace("64", "").lower() == "double":
                    if valueShape == ():
                        valueShape = 1
                    elif valueShape == (1, 1):
                        value = value[0, 0]
                        valueShape = 1
                    elif valueShape == ():
                        valueShape = 1
                    elif valueShape[0] == 1:
                        value = value[0]
                        try:
                            valueShape = valueShape[1]
                        except:
                            try:
                                valueShape = valueShape[0]
                            except:
                                valueShape = 1
                if valueType.lower() == "str":
                    if valueShape == ():
                        valueShape = 1
                    elif valueShape == (1,):
                        value = value[0]
                        valueShape = len(value)
                if valueType.lower() == "void":
                    if valueShape == ():
                        valueShape = 1
                    elif valueShape == (1, 1):
                        value = value[0, 0]
                        valueType = "complex"
                        valueShape = np.shape(value)
                if valueType.lower() == "ndarray":
                    if valueShape == ():
                        valueShape = 1
                    else:
                        if valueShape[0] == 1:
                            value = value[0]
                            valueShape = np.shape(value)

                item.setText(0, str(key).strip())
                item.setText(1, valueType)
                item.setText(2, str(valueShape).replace("(", "").replace(")", ""))
                item.setText(3, str(value).replace("\n", ""))
                ui.lwData.addTopLevelItem(item)



    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnSave_click(self):
        global data
        msgBox = QMessageBox()
        if len(ui.txtInFile.text()):
            do_compress = False
            if can_do_compression(ui.txtInFile.text()):
                reply = QMessageBox.question(None, 'Data Compress', "Do you like to compress data?", QMessageBox.Yes, QMessageBox.No)
                do_compress = True if reply == QMessageBox.Yes else False
            mainIO_save(data, ui.txtInFile.text(), do_compression=do_compress)
            ui.btnSave.setEnabled(False)
            print("Data is saved in: ", ui.txtInFile.text())
            msgBox.setText("Data is saved")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()


    def btnSaveAs_click(self):
        global data
        msgBox = QMessageBox()
        if not len(ui.txtInFile.text()):
            return False
        ofile = SaveFile("Save MatLab data file ...",['easyX files (*.ezx)', 'MatLab files (*.mat)'],'ezx',\
                             os.path.dirname(ui.txtInFile.text()))
        if len(ofile):
            if len(ui.txtInFile.text()):
                do_compress = False
                if can_do_compression(ofile):
                    reply = QMessageBox.question(None, 'Data Compress', "Do you like to compress data?",
                                                 QMessageBox.Yes, QMessageBox.No)
                    do_compress = True if reply == QMessageBox.Yes else False
                mainIO_save(data, ofile, do_compression=do_compress)
                ui.btnSave.setEnabled(False)
                ui.txtInFile.setText(ofile)
                print("Data is saved in: ", ui.txtInFile.text())
                msgBox.setText("Data is saved")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()


    def btnBack_click(self):
        global root
        if not root.empty():
            newroot = queue.Queue()
            for _ in range(root.qsize() - 1):
                val = root.get()
                if len(val):
                    newroot.put(val)
            root = newroot
            frmDataEditor.DrawData(self)

    def btnLoadFile_click(self):
        global data
        global root
        ifile = LoadFile("Open data files ...",\
                         ['Data files (*.ezx *.mat *.ezdata *.ezmat, *.model)', "easyX files (*.ezx)", 'MatLab files (*.mat)','EasyData files (*.ezdata)', \
                          'EasyMat (*.ezmat)', 'All files (*.*)'],'mat')
        if len(ifile):
            if os.path.isfile(ifile):
                root = None
                frmDataEditor.OpenFile(self, ifile)

    def btnMerge_click(self):
        global data
        global root

        if len(ui.txtInFile.text()):

            ifile = LoadFile("Open data files ...",\
                         ['Data files (*.ezx *.mat *.ezdata *.ezmat, *.model)', "easyX files (*.ezx)", 'MatLab files (*.mat)','EasyData files (*.ezdata)', \
                          'EasyMat (*.ezmat)', 'All files (*.*)'],'mat')
            if len(ifile):
                if os.path.isfile(ifile):
                    try:
                        data2 = mainIO_load(ifile)
                    except:
                        print("Cannot load file!")
                        return
                    for key in data2.keys():
                        if key != "__header__" and key != "__version__" and key != "__globals__":
                            data[key] = data2[key]

                    root = queue.Queue()
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)


    def btnValue_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)

        dat, _ = frmDataEditor.getCurrentVar(self)
        value = dat[varName]

        try:
            valueType = str(type(value[0][0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
            if valueType == 'str':
                if str(type(value)).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "") == 'ndarray':
                    valueType = 'ndarray'
        except:
            try:
                valueType = str(type(value[0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.",
                                                                                                            "")
            except:
                valueType = str(type(value)).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
        valueShape = np.shape(value)
        if valueType.replace("32", "").replace("64", "").lower() == "int" or \
                        valueType.replace("32", "").replace("64", "").lower() == "float" or \
                        valueType.replace("32", "").replace("64", "").lower() == "double":
            if valueShape == ():
                valueShape = 1
            elif valueShape == (1, 1):
                value = value[0, 0]
                valueShape = 1
            elif valueShape[0] == 1:
                value = value[0]
                try:
                    valueShape = valueShape[1]
                except:
                    try:
                        valueShape = valueShape[0]
                    except:
                        valueShape = 1
        if valueType.lower() == "str":
            if valueShape == ():
                valueShape = 1
            elif valueShape == (1,):
                value = value[0]
                valueShape = len(value)
        if valueType.lower() == "void":
            if valueShape == ():
                valueShape = 1
            elif valueShape == (1, 1):
                value = value[0, 0]
                valueType = "complex"
                valueShape = np.shape(value)
        if valueType.lower() == "ndarray":
            if valueShape == ():
                valueShape = 1
            else:
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

            elif valueType == "complex":
                root.put(varName)
                frmDataEditor.DrawData(self)
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


    def btnRefresh_click(self):
        filename = ui.txtInFile.text()
        msgBox = QMessageBox()
        if not len(filename):
            msgBox.setText("There is no opened file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not os.path.isfile(filename):
            msgBox.setText("Cannot find data file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        frmDataEditor.OpenFile(self, filename)

    def btnTranspose_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        try:
            dat = frmDataEditor.getCurrentPointer(self)
            if not len(varName):
                dat = np.transpose(dat)
            else:
                dat[varName] = np.transpose(dat[varName])
            frmDataEditor.DrawData(self)
            ui.btnSave.setEnabled(True)
        except Exception as e:
            print(str(e))
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

    def btnRemove_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        try:
            dat = frmDataEditor.getCurrentPointer(self)
            if str(type(dat)) == "<class 'numpy.ndarray'>":
                if len(varName):
                    dat.delete(varName)
            else:
                dat = dat.pop(varName, None)
            frmDataEditor.DrawData(self)
            ui.btnSave.setEnabled(True)
        except Exception as e:
            print(str(e))
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

    def btnRename_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                name, ok = QInputDialog.getText(None, "Variable Editor", "Please enter variable new name:",text=varName)

                if ok and name != varName:
                    dat[name] = dat.pop(varName)
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnScale_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:

                axis, ok = QInputDialog.getItem(None,"Select Axis", "Select Axis", [str(i) for i in tuple(range(len(np.shape(dat[varName]))))])
                if ok:
                    dat[varName] = preprocessing.scale(dat[varName], axis=int(axis))
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnClone_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        dat, _ = frmDataEditor.getCurrentVar(self)
        try:
            name, ok = QInputDialog.getText(None, "New Variable", "Please enter variable name:", text=varName)
            if ok:
                data[name] = dat[varName]
                root = queue.Queue()
                frmDataEditor.DrawData(self)
                ui.btnSave.setEnabled(True)
        except Exception as e:
            print(str(e))
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False



    def btnReshape_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)

        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                shape, ok = QInputDialog.getText(None, "Reshape Variable", "Please enter variable new shape:",text=str(np.shape(dat[varName])))
                shape = [int(i) for i in str(shape).replace("(", "").replace(")", "").replace("]","").replace("[","").rsplit(",")]
                if ok:
                    if np.prod(shape) != np.prod(np.shape(dat[varName])):
                        msgBox.setText("Shape is wrong!")
                        msgBox.setIcon(QMessageBox.Critical)
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                        return False
                    dat[varName] = np.reshape(dat[varName], shape)
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False


    def btnSelectPart_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                frm = frmSelectXRange(np.shape(dat[varName]))
                if frm.PASS:
                    selectDat = dat[varName]
                    for axis, (rf, rt) in enumerate(zip(frm.From, frm.To)):
                        selectDat = np.take(selectDat, range(rf, rt), axis=axis)
                    dat[varName] = selectDat
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnVConcat_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                item = list()
                for key in dat.keys():
                    if key != "__header__" and key != "__version__" and key != "__globals__":
                        item.append(key)
                varName2, ok = QInputDialog.getItem(None,"Select Variable", "Select Variable", item)
                if ok:
                    dat[varName] = np.concatenate((dat[varName], dat[varName2]), axis=1)
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnHConcat_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                item = list()
                for key in dat.keys():
                    if key != "__header__" and key != "__version__" and key != "__globals__":
                        item.append(key)
                varName2, ok = QInputDialog.getItem(None,"Select Variable", "Select Variable", item)
                if ok:
                    dat[varName] = np.concatenate((dat[varName], dat[varName2]), axis=0)
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnCConcat_click(self):
        print("Helllo")
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                item = list()
                for key in dat.keys():
                    if key != "__header__" and key != "__version__" and key != "__globals__":
                        item.append(key)
                varName2, ok = QInputDialog.getItem(None,"Select Variable", "Select Variable", item)
                if ok:
                    dat[varName] = np.concatenate((np.concatenate((dat[varName], np.zeros((np.shape(dat[varName])[0],np.shape(dat[varName2])[1]))), axis=1),\
                                          np.concatenate((np.zeros((np.shape(dat[varName2])[0],np.shape(dat[varName])[1])), dat[varName2]), axis=1)), axis=0)
                    frmDataEditor.DrawData(self)
                    ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnConcat_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not root.empty():
            msgBox.setText("This item only works on variables located in root!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)
        if len(varName):
            dat, _ = frmDataEditor.getCurrentVar(self)
            try:
                item = list()
                for key in dat.keys():
                    if key != "__header__" and key != "__version__" and key != "__globals__":
                        item.append(key)
                varName2, ok = QInputDialog.getItem(None,"Select Variable", "Select Variable", item)
                if ok:
                    axis, ok = QInputDialog.getItem(None, "Select Axis", "Select Axis", [str(i) for i in tuple(range(len(np.shape(dat[varName]))))])
                    if ok:
                        dat[varName] = np.concatenate((dat[varName], dat[varName2]), axis=int(axis))
                        frmDataEditor.DrawData(self)
                        ui.btnSave.setEnabled(True)
            except Exception as e:
                print(str(e))
                msgBox.setText(str(e))
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False

    def btnIn_click(self):
        global data
        global root
        msgBox = QMessageBox()
        if not len(ui.lwData.selectedItems()):
            msgBox.setText("Please select an item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        Index = ui.lwData.indexOfTopLevelItem(ui.lwData.selectedItems()[0])
        varName = ui.lwData.topLevelItem(Index).text(0)

        dat, _ = frmDataEditor.getCurrentVar(self)
        try:
            if str(type(dat[varName])) == "<class 'dict'>":
                val = dat[varName]
            else:
                val = dat[varName][ui.txtInside.value()]
            if str(type(val)) == "<class 'str'>":
                raise Exception
        except:
            msgBox.setText("Cannot find variable with current index!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        root.put([varName, ui.txtInside.value()])
        frmDataEditor.DrawData(self)

    def btnRun_click(self):
        global data
        global root
        msgBox = QMessageBox()

        Codes = ui.txtCode.toPlainText()
        try:
            allvars = dict(locals(), **globals())
            exec(Codes, allvars, allvars)
            ui.btnSave.setEnabled(True)
            frmDataEditor.DrawData(self)
            msgBox.setText("Run without error")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()


        except Exception as e:
            print(e)
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def btnSaveCode_click(self):
        global currentFile
        if currentFile is None:
            filename = SaveFile('Save code file ...',['Code files (*.py)', 'All files (*.*)'], 'py',\
                                        os.path.dirname(str(currentFile)))
            if not len(filename):
                return
            currentFile = filename
            ui.lblCodeFile.setText(filename)
        file = open(currentFile, "w")
        file.write(ui.txtCode.toPlainText())
        file.close()


    def btnOpenCode_click(self):
        global currentFile
        MustSave = False
        if (currentFile == None) and (ui.txtCode.toPlainText() != DefaultCode()):
            MustSave = True
        if (currentFile != None):
            currCode = open(currentFile).read()
            if ui.txtCode.toPlainText() != currCode:
                MustSave = True
        if MustSave:
            msgBox = QMessageBox()
            msgBox.setText("Do you want to save current code?")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            if (msgBox.exec_() == QMessageBox.Yes):
                if (currentFile != None):
                    filename = currentFile
                else:
                    filename = SaveFile('Save code file ...',['Code files (*.py)', 'All files (*.*)'], 'py', \
                                        os.path.dirname(str(currentFile)))
                    if not len(filename):
                        return
                file = open(filename, "w")
                file.write(ui.txtCode.toPlainText())
                file.close()
        filename = LoadFile('Open code file ...',['Code files (*.py)', 'All files (*.*)'], 'py')
        if len(filename):
            ui.txtCode.setPlainText(open(filename).read(),"","")
            currentFile = filename
            ui.lblCodeFile.setText(filename)

    def btnNewCode_click(self):
        global currentFile
        MustSave = False
        if (currentFile == None) and (ui.txtCode.toPlainText() != DefaultCode()):
            MustSave = True
        if (currentFile != None):
            currCode = open(currentFile).read()
            if ui.txtCode.toPlainText() != currCode:
                MustSave = True

        if MustSave:
            msgBox = QMessageBox()
            msgBox.setText("Do you want to save current code?")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setStandardButtons(QMessageBox.No| QMessageBox.Yes)
            if (msgBox.exec_() == QMessageBox.Yes):
                if (currentFile != None):
                    filename = currentFile
                else:
                    filename = SaveFile('Save code file ...',['Code files (*.py)', 'All files (*.*)'], 'py',\
                                        os.path.dirname(str(currentFile)))
                    if not len(filename):
                        return
                file = open(filename,"w")
                file.write(ui.txtCode.toPlainText())
                file.close()
        ui.txtCode.setPlainText(DefaultCode(), "", "")
        ui.lblCodeFile.setText("New File")
        currentFile = None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 2:
        frmDataEditor.show(frmDataEditor, sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        frmDataEditor.show(frmDataEditor, sys.argv[1])
    else:
        frmDataEditor.show(frmDataEditor)
    sys.exit(app.exec_())