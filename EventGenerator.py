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

        from utility import fixstr
        from Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:

            SubNum = np.int32(setting.SubNum)
            SubLen = np.int32(setting.SubLen)
            RunLen = np.int32(setting.RunLen)
            Run    = np.int32(str(setting.Run).replace("\'", " ").replace(",", " ").replace("[", "").replace("]", "").split())
            self.ConditionTitles = []
            Events = []
            # COLECT ALL EVENTS AND CALCULATE THE LIST OF CONDITION
            for s in range(1, SubNum + 1):
                print("Analyzing Subject %d ..." % (s))
                SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                for r in range(1,Run[s-1]+1):
                    # Event File Check
                    EventFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                               fixstr(r, RunLen, setting.RunPer) + "_events." + setting.Onset
                    EventFolder = SubDIR + "/func/" + "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + \
                               fixstr(r, RunLen, setting.RunPer) + "_events/"
                    EventAddr   = SubDIR + "/func/" + EventFilename
                    MatAddr     =  EventFolder + "Cond.mat"
                    if not os.path.isfile(EventAddr):
                        print(EventAddr, " - file not find!")
                        return False
                    else:
                        file = open(EventAddr, "r")
                        lines = file.readlines()
                        file.close()
                        dir = {}
                        dir.clear()
                        # Adapt by real index
                        OnRID = setting.OnsetRID     - 1
                        CoRID = setting.ConditionRID - 1
                        DuRID = setting.DurationRID  - 1
                        startRow = setting.RowStart  - 1

                        for k in range(startRow, len(lines)):
                            lines[k] = lines[k].rsplit()
                            try:
                                value = dir[lines[k][CoRID]]
                                value.append([float(lines[k][OnRID]), float(lines[k][DuRID])])
                                dir[lines[k][CoRID]] = value
                            except KeyError:
                                value = list()
                                value.append([float(lines[k][OnRID]), float(lines[k][DuRID])])
                                dir[lines[k][CoRID]] = value
                        for condinx, cond in enumerate(dir):
                            self.add_condTitle(title=cond,ConditionTitles=self.ConditionTitles)

                        Events.append([MatAddr, EventFolder, dir])
                        print("Subject %d, Run %d is verified." % (s,r))
            # Create Standard Condition Titles list
            conditions = []
            for cond in self.ConditionTitles:
                conditions.append(["Cond_"+str(self.get_condID(cond[0],self.ConditionTitles)), cond[0]])

            conditions = np.array(conditions,dtype=object)


            # Normalized the condition titile for all events
            StandardEvents = []
            for event in Events:
                StandardEvent = dict()
                StandardEvent["Cond"] = conditions
                for cond in event[2]:
                    StandardEvent["Cond_"+str(self.get_condID(cond,self.ConditionTitles))] = event[2][cond]
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