import sys
from getpass import getpass
from os.path import dirname, realpath

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow, QLineEdit
from PyQt5.uic import loadUi
import Gui
from Login import Ui_LoginWindow

user_list = ["andrey"]
pass_list = ["123"]


class LoginPage(QMainWindow,Ui_LoginWindow):

    def __init__(self):
        super(LoginPage, self).__init__()
        #loadUi('Login.ui',self)
        self.setupUi(self)
        self.PasswordInput.setEchoMode(QLineEdit.Password)
        self.LoginButton.clicked.connect(self.openMainMenu)

    def openMainMenu(self):
        username = self.UserNameInput.text()
        password = self.PasswordInput.text()
        try :
            if user_list.index(username) != ValueError:
                if password == pass_list[user_list.index(username)]:
                    self.mainmenuwindow()
                else:
                    self.display_error_message("Username / password incorrect")

        except ValueError:
            self.display_error_message("no such user")

    def mainmenuwindow(self):
        from MainMenu_Controller import MainMenuPage
        self.mainmenu_page = MainMenuPage(self)
        self.mainmenu_page.show()
        self.hide()


    def display_error_message(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    LoginWindow = LoginPage()
    LoginWindow.show()
    sys.exit(app.exec_())
