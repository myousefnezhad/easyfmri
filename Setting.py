

class Setting:
    def __init__(self):
        self.mainDIR        = None
        self.SubNum         = None
        self.SubLen         = None
        self.SubPer         = None
        self.Task           = None
        self.Run            = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.empty          = True
        self.OnsetRID       = None
        self.ConditionRID   = None
        self.DurationRID    = None

        self.RowStart       = None
        self.HighPass       = None
        self.TimeSlice      = None


    def checkValue(self, ui, checkFiles=True, checkGeneratedFiles=False):
        import numpy as np
        import scipy.io as io
        from PyQt5.QtWidgets import QMessageBox
        from utility import fixstr,getTimeSliceID
        import os

        self.empty = True
        msgBox = QMessageBox()

        mainDIR = ui.txtDIR.text()
        Task = ui.txtTask.text()
        # Check Directory
        if not len(mainDIR):
            msgBox.setText("There is no main directory")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if not os.path.isdir(mainDIR):
            msgBox.setText("Main directory doesn't exist")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Main directory is okay.")
        if not len(Task):
            msgBox.setText("There is no task title")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubNum = np.int32(ui.txtSubNum.text())
            1 / SubNum
        except:
            msgBox.setText("Number of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Number of subjects is valid")
        try:
            SubLen = np.int32(ui.txtSubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is valid")
        try:
            RunLen = np.int32(ui.txtRunLen.text())
            1 / RunLen
        except:
            msgBox.setText("Length of runs must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of runs is valid")

        StrRuns = str(ui.txtRunNum.text()).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split()
        Run = []
        for srun in StrRuns:
            try:
                Run.append(np.int32(srun))
            except:
                msgBox.setText("Run must include an integer array")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        if (len(Run) == 1):
            runValue = Run[0]
            Run = []
            for _ in range(0,SubNum):
                Run.append(runValue)
        else:
            if (len(Run) != SubNum):
                msgBox.setText("Number of Runs must include a unique number for all subject or an array with size of number of subject, e.g. [1,2,2,1]")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        print("Number of Runs are okay.")
        # Check fMRI Images
        try:
            TR = np.double(ui.txtTR.text())
            1 / TR
        except:
            msgBox.setText("TR must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if TR <= 0:
            msgBox.setText("TR must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("TR is okay")
        try:
            FWHM = np.double(ui.txtFWHM.text())
            1 / FWHM
        except:
            msgBox.setText("FWHM must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if FWHM <= 0:
            msgBox.setText("FWHM must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("FWHM is okay")
        # Advance
        try:
            TotalVol = np.int32(ui.txtTotalVol.text())
        except:
            msgBox.setText("Total Volumn must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if TotalVol < 0:
            msgBox.setText("Total Volumn must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Total Volumn is okay")
        try:
            DeleteVol = np.int32(ui.txtDeleteVol.text())
        except:
            msgBox.setText("Delete Volumn must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if DeleteVol < 0:
            msgBox.setText("Delete Volumn must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Delete Volumn is okay")
        try:
            OnsetRID = np.int32(ui.txtOnsetRID.text())
        except:
            msgBox.setText("Onset Row ID must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if OnsetRID < 0:
            msgBox.setText("Onset Row ID must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Onset Row ID is okay")
        try:
            ConditionRID = np.int32(ui.txtConditionRID.text())
        except:
            msgBox.setText("Condition Row ID must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if ConditionRID < 0:
            msgBox.setText("Condition Row ID must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Condition Row ID is okay")
        try:
            DurationRID = np.int32(ui.txtDurationRID.text())
        except:
            msgBox.setText("Duration Row ID must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if DurationRID < 0:
            msgBox.setText("Duration Row ID must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Duration Row ID is okay")
        try:
            RowStart = np.int32(ui.txtRowStart.text())
        except:
            msgBox.setText("Row Start must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if DurationRID <= 0:
            msgBox.setText("Row Start must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Row Start is okay")
        try:
            HighPass = np.double(ui.txtHighPass.text())
        except:
            msgBox.setText("High Pass cutoff must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if HighPass <= 0:
            msgBox.setText("High Pass cutoff must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("High Pass cutoff is okay")

        if checkFiles:
            print("Validating files ...")

            for s in range(1, SubNum + 1):
                print("Analyzing Subject %d ..." % (s))
                SubDIR = mainDIR + "/" + "sub-" + fixstr(s, SubLen, ui.txtSubPer.text())
                # checking anat file
                filename = "sub-" + fixstr(s, SubLen, ui.txtSubPer.text()) + "_T1w." + ui.txtBOLD.text()
                addr = SubDIR + "/anat/" + filename
                if os.path.isfile(addr):
                    print(addr, " - OKAY.")
                else:
                    print(addr, " - file not find!")
                    return False
                if checkGeneratedFiles and ui.cbRegAnat.isChecked():
                    # BET Files
                    filename = "sub-" + fixstr(s, SubLen, ui.txtSubPer.text()) + "_T1w_BET." + ui.txtBOLD.text()
                    addr = SubDIR + "/anat/" + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                for r in range(1,Run[s-1]+1):

                    # BOLD File Check
                    filename = "sub-" + fixstr(s, SubLen, ui.txtSubPer.text()) + "_task-" + Task + "_run-" + \
                               fixstr(r, RunLen, ui.txtRunPer.text()) + "_bold." + ui.txtBOLD.text()
                    addr = SubDIR + "/func/" + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                    # Event File Check
                    filename = "sub-" + fixstr(s, SubLen, ui.txtSubPer.text()) + "_task-" + Task + "_run-" + \
                               fixstr(r, RunLen, ui.txtRunPer.text()) + "_events." + ui.txtOnset.text()
                    addr = SubDIR + "/func/" + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                    if checkGeneratedFiles:
                        EventFolder = "sub-" + fixstr(s, SubLen, ui.txtSubPer.text()) + "_task-" + Task + "_run-" + \
                                   fixstr(r, RunLen, ui.txtRunPer.text()) + "_events/"
                        addr = SubDIR + "/func/" + EventFolder
                        if os.path.isdir(addr):
                            print(addr, " - OKAY.")
                            try:
                                Cond = io.loadmat(addr + "Cond.mat")
                                for fileID in range(1,Cond["Cond"].shape[0]+1):
                                    if os.path.isfile(addr + "/Cond_" + str(fileID) + ".tab"):
                                        print(addr + "Cond_" + str(fileID) + ".tab - OKAY.")
                                    else:
                                        print(addr + "Cond_" + str(fileID) + ".tab - file not find!")
                                        return False
                            except:
                                print(addr + "Cond.mat - loading error!")
                                return False
                        else:
                            print(addr, " - file not find!")
                            return False

        self.mainDIR = mainDIR

        self.SubNum = str(SubNum)
        self.SubLen = str(SubLen)
        self.SubPer = ui.txtSubPer.text()

        self.Task = str(Task)

        self.Run = str(Run)
        self.RunLen = str(RunLen)
        self.RunPer = ui.txtRunPer.text()

        self.BOLD = ui.txtBOLD.text()
        self.Onset= ui.txtOnset.text()

        self.TR = TR
        self.FWHM = FWHM

        self.DeleteVol = DeleteVol
        self.TotalVol = TotalVol
        self.OnsetRID = OnsetRID
        self.ConditionRID = ConditionRID
        self.DurationRID = DurationRID

        self.HighPass = HighPass
        self.RowStart = RowStart


        TimeSlice = getTimeSliceID(ui.cbSliceTime.currentText())
        if TimeSlice is None:
            print("Error in Slice Time!")
            return False

        self.TimeSlice = np.int32(TimeSlice)

        self.Motion = ui.cbMotionCorrection.isChecked()
        self.Anat = ui.cbRegAnat.isChecked()

        self.empty = False

        return True

    def Load(self,filename):
        import numpy as np
        import configparser as cp
        from utility import Str2Bool

        self.mainDIR        = None
        self.SubNum         = None
        self.SubLen         = None
        self.SubPer         = None
        self.Task           = None
        self.Run            = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.empty          = True
        self.OnsetRID       = None
        self.ConditionRID   = None
        self.DurationRID    = None
        self.RowStart       = None
        self.HighPass       = None
        self.TimeSlice      = None
        self.empty          = True
        if len(filename):
            try:
                config = cp.ConfigParser()
                config.read(filename)
                self.mainDIR    = config['DEFAULT']['maindir']
                self.Task       = config['DEFAULT']['task']

                self.SubNum     = config['DEFAULT']['sub_num']
                self.SubLen     = config['DEFAULT']['sub_len']
                self.SubPer     = config['DEFAULT']['sub_perfix']

                self.Run        = config['DEFAULT']['run']
                self.RunLen     = config['DEFAULT']['run_len']
                self.RunPer     = config['DEFAULT']['run_perfix']

                self.BOLD       = config['DEFAULT']['bold']
                self.Onset      = config['DEFAULT']['onset']
                self.TR         = np.double(config['DEFAULT']['TR'])
                self.FWHM       = np.double(config['DEFAULT']['FWHM'])
                self.DeleteVol  = np.int32(config['DEFAULT']['deletevol'])
                self.TotalVol   = np.int32(config['DEFAULT']['totalvol'])
                self.OnsetRID   = np.int32(config['DEFAULT']['onsetrid'])
                self.ConditionRID   = np.int32(config['DEFAULT']['conditionrid'])
                self.DurationRID    = np.int32(np.int32(config['DEFAULT']['durationrid']))

                self.DurationRID    = np.int32(np.int32(config['DEFAULT']['durationrid']))

                self.Motion     = Str2Bool(config['DEFAULT']['motion'])
                self.Anat       = Str2Bool(config['DEFAULT']['anat'])

                self.TimeSlice = np.int32(config['DEFAULT']['timeslice'])
                self.HighPass  = np.double(config['DEFAULT']['highpass'])
                self.RowStart  = np.int32(config['DEFAULT']['rowstart'])

                self.empty = False

                return True
            except:
                print("Error in loading!")
                return False

        return False

    def checkGUI(self,ui, SettingFileName,checkGeneratedFiles=False):
        import numpy as np
        import configparser as cp
        from utility import Str2Bool
        # init Empty
        self.mainDIR        = None
        self.SubNum         = None
        self.SubLen         = None
        self.SubPer         = None
        self.Task           = None
        self.Run            = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.empty          = True
        self.OnsetRID       = None
        self.ConditionRID   = None
        self.DurationRID    = None
        self.RowStart       = None
        self.HighPass       = None
        self.TimeSlice      = None
        self.empty          = True
        self.checkValue(ui,checkGeneratedFiles=checkGeneratedFiles)
        if self.empty:
            print("Error in GUI parameters")
            return None
        else:
            if not len(SettingFileName):
                print("Cannot find setting file")
                return None
            else:
                try:
                    config = cp.ConfigParser()
                    config.read(SettingFileName)
                    if self.mainDIR != config['DEFAULT']['maindir']:
                        return True
                    elif self.Task != config['DEFAULT']['task']:
                        return True
                    elif np.double(self.SubNum) != np.double(config['DEFAULT']['sub_num']):
                        return True
                    elif np.double(self.SubLen) != np.double(config['DEFAULT']['sub_len']):
                        return True
                    elif self.SubPer != config['DEFAULT']['sub_perfix']:
                        return True
                    elif self.Run != config['DEFAULT']['run']:
                        return True
                    elif np.double(self.RunLen) != np.double(config['DEFAULT']['run_len']):
                        return True
                    elif self.RunPer != config['DEFAULT']['run_perfix']:
                        return True
                    elif self.BOLD != config['DEFAULT']['bold']:
                        return True
                    elif self.Onset != config['DEFAULT']['onset']:
                        return True
                    elif np.double(self.TR) != np.double(config['DEFAULT']['TR']):
                        return True
                    elif np.double(self.FWHM) != np.double(config['DEFAULT']['FWHM']):
                        return True
                    elif np.double(self.DeleteVol) != np.double(config['DEFAULT']['deletevol']):
                        return True
                    elif np.double(self.TotalVol) != np.double(config['DEFAULT']['totalvol']):
                        return True
                    elif np.double(self.OnsetRID) != np.double(config['DEFAULT']['onsetrid']):
                        return True
                    elif np.double(self.ConditionRID) != np.double(config['DEFAULT']['conditionrid']):
                        return True
                    elif np.double(self.DurationRID) != np.double(np.int32(config['DEFAULT']['durationrid'])):
                        return True
                    elif self.Motion != Str2Bool(config['DEFAULT']['motion']):
                        return True
                    elif self.Anat != Str2Bool(config['DEFAULT']['anat']):
                        return True
                    elif self.RowStart != np.int32(config['DEFAULT']['rowstart']):
                        return True
                    elif self.HighPass != np.double(config['DEFAULT']['highpass']):
                        return True
                    elif self.TimeSlice != np.int32(config['DEFAULT']['timeslice']):
                        return True
                    return False
                except:
                    print("Error in loading!")
                    return None