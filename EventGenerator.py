class EventGenerator:

    def __init__(self):
        self.ConditionTitles = []

    def check_condTitle(self,title,ConditionTitles):
        if len(ConditionTitles):
            for titl in ConditionTitles:
                if titl[0] == title:
                    return True
        return False

    def get_condID(self,title,ConditionTitles):
        if len(ConditionTitles):
            for titl in ConditionTitles:
                if titl[0] == title:
                    return titl[1]
        return None

    def add_condTitle(self,title,ConditionTitles):
        if not self.check_condTitle(title,ConditionTitles):
            ConditionTitles.append([title,len(ConditionTitles)+1])

    def run(self,SettingFileName):
        import numpy as np
        import scipy.io as io
        import os

        from utility import fixstr,setParameters
        from Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:

            Run     = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())
            self.ConditionTitles = []
            Events = []
            # COLECT ALL EVENTS AND CALCULATE THE LIST OF CONDITION
            for si, s in enumerate(range(setting.SubFrom, setting.SubTo + 1)):
              for cnt in range(setting.ConFrom, setting.ConTo + 1):
                print("Analyzing Subject %d ..." % (s))
                #SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1,Run[si] + 1):
                    # Event File Check
                    EventFilename = setParameters(setting.Onset,fixstr(s, setting.SubLen, setting.SubPer)\
                                                  ,fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                                  fixstr(cnt, setting.ConLen, setting.ConPer))
                    #EventFilename = "sub-" +  + "_task-" + setting.Task + "_run-" + \
                                #+ "_events." + setting.Onset
                    EventFolder = setting.mainDIR + setParameters(setting.EventFolder,fixstr(s, setting.SubLen, setting.SubPer)\
                                                  ,fixstr(r, setting.RunLen, setting.RunPer), setting.Task,
                                                                  fixstr(cnt, setting.ConLen, setting.ConPer))
                    #EventFolder = SubDIR + "/func/" + "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                               #fixstr(r, RunLen, setting.RunPer) + "_events/"
                    EventAddr   = setting.mainDIR + EventFilename
                    MatAddr     =  EventFolder + setting.CondPre + ".mat"
                    if not os.path.isfile(EventAddr):
                        print(EventAddr, " - file not find!")
                        return False
                    else:
                        file = open(EventAddr, "r")
                        lines = file.readlines()
                        file.close()
                        dir = {}
                        dir.clear()

                        for k in range(0, len(lines)):
                            Event = lines[k].rsplit()
                            try:
                                allvars = dict(locals(), **globals())
                                exec(setting.EventCodes,allvars,allvars)
                            
                            except Exception as e:
                                print("Event codes generated following error:\n")
                                print(e)
                                return False

                            try:
                                RowStartID = allvars['RowStartID']
                            except:
                                print("Cannot find RowStartID variable in event code")
                                return False
                            try:
                                Condition = allvars['Condition']
                            except:
                                print("Cannot find Condition variable in event code")
                                return False
                            try:
                                Onset = allvars['Onset']
                            except:
                                print("Cannot find Onset variable in event code")
                                return False
                            try:
                                Duration = allvars['Duration']
                            except:
                                print("Cannot find Duration variable in event code")
                                return False
                            if RowStartID <= k:
                                # Create Condition Directory
                                try:
                                    value = dir[Condition]
                                    value.append([float(Onset), float(Duration)])
                                    dir[Condition] = value
                                except KeyError:
                                    value = list()
                                    value.append([float(Onset), float(Duration)])
                                    dir[Condition] = value

                        for condinx, cond in enumerate(dir):
                            self.add_condTitle(title=cond,ConditionTitles=self.ConditionTitles)

                        Events.append([MatAddr, EventFolder, dir])
                        print("Subject %d, Run %d is verified." % (s,r))
            # Create Standard Condition Titles list
            conditions = []
            for cond in self.ConditionTitles:
                conditions.append([setting.CondPre + "_" + str(self.get_condID(cond[0],self.ConditionTitles)), cond[0]])

            conditions = np.array(conditions,dtype=object)


            # Normalized the condition titile for all events
            StandardEvents = []
            for event in Events:
                StandardEvent = dict()
                StandardEvent["Cond"] = conditions
                for cond in event[2]:
                    StandardEvent[setting.CondPre + "_" + str(self.get_condID(cond,self.ConditionTitles))] = event[2][cond]
                # Add list of titles
                StandardEvents.append([event[0], event[1], StandardEvent])
            print("Events were normalized! Generating event files ...")
            # Save Files
            for event in StandardEvents:
                try:
                    os.mkdir(event[1])
                except:
                    pass
                io.savemat(event[0], event[2])
                for tabs in event[2]:
                    if  tabs == "Cond":
                        conFile = open(event[1] + tabs + ".txt","w")
                        for con in event[2][tabs]:
                            conFile.write(str(con[0]) + "\t" + str(con[1]) + "\n")
                        conFile.close()
                    else:
                        tabFile = open(event[1] + tabs + ".tab","w")
                        for onset in event[2][tabs]:
                            tabFile.write(str(onset[0]) + "\t" + str(onset[1]) + "\t1\n")
                        tabFile.close()
                print("EVENT: "+ event[1] + " is generated!")
            # # Report
            print("List of generated conditions:")
            print("Condition ID\tCondition Title")
            for cond in conditions:
                print("\t"+cond[0]+"\t\t\t"+cond[1])