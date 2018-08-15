from PyQt5.QtWidgets import QMessageBox, QSizePolicy, QTextEdit

import numpy as np
import os
from dir import getDIR

import threading

def About():
    return """<h1>easy fMRI project</h1>
<h3>A toolbox for Human Brain Mapping and Decoding</h3>
<h4>Website: <a href=\"https://easyfmri.sourceforge.io\">https://easyfmri.sourceforge.io</a></h4>
<h4>Data repository: <a href=\"https://easyfmridata.sourceforge.io\">https://easyfmridata.sourceforge.io</a></h4>

<p>Created by:</p>
<p><a href=\"https://myousefnezhad.sourceforge.io\">Muhammad Yousefnezhad</a>, <a href=\"http://ibrain.nuaa.edu.cn\">iBRAIN Group</a>,</p>
<p><a href=\"http://iao.nuaa.edu.cn\">Nanjing University of Aeronautics and Astronautics</a>, China.<p></h6>
"""


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


class RunThread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

class OpenThread(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.addr = addr

    def run(self):
        import webbrowser, time
        for _ in range(0,1000):
            time.sleep(3)
            if webbrowser.open_new("file://" + self.addr):
                break

def RunCMD(cmd):
    thread = RunThread(cmd)
    thread.daemon = True
    thread.start()


def OpenReport(addr):
    thread = OpenThread(addr)
    thread.daemon = True
    thread.start()


def getVersion():
    return "1.8"


def getBuild():
    return "4100"

def getSettingVersion():
    return "2.0"

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


def getDirSpaceINI():
    ProgramPath = getDIR()
    return ProgramPath + "/data/space.ini"

def getDirSpace():
    ProgramPath = getDIR()
    return ProgramPath + "/data/space/"

def getDirFSLAtlas():
    ProgramPath = getDIR()
    return ProgramPath + "/data/atlas/"

def getFSLxml():
    ProgramPath = getDIR()
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

def strRange(data,Unique=False):
    if not len(data):
        return None
    result = list()
    try:
        strData = data.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split()
        for D in strData:
            reformD = D.replace("-"," ").split()
            if len(reformD) == 1:
                result.append(np.int(reformD[0]))
            elif len(reformD) == 2:
                LoBand = np.int(reformD[0])
                HiBand = np.int(reformD[1])
                if LoBand == HiBand:
                    result.append(np.int(reformD[0]))
                elif LoBand < HiBand:
                    ren = np.arange(LoBand, HiBand + 1, 1)
                    for x in ren:
                        result.append(x)
                elif LoBand > HiBand:
                    ren = np.arange(LoBand, HiBand - 1, -1)
                    for x in ren:
                        result.append(x)
            else:
                print("Wrong Format!")
                return None
    except:
        print("Wrong Format!")
        return None

    if Unique:
        if not(len(result) == len(np.unique(result))):
            print("Subjects are not unique!")
            return None
    return result


def strMultiRange(data,Len=None):
    if not len(data):
        return None
    result = list()
    try:
        strData = data.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split()
        for D in strData:
            # Calculate Repate
            multiply = D.replace("*"," ").split()
            if len(multiply) == 1:
                Mul = 1
                Str = D
            elif len(multiply) == 2:
                Mul = np.int32(multiply[0])
                Str = multiply[1]
            else:
                print("Wrong Format, Symbol = *")
                return None
            # Calculate Range
            res = list()
            reformD = Str.replace("-"," ").split()
            if len(reformD) == 1:
                res.append(np.int(reformD[0]))
            elif len(reformD) == 2:
                LoBand = np.int(reformD[0])
                HiBand = np.int(reformD[1])
                if LoBand == HiBand:
                    res.append(np.int(reformD[0]))
                elif LoBand < HiBand:
                    ren = np.arange(LoBand, HiBand + 1, 1)
                    for x in ren:
                        res.append(x)
                elif LoBand > HiBand:
                    ren = np.arange(LoBand, HiBand - 1, -1)
                    for x in ren:
                        res.append(x)
            else:
                print("Wrong Format, Symbol: -")
                return None
            # Apply Repeat
            for _ in range(0, Mul):
                result.append(res)
    except:
        print("Wrong Format!")
        return None
    if Len is not None:
        if len(result) == 1:
            res = result[0]
            result = list()
            for _ in range(0,Len):
                result.append(res)
        elif not len(result) == Len:
            print("Size of Range is wrong!")
            return None
    return result

def encoding(Codes):
    Encode = None
    for code in Codes:
        Encode = str(ord(code)) if Encode is None else Encode + "," + str(ord(code))
    return Encode

def decoding(Codes):
    Encode = str(Codes).replace(",", " ").split()
    Decode = None
    for ecode in Encode:
        if len(ecode):
            Decode = chr(np.int32(ecode)) if Decode is None else Decode + chr(np.int32(ecode))
    return Decode


def LoadEzData(Header=None,data=None):
    import scipy.io as io
    if Header is None:
        print("Please enter header file!")
        return None

    if not os.path.isfile(Header):
        print("Header file is not found!")
        return None

    try:
        Out = io.loadmat(Header,appendmat=False)
        Int = Out["Integration"]
    except:
        print("Cannot load header file!")
        return None
    try:
        DataStruct = Int["DataStructure"][0]
        DataKey = list()
        for key in DataStruct:
            if data is None:
                DataKey.append(key)
            else:
                if key in data:
                    DataKey.append(key)

        if not len(DataKey):
            print("WARNING: No data key found!")
        else:
            for dkey in DataKey:
                X = None
                dfiles = np.array(Int[dkey[0] + "_files"])[0][0]
                for fdata in dfiles:
                    try:
                        del io
                        import scipy.io as io
                        dat = io.loadmat(os.path.dirname(Header) + "/" + fdata,appendmat=False)[dkey[0]]
                        X = dat if X is None else np.concatenate((X,dat))
                        del dat
                        print("Data %s is load!" % (fdata))
                    except Exception as e:
                        print(str(e))
                        return None
                Out[dkey[0]] = X
    except:
        print("DEBUG: Error in loading data files!")
        return None
    return Out


class SimilarityMatrixBetweenClass:
    def __init__(self, Matrix):
        Sx, Sy = np.shape(Matrix)
        if Sx != Sy:
            print("Matrix must have square size!")
            return None
        self.Matrix = list()
        for i in range(Sx):
            for j in range(i + 1, Sy):
                self.Matrix.append(Matrix[i,j])
        self.Matrix = np.array(self.Matrix)

    def mean(self):
        return  np.mean(self.Matrix)

    def max(self):
        return np.max(self.Matrix)

    def min(self):
        return np.min(self.Matrix)

    def std(self):
        return np.std(self.Matrix)

# Auto Run
if __name__ == "__main__":
    x = np.array([[1,2,3],\
                  [2,5,6],\
                  [3,6,8]])
    cov = SimilarityMatrixBetweenClass(x)
    print(cov.Matrix, cov.mean(), cov.max(), cov.min(), cov.std())
