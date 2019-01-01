# Copyright (c) 2014--2019 Muhammad Yousefnezhad
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


def SaveFile(Title="Save ...", Filters=['All files (*.*)'], Suffix=None, currentDirectory=None, currentFile=None):
    from PyQt5.QtWidgets import QDialog, QFileDialog
    import PyQt5.QtCore as QtCore
    dialog = QFileDialog()
    dialog.setOption(QFileDialog.DontUseNativeDialog)
    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
    dialog.setWindowTitle(Title)
    if currentDirectory is not None:
        if len(currentDirectory):
            dialog.setDirectory(currentDirectory)
    if currentFile is not None:
        dialog.selectFile(currentFile)
    if Suffix is not None:
        dialog.setDefaultSuffix(Suffix)
    dialog.setAcceptMode(QFileDialog.AcceptSave)
    dialog.setNameFilters(Filters)
    if dialog.exec_() == QDialog.Accepted:
        return dialog.selectedFiles()[0]
    return []


def LoadFile(Title="Load ...", Filters=['All files (*.*)'], Suffix=None, currentDirectory=None, currentFile=None):
    from PyQt5.QtWidgets import QDialog, QFileDialog
    import PyQt5.QtCore as QtCore
    dialog = QFileDialog()
    dialog.setWindowTitle(Title)
    if currentDirectory is not None:
        if len(currentDirectory):
            dialog.setDirectory(currentDirectory)
    if currentFile is not None:
        dialog.selectFile(currentFile)
    if Suffix is not None:
        dialog.setDefaultSuffix(Suffix)
    dialog.setOption(QFileDialog.DontUseNativeDialog)
    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
    dialog.setNameFilters(Filters)
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    if dialog.exec_() == QDialog.Accepted:
        return dialog.selectedFiles()[0]
    return []


def LoadMultiFile(Title="Load ...", Filters=['All files (*.*)'], Suffix=None, currentDirectory=None, currentFile=None):
    from PyQt5.QtWidgets import QDialog, QFileDialog
    import PyQt5.QtCore as QtCore
    dialog = QFileDialog()
    dialog.setWindowTitle(Title)
    if currentDirectory is not None:
        if len(currentDirectory):
            dialog.setDirectory(currentDirectory)
    if currentFile is not None:
        dialog.selectFile(currentFile)
    if Suffix is not None:
        dialog.setDefaultSuffix(Suffix)
    dialog.setOption(QFileDialog.DontUseNativeDialog)
    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
    dialog.setNameFilters(Filters)
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    if dialog.exec_() == QDialog.Accepted:
        return dialog.selectedFiles()
    return []



def SelectDir(Title="Select a direcory", currentDirectory=None):
    from PyQt5.QtWidgets import QFileDialog
    import os
    flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
    if currentDirectory is not None:
        if len(currentDirectory):
            current = currentDirectory
        else:
            current = os.getcwd()
    else:
        current = os.getcwd()
    dialog = QFileDialog()
    dir = dialog.getExistingDirectory(None, Title, current, flags)
    if len(dir):
        return dir
    return []
