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
                            del io
                            import scipy.io as io
                            dat = io.loadmat(str.strip(os.path.dirname(Header) + "/" + fdata), appendmat=False)[dkey[0]]
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
