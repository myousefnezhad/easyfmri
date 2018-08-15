import sys
from PyQt5.QtWidgets import QMessageBox
import PyQt5.QtWidgets as QtWidgets
import os
from PyQt5.QtWidgets import QFileDialog
import configparser as cp
import glob
import nibabel as nb

from frmPreprocessingGUI import *
from utility            import getTimeSliceText
from Setting            import Setting
from SettingHistory     import History
from BrainExtractor     import BrainExtractor
from EventGenerator     import EventGenerator
from ScriptGenerator    import ScriptGenerator
from RunPreprocess      import RunPreprocess


class frmPreprocess(Ui_frmPreprocess):
    ui = Ui_frmPreprocess()

    def show(self,ui=ui):
        app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        frmMainGUI = QtWidgets.QDialog()
        ui.setupUi(frmMainGUI)
        self.set_events(self)
        self.set_history(self)
        ui.tabWidget.setCurrentIndex(0)
        ui.cbSliceTime.addItem("None")
        ui.cbSliceTime.addItem("Regular up (1, 2, ..., n)")
        ui.cbSliceTime.addItem("Regular down (n, n-1, ..., 1)")
        ui.cbSliceTime.addItem("Interleaved (2, 4, 6, ...), (1, 3, 5, ...)")
        frmMainGUI.show()
        sys.exit(app.exec_())

    def showIn(self,ui=ui):
        app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        frmMainGUI = QtWidgets.QDialog()
        ui.setupUi(frmMainGUI)
        self.set_events(self)
        self.set_history(self)
        ui.tabWidget.setCurrentIndex(0)
        ui.cbSliceTime.addItem("None")
        ui.cbSliceTime.addItem("Regular up (1, 2, ..., n)")
        ui.cbSliceTime.addItem("Regular down (n, n-1, ..., 1)")
        ui.cbSliceTime.addItem("Interleaved (2, 4, 6, ...), (1, 3, 5, ...)")
        frmMainGUI.show()
        #sys.exit(app.exec_())


    def set_events(self,ui=ui):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnDIR.clicked.connect(self.btnDIR_click)
        ui.btnTest.clicked.connect(self.btnTest_click)
        ui.btnSave.clicked.connect(self.btnSave_click)
        ui.btnLoad.clicked.connect(self.btnLoad_click)
        ui.btnLoadHistory.clicked.connect(self.btnLoadHistory_click)
        ui.btnClearAllHistory.clicked.connect(self.btnClearAllHistory_click)
        ui.btnRemoveHistory.clicked.connect(self.btnRemoveHistory_click)
        ui.lwHistory.itemDoubleClicked.connect(self.btnLoadHistory_click)
        ui.btnExtractor.clicked.connect(self.btnBrainExtractor_click)
        ui.btnEvent.clicked.connect(self.btnEventGenerator_click)
        ui.btnPreprocessScripts.clicked.connect(self.btnPreprocessingScript_click)
        ui.btnPreprocess.clicked.connect(self.btn_RunProcess_click)

    def set_history(self,ui=ui):
        history = History()
        histories = history.load_history()
        ui.lwHistory.clear()
        for hist in histories:
            item = QtWidgets.QListWidgetItem(hist)
            ui.lwHistory.addItem(item)


    def btnClose_click(self):
       sys.exit()

    def btnDIR_click(self,ui=ui):
        from utility import fixstr
        import numpy as np
        current = ui.txtDIR.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        directory = dialog.getExistingDirectory(None,"Open Main Directory",current,flags)
        if len(directory):
            ui.txtDIR.setText(directory)
            listFiles = glob.glob(directory+"/sub-" + fixstr(1, np.int32(ui.txtSubLen.text()), ui.txtSubPer.text()) + "/func/*."+ui.txtBOLD.text())
            if not len(listFiles):
                msgBox = QMessageBox()
                msgBox.setText("Cannot find the BOLD data for the first subject, please check the parameters")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            ui.txtTask.setText(str(listFiles[0]).replace(directory+"/sub-" + fixstr(1, np.int32(ui.txtSubLen.text()), ui.txtSubPer.text()) + "/func/sub-" + fixstr(1, np.int32(ui.txtSubLen.text()), ui.txtSubPer.text()) + "_task-","").replace("_run-01_bold." + ui.txtBOLD.text(),""))
            try:
                BoldHDR = nb.load(listFiles[0])
                ui.txtTR.setText(str(BoldHDR.header.get_zooms()[3]))
                ui.txtTotalVol.setText(str(BoldHDR.get_shape()[3]))
                Voxels = BoldHDR.header.get_zooms()[0:3]
                ui.txtVoxel.setText("Voxel Size: " + str(Voxels))
                ui.txtFWHM.setText(str(np.max(Voxels)*3))
            except:
                pass

    def btnTest_click(self,ui=ui):
        setting = Setting()
        if setting.checkValue(ui):
            msgBox = QMessageBox()
            msgBox.setText("It is okay")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def btnSave_click(self,ui=ui):
        SettingFileName = ui.txtSetting.text()
        setting = Setting()
        if not setting.checkValue(ui):
            print("TEST: It is failed")
        else:
            print("TEST: It is okay")
            OpenDialog = False

            if not len(SettingFileName):
                OpenDialog = True
            else:
                msgBox = QMessageBox()
                reply = msgBox.question(msgBox, 'Save as ...', 'Do you want to save settting in the same file?'
                                                   , QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.No:
                    OpenDialog = True


            if OpenDialog:
                dialog = QFileDialog()
                settingFileName = setting.mainDIR + "/setting-" + setting.Task + ".ini"
                filename = dialog.getSaveFileName(None,"Save setting file ...",settingFileName,options=QFileDialog.DontUseNativeDialog)
                if len(filename):
                    SettingFileName = filename[0]
                else:
                    SettingFileName = ""



            if len(SettingFileName):
                config = cp.ConfigParser()
                config.read(SettingFileName)
                config['DEFAULT']['maindir']    = setting.mainDIR
                config['DEFAULT']['task']       = setting.Task
                config['DEFAULT']['sub_num']    = setting.SubNum
                config['DEFAULT']['sub_len']    = setting.SubLen
                config['DEFAULT']['sub_perfix'] = setting.SubPer
                config['DEFAULT']['run']        = setting.Run
                config['DEFAULT']['run_len']    = setting.RunLen
                config['DEFAULT']['run_perfix'] = setting.RunPer
                config['DEFAULT']['bold']       = setting.BOLD
                config['DEFAULT']['onset']      = setting.Onset
                config['DEFAULT']['TR']         = str(setting.TR)
                config['DEFAULT']['FWHM']       = str(setting.FWHM)
                config['DEFAULT']['deletevol']  = str(setting.DeleteVol)
                config['DEFAULT']['totalvol']   = str(setting.TotalVol)

                config['DEFAULT']['onsetrid']   = str(setting.OnsetRID)
                config['DEFAULT']['conditionrid'] = str(setting.ConditionRID)
                config['DEFAULT']['durationrid'] = str(setting.DurationRID)

                config['DEFAULT']['timeslice']  = str(setting.TimeSlice)
                config['DEFAULT']['highpass']   = str(setting.HighPass)
                config['DEFAULT']['rowstart']   = str(setting.RowStart)

                config['DEFAULT']['motion']     = str(setting.Motion)
                config['DEFAULT']['anat']       = str(setting.Anat)

                with open(SettingFileName, 'w') as configfile:
                    config.write(configfile)

                ui.txtSetting.setText(SettingFileName)
                ui.btnExtractor.setEnabled(setting.Anat)
                ui.cbShowResult.setEnabled(setting.Anat)

                history = History()
                history.add_history(SettingFileName)
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)

                print("Saved setting in ",SettingFileName)

    def btnLoad_click(self,ui=ui):
        dialog = QFileDialog()
        filename = dialog.getOpenFileName(None, "Open setting file ...", ui.txtDIR.text(), options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            setting = Setting()
            setting.Load(filename)
            if not setting.empty:
                ui.txtSetting.setText(filename)
                ui.txtDIR.setText(setting.mainDIR)
                ui.txtTask.setText(setting.Task)
                ui.txtBOLD.setText(setting.BOLD)
                ui.txtOnset.setText(setting.Onset)
                ui.txtSubNum.setText(setting.SubNum)
                ui.txtSubLen.setText(setting.SubLen)
                ui.txtSubPer.setText(setting.SubPer)
                ui.txtRunNum.setText(setting.Run)
                ui.txtRunPer.setText(setting.RunPer)
                ui.txtRunNum.setText(setting.Run)
                ui.txtTR.setText(str(setting.TR))
                ui.txtFWHM.setText(str(setting.FWHM))
                ui.txtTotalVol.setText(str(setting.TotalVol))
                ui.txtDeleteVol.setText(str(setting.DeleteVol))
                ui.txtOnsetRID.setText(str(setting.OnsetRID))
                ui.txtDurationRID.setText(str(setting.DurationRID))
                ui.txtConditionRID.setText(str(setting.ConditionRID))
                ui.txtRowStart.setText(str(setting.RowStart))
                ui.txtHighPass.setText(str(setting.HighPass))
                Title = getTimeSliceText(setting.TimeSlice)
                if Title is None:
                    print("Time Slice loading error!")
                else:
                    ui.cbSliceTime.setCurrentText(Title)
                ui.cbMotionCorrection.setChecked(setting.Motion)
                ui.cbRegAnat.setChecked(setting.Anat)
                ui.txtVoxel.setText("Voxel Size: None")
                ui.btnExtractor.setEnabled(setting.Anat)
                ui.cbShowResult.setEnabled(setting.Anat)

                history = History()
                history.add_history(filename)
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)

    def btnLoadHistory_click(self,ui=ui):
        try:
            filename = ui.lwHistory.selectedItems()[0].text()
            if len(filename):
                setting = Setting()
                setting.Load(filename)
                if not setting.empty:
                    ui.txtSetting.setText(filename)
                    ui.txtDIR.setText(setting.mainDIR)
                    ui.txtTask.setText(setting.Task)
                    ui.txtBOLD.setText(setting.BOLD)
                    ui.txtOnset.setText(setting.Onset)
                    ui.txtSubNum.setText(setting.SubNum)
                    ui.txtSubLen.setText(setting.SubLen)
                    ui.txtSubPer.setText(setting.SubPer)
                    ui.txtRunNum.setText(setting.Run)
                    ui.txtRunPer.setText(setting.RunPer)
                    ui.txtRunNum.setText(setting.Run)
                    ui.txtTR.setText(str(setting.TR))
                    ui.txtFWHM.setText(str(setting.FWHM))
                    ui.txtTotalVol.setText(str(setting.TotalVol))
                    ui.txtDeleteVol.setText(str(setting.DeleteVol))
                    ui.txtOnsetRID.setText(str(setting.OnsetRID))
                    ui.txtDurationRID.setText(str(setting.DurationRID))
                    ui.txtConditionRID.setText(str(setting.ConditionRID))
                    ui.txtRowStart.setText(str(setting.RowStart))
                    ui.txtHighPass.setText(str(setting.HighPass))
                    ui.txtVoxel.setText("Voxel Size: None")
                    Title = getTimeSliceText(setting.TimeSlice)
                    if Title is None:
                        print("Time Slice loading error!")
                    else:
                        ui.cbSliceTime.setCurrentText(Title)
                    ui.cbMotionCorrection.setChecked(setting.Motion)
                    ui.cbRegAnat.setChecked(setting.Anat)
                    ui.btnExtractor.setEnabled(setting.Anat)
                    ui.cbShowResult.setEnabled(setting.Anat)
                    ui.tabWidget.setCurrentIndex(3)
        except:
            return

    def btnClearAllHistory_click(self,ui=ui):
        history = History()
        history.clear_history()
        ui.lwHistory.clear()

    def btnRemoveHistory_click(self,ui=ui):
        try:
            filename = ui.lwHistory.selectedItems()[0].text()
            if len(filename):
                history = History()
                history.del_history(str(filename).replace("\n",""))
                histories = history.load_history()
                ui.lwHistory.clear()
                for hist in histories:
                    item = QtWidgets.QListWidgetItem(hist)
                    ui.lwHistory.addItem(item)
        except:
            return

    def btnBrainExtractor_click(self,ui=ui):
        setting = Setting()
        isChange = setting.checkGUI(ui,ui.txtSetting.text())
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                brainExtractor = BrainExtractor()
                brainExtractor.run(ui.txtSetting.text(),ui.cbShowResult.checkState())
                print("TASK FINISHED!")
                msgBox = QMessageBox()
                msgBox.setText("All brains are extracted!")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return

    def btnEventGenerator_click(self, ui=ui):
            setting = Setting()
            isChange = setting.checkGUI(ui, ui.txtSetting.text())
            if isChange == None:
                msgBox = QMessageBox()
                if len(ui.txtSetting.text()):
                    msgBox.setText("Please verify parameters")
                else:
                    msgBox.setText("You must save setting first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                if isChange == True:
                    msgBox = QMessageBox()
                    msgBox.setText("Parameters are changed. Please save them first!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                else:
                    eventGenerator = EventGenerator()
                    eventGenerator.run(ui.txtSetting.text())
                    #,setting.OnsetRID,setting.DurationRID,setting.ConditionRID,setting.DontReadFist)
                    print("TASK FINISHED!")
                    msgBox = QMessageBox()
                    msgBox.setText("All events are generated!")
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return

    def btnPreprocessingScript_click(self,ui=ui):
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(),checkGeneratedFiles=True)
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                scriptGenerator = ScriptGenerator()
                scriptGenerator.run(ui.txtSetting.text())
                print("TASK FINISHED!")
                msgBox = QMessageBox()
                msgBox.setText("All scripts are generated!")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return


    def btn_RunProcess_click(self,ui=ui):
        setting = Setting()
        isChange = setting.checkGUI(ui, ui.txtSetting.text(),checkGeneratedFiles=True)
        if isChange == None:
            msgBox = QMessageBox()
            if len(ui.txtSetting.text()):
                msgBox.setText("Please verify parameters")
            else:
                msgBox.setText("You must save setting first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        else:
            if isChange == True:
                msgBox = QMessageBox()
                msgBox.setText("Parameters are changed. Please save them first!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return
            else:
                runPreprocess = RunPreprocess()
                if not runPreprocess.Check(ui.txtSetting.text(),ui.cbJustRun.checkState()):
                    msgBox = QMessageBox()
                    msgBox.setText("Script(s) are not found!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return
                else:
                    runPreprocess.Run(ui.txtSetting.text(),ui.cbJustRun.checkState(),ui.cbRemoveOlds.checkState())
                    print("TASK FINISHED!")
                    msgBox = QMessageBox()
                    msgBox.setText("All scripts are generated!")
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return






# Auto Run
if __name__ == "__main__":
    frmPreprocess.show(frmPreprocess)