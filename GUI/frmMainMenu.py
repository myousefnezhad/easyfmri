#!/usr/bin/env python3
import PyQt5.QtWidgets as QtWidgets
from GUI.frmMainMenuGUI import *
from GUI.frmFeatureAnalysis import *
from GUI.frmModelAnalysis import *
from GUI.frmPreprocess import *
from GUI.frmVisualization import *

from Base.utility import About





class frmMainMenuGUI(QtWidgets.QMainWindow):
    dialog = None
    ui = Ui_frmMainMenuGUI()


    def show(self):
        from Base.utility import getVersion,getBuild
        global dialog, ui
        ui = Ui_frmMainMenuGUI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        dialog.setWindowTitle("easy fMRI - V" + getVersion() + "B" + getBuild())

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_events(self):
        global ui
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnPreprocess.clicked.connect(self.btnPreprocess_click)
        ui.btnFeatureAnalysis.clicked.connect(self.btnFeatureAnalysis_click)
        ui.btnModelAnalysis.clicked.connect(self.btnModelAnalysis_click)
        ui.btnAbout.clicked.connect(self.btnAbout_click)
        ui.btnVisualization.clicked.connect(self.btnVisualization_click)


    def btnExit_click(self):
         import sys
         sys.exit()

    def btnAbout_click(self):
        from Base.utility import MyMessageBox

        msgBox = MyMessageBox()
        msgBox.setMinimumWidth(800)
        msgBox.setText(About())
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        pass

    def btnPreprocess_click(self):
        global dialog
        dialog.hide()
        frmPreprocess.show(frmPreprocess,dialog)
        #dialog.show()


    def btnFeatureAnalysis_click(self):
        global dialog
        dialog.hide()
        frmFeatureAnalysis.show(frmFeatureAnalysis,dialog)

    def btnModelAnalysis_click(self):
        global dialog
        dialog.hide()
        frmModelAnalysis.show(frmModelAnalysis,dialog)

    def btnVisualization_click(self):
        global dialog
        dialog.hide()
        frmVisalization.show(frmVisalization,dialog)


# Auto Run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMainMenuGUI.show(frmMainMenuGUI)
    sys.exit(app.exec_())