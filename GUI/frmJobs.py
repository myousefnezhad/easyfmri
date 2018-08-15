#!/usr/bin/env python3
import os
import sys
import time
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from Base.utility import getVersion, getBuild, OpenReport
from Base.dialogs import SaveFile
from GUI.frmJobsGUI import *


class JobRunner(QThread):
    setItem     = QtCore.pyqtSignal(object)
    setStatus   = QtCore.pyqtSignal(object)


    def __init__(self):
        QtCore.QThread.__init__(self)
        self.RunState = False
        self.currJ    = None
        self.currCol  = None
        self.currStr  = None


    def setDoRun(self,state):
        self.RunState = state


    def run(self):
        try:
            TotalRow = ui.lvJobs.topLevelItemCount()
            print("%d jobs are started ..." % (TotalRow))
            while self.RunState:
                 # Refresh Status
                RunCounter = 0
                stStop = 0
                stDone = 0
                stFail = 0
                for j in range(0,TotalRow):
                    item = dialog.TreeView_getItem(j)
                    # Check Status
                    if item.text(2) == "Ready":
                        stStop = stStop + 1
                    elif item.text(2) == "Done":
                        stDone = stDone + 1
                    elif item.text(2) == "Failed":
                        stFail = stFail + 1
                    # Find Job
                    jID  = np.int32(item.text(0)) - 1
                    job  = JobList[jID]
                    job[2].open = ui.cbOpen.isChecked()
                    job[2].isKill = False
                    # Update Status
                    if not item.text(2) == job[2].status:
                        self.setItem.emit([j, 2, job[2].status])
                    # Counting Running Jobs
                    if job[2].status == "Running":
                        RunCounter = RunCounter + 1

                # Run New Task
                NumAvailaleTask = np.int32(ui.txtActive.text()) - RunCounter
                if NumAvailaleTask > 0:
                    for j in range(0, TotalRow):
                        # Check Job State
                        item = dialog.TreeView_getItem(j)
                        jID = np.int32(item.text(0)) - 1
                        job = JobList[jID]
                        # Run a stop-job
                        if job[2].status == "Ready":
                            job[2].start()
                            print("Job: " + job[1] + " - is running ...")
                            self.setItem.emit([j , 2, "Running"])
                            NumAvailaleTask = NumAvailaleTask - 1
                        # Active Session Limit
                        if NumAvailaleTask <= 0:
                            break
                Message = ["Running " + str(TotalRow) + " jobs, Active " + ui.txtActive.text() + ", Ready " + \
                          str(stStop) + ", Failed " + str(stFail) + ", Done " + str(stDone)]
                self.setStatus.emit(Message)

                # Finishing condition
                if TotalRow == stDone + stFail:
                    ui.btnRun.setText("Run")
                    self.RunState = False
                    break
                time.sleep(2)

            # Killing Procedure
            stStop = 0
            stDone = 0
            stFail = 0
            for j in range(0, TotalRow):
                item = dialog.TreeView_getItem(j)
                jID = np.int32(item.text(0)) - 1
                job = JobList[jID]
                if item.text(2) == "Ready":
                    stStop = stStop + 1
                elif item.text(2) == "Done":
                    stDone = stDone + 1
                elif item.text(2) == "Failed":
                    stFail = stFail + 1
                if job[2].status == "Running":
                    job[2].kill()
                    self.setItem.emit([j, 2, "Failed"])
                    print("Job: " + job[1] + " is terminated.")
                    stFail = stFail + 1

            Message = [str(TotalRow) + " jobs, Ready " + str(stStop) + ", Failed " + str(stFail) + ", Done " + str(stDone)]
            self.setStatus.emit(Message)
            print("Jobs are finished.")
        except Exception as e:
            print(str(e))


class MainWindow(QtWidgets.QMainWindow):
    parent = None
    jobRunner = None
    def __init__(self,parentin=None, JobRunner=None):
        super().__init__()
        global parent, jobRunner
        if parentin is not None:
            parent = parentin
        if JobRunner is not None:
            jobRunner = JobRunner

    def closeEvent(self,event):
        global parent, jobRunner
        try:
            JRunner.setDoRun(False)
            time.sleep(3)
        except:
            pass
        try:
            if parent is not None:
                parent.show()
        except:
            pass
    pass

    def TreeView_getItem(self, data):
        return ui.lvJobs.topLevelItem(data)

    def TreeView_setItem(self, data):
        global JRunner
        ui.lvJobs.topLevelItem(data[0]).setText(data[1], data[2])

    def Status_setMessage(self, data):
        ui.stb.showMessage(data[0])


