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
from PyQt6.QtWidgets import *
from torch import layout

from Base.utility import getVersion, getBuild
from Base.dialogs import SaveFile, LoadFile
from GUI.frmManuallyDesignROIGUI import *

from Base.codeEditor import codeEditor

def DefaultCode():
    return """# This is a template for writing any code in Python 3 style!
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

        # New Code Editor Library
        cEditor = codeEditor(ui)
        ui.txtCode = cEditor.Obj
        cEditor.setObjectName("txtCode")
        cEditor.setText(DefaultCode())
        ui.Code.layout().addWidget(cEditor.Obj)

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
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()



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
            msgBox.setIcon(QMessageBox.Icon.Question)
            msgBox.setStandardButtons(QMessageBox.StandardButton.No| QMessageBox.StandardButton.Yes)
            if (msgBox.exec() == QMessageBox.StandardButton.Yes):
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
            msgBox.setIcon(QMessageBox.Icon.Question)
            msgBox.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
            if (msgBox.exec() == QMessageBox.StandardButton.Yes):
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
    sys.exit(app.exec())
