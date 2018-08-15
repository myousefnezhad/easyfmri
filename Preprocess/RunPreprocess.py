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
    def Check(self,SettingFileName,isOne=False,SubID=None,RunID=None,ConID=None):
        import numpy as np
        import os
        from Base.utility import fixstr,setParameters3, strRange, strMultiRange
        from Base.Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                Subjects   = [SubID]
                Counters   = [[ConID]]
                Runs       = [[RunID]]
            else:
                Subjects = strRange(setting.SubRange, Unique=True)
                if Subjects is None:
                    print("Cannot load Subject Range!")
                    return False
                SubSize = len(Subjects)

                Counters = strMultiRange(setting.ConRange, SubSize)
                if Counters is None:
                    print("Cannot load Counter Range!")
                    return False

                Runs = strMultiRange(setting.RunRange, SubSize)
                if Runs is None:
                    print("Cannot load Run Range!")
                    return False

            for si, s in enumerate(Subjects):
                  for cnt in Counters[si]:
                        print("Checking script for Subject %d ..." % (s))
                        for r in Runs[si]:
                            ScriptAddr = setParameters3(setting.Script, setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                    fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                    fixstr(cnt, setting.ConLen, setting.ConPer))

                            if os.path.isfile(ScriptAddr):
                               print("CHECK: " + ScriptAddr + " - checked!")
                            else:
                                print("CHECK: " + ScriptAddr + " - not found!")
                                return False
        return True


    def Run(self, SettingFileName, isOne=False, Remove=True, feat=None, SubID=None,RunID=None,ConID=None):
        import numpy as np
        import os,subprocess
        from Base.utility import fixstr,setParameters3, strRange, strMultiRange
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
                Subjects   = [SubID]
                Counters   = [[ConID]]
                Runs       = [[RunID]]
            else:
                Subjects = strRange(setting.SubRange, Unique=True)
                if Subjects is None:
                    print("Cannot load Subject Range!")
                    return False, None
                SubSize = len(Subjects)

                Counters = strMultiRange(setting.ConRange, SubSize)
                if Counters is None:
                    print("Cannot load Counter Range!")
                    return False, None

                Runs = strMultiRange(setting.RunRange, SubSize)
                if Runs is None:
                    print("Cannot load Run Range!")
                    return False, None

            for si, s in enumerate(Subjects):
                  for cnt in Counters[si]:
                        print("Run script for Subject %d ..." % (s))
                        for r in Runs[si]:
                            ScriptAddr = setParameters3(setting.Script,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer), \
                                                        fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                                        fixstr(cnt, setting.ConLen, setting.ConPer))
                            ScriptTitle = setParameters3(setting.Script, "", fixstr(s, setting.SubLen, setting.SubPer), \
                                                        fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                                        fixstr(cnt, setting.ConLen, setting.ConPer))
                            ScriptOutputAddr = setParameters3(setting.Analysis, setting.mainDIR,
                                                              fixstr(s, setting.SubLen, setting.SubPer), \
                                                              fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                                              fixstr(cnt, setting.ConLen, setting.ConPer)) + ".feat"
                            files  = [ScriptOutputAddr + "/filtered_func_data.nii.gz", ScriptOutputAddr + \
                                      "/mask.nii.gz", ScriptOutputAddr + "/cluster_mask_zstat1.nii.gz"]
                            cmd    = ScriptAddr
                            report = ScriptOutputAddr + "/report_log.html"
                            thread = PreprocessThread(feat=feat, cmd=cmd, report=report, files=files, \
                                                      remove=Remove, removefile=ScriptOutputAddr)
                            Jobs.append(["Preprocess", ScriptTitle, thread])
                            print("Job for " + ScriptAddr + " - is created!")
            return True, Jobs