class frmJobs(Ui_frmJobs):
    ui          = Ui_frmJobs()
    dialog      = None
    JRunner     = JobRunner()
    JobList     = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, Jobs=None, parentin=None):
        global dialog, ui, parent, JRunner, JobList, JobListBack
        ui = Ui_frmJobs()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        JobList     = Jobs
        JRunner     = None
        if parentin is not None:
            dialog = MainWindow(parentin,JRunner)
        else:
            dialog = MainWindow()

        ui.setupUi(dialog)
        self.set_events(self)
        self.refresh_list(self)

        ui.tabWidget.setCurrentIndex(0)

        ui.lvJobs.setColumnCount(4)
        ui.lvJobs.setHeaderLabels(['ID','Type','Status','File'])
        ui.lvJobs.setColumnWidth(0,50)
        ui.lvJobs.setColumnWidth(1,150)
        ui.lvJobs.setColumnWidth(2,150)
        dialog.setWindowTitle("easy fMRI Job Manager - V" + getVersion() + "B" + getBuild())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnUp.clicked.connect(self.btnMoveUp_click)
        ui.btnDown.clicked.connect(self.btnMoveDown_click)
        ui.btnRun.clicked.connect(self.btnRun_click)
        ui.btnDelete.clicked.connect(self.btnDelete_click)
        ui.btnReport.clicked.connect(self.btnReport_click)
        #ui.btnReset.clicked.connect(self.btnReset_click)


    # Close
    def btnClose_click(self):
        global dialog, parent
        dialog.close()


    def refresh_list(self):
        ui.lvJobs.clear()
        ui.txtVerify.clear()
        if JobList is not None:
            for jinx, job in enumerate(JobList):
                ui.txtVerify.append("Job ID: " + str(jinx + 1))
                for fil in job[2].files:
                    ui.txtVerify.append(fil)
                item = QtWidgets.QTreeWidgetItem()
                item.setText(0, str(jinx + 1))
                item.setText(1, job[0])
                item.setText(2, job[2].status)
                item.setText(3, job[1])
                ui.lvJobs.addTopLevelItem(item)
        ui.lvJobs.sortByColumn(3, QtCore.Qt.AscendingOrder)
        ui.stb.showMessage("Number of jobs: %d " % (ui.lvJobs.topLevelItemCount()))


    def btnMoveUp_click(self):
        if ui.btnRun.text() == "Stop":
            msgBox = QMessageBox()
            msgBox.setText("Please stop jobs first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        item = ui.lvJobs.currentItem()
        row  = ui.lvJobs.currentIndex().row()
        if row > 0:
            ui.lvJobs.takeTopLevelItem(row)
            ui.lvJobs.insertTopLevelItem(row - 1, item)
            ui.lvJobs.setCurrentItem(item)


    def btnMoveDown_click(self):
        if ui.btnRun.text() == "Stop":
            msgBox = QMessageBox()
            msgBox.setText("Please stop jobs first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        item = ui.lvJobs.currentItem()
        row  = ui.lvJobs.currentIndex().row()

        if (row >= 0) and (row < ui.lvJobs.topLevelItemCount() - 1):
            ui.lvJobs.takeTopLevelItem(row)
            ui.lvJobs.insertTopLevelItem(row + 1, item)
            ui.lvJobs.setCurrentItem(item)


    def btnDelete_click(self):
        if ui.btnRun.text() == "Stop":
            msgBox = QMessageBox()
            msgBox.setText("Please stop jobs first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        root = ui.lvJobs.invisibleRootItem()
        for item in ui.lvJobs.selectedItems():
            (item.parent() or root).removeChild(item)


    def btnRun_click(self):
        global JRunner
        if ui.lvJobs.topLevelItemCount() < 1:
            msgBox = QMessageBox()
            msgBox.setText("There is no job!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        if ui.btnRun.text() == "Run":
            JRunner = None
            time.sleep(1)
            JRunner = JobRunner()
            JRunner.setItem.connect(dialog.TreeView_setItem)
            JRunner.setStatus.connect(dialog.Status_setMessage)
            ui.btnRun.setText("Stop")
            JRunner.setDoRun(True)
            JRunner.start()
        else:
            ui.stb.showMessage("Please wait ...")
            JRunner.setDoRun(False)
            time.sleep(1)
            JRunner = None
            ui.btnRun.setText("Run")


    def btnReport_click(self):
        if ui.btnRun.text() == "Stop":
            msgBox = QMessageBox()
            msgBox.setText("Please stop jobs first!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        TotalRow = ui.lvJobs.topLevelItemCount()
        if TotalRow < 1:
            msgBox = QMessageBox()
            msgBox.setText("There is no job!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        ofile = SaveFile("Saving Report ...",['Text files (*.txt)'],'txt')
        if len(ofile):
            file = open(ofile,"w")
            file.write("Type\tStatus\tFile\n")
            for j in range(0, TotalRow):
                item = ui.lvJobs.topLevelItem(j)
                file.write(item.text(1) + "\t" + item.text(2) + "\t" + item.text(3) + "\n")
            file.close()
            print("Report is saved!")
            OpenReport(ofile)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmJobs.show(frmJobs)
    sys.exit(app.exec_())