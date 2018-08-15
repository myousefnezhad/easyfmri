import os

from dir import getDIR

class History:
    def exist(self):
        ProgramPath = getDIR()
        if not os.path.isfile(ProgramPath + "/history"):
            HFile = open(ProgramPath + "/history", "w")
            HFile.close()

    def clear_history(self):
        ProgramPath = getDIR()
        try:
            os.remove(ProgramPath + "/history")
        except:
            return

    def check_history(self,filename):
        self.exist()
        ProgramPath = getDIR()
        HFile = open(ProgramPath + "/history","r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if line.replace("\n","") == filename:
                HFile.close()
                return True
        HFile.close()
        return False

    def del_history(self,filename):
        self.exist()
        ProgramPath = getDIR()
        HFile = open(ProgramPath + "/history","r")
        Lines = HFile.read().split("\n")
        HFile.close()
        self.clear_history()
        for line in Lines:
            if line != filename:
                self.add_history(line.replace("\n",""))

    def add_history(self,filename):
        self.exist()
        ProgramPath = getDIR()
        if not self.check_history(filename):
            HFile = open(ProgramPath + "/history", "a")
            HFile.write(filename+"\n")
            HFile.close()

    def load_history(self):
        self.exist()
        ProgramPath = getDIR()
        history = []
        HFile = open(ProgramPath + "/history", "r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if len(line):
                history.append(line)
        HFile.close()
        return history