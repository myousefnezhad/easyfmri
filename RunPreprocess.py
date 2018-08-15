class RunPreprocess:

    def Check(self,SettingFileName,isOne=False):
        import numpy as np
        import os
        from utility import fixstr
        from Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                SubNum = 1
                Run = [1]
            else:
                SubNum = np.int32(setting.SubNum)
                Run = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            SubLen = np.int32(setting.SubLen)
            RunLen = np.int32(setting.RunLen)

            for s in range(1, SubNum + 1):
                print("Checking script for Subject %d ..." % (s))
                SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[s - 1] + 1):
                    ScriptFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                                     fixstr(r, RunLen, setting.RunPer) + "_script.fsf"

                    ScriptAddr = SubDIR + "/func/" + ScriptFilename
                    if os.path.isfile(ScriptAddr):
                       print("CHECK: " + ScriptAddr + " - checked!")
                    else:
                        print("CHECK: " + ScriptAddr + " - not found!")
                        return False
        return True

    def Run(self, SettingFileName, isOne=False, Remove=True):
        import numpy as np
        import shutil
        import os
        from utility import fixstr
        from Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            if isOne:
                SubNum = 1
                Run = [1]
            else:
                SubNum = np.int32(setting.SubNum)
                Run = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())

            SubLen = np.int32(setting.SubLen)
            RunLen = np.int32(setting.RunLen)

            for s in range(1, SubNum + 1):
                print("Run script for Subject %d ..." % (s))
                SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1, Run[s - 1] + 1):
                    ScriptFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                                     fixstr(r, RunLen, setting.RunPer) + "_script.fsf"

                    ScriptAddr = SubDIR + "/func/" + ScriptFilename

                    if Remove:
                        ScriptOutputFolder = "sub-" + fixstr(s, SubLen,
                                                             setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                                             fixstr(r, RunLen, setting.RunPer) + "_analyze.feat"
                        ScriptOutputAddr = SubDIR + "/func/" + ScriptOutputFolder

                        try:
                            shutil.rmtree(ScriptOutputAddr)
                            print("DELETE: " + ScriptOutputAddr + " - DONE")
                        except:
                            print("DELETE: " + ScriptOutputAddr + " - not found!")
                            pass

                    print("RUN: " + ScriptAddr + " - running ...")
                    os.system("feat " + ScriptAddr)
                    print("RUN: " + ScriptAddr + " - DONE!")