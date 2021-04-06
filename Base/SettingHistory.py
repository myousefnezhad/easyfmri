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


import os

from dir import getDIR, getHome

class History:
    def HistoryPath(self):
        if getHome() is None:
            return getDIR()
        elif not os.path.isdir(getHome() + "/.config"):
            return getDIR()
        else:
            return getHome() + "/.config"

    def exist(self):
        if not os.path.isfile(self.HistoryPath() + "/easyfmri_history"):
            HFile = open(self.HistoryPath() + "/easyfmri_history", "w")
            HFile.close()

    def clear_history(self):
        try:
            os.remove(self.HistoryPath() + "/easyfmri_history")
        except:
            return

    def check_history(self,filename):
        self.exist()
        HFile = open(self.HistoryPath() + "/easyfmri_history","r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if line.replace("\n","") == filename:
                HFile.close()
                return True
        HFile.close()
        return False

    def del_history(self,filename):
        self.exist()
        HFile = open(self.HistoryPath() + "/easyfmri_history","r")
        Lines = HFile.read().split("\n")
        HFile.close()
        self.clear_history()
        for line in Lines:
            if line != filename:
                self.add_history(line.replace("\n",""))

    def add_history(self,filename):
        self.exist()
        if not self.check_history(filename):
            HFile = open(self.HistoryPath() + "/easyfmri_history", "a")
            HFile.write(filename+"\n")
            HFile.close()

    def load_history(self):
        self.exist()
        history = []
        HFile = open(self.HistoryPath() + "/easyfmri_history", "r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if len(line):
                history.append(line)
        HFile.close()
        return history