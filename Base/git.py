import os
import subprocess
from urllib.parse import quote

def has_git_branch(dir="$EASYFMRI"):
    return True if len(os.popen("cd " + dir + "\n git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'").read().replace('\n', '')) else False

def clone_git(url, protocol, user=None, passwd=None):
    if user is None:
        cmd =  "git clone " + protocol + "://" + url
    else:
        cmd =  "git clone " + protocol + "://" + user + ":" + quote(passwd) + "@" + url

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()



if __name__ == "__main__":
    print(has_git_branch())
    print(has_git_branch('/home/tony/'))