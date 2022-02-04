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
import icon_rc
import subprocess
import PyQt5.QtWidgets as QtWidgets
from GUI.frmMainMenuGUI import *
from GUI.frmFeatureAnalysis import *
from GUI.frmModelAnalysis import *
from GUI.frmPreprocess import *
from GUI.frmVisualization import *
from GUI.Login import Login
from Base.tools import Tools
from Base.utility import About, getHostname
from Base.git import clone_git, has_git_branch, getGitBranch
from Base.utility import MyMessageBox


class frmMainMenuGUI(QtWidgets.QMainWindow):
    dialog = None
    ui = Ui_frmMainMenuGUI()


    def show(self):
        from Base.utility import getVersion,getBuild
        global dialog, ui
        ui = Ui_frmMainMenuGUI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        tools = Tools()
        tools.combo(ui.cbTools)
        print()
        print(20*"#" + " Platform Information " + 20*"#")
        # Hostname
        print("Hostname:", getHostname())
        # Base Info
        print("Base:", os.name)
        # OS Info
        try:
            import platform
            print("OS:", platform.system())
            print("Kernel:", platform.release())
        except:
            pass
        # Python Info
        try:
            pythonInfo = str(sys.version).split("\n")
            print("Python:", pythonInfo[0])
            print("C Compiler:", pythonInfo[1])

        except:
            pass
        print(20*"#" + " Software Information " + 20*"#")
        print(f"easy fMRI - V{getVersion()}B{getBuild()} ({getGitBranch()})")
        try:
            ezdir = str(os.environ['EASYFMRI'])
            if len(ezdir):
                ui.txtEZDIR.setText(ezdir)
                assert os.path.isfile(ezdir + "/main.py")
                print(f"Software directory: {ezdir}")
            else:
                print("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
                msgBox = QMessageBox()
                msgBox.setText("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
        except:
                print("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
                msgBox = QMessageBox()
                msgBox.setText("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
        if has_git_branch():
            ui.cbSource.addItem("Fast via pull request", ["", "", False, True ])
        ui.cbSource.addItem("GitLab (Clone/Full)", ["gitlab.com/easyfmri/easyfmri.git", "https", False, False])
        ui.cbSource.addItem("GitHub (Clone/Full)", ["github.com/easyfmri/easyfmri.git", "https", False, False])


        dialog.setWindowTitle(f"easy fMRI - V{getVersion()}B{getBuild()} ({getGitBranch()})")

        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    def set_events(self):
        ui.btnExit.clicked.connect(self.btnExit_click)
        ui.btnPreprocess.clicked.connect(self.btnPreprocess_click)
        ui.btnFeatureAnalysis.clicked.connect(self.btnFeatureAnalysis_click)
        ui.btnModelAnalysis.clicked.connect(self.btnModelAnalysis_click)
        ui.btnAbout.clicked.connect(self.btnAbout_click)
        ui.btnVisualization.clicked.connect(self.btnVisualization_click)
        ui.btnTools.clicked.connect(self.btnTools_click)
        ui.btnStable.clicked.connect(self.btnStable_click)
        ui.btnDev.clicked.connect(self.btnDev_click)
        ui.btnUpdate.clicked.connect(self.btnUpdate_click)


    def btnExit_click(self):
         import sys
         sys.exit()

    def btnStable_click(self):
        ezdir = ui.txtEZDIR.text()
        msgBox = QMessageBox()

        if not len(ezdir):
            print("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setText("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        cmd = "cd " + ezdir + "; git checkout master"
        os.popen(cmd)
        msgBox.setText("You have to reopen easy fMRI in order to apply the new mode!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnDev_click(self):
        msgBox = QMessageBox()
        ezdir = ui.txtEZDIR.text()
        if not len(ezdir):
            print("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setText("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        cmd = "cd " + ezdir + "; git checkout developing"
        os.popen(cmd)
        msgBox.setText("You have to reopen easy fMRI in order to apply the new mode!")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


    def btnUpdate_click(self):
        msgBox = QMessageBox()
        ezdir = ui.txtEZDIR.text()
        if not len(ezdir):
            print("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setText("WARNING: cannot find $EASYFMRI! Please setup ~/.startupscript or ~/.zstartupscript")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        ezcmd = os.popen('which ezfmri').read().replace('\n', '')
        if not os.path.isfile(ezcmd):
            print("WARNING: cannot find ezfmri path!")
            ezcmd = "ezfmri"
        item = ui.cbSource.currentData()
        if item[3]:
            branch = getGitBranch() if has_git_branch(ezdir) else None
            cmd = ezdir + "/bin/ezupdate_pull_request.sh"
            print("Running:", cmd)
            process1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            process1.wait()
            if branch is not None:
                process2 = subprocess.Popen(["git", "checkout", branch], cwd=ezdir)
                process2.wait()
                print(f"Checkout to {branch}")
            msgBox.setText("Update is done!")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            sys.exit()
        else:
            user   = None
            passwd = None
            if item[2]:
                login = Login()
                if not login.exec_() == QtWidgets.QDialog.Accepted:
                    return
                passwd  = login.passwd
                user    = login.user

            print("Updating ...")
            global dialog
            dialog.hide()
            update_dir = os.popen('echo $HOME').read().replace('\n', '') + "/.ezupdate"
            print("Removing update directory...")
            os.popen("rm -rf " + update_dir)
            print("Cloning repository to " + update_dir + "...")
            clone_git(url=item[0], protocol=item[1], user=user, passwd=passwd, dir=update_dir)
            print("Checking update directory...")
            if not os.path.isdir(update_dir):
                print("Cannot find " + update_dir + "! Update is canceled.")
                msgBox.setText("Cannot find " + update_dir + "! Update is canceled.")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                sys.exit()
            if not has_git_branch(ezdir):
                print("Cannot find " + update_dir + "! Update is canceled.")
                msgBox.setText("Cannot find " + update_dir + "! Update is canceled.")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                sys.exit()
            os.popen("rm -rf " + ezdir + "; mv " + update_dir + " " + ezdir + "; " + ezcmd)
            msgBox.setText("Update is done!")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            sys.exit()


    def btnAbout_click(self):
        msgBox = MyMessageBox()
        msgBox.setMinimumWidth(800)
        msgBox.setText(About())
        msgBox.setWindowTitle("easy fMRI project")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        pass

    def btnPreprocess_click(self):
        frmPreprocess.show(frmPreprocess,dialog)


    def btnFeatureAnalysis_click(self):
        frmFeatureAnalysis.show(frmFeatureAnalysis,dialog)

    def btnModelAnalysis_click(self):
        frmModelAnalysis.show(frmModelAnalysis,dialog)

    def btnVisualization_click(self):
        frmVisalization.show(frmVisalization,dialog)
        # global dialog
        # dialog.hide()

    def btnTools_click(self):
        tools = Tools()
        tools.run(ui.cbTools.currentData())


# Auto Run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMainMenuGUI.show(frmMainMenuGUI)
    sys.exit(app.exec_())