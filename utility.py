from PyQt5.QtWidgets import QMessageBox, QSizePolicy, QTextEdit

def fixstr(Value, Length, Perfix="0"):
    strVal = str(Value)
    while (len(strVal) < Length):
        strVal = Perfix + strVal
    return strVal


def Str2Bool(Value):
    valueS = str(Value).lower()
    if  valueS == "true":
        return True
    else:
        if valueS == "false":
            return False
    return None


def getTimeSliceID(str):
    if str == "None":
        return 0
    elif str == "Regular up (1, 2, ..., n)":
        return 1
    elif str == "Regular down (n, n-1, ..., 1)":
        return 2
    elif str == "Interleaved (2, 4, 6, ...), (1, 3, 5, ...)":
        return 5
    return None


def getTimeSliceText(ID):
    if ID == 0:
        return "None"
    elif ID == 1:
        return "Regular up (1, 2, ..., n)"
    elif ID == 2:
        return "Regular down (n, n-1, ..., 1)"
    elif ID == 5:
        return "Interleaved (2, 4, 6, ...), (1, 3, 5, ...)"
    return None


def setParameters(STR, Sub, Run, Task, Counter=None):
    outSTR = str(STR)
    outSTR = outSTR.replace("$SUB$",Sub)
    outSTR = outSTR.replace("$RUN$",Run)
    outSTR = outSTR.replace("$TASK$",Task)
    if Counter is not None:
        outSTR = outSTR.replace("$COUNT$", Counter)
    return outSTR


def setParameters2(STR, Dir, Sub, Run, Task, Counter=None):
    outSTR = str(STR)
    outSTR = outSTR.replace("$MAINDIR$",Dir)
    outSTR = outSTR.replace("$SUB$",Sub)
    outSTR = outSTR.replace("$RUN$",Run)
    outSTR = outSTR.replace("$TASK$",Task)
    if Counter is not None:
        outSTR = outSTR.replace("$COUNT$", Counter)
    return outSTR


def setParameters3(STR, Dir, Sub, Run, Task, Counter=None,Condition=None):
    outSTR = str(STR)
    outSTR = outSTR.replace("$MAINDIR$",Dir)
    outSTR = outSTR.replace("$SUB$",Sub)
    outSTR = outSTR.replace("$RUN$",Run)
    outSTR = outSTR.replace("$TASK$",Task)
    if Counter is not None:
        outSTR = outSTR.replace("$COUNT$", Counter)
    if Condition is not None:
        outSTR = outSTR.replace("$COND$", Condition)
    return outSTR


def getVersion():
    return "1.2"


def getBuild():
    return "1000"


def getDirSpaceINI():
    import os
    ProgramPath = os.path.dirname(os.path.abspath(__file__))
    return ProgramPath + "/data/space.ini"


def getDirSpace():
    import os
    ProgramPath = os.path.dirname(os.path.abspath(__file__))
    return ProgramPath + "/data/space/"


def getDirFSLAtlas():
    import os
    ProgramPath = os.path.dirname(os.path.abspath(__file__))
    return ProgramPath + "/data/atlas/FSL/"


def getFSLxml():
    import os
    ProgramPath = os.path.dirname(os.path.abspath(__file__))
    return ProgramPath + "/data/fslatlas.ini"


def convertDesignMatrix(filename,cond=None):
    import os
    if not len(filename):
        print("Please enter file address!")
        return None

    if not os.path.isfile(filename):
        print("File not found!")
        return None

    file = open(filename).readlines()
    isValue = False

    DM = list()
    for line in file:
        if isValue:
            values = str.rsplit(line)
            DMLine = list()
            for valindx, val in enumerate(values):
                if cond is not None:
                    if valindx >= cond:
                        break
                DMLine.append(float(val))
            DM.append(DMLine)

        if str.strip(line) == "/Matrix":
            isValue = True
    return DM


def fitLine(interval):
    import numpy as np
    coeffs   = np.unique(interval)
    intLen  = len(interval)
    errors = list()
    for coeff in coeffs:
        covec = coeff * np.ones([1, intLen])[0]
        err = np.linalg.norm(covec - interval)
        errors.append(err)
    return coeffs[np.argmin(errors)]







    pass



class MyMessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setSizeGripEnabled(True)

    def event(self, e):
        result = QMessageBox.event(self, e)
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(550)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        textEdit = self.findChild(QTextEdit)
        if textEdit != None :
            textEdit.setMinimumHeight(0)
            textEdit.setMaximumHeight(16777215)
            textEdit.setMinimumWidth(0)
            textEdit.setMaximumWidth(16777215)
            textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        return result



# Auto Run
if __name__ == "__main__":
    import scipy.io as io

    DLine = io.loadmat("/Users/tony/Workspace/ali.mat")["dm"][:,0]
    print(fitLine(DLine))





