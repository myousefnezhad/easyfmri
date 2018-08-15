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
