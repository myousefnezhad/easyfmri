import os
import configparser as cp
from Base.utility import getDIR
import subprocess as sub
from Base.utility import Str2Bool


class AFNI:
    def __init__(self):
        self.AFNI       = None
        self.SUMA       = None
        self.COPY       = None
        self.REFIT      = None
        self.SUMADIR    = None
        self.MNI        = None
        self.Both       = None
        self.Right      = None
        self.Left       = None
        self.Validate   = None

    def setting(self):
        self.AFNI       = None
        self.SUMA       = None
        self.COPY       = None
        self.REFIT      = None
        self.SUMADIR    = None
        self.MNI        = None
        self.Both       = None
        self.Right      = None
        self.Left       = None
        self.Validate   = None
        MainDir = getDIR()
        try:
            config = cp.ConfigParser()
            config.read(MainDir + "/afni.ini")
            self.MNI    = config['DEFAULT']['mni']
            self.Both   = config['DEFAULT']['both']
            self.Right  = config['DEFAULT']['right']
            self.Left   = config['DEFAULT']['left']
            if Str2Bool(config['DEFAULT']['manualdir']) == False:
                self.SUMADIR = MainDir + "/data/suma/"
                print("SUMA DIR is automatically detect, Directory: " + self.SUMADIR)
            else:
                self.SUMADIR = config['DEFAULT']['sumadir']
                print("SUMA DIR is manually detect, Directory: " + self.SUMADIR)

            if not os.path.isfile(self.SUMADIR + self.Both):
                print("Cannot find SUMA Both Hemisphere!")
                return

            if not os.path.isfile(self.SUMADIR + self.Left):
                print("Cannot find SUMA Left Hemisphere!")
                return

            if not os.path.isfile(self.SUMADIR + self.Right):
                print("Cannot find SUMA Right Hemisphere!")
                return

            if Str2Bool(config['DEFAULT']['manualcmd']):
                print("Reading Manual CMDs ...")
                CMD = config['DEFAULT']['afnicmd']
                if not os.path.isfile(CMD):
                    print("Cannot find AFNI binary file!")
                    return
                self.AFNI = CMD

                CMD = config['DEFAULT']['sumacmd']
                if not os.path.isfile(CMD):
                    print("Cannot find SUMA binary file!")
                    return
                self.SUMA = CMD

                CMD = config['DEFAULT']['copycmd']
                if not os.path.isfile(CMD):
                    print("Cannot find 3dcopy binary file!")
                    return
                self.COPY = CMD

                CMD = config['DEFAULT']['refitcmd']
                if not os.path.isfile(CMD):
                    print("Cannot find 3drefit binary file!")
                    return
                self.REFIT = CMD
            else:
                print("Automatically detecting CMDs ...")
                p = sub.Popen(['which', 'afni'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find AFNI Path!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find AFNI binary file!")
                    return
                else:
                    self.AFNI = CMD
                    print("AFNI cmd is automatically detected, Address: " + CMD)

                p = sub.Popen(['which', 'suma'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find SUMA Path!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find SUMA binary file!")
                    return
                else:
                    self.SUMA = CMD
                    print("SUMA cmd is automatically detected, Address: " + CMD)

                p = sub.Popen(['which', '3dcopy'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find 3dcopy Path!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find 3dcopy binary file!")
                    return
                else:
                    self.COPY = CMD
                    print("3dcopy cmd is automatically detected, Address: " + CMD)

                p = sub.Popen(['which', '3drefit'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find 3drefit Path!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find 3drefit binary file!")
                    return
                else:
                    self.REFIT = CMD
                    print("3drefit cmd is automatically detected, Address: " + CMD)

            self.Validate = True
        except:
            self.Validate = False
