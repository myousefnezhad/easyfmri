import os
import platform
import configparser as cp
from Base.utility import getDIR
import subprocess as sub
from Base.utility import Str2Bool


class FSL:
    def __init__(self):
        self.FSLDIR     = None
        self.bet        = None
        self.feat       = None
        self.FeatGUI    = None
        self.flirt      = None
        self.FlirtGUI   = None
        self.platform   = None
        self.version    = None
        self.Validate   = False


    def setting(self):
        self.FSLDIR     = None
        self.bet        = None
        self.feat       = None
        self.FeatGUI    = None
        self.flirt      = None
        self.FlirtGUI   = None
        self.platform   = None
        self.version    = None
        self.Validate   = False
        MainDir = getDIR()
        try:
            config = cp.ConfigParser()
            config.read(MainDir + "/fsl.ini")
            if Str2Bool(config['DEFAULT']['manual']) == False:
                Manual = False
            else:
                print("FSL: set settings manually!")
                if not os.path.isdir(config['DEFAULT']['fsldir']):
                    print("Cannot find FSL directory!")
                    return
                else:
                    self.FSLDIR = config['DEFAULT']['fsldir']
                    print("FSLDIR:" + self.FSLDIR)
                    if not (os.path.isfile(self.FSLDIR + config['DEFAULT']['bet']) and \
                        os.path.isfile(self.FSLDIR + config['DEFAULT']['feat']) and \
                        os.path.isfile(self.FSLDIR + config['DEFAULT']['featgui']) and \
                        os.path.isfile(self.FSLDIR + config['DEFAULT']['flirt']) and \
                        os.path.isfile(self.FSLDIR + config['DEFAULT']['flirtgui'])):
                        print("Cannot find FSL cmds!")
                        return
                    else:
                        self.bet        = config['DEFAULT']['bet']
                        self.feat       = config['DEFAULT']['feat']
                        self.FeatGUI    = config['DEFAULT']['featgui']
                        self.flirt      = config['DEFAULT']['flirt']
                        self.FlirtGUI   = config['DEFAULT']['flirtgui']
                        self.platform   = platform.system()
                        self.version    = "manual"
                        self.Validate   = True
                        print("FSL: parameters are okay!")
                        return
        except:
            Manual = False

        if not Manual:
            print("FSL: set settings automatically!")
            # Linux Platform
            if platform.system() == "Linux":
                # Check for fix path of fsl-complete
                if os.path.isfile("/usr/bin/fsl5.0-Feat") and os.path.isfile("/usr/bin/fsl5.0-feat") \
                    and os.path.isfile("/usr/bin/fsl5.0-flirt") and os.path.isfile("/usr/bin/fsl5.0-Flirt") \
                    and os.path.isfile("/usr/bin/fsl5.0-bet"):
                    self.FSLDIR = "/usr/bin/"
                    self.bet = "fsl5.0-bet"
                    self.feat = "fsl5.0-feat"
                    self.FeatGUI = "fsl5.0-Feat"
                    self.flirt = "fsl5.0-flirt"
                    self.FlirtGUI = "fsl5.0-Flirt"
                    self.platform = "linux"
                    self.version = "fsl-complete"
                    self.Validate = True
                    print("FSL: parameters are okay! version: Linux, fsl-complete.")
                    return
            try:
                FSLDIR = str(os.environ["FSLDIR"])
                if not len(FSLDIR):
                    FSLDIR = None
            except:
                FSLDIR = None

            if FSLDIR is None:
                # Read from $PATHs
                self.FSLDIR = ""
                print("WARNING: Cannot find environment variable $FSLDIR!")

                # Try to find bet
                p = sub.Popen(['which', 'bet'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find bet from $PATH!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find bet from address!")
                    return
                else:
                    self.bet = CMD

                # Try to find feat
                p = sub.Popen(['which', 'feat'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find feat from $PATH!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find feat from address!")
                    return
                else:
                    self.feat = CMD

                # Try to find FeatGUI
                if platform.system() == "Linux":
                    p = sub.Popen(['which', 'Feat'], stdout=sub.PIPE, stderr=sub.PIPE)
                else:
                    p = sub.Popen(['which', 'Feat_gui'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find Feat from $PATH!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find Feat from address!")
                    return
                else:
                    self.FeatGUI = CMD

                # Try to find flirt
                p = sub.Popen(['which', 'flirt'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find flirt from $PATH!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find flirt from address!")
                    return
                else:
                    self.flirt = CMD

                # Try to find FlirtGUI
                if platform.system() == "Linux":
                    p = sub.Popen(['which', 'Flirt'], stdout=sub.PIPE, stderr=sub.PIPE)
                else:
                    p = sub.Popen(['which', 'Flirt_gui'], stdout=sub.PIPE, stderr=sub.PIPE)
                CMD, _ = p.communicate()
                CMD = CMD.decode("utf-8").replace("\n", "")
                if not len(CMD):
                    print("Cannot find Flirt from $PATH!")
                    return
                elif not os.path.isfile(CMD):
                    print("Cannot find Flirt from address!")
                    return
                else:
                    self.FlirtGUI = CMD

                self.platform = platform.system()
                self.version = "PATH"
                self.Validate = True
                print("FSL: parameters are okay! version: read from os $PATH.")
                return
            else:
                self.FSLDIR = FSLDIR
                print("$FSLDIR=" + FSLDIR)

                # BET
                if not os.path.isfile(FSLDIR + "/bin/bet"):
                    print("$FSLDIR: Cannot find bet cmd!")
                    return
                else:
                    self.bet = "/bin/bet"

                # feat
                if not os.path.isfile(FSLDIR + "/bin/feat"):
                    print("$FSLDIR: Cannot find feat cmd!")
                    return
                else:
                    self.feat = "/bin/feat"

                # flirt
                if not os.path.isfile(FSLDIR + "/bin/flirt"):
                    print("$FSLDIR: Cannot find flirt cmd!")
                    return
                else:
                    self.flirt = "/bin/flirt"

                # Feat
                if os.path.isfile(FSLDIR + "/bin/Feat_gui"):
                    self.FeatGUI = "/bin/Feat_gui"
                elif os.path.isfile(FSLDIR + "/bin/Feat"):
                    self.FeatGUI = "/bin/Feat"
                else:
                    print("$FSLDIR: Cannot find Feat cmd!")
                    return

                # Flirt
                if os.path.isfile(FSLDIR + "/bin/Flirt_gui"):
                    self.FlirtGUI = "/bin/Flirt_gui"
                elif os.path.isfile(FSLDIR + "/bin/Flirt"):
                    self.FlirtGUI = "/bin/Flirt"
                else:
                    print("$FSLDIR: Cannot find Flirt cmd!")
                    return

                self.platform = platform.system()
                self.version = "Normal"
                self.Validate = True
                print("FSL: parameters are okay! version: read from os $FSLDIR.")