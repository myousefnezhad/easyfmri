import os
import numpy as np
import scipy.io as io
import configparser as cp
from PyQt5.QtWidgets import QMessageBox
from Base.utility import fixstr, getTimeSliceID, setParameters3, decoding
from Base.utility import getSettingVersion, strRange, strMultiRange, Str2Bool


class Setting:
    def __init__(self):
        self.Version        = None
        self.mainDIR        = None
        self.MNISpace       = None
        self.Task           = None
        self.SubRange       = None
        self.SubLen         = None
        self.SubPer         = None
        self.ConRange       = None
        self.ConLen         = None
        self.ConPer         = None
        self.RunRange       = None
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
        self.empty = True
        msgBox = QMessageBox()

        FSLDIR = ui.txtFSLDIR.text()
        if (os.path.isfile(ui.txtMNI.currentText()) == False):
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


        Task = ui.txtTask.currentText()
        if not len(Task):
            msgBox.setText("There is no task title")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False


        try:
            SubRange = strRange(ui.txtSubRange.text(),Unique=True)
            if SubRange is None:
                raise Exception
            SubSize = len(SubRange)
        except:
            msgBox.setText("Subject Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Range of subjects is okay!")
        try:
            SubLen = np.int32(ui.txtSubLen.text())
            1 / SubLen
        except:
            msgBox.setText("Length of subjects must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of subjects is okay!")


        try:
            ConRange = strMultiRange(ui.txtConRange.text(),SubSize)
            if ConRange is None:
                raise Exception
            if not (len(ConRange) == SubSize):
                msgBox.setText("Counter Size must be equal to Subject Size!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        except:
            msgBox.setText("Counter Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Counter Range is okay!")
        try:
            ConLen = np.int32(ui.txtConLen.text())
            1 / ConLen
        except:
            msgBox.setText("Length of counter must be an integer number")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Length of Counter is okay!")


        try:
            RunRange = strMultiRange(ui.txtRunRange.text(),SubSize)
            if RunRange is None:
                raise Exception
            if not (len(RunRange) == SubSize):
                msgBox.setText("Run Size must be equal to Subject Size!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
        except:
            msgBox.setText("Run Range is wrong!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Run Range is okay!")
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


        try:
            TotalVol = np.int32(ui.txtTotalVol.value())
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


        ECodes = ui.txtEvents.toPlainText()
        if ECodes == "":
            msgBox.setText("Event code is empty")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        print("Event codes are okay")

        if checkFiles:
            print("Validating files ...")
            for si, s in enumerate(SubRange):
                  for c in ConRange[si]:
                        print("Analyzing Subject %d, Counter %d ..." % (s, c))
                        # checking anat file
                        addr =  setParameters3(ui.txtAnat.text(),mainDIR, fixstr(s, SubLen, ui.txtSubPer.text()), "",\
                                               ui.txtTask.currentText(),fixstr(c, ConLen, ui.txtConPer.text()))
                        if os.path.isfile(addr):
                            print(addr, " - OKAY.")
                        else:
                            print(addr, " - file not find!")
                            return False
                        if checkGeneratedFiles and ui.cbRegAnat.isChecked():
                            # BET Files
                            addr = setParameters3(ui.txtBET.text(),mainDIR, fixstr(s, SubLen, ui.txtSubPer.text()), "", ui.txtTask.currentText(),fixstr(c, ConLen, ui.txtConPer.text()))
                            if os.path.isfile(addr):
                                print(addr, " - OKAY.")
                            else:
                                print(addr, " - file not find!")
                                return False

                        for r in RunRange[si]:

                            # BOLD File Check
                            addr = setParameters3(ui.txtBOLD.text(),mainDIR, fixstr(s, SubLen, ui.txtSubPer.text()), \
                                                     fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.currentText(),fixstr(c, ConLen, ui.txtConPer.text()))
                            if os.path.isfile(addr):
                                print(addr, " - OKAY.")
                            else:
                                print(addr, " - file not find!")
                                return False

                            # Event File Check
                            addr = setParameters3(ui.txtOnset.text(), mainDIR, fixstr(s, SubLen, ui.txtSubPer.text()), \
                                                     fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.currentText(),fixstr(c, ConLen, ui.txtConPer.text()))
                            if os.path.isfile(addr):
                                print(addr, " - OKAY.")
                            else:
                                print(addr, " - file not find!")
                                return False

                            if checkGeneratedFiles:
                                addr = setParameters3(ui.txtEventDIR.text(),mainDIR, fixstr(s, SubLen, ui.txtSubPer.text()), \
                                                     fixstr(r,RunLen,ui.txtRunPer.text()), ui.txtTask.currentText(),fixstr(c, ConLen, ui.txtConPer.text()))
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

        self.Version        = getSettingVersion()
        self.mainDIR        = mainDIR
        self.MNISpace       = ui.txtMNI.currentText()
        self.SubRange       = ui.txtSubRange.text()
        self.SubLen         = SubLen
        self.SubPer         = ui.txtSubPer.text()
        self.ConRange       = ui.txtConRange.text()
        self.ConLen         = ConLen
        self.ConPer         = ui.txtConPer.text()
        self.Task           = str(Task)
        self.RunRange       = ui.txtRunRange.text()
        self.RunLen         = str(RunLen)
        self.RunPer         = ui.txtRunPer.text()
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
        self.TR             = TR
        self.FWHM           = FWHM
        self.DeleteVol      = DeleteVol
        self.TotalVol       = TotalVol
        self.HighPass       = HighPass
        self.DENL           = DENL
        self.DETS           = DETS
        self.DEZT           = DEZT
        self.CTZT           = CTZT
        self.CTPT           = CTPT

        TimeSlice = getTimeSliceID(ui.cbSliceTime.currentText())
        if TimeSlice is None:
            print("Error in Slice Time!")
            return False
        self.TimeSlice      = np.int32(TimeSlice)
        self.Motion         = ui.cbMotionCorrection.isChecked()
        self.Anat           = ui.cbRegAnat.isChecked()
        self.empty          = False
        return True

    def Load(self,filename):
        self.Version        = None
        self.mainDIR        = None
        self.MNISpace       = None
        self.Task           = None
        self.SubRange       = None
        self.SubLen         = None
        self.SubPer         = None

        self.ConRange       = None
        self.ConLen         = None
        self.ConPer         = None

        self.RunRange       = None
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
                self.Version    = config['DEFAULT']['ver']
                self.mainDIR    = config['DEFAULT']['maindir']
                self.MNISpace   = config['DEFAULT']['mni_space']
                self.Task       = config['DEFAULT']['task']
                self.SubRange   = config['DEFAULT']['sub_range']
                self.SubLen     = np.int32(config['DEFAULT']['sub_len'])
                self.SubPer     = config['DEFAULT']['sub_perfix']
                self.ConRange   = config['DEFAULT']['con_range']
                self.ConLen     = np.int32(config['DEFAULT']['con_len'])
                self.ConPer     = config['DEFAULT']['con_perfix']
                self.RunRange   = config['DEFAULT']['run_range']
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
                self.TR         = np.double(config['DEFAULT']['TR'])
                self.FWHM       = np.double(config['DEFAULT']['FWHM'])
                self.DeleteVol  = np.int32(config['DEFAULT']['deletevol'])
                self.TotalVol   = np.int32(config['DEFAULT']['totalvol'])
                self.Motion     = Str2Bool(config['DEFAULT']['motion'])
                self.Anat       = Str2Bool(config['DEFAULT']['anat'])
                self.TimeSlice  = np.int32(config['DEFAULT']['timeslice'])
                self.HighPass   = np.double(config['DEFAULT']['highpass'])
                self.DENL       = np.double(config['DEFAULT']['denl'])
                self.DETS       = np.double(config['DEFAULT']['dets'])
                self.DEZT       = np.double(config['DEFAULT']['dezt'])
                self.CTZT       = np.double(config['DEFAULT']['ctzt'])
                self.CTPT       = np.double(config['DEFAULT']['ctpt'])
                self.EventCodes = decoding(config['CODE']['event_code'])

                #self.EventCodes = open(filename+".code").read()

                self.empty      = False
                return True
            except:
                print("Error in loading!")
                return False

        return False

    def checkGUI(self,ui, SettingFileName,checkGeneratedFiles=False):
        # init Empty
        self.Version        = getSettingVersion()
        self.mainDIR        = None
        self.MNISpace       = None
        self.Task           = None
        self.SubRange       = None
        self.SubLen         = None
        self.SubPer         = None
        self.ConRange       = None
        self.ConLen         = None
        self.ConPer         = None
        self.RunRange       = None
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
                    if self.MNISpace != config['DEFAULT']['mni_space']:
                        return True
                    elif self.Task != config['DEFAULT']['task']:
                        return True
                    elif self.SubRange != config['DEFAULT']['sub_range']:
                        return True
                    elif np.double(self.SubLen) != np.double(config['DEFAULT']['sub_len']):
                        return True
                    elif self.SubPer != config['DEFAULT']['sub_perfix']:
                        return True
                    elif self.ConRange != config['DEFAULT']['con_range']:
                        return True
                    elif np.double(self.ConLen) != np.double(config['DEFAULT']['con_len']):
                        return True
                    elif self.ConPer != config['DEFAULT']['con_perfix']:
                        return True
                    elif self.RunRange != config['DEFAULT']['run_range']:
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
                    elif self.EventCodes != decoding(config['CODE']['event_code']):
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