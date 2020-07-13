import json
import h5py
import numpy as np

class easyX:

    def _obj_to_binary(self, objdat):
        jsondat = json.dumps(objdat)
        binary = list()
        for letter in jsondat:
            binary.append(np.uint8(format(ord(letter), 'd')))
        return binary

    def _binary_to_obj(self, bdata):
        jsn = ''.join(chr(x) for x in bdata)
        d = json.loads(jsn)
        return d

    def save(self, data, fname, verbose=True):
        binaryKeys = list()
        hf = h5py.File(fname, "w")
        # Save RAW data
        rawGroup = hf.create_group("raw")
        for k in data.keys():
            try:
                rawGroup.create_dataset(k, data=data[k])
                if verbose:
                    print(f"Raw data {k} is saved!")
            except:
                binaryKeys.append(k)
        # Save Binary data
        binaryGroup = hf.create_group("binary")
        for bk in binaryKeys:
            try:
                binaryGroup.create_dataset(bk, data=self._obj_to_binary(data[bk]))
                if verbose:
                    print(f"Binary data {bk} is saved!")
            except Exception as e:
                raise Exception(f"Cannot save data: {bk}\n" + str(e))
        hf.close()


    def load(self, fname, verbose=True):
        out = {}
        hf = h5py.File(fname, "r")
        # Load RAW data
        rawData = hf['raw']
        for k in rawData.keys():
            out[k] = np.asarray(rawData[k])
            if verbose:
                print(f"Raw data {k} is loaded!")
        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            out[bk] = self._binary_to_obj(np.asarray(binaryData[bk]))
            if verbose:
                print(f"Binary data {bk} is loaded!")
        return out

    def load_keys(self, fname):
        out = list()
        hf = h5py.File(fname, "r")
        rawData = hf['raw']
        for k in rawData.keys():
            out.append(k)
        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            out.append(bk)
        return out

if __name__=="__main__":
    fname = "/tmp/a.ezx"
    d = {"a": np.array([[1, 2, 5, 8], [2., 4, 1, 6]]),
         "b": [[1], [2, 4]],
         "c": [[1, 20], [7, 4]],
         "d": "Hi There",
         "e": ["A", "B"],
         "f": [["a", "b"], ["c", "d"]],
         "data": np.random.rand(100, 1900)
        }
    print("Original data:\n", d)
    ezx = easyX()
    ezx.save(d, fname=fname)
    kout = ezx.load_keys(fname=fname)
    print("Keys:\n", kout)
    out = ezx.load_keys(fname=fname)
    print("Loaded data:\n", out)
