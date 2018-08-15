#!/usr/bin/env python3
from frmMainMenuGUI import *
from frmPreprocess import *
import PyQt5.QtWidgets as QtWidgets
#import PyQt5.QtCore as QtCore
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets
import numpy, scipy, sklearn
import os, platform
import nibabel, nipype

import sys
import subprocess
import configparser as cp
import glob

from frmSelectSession   import frmSelectSession
from frmEventViewer     import frmEventViewer
from frmRenameFile      import frmRenameFile
from frmScriptEditor    import frmScriptEditor

from utility            import getTimeSliceText,fixstr,setParameters
from Setting            import Setting
from SettingHistory     import History
from BrainExtractor     import BrainExtractor
from EventGenerator     import EventGenerator
from ScriptGenerator    import ScriptGenerator
from RunPreprocess      import RunPreprocess



class frmMainMenuGUI(QtWidgets.QMainWindow):
    dialog = None
    ui = Ui_frmMainMenuGUI()


    def show(self):
        global dialog, ui
        ui = Ui_frmMainMenuGUI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_events(self):
        global ui
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnPreprocess.clicked.connect(self.btnPreprocess_click)


    def btnExit_click(self):
         import sys
         sys.exit()


    def btnPreprocess_click(self):
        global dialog
        dialog.hide()
        frmPreprocess.show(frmPreprocess,dialog)
        #dialog.show()

# Auto Run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMainMenuGUI.show(frmMainMenuGUI)
    sys.exit(app.exec_())