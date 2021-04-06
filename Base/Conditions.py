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

import numpy as np

def reshape_condition_cell(x):
    try:
        if isinstance(x, np.ndarray):
            return x[0]
    except:
        pass
    return x


class Conditions:
    def __init__(self):
        self.Conditions = list()

    def check_cond(self,name):
        if len(self.Conditions):
            for cond in self.Conditions:
                if cond[0] == name:
                    return True
        return False

    def add_cond(self,name,title):
        if not self.check_cond(name):
            self.Conditions.append([name,title])

    def get_cond(self):
        return self.Conditions