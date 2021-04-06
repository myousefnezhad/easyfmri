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
import numpy as np
import scipy.io as sio


def LoadEzData(Header=None,data=None):
    if Header is None:
        print("Please enter header file!")
        return None

    if not os.path.isfile(Header):
        print("Header file is not found!")
        return None

    try:
        Out = sio.loadmat(Header, appendmat=False)
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
            if Out['DataFileType'][0][0] == 0:
                print("Data file type is NII.GZ")
            else:
                print("Data file type is EZMAT")
            for dkey in DataKey:
                X = None
                dfiles = np.array(Int[dkey[0] + "_files"])[0][0]
                for fdata in dfiles:
                    try:
                        if Out['DataFileType'][0][0] == 0:
                            import nibabel as nb
                            niiimgdata = nb.load(str.strip(os.path.dirname(Header) + "/" + fdata))
                            dat = np.transpose(niiimgdata.get_data())
                            X = dat if X is None else np.concatenate((X, dat))
                            del dat, niiimgdata
                        else:
                            dat = sio.loadmat(str.strip(os.path.dirname(Header) + "/" + fdata), appendmat=False)[dkey[0]]
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
