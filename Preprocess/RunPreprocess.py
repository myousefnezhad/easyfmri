class RunPreprocess:

    def Check(self,SettingFileName,isOne=False,SubID=None,RunID=None,ConID=None):
        import numpy as np
        import os
        from Base.utility import fixstr,setParameters3
        from Base.Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                SubFrom = SubID
                SubTo   = SubID
                ConFrom = ConID
                ConTo   = ConID
                Run     = [RunID]
            else:
                SubFrom = setting.SubFrom
                SubTo   = setting.SubTo
                ConTo   = setting.ConTo
                ConFrom = setting.ConFrom
                Run     = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            for si, s in enumerate(range(SubFrom, SubTo + 1)):
              for cnt in range(ConFrom, ConTo + 1):
                print("Checking script for Subject %d ..." % (s))
                #SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    #ScriptFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                    #                 fixstr(r, RunLen, setting.RunPer) + "_script.fsf"
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
        import shutil
        import os,subprocess
        from Base.utility import fixstr,setParameters3
        from Base.Setting import Setting

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
                SubFrom = SubID
                SubTo = SubID
                ConFrom = ConID
                ConTo = ConID
                Run = [RunID]
            else:
                SubFrom = setting.SubFrom
                SubTo = setting.SubTo
                ConTo = setting.ConTo
                ConFrom = setting.ConFrom
                Run = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            #SubLen = np.int32(setting.SubLen)
            #RunLen = np.int32(setting.RunLen)

            for si, s in enumerate(range(SubFrom, SubTo + 1)):
              for cnt in range(ConFrom, ConTo + 1):
                print("Run script for Subject %d ..." % (s))
                #SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[si] + 1):
                    ScriptAddr = setParameters3(setting.Script,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                            fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                            fixstr(cnt, setting.ConLen, setting.ConPer))

                    if Remove:
                        ScriptOutputAddr = setParameters3(setting.Analysis,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                                       fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                            fixstr(cnt, setting.ConLen, setting.ConPer)) + ".feat"

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