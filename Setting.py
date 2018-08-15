

class Setting:
    def __init__(self):
        self.mainDIR        = None
        self.Task           = None
        self.SubFrom        = None
        self.SubTo          = None
        self.SubLen         = None
        self.SubPer         = None
        self.RunNum         = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.AnatDIR        = None
        self.EventFolder    = None
        self.CondPre        = None
        self.BET            = None
        self.BETPDF         = None
        self.Analysis       = None
        self.Script         = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.HighPass       = None
        self.DENL           = None
        self.DETS           = None
        self.DEZT           = None
        self.CTZT           = None
        self.CTPT           = None
        self.TimeSlice      = None
        self.EventCodes     = None

        self.empty          = True



    def checkValue(self, ui, checkFiles=True, checkGeneratedFiles=False):
        import numpy as np
        import scipy.io as io
        from PyQt5.QtWidgets import QMessageBox
        from utility import fixstr,getTimeSliceID,setParameters
        import os

        self.empty = True
        msgBox = QMessageBox()
        FSLDIR = ui.txtFSLDIR.text()

        #if (os.path.isdir(FSLDIR) == False):
        #    msgBox = QMessageBox()
        #    msgBox.setText("$FSLDIR does not exist!")
        #    msgBox.setIcon(QMessageBox.Critical)
        #    msgBox.setStandardButtons(QMessageBox.Ok)
        #    msgBox.exec_()
        #    return False

        if (os.path.isfile(ui.txtMNI.text()) == False):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find MNI file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if (os.path.isfile(FSLDIR + ui.txtFeat.text()) == False):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find feat cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if (os.path.isfile(FSLDIR + ui.txtFeat_gui.text()) == False):
            msgBox = QMessageBox()
            msgBox.setText("Cannot find Feat_gui cmd!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

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
            SubFrom = np.int32(ui.txtSubFrom.value())
            1 / SubFrom
        except:
            msgBox.setText("Subject From must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        try:
            SubTo = np.int32(ui.txtSubTo.value())
            1 / SubTo
        except:
            msgBox.setText("Subject To must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if SubTo < SubFrom:
            msgBox.setText("Subject To is smaller then Subject From!")
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
            RunLen = np.int32(ui.txtRunLen.value())
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
            for _ in range(int(ui.txtSubFrom.value()),int(ui.txtSubTo.value())+1):
                Run.append(runValue)
        else:
            if (len(Run) != (ui.txtSubTo.value() - ui.txtSubFrom.value() + 1)):
                msgBox.setText("Number of Runs must include a unique number for all subject or an array with size of number of subject, e.g. [1,2,2,1]")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        print("Number of Runs are okay.")
        # Check fMRI Images
        try:
            TR = np.double(ui.txtTR.value())
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
            FWHM = np.double(ui.txtFWHM.value())
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
            TotalVol = np.int32(ui.txtTotalVol.value())
        except:
            msgBox.setText("Total Volumn must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        if TotalVol <= 0:
            msgBox.setText("Total Volumn must be a positive number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Total Volumn is okay")
        try:
            DeleteVol = np.int32(ui.txtDeleteVol.value())
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

        ECodes = ui.txtEvents.toPlainText()

        if ECodes == "":
            msgBox.setText("Event code is empty")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Event codes are okay")

        try:
            HighPass = np.double(ui.txtHighPass.value())
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


        try:
            DENL = np.double(ui.txtDENL.text())
        except:
            msgBox.setText("Noise level must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Noise level is okay")

        try:
            DETS = np.double(ui.txtDETS.text())
        except:
            msgBox.setText("Temporal smoothness must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Temporal smoothness is okay")

        try:
            DEZT = np.double(ui.txtDEZT.text())
        except:
            msgBox.setText("Z threshold in the design efficiency must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Z threshold in the design efficiency is okay")

        try:
            CTZT = np.double(ui.txtCTZT.text())
        except:
            msgBox.setText("Z threshold in the clustering must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Z threshold in the clustering is okay")

        try:
            CTPT = np.double(ui.txtCTPT.text())
        except:
            msgBox.setText("Clustering P threshold must be a number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Clustering P threshold is okay")

        if ui.txtBOLD.text() == "":
            msgBox.setText("Structure of the BOLD files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtScript.text() == "":
            msgBox.setText("Structure of the script files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if ui.txtAnat.text() == "":
            msgBox.setText("Structure of the Anatomical files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtOnset.text() == "":
            msgBox.setText("Structure of the BOLD files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtBET.text() == "":
            msgBox.setText("Structure of the BET files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtBETPDF.text() == "":
            msgBox.setText("Structure of the BET report (PDF) is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False

        if ui.txtAnalysis.text() == "":
            msgBox.setText("Structure of the analysis folder is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if ui.txtEventDIR.text() == "":
            msgBox.setText("Structure of the event folders is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if ui.txtCondPre.text() == "":
            msgBox.setText("The prefix of condition files is empty!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        if checkFiles:
            print("Validating files ...")

            for si, s in enumerate(range(SubFrom, SubTo + 1)):
                print("Analyzing Subject %d ..." % (s))

                #SubDIR = mainDIR + "/" + "sub-" + fixstr(s, SubLen, ui.txtSubPer.text())

                # checking anat file
                filename =  setParameters(ui.txtAnat.text(),fixstr(s, SubLen, ui.txtSubPer.text()), "", ui.txtTask.text())
                addr = mainDIR + filename
                if os.path.isfile(addr):
                    print(addr, " - OKAY.")
                else:
                    print(addr, " - file not find!")
                    return False
                if checkGeneratedFiles and ui.cbRegAnat.isChecked():
                    # BET Files
                    filename = setParameters(ui.txtBET.text(), fixstr(s, SubLen, ui.txtSubPer.text()), "", ui.txtTask.text())
                    addr = mainDIR + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                for r in range(1,Run[si] + 1):

                    # BOLD File Check
                    filename = setParameters(ui.txtBOLD.text(), fixstr(s, SubLen, ui.txtSubPer.text()), \
                                             fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.text())
                    addr = mainDIR + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                    # Event File Check
                    filename = setParameters(ui.txtOnset.text(), fixstr(s, SubLen, ui.txtSubPer.text()), \
                                             fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.text())
                    addr = mainDIR + filename
                    if os.path.isfile(addr):
                        print(addr, " - OKAY.")
                    else:
                        print(addr, " - file not find!")
                        return False

                    if checkGeneratedFiles:
                        EventFolder = setParameters(ui.txtEventDIR.text(), fixstr(s, SubLen, ui.txtSubPer.text()), \
                                             fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.text())
                        addr = mainDIR + EventFolder
                        if os.path.isdir(addr):
                            print(addr, " - OKAY.")
                            try:
                                Cond = io.loadmat(addr + ui.txtCondPre.text() + ".mat")
                                for fileID in range(1,Cond["Cond"].shape[0]+1):
                                    if os.path.isfile(addr + ui.txtCondPre.text() + "_" + str(fileID) + ".tab"):
                                        print(addr + ui.txtCondPre.text() + "_" + str(fileID) + ".tab - OKAY.")
                                    else:
                                        print(addr + ui.txtCondPre.text() + "_" + str(fileID) + ".tab - file not find!")
                                        return False
                            except:
                                print(addr + ui.txtCondPre.text() + ".mat - loading error!")
                                return False
                        else:
                            print(addr + ui.txtCondPre.text() + ".mat - file not find!")
                            return False

        self.mainDIR = mainDIR

        self.SubFrom = SubFrom
        self.SubTo   = SubTo
        self.SubLen = SubLen
        self.SubPer = ui.txtSubPer.text()

        self.Task = str(Task)

        self.Run = str(Run)
        self.RunLen = str(RunLen)
        self.RunPer = ui.txtRunPer.text()

        self.BOLD           = ui.txtBOLD.text()
        self.Onset          = ui.txtOnset.text()
        self.AnatDIR        = ui.txtAnat.text()
        self.BET            = ui.txtBET.text()
        self.BETPDF         = ui.txtBETPDF.text()
        self.Analysis       = ui.txtAnalysis.text()
        self.Script         = ui.txtScript.text()
        self.EventFolder    = ui.txtEventDIR.text()
        self.EventCodes     = ui.txtEvents.toPlainText()
        self.CondPre        = ui.txtCondPre.text()

        self.TR = TR
        self.FWHM = FWHM

        self.DeleteVol = DeleteVol
        self.TotalVol = TotalVol


        self.HighPass = HighPass
        self.DENL     = DENL
        self.DETS     = DETS
        self.DEZT     = DEZT
        self.CTZT     = CTZT
        self.CTPT     = CTPT

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
        self.Task           = None
        self.SubFrom        = None
        self.SubTo          = None
        self.SubLen         = None
        self.SubPer         = None
        self.RunNum         = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.AnatDIR        = None
        self.EventFolder    = None
        self.CondPre        = None
        self.BET            = None
        self.BETPDF         = None
        self.Analysis       = None
        self.Script         = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.HighPass       = None
        self.DENL           = None
        self.DETS           = None
        self.DEZT           = None
        self.CTZT           = None
        self.CTPT           = None
        self.TimeSlice      = None
        self.EventCodes     = None

        self.empty          = True



        if len(filename):
            try:
                config = cp.ConfigParser()
                config.read(filename)
                self.mainDIR    = config['DEFAULT']['maindir']
                self.Task       = config['DEFAULT']['task']

                self.SubFrom    = np.int32(config['DEFAULT']['sub_from'])
                self.SubTo      = np.int32(config['DEFAULT']['sub_to'])
                self.SubLen     = np.int32(config['DEFAULT']['sub_len'])
                self.SubPer     = config['DEFAULT']['sub_perfix']

                self.Run        = config['DEFAULT']['run']
                self.RunLen     = np.int32(config['DEFAULT']['run_len'])
                self.RunPer     = config['DEFAULT']['run_perfix']

                self.BOLD       = config['DEFAULT']['bold']
                self.Onset      = config['DEFAULT']['onset']
                self.AnatDIR    = config['DEFAULT']['anat_dir']
                self.BET        = config['DEFAULT']['bet']
                self.BETPDF     = config['DEFAULT']['bet_pdf']
                self.EventFolder= config['DEFAULT']['event_dir']
                self.CondPre    = config['DEFAULT']['cond_per']
                self.Analysis   = config['DEFAULT']['analysis']
                self.Script     = config['DEFAULT']['script']

                #self.EventCodes = config['DEFAULT']['event_codes']
                self.EventCodes = open(filename+".code").read()

                self.TR         = np.double(config['DEFAULT']['TR'])
                self.FWHM       = np.double(config['DEFAULT']['FWHM'])

                self.DeleteVol  = np.int32(config['DEFAULT']['deletevol'])
                self.TotalVol   = np.int32(config['DEFAULT']['totalvol'])

                #self.OnsetRID   = np.int32(config['DEFAULT']['onsetrid'])
                #self.ConditionRID   = np.int32(config['DEFAULT']['conditionrid'])
                #self.DurationRID    = np.int32(np.int32(config['DEFAULT']['durationrid']))

                #self.DurationRID    = np.int32(np.int32(config['DEFAULT']['durationrid']))

                self.Motion     = Str2Bool(config['DEFAULT']['motion'])
                self.Anat       = Str2Bool(config['DEFAULT']['anat'])

                self.TimeSlice = np.int32(config['DEFAULT']['timeslice'])
                self.HighPass  = np.double(config['DEFAULT']['highpass'])
                self.DENL  = np.double(config['DEFAULT']['denl'])
                self.DETS  = np.double(config['DEFAULT']['dets'])
                self.DEZT  = np.double(config['DEFAULT']['dezt'])
                self.CTZT  = np.double(config['DEFAULT']['ctzt'])
                self.CTPT  = np.double(config['DEFAULT']['ctpt'])

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
        self.Task           = None
        self.SubFrom        = None
        self.SubTo          = None
        self.SubLen         = None
        self.SubPer         = None
        self.RunNum         = None
        self.RunLen         = None
        self.RunPer         = None
        self.Onset          = None
        self.BOLD           = None
        self.AnatDIR        = None
        self.EventFolder    = None
        self.CondPre        = None
        self.BET            = None
        self.BETPDF         = None
        self.Analysis       = None
        self.Script         = None
        self.TR             = None
        self.FWHM           = None
        self.TotalVol       = 0
        self.DeleteVol      = 0
        self.Motion         = True
        self.Anat           = True
        self.HighPass       = None
        self.DENL           = None
        self.DETS           = None
        self.DEZT           = None
        self.CTZT           = None
        self.CTPT           = None
        self.TimeSlice      = None
        self.EventCodes     = None

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
                    elif np.double(self.SubFrom) != np.double(config['DEFAULT']['sub_from']):
                        return True
                    elif np.double(self.SubTo) != np.double(config['DEFAULT']['sub_to']):
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
                    elif self.AnatDIR != config['DEFAULT']['anat_dir']:
                        return True
                    elif self.BET != config['DEFAULT']['bet']:
                        return True
                    elif self.BETPDF != config['DEFAULT']['bet_pdf']:
                        return True
                    elif self.Analysis != config['DEFAULT']['analysis']:
                        return True
                    elif self.Script   !=  config['DEFAULT']['script']:
                        return True
                    elif self.EventFolder != config['DEFAULT']['event_dir']:
                        return True
                    elif self.CondPre != config['DEFAULT']['cond_per']:
                        return True
                    elif self.EventCodes != open(SettingFileName+".code").read():
                        return True
                    elif np.double(self.TR) != np.double(config['DEFAULT']['TR']):
                        return True
                    elif np.double(self.FWHM) != np.double(config['DEFAULT']['FWHM']):
                        return True
                    elif np.double(self.DeleteVol) != np.double(config['DEFAULT']['deletevol']):
                        return True
                    elif np.double(self.TotalVol) != np.double(config['DEFAULT']['totalvol']):
                        return True
                    elif self.Motion != Str2Bool(config['DEFAULT']['motion']):
                        return True
                    elif self.Anat != Str2Bool(config['DEFAULT']['anat']):
                        return True
                    elif self.HighPass != np.double(config['DEFAULT']['highpass']):
                        return True
                    elif self.DENL != np.double(config['DEFAULT']['denl']):
                        return True
                    elif self.DETS != np.double(config['DEFAULT']['dets']):
                        return True
                    elif self.DEZT != np.double(config['DEFAULT']['dezt']):
                        return True
                    elif self.CTZT != np.double(config['DEFAULT']['ctzt']):
                        return True
                    elif self.CTPT != np.double(config['DEFAULT']['ctpt']):
                        return True
                    elif self.TimeSlice != np.int32(config['DEFAULT']['timeslice']):
                        return True
                    return False
                except:
                    print("Error in loading!")
                    return None