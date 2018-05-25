# Life is short, use Python
# ----      utf-8         ----    
# @Time     : 2018/5/22  10:25
# @Author   : Gao DongShan
# @File     : login.py
# @Start    :-----------------


import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import main_menu


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        loadUi("./UI/ui_login.ui", self)
        self.label_3.hide()
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.setWindowIcon(QIcon("./image/1.ico"))

    def slotLogin(self):
        if self.lineEdit.text() != 'admin':
            self.label_3.show()
            self.label_3.setText("密码错误！")
        else:
            self.hide()
            self.mainWindow = main_menu.MainMenu()
            self.mainWindow.reselect()
            self.mainWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_user = Login()
    login_user.show()
    login_user.exec_()
    sys.exit(app.exec_())
