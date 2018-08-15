#!/usr/bin/env python3
import os
import sys

from PyQt5.QtWidgets import *

from GUI.frmEventConcatenatorGUI import *
from Base.dialogs import SaveFile, LoadFile


class frmEventConcatenator(Ui_frmEventConcatenator):
    ui = Ui_frmEventConcatenator()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmEventConcatenator()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.lwFiles.setColumnCount(2)
        ui.lwFiles.setHeaderLabels(['Offset','File'])


        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnOFile.clicked.connect(self.btnOFile_click)
        ui.btnConcatenate.clicked.connect(self.btnConcatenate_click)
        ui.btnRemove.clicked.connect(self.btnRemove_click)
        ui.btnAdd.clicked.connect(self.btnAdd_click)




    def btnClose_click(self):
        global dialog
        dialog.close()
        pass

    def btnAdd_click(self):
        global ui
        ifile = LoadFile("Select an event file ...",['Event files (*.tsv)','Text files (*.txt)','All files (*.*)'],"tsv")
        if len(ifile):
            if os.path.isfile(ifile):
                item = QtWidgets.QTreeWidgetItem()
                item.setText(0,str(ui.txtOffset.value()))
                item.setText(1,ifile)
                ui.lwFiles.addTopLevelItem(item)

    def btnRemove_click(self):
        if not len(ui.lwFiles.selectedItems()):
            msgBox = QMessageBox()
            msgBox.setText("Please select a item first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        ui.lwFiles.takeTopLevelItem(ui.lwFiles.indexOfTopLevelItem(ui.lwFiles.selectedItems()[0]))

    def btnOFile_click(self):
        global ui
        ofile = SaveFile("Output event files ...",['Event files (*.tsv)'], 'tsv',os.path.dirname(ui.txtOFile.text()))
        if len(ofile):
                ui.txtOFile.setText(ofile)


    def btnConcatenate_click(self):
        if ui.lwFiles.topLevelItemCount() < 1:
            msgBox = QMessageBox()
            msgBox.setText("There is no input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.lwFiles.topLevelItemCount() < 2:
            msgBox = QMessageBox()
            msgBox.setText("You must select at least two files!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        files = []
        offsets = []
        for index in range(ui.lwFiles.topLevelItemCount()):
            item = ui.lwFiles.topLevelItem(index)
            offsets.append(int(item.text(0))-1)
            file = item.text(1)
            if not os.path.isfile(file):
                print(file + " not found!")
                return
            files.append(file)

        ofile = ui.txtOFile.text()
        if not len(ofile):
            print("Please enter Output File!")
            msgBox = QMessageBox()
            msgBox.setText("Please enter Output File!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        print("Generating Output File ...")

        with open(ofile,"w") as outfile:

            if len(ui.txtHDR.text()):
                header = str(ui.txtHDR.text()).replace("\n","")
                outfile.write(header+"\n")
            for offsetinx, filename in enumerate(files):
                print("Loading File: " + filename)
                with open(filename) as infile:
                    for lineinx, line in enumerate(infile):
                        if lineinx >= offsets[offsetinx]:
                            outfile.write(line)

        print("Output is generated!")
        msgBox = QMessageBox()
        msgBox.setText("Output is generated!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmEventConcatenator.show(frmEventConcatenator)
    sys.exit(app.exec_())