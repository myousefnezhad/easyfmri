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
    _, fileExt = os.path.split(fname)
    fileExt = str(fileExt).replace(".", "").lower()
    if  fileExt == "mat":
        FileType = "mat"
    elif fileExt == "ezdata":
        FileType = "ezdata"
    elif fileExt == "ezmat":
        FileType = "ezmat"
    elif fileExt == "ezx":
        FileType = "ezx"
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


def mainIO_load(fname):
    # Check file exists
    assert os.path.isfile(fname), "Cannot find file!"
    FileType, dat = get_file_type(fname)
    if FileType == "ezx":
        ezx = easyX()
        return ezx.load(fname)
    if FileType == "mat" or FileType == "ezmat":
        if dat is not None:
            return dat
        return sio.loadmat(fname)
    if FileType == "ezdata":
        return LoadEzData(fname)

