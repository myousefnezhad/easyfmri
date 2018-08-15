import threading

class BrainExtractorThread(threading.Thread):
    def __init__(self, bet=None, InAddr=None, OutAddr=None, PDFAddr=None, InFile=None, files=list()):
        super(BrainExtractorThread, self).__init__()
        self.bet    = bet
        self.InAddr = InAddr
        self.OutAddr= OutAddr
        self.PDFAddr= PDFAddr
        self.InFile = InFile

        # Necessary
        self.files  = files
        self.open   = False
        self.status = "Ready"
        self.isKill   = False

    def kill(self):
        self.isKill = True

    def run(self):
        import numpy as np
        import nibabel as nb
        import subprocess
        import matplotlib
        import os
        matplotlib.rcParams['backend'] = "Qt5Agg"
        matplotlib.interactive(False)
        import matplotlib.pyplot as plt
        from Base.utility import OpenReport

        self.status = "Running"

        # Run Bet
        cmd = subprocess.Popen([self.bet, self.InAddr, self.OutAddr])
        while (not self.isKill) and (cmd.poll() is None):
            pass
        cmd.kill()
        if self.isKill:
            self.status = "Failed"
            return
        # Visualize In File
        nii = nb.load(self.InAddr)
        data = nii.get_data()
        dim = np.shape(data)
        if len(dim) > 3:
            data = data[:, :, :, 0]
        Ox = int(dim[0] / 2)
        imgIn = data[Ox, :, :]
        if self.isKill:
            self.status = "Failed"
            return
        # Visualize Out File
        nii = nb.load(self.OutAddr)
        data = nii.get_data()
        dim = np.shape(data)
        if len(dim) > 3:
            data = data[:, :, :, 0]
        Ox = int(dim[0] / 2)
        imgOut = data[Ox, :, :]
        # Plot In and Out Images in a PDF file
        fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col', sharey='row')
        ax1.set_title("Image: " + self.InFile)
        ax1.imshow(np.flipud(np.transpose(imgIn)), interpolation='nearest', aspect='auto', cmap=plt.cm.gray)
        ax2.imshow(np.flipud(np.transpose(imgOut)), interpolation='nearest', aspect='auto', cmap=plt.cm.gray)
        if self.isKill:
            self.status = "Failed"
            return
        plt.savefig(self.PDFAddr)
        if self.open:
            OpenReport(self.PDFAddr)
        # Check Outputs
        isFailed = False
        for fil in self.files:
            if not os.path.isfile(fil):
                print("Cannot find " + fil + "!")
                isFailed = True
                break
        if isFailed:
            self.status = "Failed"
        else:
            self.status = "Done"


class BrainExtractor():
    def run(self,SettingFileName, betcmd=None):
        import os

        from Base.utility import fixstr,setParameters3, strRange, strMultiRange
        from Base.Setting import Setting

        if betcmd is None:
            print("Cannot find bet cmd")
            return

        if not os.path.isfile(betcmd):
            print("Cannot find bet cmd")
            return

        setting = Setting()
        setting.Load(SettingFileName)
        if (setting.empty) or (setting.Anat == False) :
            if setting.empty:
                print("Error in loading the setting file!")
            if not setting.Anat:
                print("This feature is disable for in setting file. Please turn it on from Advance menu!")
            return False
        else:

            Subjects = strRange(setting.SubRange,Unique=True)
            if Subjects is None:
                print("Cannot load Subject Range!")
                return False
            SubSize = len(Subjects)

            Counters = strMultiRange(setting.ConRange,SubSize)
            if Counters is None:
                print("Cannot load Counter Range!")
                return False

            Runs = strMultiRange(setting.RunRange,SubSize)
            if Runs is None:
                print("Cannot load Run Range!")
                return False

            Jobs = list()
            for sindx, s in enumerate(Subjects):
                  for cnt in Counters[sindx]:
                        print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                        InAddr = setParameters3(setting.AnatDIR,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),"", setting.Task,
                                                   fixstr(cnt, setting.ConLen, setting.ConPer))
                        InFile = setParameters3(setting.AnatDIR,"", fixstr(s, setting.SubLen, setting.SubPer),"", setting.Task,
                                                   fixstr(cnt, setting.ConLen, setting.ConPer))
                        OutAddr = setParameters3(setting.BET,setting.mainDIR,fixstr(s, setting.SubLen, setting.SubPer),"", setting.Task,
                                                    fixstr(cnt, setting.ConLen, setting.ConPer))
                        PDFAddr = setParameters3(setting.BETPDF,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),"", setting.Task,
                                                    fixstr(cnt, setting.ConLen, setting.ConPer))
                        if not os.path.isfile(InAddr):
                            print(InAddr, " - file not find!")
                            return False
                        else:
                            files = [OutAddr, PDFAddr]
                            thread = BrainExtractorThread(bet=betcmd, InAddr=InAddr, OutAddr=OutAddr, PDFAddr=PDFAddr,\
                                                          InFile=InFile, files=files)
                            Jobs.append(["BrainExtractor", InFile, thread])
                            print("Job: Anatomical Brain Extractor for Subject %d, Counter %d is created." % (s, cnt))
            return True, Jobs