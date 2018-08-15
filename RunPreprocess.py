class RunPreprocess:

    def Check(self,SettingFileName,isOne=False):
        import numpy as np
        import os
        from utility import fixstr,setParameters
        from Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                SubTo = setting.SubFrom
                Run = [1]
            else:
                #SubNum = np.int32(setting.SubNum)
                SubTo = setting.SubTo
                Run = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            #SubLen = np.int32(setting.SubLen)
            #RunLen = np.int32(setting.RunLen)

            for si, s in enumerate(range(setting.SubFrom, SubTo + 1)):
                print("Checking script for Subject %d ..." % (s))
                #SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    #ScriptFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                    #                 fixstr(r, RunLen, setting.RunPer) + "_script.fsf"
                    ScriptFilename = setParameters(setting.Script, fixstr(s, setting.SubLen, setting.SubPer),\
                            fixstr(r, setting.RunLen, setting.RunPer), setting.Task)

                    ScriptAddr = setting.mainDIR + ScriptFilename
                    if os.path.isfile(ScriptAddr):
                       print("CHECK: " + ScriptAddr + " - checked!")
                    else:
                        print("CHECK: " + ScriptAddr + " - not found!")
                        return False
        return True

    def Run(self, SettingFileName, isOne=False, Remove=True, feat=None):
        import numpy as np
        import shutil
        import os,subprocess
        from utility import fixstr,setParameters
        from Setting import Setting

        if (feat == None) or (os.path.isfile(feat) == False):
            print("Cannot find feat cmd!")
            return False

        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            SubTo = setting.SubTo
            if isOne:
                SubTo = setting.SubFrom
                Run = [1]
            else:
                #SubNum = np.int32(setting.SubNum)
                Run = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            #SubLen = np.int32(setting.SubLen)
            #RunLen = np.int32(setting.RunLen)

            for si, s in enumerate(range(setting.SubFrom, SubTo + 1)):
                print("Run script for Subject %d ..." % (s))
                #SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    ScriptFilename = setParameters(setting.Script, fixstr(s, setting.SubLen, setting.SubPer),\
                            fixstr(r, setting.RunLen, setting.RunPer), setting.Task)

                    ScriptAddr = setting.mainDIR + ScriptFilename

                    if Remove:
                        ScriptOutputFolder = setParameters(setting.Analysis, fixstr(s, setting.SubLen, setting.SubPer),\
                                                       fixstr(r, setting.RunLen, setting.RunPer), setting.Task) + ".feat"

                        #ScriptOutputFolder = "sub-" + fixstr(s, SubLen,
                        #                                    setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                        #                     fixstr(r, RunLen, setting.RunPer) + "_analyze.feat"
                        ScriptOutputAddr = setting.mainDIR + ScriptOutputFolder

                        try:
                            shutil.rmtree(ScriptOutputAddr)
                            print("DELETE: " + ScriptOutputAddr + " - DONE")
                        except:
                            print("DELETE: " + ScriptOutputAddr + " - not found!")
                            pass

                    print("RUN: " + ScriptAddr + " - running ...")
                    #os.system(feat + " " + ScriptAddr)
                    cmd = subprocess.Popen([feat,ScriptAddr])
                    cmd.wait()
                    print("RUN: " + ScriptAddr + " - DONE!")