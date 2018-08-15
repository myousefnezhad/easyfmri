from frmMainMenuGUI import *
from frmPreprocess import *

class frmMainMenuGUI(Ui_frmMainMenuGUI):
    ui = Ui_frmMainMenuGUI()
    import sys
    import PyQt5.QtWidgets as QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    frmMainGUI = QtWidgets.QDialog()

    def show(self, ui=ui, frmMainGUI=frmMainGUI, app=app):
        ui.setupUi(frmMainGUI)
        self.set_events(self)
        frmMainGUI.show()
        sys.exit(app.exec_())

    def set_events(self, ui=ui):
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnPreprocess.clicked.connect(self.btnPreprocess_click)


    def btnExit_click(self):
         import sys
         sys.exit()


    def btnPreprocess_click(self, ui=ui, frmMainGUI=frmMainGUI):
        import os
        frmMainGUI.hide()
        os.system("python3 frmPreprocess.py")
        frmMainGUI.show()

# Auto Run
if __name__ == "__main__":
    frmMainMenuGUI.show(frmMainMenuGUI)