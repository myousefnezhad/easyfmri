#!/usr/bin/env python3
import sys

from GUI.frmModelAnalysisGUI import *
from GUI.frmDataEditor import frmDataEditor
from GUI.frmSKModelEditor import frmSKModelEditor
from GUI.frmSKCModelEditor import frmSKCModelEditor


class MainWindow(QtWidgets.QMainWindow):
    parent = None

    def __init__(self, parentin=None):
        super().__init__()
        global parent
        if parentin is not None:
            parent = parentin

    def closeEvent(self, event):
        global parent
        try:
            if parent is not None:
                parent.show()
        except:
            pass

    pass


class frmModelAnalysis(Ui_frmModelAnalysis):
    ui = Ui_frmModelAnalysis()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, parentin=None):
        from Base.utility import getVersion, getBuild
        global dialog, ui, parent
        ui = Ui_frmModelAnalysis()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        if parentin is not None:
            dialog = MainWindow(parentin)
        else:
            dialog = MainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        ui.tabWidget.setCurrentIndex(0)
        # Unsupervised
        ui.cbMAU.addItem("MatLab, SK: RSA: Agglomerative Clustering",10002)
        ui.cbMAU.addItem("MatLab, SK: RSA: Birch Clustering",10003)
        ui.cbMAU.addItem("MatLab, SK: RSA: Gaussian Mixture Clustering",10004)
        ui.cbMAU.addItem("MatLab, SK: RSA: KMeans Clustering",10000)
        ui.cbMAU.addItem("MatLab, SK: RSA: Spectral Clustering",10001)



        # Supervised
        ui.cbMAS.addItem("MatLab, SK: MVPA: AdaBoost Classifier",80005)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Decision Tree",80001)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Gaussian Naive Bayes",80000)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Linear Support Vector Classification (liblinear)",10001)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Multi-Layer Perceptron (MLP)",80002)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Nu Support Vector Classification (libsvm)",10002)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Random Forest",80004)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Stochastic Gradient Descent based Classification",80003)
        ui.cbMAS.addItem("MatLab, SK: MVPA: Support Vector Classification (libsvm)",10000)

        dialog.setWindowTitle("easy fMRI model analysis - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnMASRun.clicked.connect(self.btnMAS_click)
        ui.btnMAURun.clicked.connect(self.btnMAU_click)
        ui.btnDataEditor.clicked.connect(self.btnDataEditor_click)
        ui.btnSKModel.clicked.connect(self.btnSKModelEdior_click)
        ui.btnSKCModel.clicked.connect(self.btnSKCModelEdior_click)


    # Exit function
    def btnClose_click(self):
        global dialog, parent
        dialog.close()

    def btnDataEditor_click(self):
        frmDataEditor.show(frmDataEditor)

    def btnSKModelEdior_click(self):
        frmSKModelEditor.show(frmSKModelEditor)

    def btnSKCModelEdior_click(self):
        frmSKCModelEditor.show(frmSKCModelEditor)

    def btnMAU_click(self):
        MAID = ui.cbMAU.currentData()
        if MAID == 10000:
            from GUI.frmMAKMeans import frmMAKMeans
            frmMAKMeans.show(frmMAKMeans)
            return
        if MAID == 10001:
            from GUI.frmMASpectral import frmMASpectral
            frmMASpectral.show(frmMASpectral)
            return
        if MAID == 10002:
            from GUI.frmMAAgglomerative import frmMAAgglomerative
            frmMAAgglomerative.show(frmMAAgglomerative)
            return
        if MAID == 10003:
            from GUI.frmMABirch import frmMABirch
            frmMABirch.show(frmMABirch)
            return
        if MAID == 10004:
            from GUI.frmMAGaussian import frmMAGaussian
            frmMAGaussian.show(frmMAGaussian)
            return



    def btnMAS_click(self):
        MAID = ui.cbMAS.currentData()
        if MAID == 10000:
            from GUI.frmMASVM import frmMASVM
            frmMASVM.show(frmMASVM)
            return
        if MAID == 10001:
            from GUI.frmMALSVM import frmMALSVM
            frmMALSVM.show(frmMALSVM)
            return
        if MAID == 10002:
            from GUI.frmMANuSVM import frmMANuSVM
            frmMANuSVM.show(frmMANuSVM)
            return

        if MAID == 80000:
            from GUI.frmMAGNB import frmMAGNB
            frmMAGNB.show(frmMAGNB)
            return
        if MAID == 80001:
            from GUI.frmMADT import frmMADT
            frmMADT.show(frmMADT)
            return
        if MAID == 80002:
            from GUI.frmMAMLP import frmMAMLP
            frmMAMLP.show(frmMAMLP)
            return
        if MAID == 80003:
            from GUI.frmMASGDC import frmMASGDC
            frmMASGDC.show(frmMASGDC)
            return
        if MAID == 80004:
            from GUI.frmMARFC import frmMARFC
            frmMARFC.show(frmMARFC)
            return
        if MAID == 80005:
            from GUI.frmMAAdaBoost import frmMAAdaBoost
            frmMAAdaBoost.show(frmMAAdaBoost)
            return

# Auto Run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmModelAnalysis.show(frmModelAnalysis)
    sys.exit(app.exec_())
