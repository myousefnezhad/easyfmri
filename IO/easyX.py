# Copyright (c) 2020 Tony Muhammad Yousefnezhad
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

import h5py
import pickle
import codecs
import numpy as np

class easyX:
    def _obj_to_binary(self, objdat):
        return codecs.encode(pickle.dumps(objdat), "base64").decode()

    def _binary_to_obj(self, bdata):
        return pickle.loads(codecs.decode(str(np.array(bdata, dtype=str)).encode(), "base64"))
        # Althernatively:
        #return pickle.loads(codecs.decode(str(np.array2string(bdata)[2:-1]).replace("\\n", "").encode(), "base64"))
        # Failed
        #return pickle.loads(codecs.decode(str(bdata).encode(), "base64"))

    def save(self, data, fname, verbose=True):
        binaryKeys = list()
        hf = h5py.File(fname, "w")
        hf.create_dataset("__easyfMRI__", data="easyX")
        # Save RAW data
        rawGroup = hf.create_group("raw")
        for k in data.keys():
            try:
                if verbose:
                    print('\x1b[0m' + f"SAVE::RAW::{k}", end='')
                rawGroup.create_dataset(k, data=data[k])
                if verbose:
                    print('\x1b[32m' + " ✓" + '\x1b[0m')
            except:
                binaryKeys.append(k)
                print('\x1b[0m' + " [" + '\x1b[94m' + "R2B" + '\x1b[0m' + "]" + '\x1b[0m')
        # Save Binary data
        binaryGroup = hf.create_group("binary")
        for bk in binaryKeys:
            try:
                if verbose:
                    print('\x1b[0m' + f"SAVE::BINARY::{bk}", end='')
                binaryGroup.create_dataset(bk, data=self._obj_to_binary(data[bk]))
                if verbose:
                    print('\x1b[32m' + " ✓" + '\x1b[0m')
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
                if verbose:
                    print('\x1b[0m' + f"LOAD::RAW::{k}" , end='')
                out[k] = np.asarray(rawData[k])
                if verbose:
                    print('\x1b[32m' + " ✓" + '\x1b[0m')

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
                if verbose:
                    print('\x1b[0m' + f"LOAD::BINARY::{bk}", end='')
                try:
                    out[bk] = self._binary_to_obj(np.asarray(binaryData[bk]))
                    if verbose:
                        print('\x1b[32m' + " ✓" + '\x1b[0m')
                except:
                    if verbose:
                        print('\x1b[31m' + " x" + '\x1b[0m')
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
    # Create a complex data structre
    d = {"a": np.array([[1, 2, 5, 8], [2., 4, 1, 6]]),
         "b": [[1], [2, 4]],
         "c": [[1, 20], [7, 4]],
         "d": "Hi There",
         "e": ["A", "B"],
         "f": [["a", "b"], ["c", "d"]],
         "data": np.random.rand(100, 1000)
        }
    print("Original data:\n", d)
    # Example 1: Save dict to a file
    ezx = easyX()
    fname = "/tmp/a.ezx"
    ezx.save(d, fname=fname)
    # Example 2: Load a file to dict
    ezx = easyX()
    fname = "/tmp/a.ezx"
    data = ezx.load(fname=fname)
    print("Loaded data:\n", data)
    # Example 3: Load only the keys in a file to a dict
    ezx = easyX()
    fname = "/tmp/a.ezx"
    keys = ezx.load_keys(fname=fname)
    print("Keys:\n", kout)
