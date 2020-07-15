# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
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
import sys
import h5py
import numpy as np
import scipy.io as sio
from IO.easyX import easyX
from IO.EasyData import LoadEzData

def reshape_1Dvector(vec):
    if len(np.shape(vec)) != 1:
        return vec
    try:
        if len(vec) < 1:
            raise Exception
    except:
        return vec
    return [vec]

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

def mainIO_load(fname, only_keys=False, partial=None):
    # Check file exists
    assert os.path.isfile(fname), "Cannot find file!"
    FileType, dat = get_file_type(fname)
    if FileType == "ezx":
        print("File type: easyX")
        ezx = easyX()
        if only_keys:
            return ezx.load_keys(fname)
        return ezx.load(fname, partial=partial)
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