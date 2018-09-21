# Copyright (c) 2014--2018 Muhammad Yousefnezhad
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
import subprocess
from urllib.parse import quote

def has_git_branch(dir="$EASYFMRI"):
    return True if len(os.popen("cd " + dir + "\n git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'").read().replace('\n', '')) else False

def clone_git(url, protocol, user=None, passwd=None, dir='~/.ezupdate'):
    if user is None:
        cmd =  "git clone " + protocol + "://" + url + " " + dir
    else:
        cmd =  "git clone " + protocol + "://" + user + ":" + quote(passwd) + "@" + url + " " + dir

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()



if __name__ == "__main__":
    print(has_git_branch())
    print(has_git_branch('/home/tony/'))