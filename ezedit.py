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

import sys
from PyQt6.QtWidgets import *
from GUI.frmDataEditor import frmDataEditor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 2:
        frmDataEditor.show(frmDataEditor, sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        frmDataEditor.show(frmDataEditor, sys.argv[1])
    else:
        frmDataEditor.show(frmDataEditor)
    sys.exit(app.exec_())