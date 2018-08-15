#!/usr/bin/env python3
import os
import sys
import nibabel as nb
from PyQt5.QtWidgets import *
from Base.utility import getVersion, getBuild
from Base.dialogs import LoadFile
from GUI.frmImageInfoGUI import *


class frmImageInfo(Ui_frmImageInfo):
    ui = Ui_frmImageInfo()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmImageInfo()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        dialog.setWindowTitle("easy fMRI Image Information - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnImage.clicked.connect(self.btnImage_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnImage_click(self):
        filename = LoadFile("Select an image file ...",['(f)MRI image files (*.nii.gz)', 'All files (*.*)'],'nii.gz',
                            os.path.dirname(ui.txtImage.text()))
        if len(filename):
            if os.path.isfile(filename):
                try:
                    mriHDR = nb.load(filename)
                    ui.txtImageInfo.clear()
                    ui.txtImageInfo.append("Image Shape:")
                    ui.txtImageInfo.append(str(mriHDR.header.get_data_shape()))
                    ui.txtImageInfo.append("Header Information:")
                    ui.txtImageInfo.append(str(mriHDR.header).replace("<class 'nibabel.nifti1.Nifti1Header'> object, endian='<'","").replace("\n","",1))
                    ui.txtImageInfo.append("Affine Matrix:")
                    ui.txtImageInfo.append(str(mriHDR.affine))
                    ui.txtImage.setText(filename)
                except:

                    print("Cannot load image file!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmImageInfo.show(frmImageInfo)
    sys.exit(app.exec_())