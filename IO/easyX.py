import h5py
import pickle
import codecs
import numpy as np

class easyX:
    def _obj_to_binary(self, objdat):
        return codecs.encode(pickle.dumps(objdat), "base64").decode()

    def _binary_to_obj(self, bdata):
        return pickle.loads(codecs.decode(str(bdata).encode(), "base64"))

    def save(self, data, fname, verbose=True):
        binaryKeys = list()
        hf = h5py.File(fname, "w")
        hf.create_dataset("__easyfMRI__", data="easyX")
        # Save RAW data
        rawGroup = hf.create_group("raw")
        for k in data.keys():
            try:
                rawGroup.create_dataset(k, data=data[k])
                if verbose:
                    print(f"Raw data \"{k}\" is saved!")
            except:
                binaryKeys.append(k)
        # Save Binary data
        binaryGroup = hf.create_group("binary")
        for bk in binaryKeys:
            try:
                binaryGroup.create_dataset(bk, data=self._obj_to_binary(data[bk]))
                if verbose:
                    print(f"Binary data \"{bk}\" is saved!")
            except Exception as e:
                raise Exception(f"Cannot save data: \"{bk}\"\n" + str(e))
        hf.close()


    def load(self, fname, partial=None, verbose=True):
        out = dict()
        hf = h5py.File(fname, "r")
        try:
            if str(np.asanyarray(hf.get("__easyfMRI__"))) == "easyX":
                print("Signed by easyX project!")
        except:
            pass
        try:
            if len(partial) == 0:
                raise Exception
        except:
            partial = None
        # Load RAW data
        rawData = hf['raw']
        for k in rawData.keys():
            is_load = True
            if partial is not None:
                is_load = False
                try:
                    if k in partial:
                        is_load = True
                except:
                    pass
            if is_load:
                out[k] = np.asarray(rawData[k])
                if verbose:
                    print(f"Raw data {k} is loaded!")
        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            is_load = True
            if partial is not None:
                is_load = False
                try:
                    if bk in partial:
                        is_load = True
                except:
                    pass
            if is_load:
                out[bk] = self._binary_to_obj(np.asarray(binaryData[bk]))
                if verbose:
                    print(f"Binary data {bk} is loaded!")
        return out

    def load_keys(self, fname):
        out = dict()
        hf = h5py.File(fname, "r")
        rawData = hf['raw']
        for k in rawData.keys():
            out[k] = None
        # Load Binary data
        binaryData = hf['binary']
        for bk in binaryData.keys():
            out[bk] = None
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
    out = ezx.load(fname=fname)
    print("Loaded data:\n", out)

