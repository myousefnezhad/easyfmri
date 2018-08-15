#!/usr/bin/env python3
import logging
import os

from PyQt5.QtWidgets import *

from Base.utility import getVersion, getBuild
from Base.dialogs import SaveFile, LoadFile
from GUI.frmManuallyDesignROIGUI import *

logging.basicConfig(level=logging.DEBUG)
import sys
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels


def DefaultCode():
    return """# This is a template for writting any code in Python 3 style!
import os
import sys
import numpy as np
import nibabel as nb
import scipy as sp

# Write Your Code Here
print("Hello World!")    
"""



class frmManuallyDesignROI(Ui_frmManuallyDesignROI):
    ui = Ui_frmManuallyDesignROI()
    dialog = None
    currentFile = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui, currentFile
        ui = Ui_frmManuallyDesignROI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.stb.showMessage("New File")
        currentFile = None

        ui.txtCode = api.CodeEdit(ui.Code)
        #ui.txtCode.setGeometry(QtCore.QRect(10, 10, 641, 451))
        ui.gridLayout.addWidget(ui.txtCode, 0, 0, 1, 1)
        ui.txtCode.setObjectName("txtCode")

        #ui.txtCode.backend.start('backend/server.py')

        ui.txtCode.modes.append(modes.CodeCompletionMode())
        ui.txtCode.modes.append(modes.CaretLineHighlighterMode())
        ui.txtCode.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtCode.document()))
        ui.txtCode.panels.append(panels.SearchAndReplacePanel(), api.Panel.Position.TOP)
        ui.txtCode.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtCode.setFont(font)
        ui.txtCode.setPlainText(DefaultCode(),"","")

        dialog.setWindowTitle("easy fMRI manually design ROI - V" + getVersion() + "B" + getBuild())
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnRun.clicked.connect(self.btnRun_click)
        ui.btnNew.clicked.connect(self.btnNew_click)
        ui.btnOpen.clicked.connect(self.btnOpen_click)
        ui.btnSave.clicked.connect(self.btnSave_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnRun_click(self):
        Codes = ui.txtCode.toPlainText()
        try:
            allvars = dict(locals(), **globals())
            exec(Codes, allvars, allvars)
        except Exception as e:
            print(e)
            msgBox = QMessageBox()
            msgBox.setText(str(e))
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()



    def btnNew_click(self):
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
        ui.stb.showMessage("New File")
        currentFile = None


    def btnOpen_click(self):
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
            ui.stb.showMessage(filename)

    def btnSave_click(self):
        global currentFile
        if (currentFile == None):
            filename = SaveFile('Save code file ...',['Code files (*.py)', 'All files (*.*)'], 'py',\
                                        os.path.dirname(str(currentFile)))
            if not len(filename):
                return
            currentFile = filename
            ui.stb.showMessage(filename)
        file = open(currentFile, "w")
        file.write(ui.txtCode.toPlainText())
        file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmManuallyDesignROI.show(frmManuallyDesignROI)
    sys.exit(app.exec_())
