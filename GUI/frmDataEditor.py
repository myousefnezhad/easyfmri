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
import queue
import numpy as np
import scipy.io as io
from sklearn import preprocessing
from PyQt5.QtWidgets import *
from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile, SaveFile
from GUI.frmDataEditorGUI import *
from GUI.frmDataViewer import frmDataViewer
from GUI.frmSelectRange import frmSelectRange
from GUI.frmSelectXRange import frmSelectXRange


class frmDataEditor(Ui_frmDataEditor):
    ui = Ui_frmDataEditor()
    dialog = None
    data = None
    root = queue.Queue()
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, filename=None, pwd=None):
        global dialog
        global ui
        global data
        global root
        ui = Ui_frmDataEditor()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.lwData.setColumnCount(4)
        ui.lwData.setHeaderLabels(['Name','Class','Shape','Value'])
        ui.lwData.setColumnWidth(0,200)
        dialog.setWindowTitle("easy fMRI Data Viewer - V" + getVersion() + "B" + getBuild())
        ui.tabWidget.setCurrentIndex(0)
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



    def OpenFile(self, ifile):
        global data
        global root
        if len(ifile):
            if os.path.isfile(ifile):
                try:
                    data = io.loadmat(ifile)
                except:
                    print("Cannot load file!")
                    return
                root = queue.Queue()
                frmDataEditor.DrawData(self)
                ui.txtInFile.setText(ifile)
                print(ifile + " is loaded!")

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
                    if valueShape == (1, 1):
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
                                pass
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
            reply = QMessageBox.question(None, 'Data Compress', "Do you like to compress data?", QMessageBox.Yes, QMessageBox.No)
            do_compress = True if reply == QMessageBox.Yes else False
            io.savemat(ui.txtInFile.text(), data, do_compression=do_compress,appendmat=False)
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
        ofile = SaveFile("Save MatLab data file ...",['MatLab files (*.mat)'],'mat',\
                             os.path.dirname(ui.txtInFile.text()))
        if len(ofile):
            if len(ui.txtInFile.text()):
                reply = QMessageBox.question(None, 'Data Compress', "Do you like to compress data?", QMessageBox.Yes, QMessageBox.No)
                do_compress = True if reply == QMessageBox.Yes else False
                io.savemat(ofile, data, do_compression=do_compress,appendmat=False)
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
                         ['Data files (*.mat *.ezdata *.ezmat, *.model)', 'MatLab files (*.mat)','EasyData files (*.ezdata)', \
                          'EasyMat (*.ezmat)', 'All files (*.*)'],'mat')
        if len(ifile):
            if os.path.isfile(ifile):
                root = None
                frmDataEditor.OpenFile(self, ifile)

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
        except:
            try:
                valueType = str(type(value[0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.",
                                                                                                            "")
            except:
                valueType = str(type(value)).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")

        # valueType = str(type(value[0][0])).strip().replace("<class \'", "").replace("\'>", "").replace("numpy.", "")
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








if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 2:
        frmDataEditor.show(frmDataEditor, sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        frmDataEditor.show(frmDataEditor, sys.argv[1])
    else:
        frmDataEditor.show(frmDataEditor)
    sys.exit(app.exec_())