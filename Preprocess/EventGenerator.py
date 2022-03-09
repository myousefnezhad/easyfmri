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
        from Base.Setting import Setting
        from Preprocess.BIDS import load_BIDS
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            self.ConditionTitles = []
            Events = []

            # Tasks = strTaskList(setting.Task)

            # Subjects = strRange(setting.SubRange, Unique=True)
            # if Subjects is None:
            #     print("Cannot load Subject Range!")
            #     return False
            # SubSize = len(Subjects)

            # Counters = strMultiRange(setting.ConRange, SubSize)
            # if Counters is None:
            #     print("Cannot load Counter Range!")
            #     return False
            # #strMultiRange(setting.RunRange, SubSize)
            # Runs = strMultiLineRuns(setting.RunRange, Subjects, Counters, setting.RunLen, setting.RunPer)
            # if Runs is None:
            #     print("Cannot load Run Range!")
            #     return False

            bids = load_BIDS(setting)

            # COLECT ALL EVENTS AND CALCULATE THE LIST OF CONDITION
            for (_, t, _, s, _, c, runs) in bids:
            # for si, s in enumerate(Subjects):
                #   for cnt in Counters[si]:
                print(f"Analyzing Subject {s}, Counter {c} ...")
                for r in runs:
                    # Event File Check
                    EventAddr   = setParameters3(setting.Onset, setting.mainDIR, s, r, t, c)
                    EventFolder = setParameters3(setting.EventFolder, setting.mainDIR, s, r, t, c)
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
                        print(f"Subject {s}, Counter {c}, Run {r} is verified.")
            # Create Standard Condition Titles list
            conditions = []
            for cond in self.ConditionTitles:
                conditions.append([setting.CondPre + "_" + str(self.get_condID(cond[0],self.ConditionTitles)), cond[0]])

            conditions = np.array(conditions, dtype=object)


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

            # Check Tab File
            for cond in conditions:
                for (_, t, _, s, _, c, runs) in bids:
                    print(f"Checking Tab Files: Subject {s}, Counter {c} ...")
                    for r in runs:
                        EventFolder = setParameters3(setting.EventFolder, setting.mainDIR, s, r, t, c)
                        fname = EventFolder + cond[0] + '.tab'
                        if os.path.isfile(fname):
                            print(fname + " - is okay.")
                        else:
                            tabfile = open(fname, "w")
                            tabfile.write("0\t0\t0\n")
                            tabfile.close()
                            print(fname + " - is EMPTY!")

            # Report
            print("List of generated conditions:")
            print("Condition ID\tCondition Title")
            for cond in conditions:
                print("\t"+cond[0]+"\t\t\t"+cond[1])