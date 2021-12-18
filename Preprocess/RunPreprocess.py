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

class PreprocessThread(threading.Thread):
    def __init__(self, feat=None, cmd=None, report=None, files=list(), remove=False, removefile=None):
        super(PreprocessThread, self).__init__()
        self.feat   = feat
        self.cmd    = cmd
        self.report = report
        self.open   = False
        self.files  = files
        self.remove = remove
        self.rfile  = removefile
        self.status = "Ready"
        self.isKill   = False

    def kill(self):
        self.isKill = True

    def run(self):
        import subprocess, os, shutil
        from Base.utility import OpenReport
        self.status = "Running"
        if self.remove:
            try:
                shutil.rmtree(self.rfile)
                print("DELETE: " + self.rfile + " - DONE")
            except:
                print("DELETE: " + self.rfile + " - not found!")
                pass
        cmd = subprocess.Popen([self.feat, self.cmd])
        if self.open:
            print("Opening: " + self.report)
            OpenReport(self.report)

        while (not self.isKill) and (cmd.poll() is None):
            pass
        cmd.kill()

        if self.isKill:
            self.status = "Failed"
            return

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


class RunPreprocess:
    def Check(self,SettingFileName,isOne=False,SubID=None,RunID=None,ConID=None,TaskID=None):
        import numpy as np
        import os
        from Preprocess.BIDS import load_BIDS
        from Base.utility import setParameters3
        from Base.Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                bids = [[0, TaskID, 0, SubID, 0, ConID, [RunID]]]
            else:
                # Subjects = strRange(setting.SubRange, Unique=True)
                # if Subjects is None:
                #     print("Cannot load Subject Range!")
                #     return False
                # SubSize = len(Subjects)

                # Counters = strMultiRange(setting.ConRange, SubSize)
                # if Counters is None:
                #     print("Cannot load Counter Range!")
                #     return False

                # Runs = strMultiRange(setting.RunRange, SubSize)
                # if Runs is None:
                #     print("Cannot load Run Range!")
                #     return False
                bids = load_BIDS(setting)
            for (_, t, _, s, _, c, runs) in bids:
            # for si, s in enumerate(Subjects):
            #       for cnt in Counters[si]:
                print(f"Checking script for Subject {s} ...")
                for r in runs:
                    ScriptAddr = setParameters3(setting.Script, setting.mainDIR, s, r, t, c)

                    if os.path.isfile(ScriptAddr):
                        print("CHECK: " + ScriptAddr + " - checked!")
                    else:
                        print("CHECK: " + ScriptAddr + " - not found!")
                        return False
        return True


    def Run(self, SettingFileName, isOne=False, Remove=True, feat=None, SubID=None,RunID=None,ConID=None,TaskID=None):
        import numpy as np
        import os,subprocess
        from Preprocess.BIDS import load_BIDS
        from Base.utility import setParameters3
        from Base.Setting import Setting

        if (feat == None) or (os.path.isfile(feat) == False):
            print("Cannot find feat cmd!")
            return False, None

        Jobs = list()
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False, None
        else:
            if isOne:
                bids = [[0, TaskID, 0, SubID, 0, ConID, [RunID]]]
            else:
                bids = load_BIDS(setting)
            for (_, t, _, s, _, c, runs) in bids:
                print(f"Run script for Subject {s} ...")
                for r in runs:
                    ScriptAddr = setParameters3(setting.Script,setting.mainDIR, s, r, t, c)
                    ScriptTitle = setParameters3(setting.Script, "", s, r, t, c)
                    ScriptOutputAddr = setParameters3(setting.Analysis, setting.mainDIR, s, r, t, c) + ".feat"
                    files  = [ScriptOutputAddr + "/filtered_func_data.nii.gz", ScriptOutputAddr + \
                                "/mask.nii.gz", ScriptOutputAddr + "/cluster_mask_zstat1.nii.gz"]
                    cmd    = ScriptAddr
                    report = ScriptOutputAddr + "/report_log.html"
                    thread = PreprocessThread(feat=feat, cmd=cmd, report=report, files=files, \
                                                remove=Remove, removefile=ScriptOutputAddr)
                    Jobs.append(["Preprocess", ScriptTitle, thread])
                    print("Job for " + ScriptAddr + " - is created!")
            return True, Jobs