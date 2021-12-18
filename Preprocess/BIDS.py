import numpy as np
from Base.utility import fixstr

# This Function convert a string including list of tasks to an array based on , separators
def strTaskList(data):
    if not len(data):
        return None
    result = list()
    try:
        return np.unique(data.replace("\'", " ").replace(",", " ").replace("[", "").replace("]","").split())
    except:
        return None

# This function convert a string including ranges of subject to a list of numerical ranges
def strRange(data, Unique=False):
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

# This function convert a string including ranges of sessions,counter,runs to a list of numerical ranges
def strMultiRange(data, Len=None):
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


def strSplitX(strVal):
    try:
        strData = str(strVal).lower().split("x")
        if len(strData) == 1:
            return [1, strData[0]]
        elif len(strData) == 2:
            return [np.int32(strData[0]), strData[1]]
        raise Exception
    except:
        return [None, None]


# This function convert a string including ranges of runs to a 3D tensor of string runs
def strMultiLineRuns(data, SubArr, SesMat, RunLen, RunPerfix, AddPrefix=True):
    SubLen = len(SubArr)
    if SubLen < 1:
        print("Size of Subjects is less than 1")        
        return None

    if not len(data):
        return None
    if not len(SesMat) == SubLen:
        print("Counter Size is not matched to Subject Size")
        return None

    try:
        strData = data.lower().replace("\'", " ").replace("{", "").replace("}","").split(";")
        if not len(strData):
            return None                    
        subRangeList = list()
        if len(strData) == 1:
            Mul, Range = strSplitX(strData[0])
            if Mul is None:
                print("Incorrect format!")
                return None
            if Mul == 1:
                Mul = SubLen
            elif not Mul == SubLen:
                print("The outer multiplex 'x' is not matched")
                return None
            for _ in range(Mul):
                subRangeList.append(Range)
        else:
            for element in strData:
                Mul, Range = strSplitX(element)
                if Mul is None:
                    print("Incorrect format!")
                    return None
                for _ in range(Mul):
                    subRangeList.append(Range)            
            if not len(subRangeList) == SubLen:
                print("The outer multiplex 'x' is not matched")
                return None
        if not len(subRangeList):
            return None
        
        result = list()
        for subRange, subID, sesElement in zip(subRangeList, SubArr, SesMat):
            rangeRes = strMultiRange(subRange, len(sesElement))
            if rangeRes is None:
                print(f"Size of counter is not matched for Subject {subID}")            
            if AddPrefix:
                runStr = list()
                for rArr in rangeRes:
                    rOut = list()
                    for r in rArr:
                        rOut.append(fixstr(r, RunLen, RunPerfix))
                    runStr.append(rOut)
            else:
                runStr = rangeRes
            result.append(runStr)
        if not len(result):
            return None
        return result
    except:
        print("Wrong Format!")
        return None

# An array of [ti, t, si, fixstr(s, arrSubLen, SubPrefix), ci, fixstr(c, arrSesLen, SesPrefix), runs]
def BIDS(Tasks, SubRange, SubLen, SubPrefix, SesRange, SesLen, SesPrefix, RunRange, RunLen, RunPrefix):
        assert len(Tasks), "There is no task title"
        arrTasks = strTaskList(Tasks)
        assert arrTasks is not None, "There is no task title"
        assert len(arrTasks), "There is no task title"
        print("Tasks is okay!")

        try:
            arrSubLen = np.int32(SubLen)
            1 / arrSubLen
        except:
            raise Exception("Length of subjects must be an integer number")
        print("Length of subjects is okay!")

        assert len(SubRange), "Subject Range is wrong!"
        arrSubRange = strRange(SubRange, Unique=True)
        assert arrSubRange is not None, "Subject Range is wrong!"
        assert len(arrSubRange), "Subject Range is wrong!"
        print("Range of subjects is okay!")        
        
        SubSize = len(arrSubRange)

        try:
            arrSesLen = np.int32(SesLen)
            1 / arrSesLen
        except:
            raise Exception("Length of counter must be an integer number")
        print("Length of Counter is okay!")

        assert len(SesRange), "Counter Range is wrong!"
        arrSesRange = strMultiRange(SesRange, SubSize)
        assert arrSesRange is not None, "Counter Range is wrong!"
        assert len(arrSesRange) == SubSize, "Counter Size must be equal to Subject Size!"
        print("Counter Range is okay!")
        

        try:
            arrRunLen = np.int32(RunLen)
            1 / arrRunLen
        except:
            raise Exception("Length of runs must be an integer number")
        print("Length of runs is valid")
        
        assert len(RunRange), "Run Range is wrong!"
        arrRunRange = strMultiLineRuns(RunRange, arrSubRange, arrSesRange, arrRunLen, RunPrefix)
        assert arrRunRange is not None, "Run Range is wrong!"

        result = list()
        for ti, t in enumerate(arrTasks):
            for si, s in enumerate(arrSubRange):
                for ci, c in enumerate(arrSesRange[si]):
                    runs = arrRunRange[si][ci]
                    result.append([ti, t, si, fixstr(s, arrSubLen, SubPrefix), ci, fixstr(c, arrSesLen, SesPrefix), runs])
            
        assert len(result), "The BIDS list is empty"
        return result

def load_BIDS(settings):
    return BIDS(settings.Task, settings.SubRange, settings.SubLen, settings.SubPer,\
        settings.ConRange, settings.ConLen, settings.ConPer, \
        settings.RunRange, settings.RunLen, settings.RunPer)