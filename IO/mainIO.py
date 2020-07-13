import os
import sys
import h5py
import numpy as np
import scipy.io as sio
from IO.easyX import easyX
from IO.EasyData import LoadEzData



def get_file_type(fname):
    FileType = None
    dat = None
    # Detect file type based on extension
    if  str(fname[-3:]).lower() == "mat":
        FileType = "mat"
    elif str(fname[-3:]).lower() == "ezx":
        FileType = "ezx"
    elif str(fname[-6:]).lower() == "ezdata":
        FileType = "ezdata"
    elif str(fname[-5:]).lower() == "ezmat":
        FileType = "ezmat"
    # Detect file type based on loading data
    if FileType is None:
        try:
            h5py.File(fname, "r")
            FileType = "ezx"
        except:
            pass
        try:
            dat = sio.loadmat(fname)
            try:
                _ = dat["Integration"]
                FileType = "ezdata"
            except:
                FileType = "mat"
        except:
            pass
    assert FileType is not None, "Cannot find file type"
    return FileType, dat

def can_do_compression(fname):
    try:
        FileType, _ = get_file_type(fname)
        assert FileType != "ezx"
    except:
        return False
    return True

def mainIO_load(fname):
    # Check file exists
    assert os.path.isfile(fname), "Cannot find file!"
    FileType, dat = get_file_type(fname)
    if FileType == "ezx":
        print("File type: easyX")
        ezx = easyX()
        return ezx.load(fname)
    if FileType == "mat" or FileType == "ezmat":
        if dat is not None:
            return dat
        print(f"File type: {FileType}")
        return sio.loadmat(fname)
    if FileType == "ezdata":
        print(f"File type: {FileType}")
        return LoadEzData(fname)


def mainIO_save(data, fname, do_compression=False):
    FileType, dat = get_file_type(fname)
    if FileType == "ezx":
        print("File type: easyX")
        ezx = easyX()
        ezx.save(data, fname)
        return
    print(f"File type: {FileType}")
    sio.savemat(fname, data, do_compression=do_compression, appendmat=False)
    return