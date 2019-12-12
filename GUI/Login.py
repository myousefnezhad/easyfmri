# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
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