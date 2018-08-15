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

        from Base.utility import fixstr,setParameters3
        from Base.Setting import Setting, strRange, strMultiRange
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            self.ConditionTitles = []
            Events = []

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

            # COLECT ALL EVENTS AND CALCULATE THE LIST OF CONDITION
            for si, s in enumerate(Subjects):
                  for cnt in Counters[si]:
                        print("Analyzing Subject %d, Counter %d ..." % (s,cnt))
                        for r in Runs[si]:
                            # Event File Check
                            EventAddr = setParameters3(setting.Onset,setting.mainDIR,fixstr(s, setting.SubLen, setting.SubPer)\
                                                          ,fixstr(r, setting.RunLen, setting.RunPer), setting.Task, \
                                                          fixstr(cnt, setting.ConLen, setting.ConPer))
                            #EventFilename = "sub-" +  + "_task-" + setting.Task + "_run-" + \
                                        #+ "_events." + setting.Onset
                            EventFolder = setParameters3(setting.EventFolder,setting.mainDIR,fixstr(s, setting.SubLen, setting.SubPer)\
                                                          ,fixstr(r, setting.RunLen, setting.RunPer), setting.Task,
                                                                          fixstr(cnt, setting.ConLen, setting.ConPer))
                            #EventFolder = SubDIR + "/func/" + "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                                       #fixstr(r, RunLen, setting.RunPer) + "_events/"
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

                                    try:
                                        Skip = int(allvars["Skip"])
                                    except:
                                        print("Cannot find Skip variable in event code")
                                        return False
                                    if RowStartID <= k and Skip == 0:
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
                                print("Subject %d, Counter %d, Run %d is verified." % (s,cnt, r))
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