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


def getGitBranch(dir=None):
    try:
        from subprocess import check_output

        if dir is None:
            import  os
            dir = str(os.environ['EASYFMRI'])

        out = check_output(["git", "branch"], cwd=dir).decode("utf8")
        current = next(line for line in out.split("\n") if line.startswith("*"))
        #print(current.strip("*").strip())
        branch = current.strip("*").strip()
        return branch
    except:
        return "unknown"


if __name__ == "__main__":
    print(getGitBranch())