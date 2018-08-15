from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore

class frmEventViewer(QDialog):
    def __init__(self, Events=None, StartRow=None, SubID=None, RowID=None, Task=None):
        super().__init__()
        self.title = 'Event Viewer (Subject: ' + str(SubID) + ', Row: ' + str(RowID) + ', Task: ' + str(Task) + ')'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Contents are read from row:")
        self.txtRowStart = QLineEdit()
        self.txtRowStart.setReadOnly(True)
        self.txtRowStart.setText(str(StartRow))
        self.tableWidget = QTableWidget()
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)

        if Events is not None:
            ESize = len(Events)
            self.tableWidget.setRowCount(ESize)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(['Onset', 'Duration', 'Condition'])
            for i in range(0, ESize):
                for j in range(0, 3):
                    item = QTableWidgetItem(str(Events[i][j]))
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, j, item)
            self.tableWidget.move(0, 0)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.txtRowStart)
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()
        pass

    def btnExit_onclick(self):
        self.close()