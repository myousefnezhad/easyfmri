from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.user   = None
        self.passwd = None
        self.isAdd = False
        self.title = 'Enter Username & Password'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 150
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Username:")
        self.txtUser = QLineEdit()
        self.label2 = QLabel()
        self.label2.setText("Password:")
        self.txtPass = QLineEdit()
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.btnAdd = QPushButton()
        self.btnAdd.setText("OK")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Cancel")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.txtUser)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.txtPass)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)


    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        if len(self.txtUser.text()) <= 0:
            print("Please enter username!")
            return

        if len(self.txtPass.text()) <= 0:
            print("Please enter password")
            return

        self.user   = self.txtUser.text()
        self.passwd = self.txtPass.text()
        self.isAdd  = True
        self.accept()



if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        print(login.user, login.passwd)

    login.close()


    sys.exit(app.exec_())