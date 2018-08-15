#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io
from Base.Conditions import Conditions
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sklearn.preprocessing import label_binarize
from Base.dialogs import LoadFile, SaveFile, LoadMultiFile
from Base.utility import getVersion, getBuild
from GUI.frmResultReportGUI import *


class frmResultReport(Ui_frmResultReport):
    ui = Ui_frmResultReport()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmResultReport()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()

        ui.setupUi(dialog)
        self.set_events(self)



        dialog.setWindowTitle("easy fMRI report from multi-file results - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        ui.btnExit.clicked.connect(self.btnClose_click)
        ui.btnAdd.clicked.connect(self.btnAdd_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)
        ui.btnReport.clicked.connect(self.btnReport_click)
        ui.btnClear.clicked.connect(self.btnClear_click)
        ui.btnSave.clicked.connect(self.btnSave_click)


    def btnClose_click(self):
        global dialog
        dialog.close()

    def btnAdd_click(self):
        files = LoadMultiFile("Select data/results files ...",['Data or Result Files (*.mat *.ezdata *.ezmat)', 'All files (*.*)'],'mat')
        if len(files):
            for file in files:
                item = QListWidgetItem()
                item.setText(str(file))
                ui.lvFile.addItem(item)

    def btnRemove_click(self):
        for item in ui.lvFile.selectedItems():
            ui.lvFile.takeItem(ui.lvFile.row(item))

    def btnClear_click(self):
        ui.txtReport.clear()

    def btnReport_click(self):
        msgBox = QMessageBox()

        Vars = str(ui.txtVars.text()).replace(","," ").split()
        if not len(Vars):
            msgBox.setText("Please enter variables!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.lvFile.count() <= 0:
            msgBox.setText("Please enter files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.cbClear.isChecked():
            ui.txtReport.clear()

        Len = ui.txtChar.value()

        str1 = ""

        for var in Vars:
            str1 = str1 + "\t" + var if str != "" else var
        ui.txtReport.append(str1 + "\n")


        for itemIndx in range(ui.lvFile.count()):
            filename = ui.lvFile.item(itemIndx).text()
            print("Reading " + filename)
            data = io.loadmat(filename)
            dat1 = ""

            if   ui.rbAddress.isChecked():
                str1 =  filename
            elif ui.rbNone.isChecked():
                str1 = ""
            elif ui.rbIndex.isChecked():
                str1 = str(itemIndx)
            else:
                str1 = os.path.split(os.path.abspath(filename))[1]


            if not ui.rbNone.isChecked():
                if len(str1) < Len:
                    for _ in range(Len - len(str1)):
                        str1 = str1 + ' '
                else:
                    str1 = str1[0:Len]

            for var in Vars:
                try:
                    dat1 = str(data[var])
                except:
                    dat1 = 'None'
                str1 = str1 + "\t" + dat1 if str1 != "" else dat1
            ui.txtReport.append(str1 + "\n")

    def btnSave_click(self):
        file = SaveFile('Save Report',['Text files (*.txt)', 'All files (*.*)'],'txt')
        if len(file):
            open(file,"w").write(ui.txtReport.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmResultReport.show(frmResultReport)
    sys.exit(app.exec_())