# Copyright (c) 2014--2018 Muhammad Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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