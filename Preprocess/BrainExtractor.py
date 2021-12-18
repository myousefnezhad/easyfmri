# This file is part of the easy fMRI distribution 
#
# Copyright (c) 2014—2021 Tony Muhammad Yousefnezhad.
#
# Website: https://easyfmri.learningbymachine.com
# GitLab:  https://gitlab.com/easyfmri/easyfmri
# GitHub:  https://github.com/easyfmri/easyfmri
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#

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
        from Preprocess.BIDS import load_BIDS
        from Base.utility import fixstr,setParameters3 #, strRange, strMultiRange
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

            # Subjects = strRange(setting.SubRange,Unique=True)
            # if Subjects is None:
            #     print("Cannot load Subject Range!")
            #     return False
            # SubSize = len(Subjects)

            # Counters = strMultiRange(setting.ConRange,SubSize)
            # if Counters is None:
            #     print("Cannot load Counter Range!")
            #     return False

            # Runs = strMultiRange(setting.RunRange,SubSize)
            # if Runs is None:
            #     print("Cannot load Run Range!")
            #     return False
            bids = load_BIDS(setting)

            Jobs = list()
            for (_, t, _, s, _, c, _) in bids:
                print(f"Analyzing Subject {s}, Counter {c} ...")
                InAddr = setParameters3(setting.AnatDIR, setting.mainDIR, s, "", t, c)
                InFile = setParameters3(setting.AnatDIR, "", s, "", t, c)
                OutAddr = setParameters3(setting.BET, setting.mainDIR, s, "", t, c)
                PDFAddr = setParameters3(setting.BETPDF, setting.mainDIR, s,"", t, c)
                if not os.path.isfile(InAddr):
                    print(InAddr, " - file not find!")
                    return False
                else:
                    files = [OutAddr, PDFAddr]
                    thread = BrainExtractorThread(bet=betcmd, InAddr=InAddr, OutAddr=OutAddr, PDFAddr=PDFAddr, InFile=InFile, files=files)
                    Jobs.append(["BrainExtractor", InFile, thread])
                    print(f"Job: Anatomical Brain Extractor for Subject {s}, Counter {c} is created.")
            return True, Jobs