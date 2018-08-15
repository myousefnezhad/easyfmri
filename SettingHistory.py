import os

class History:
    def exist(self):
        if not os.path.isfile("/tmp/easyfMRI_history.txt"):
            HFile = open("/tmp/easyfMRI_history.txt", "w")
            HFile.close()

    def clear_history(self):
        try:
            os.remove("/tmp/easyfMRI_history.txt")
        except:
            return

    def check_history(self,filename):
        self.exist()
        HFile = open("/tmp/easyfMRI_history.txt","r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if line.replace("\n","") == filename:
                HFile.close()
                return True
        HFile.close()
        return False

    def del_history(self,filename):
        self.exist()
        HFile = open("/tmp/easyfMRI_history.txt","r")
        Lines = HFile.read().split("\n")
        HFile.close()
        self.clear_history()
        for line in Lines:
            if line != filename:
                self.add_history(line.replace("\n",""))

    def add_history(self,filename):
        self.exist()
        if not self.check_history(filename):
            HFile = open("/tmp/easyfMRI_history.txt", "a")
            HFile.write(filename+"\n")
            HFile.close()

    def load_history(self):
        self.exist()
        history = []
        HFile = open("/tmp/easyfMRI_history.txt", "r")
        Lines = HFile.read().split("\n")
        for line in Lines:
            if len(line):
                history.append(line)
        HFile.close()
        return history