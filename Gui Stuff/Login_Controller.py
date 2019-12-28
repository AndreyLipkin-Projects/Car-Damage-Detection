import sys
from os.path import dirname, realpath

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
import Gui

user_list = ["andrey"]
pass_list = ["123"]


class LoginPage(QMainWindow):

    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi('Login.ui',self)
        self.LoginButton.clicked.connect(self.openMainMenu)

    def openMainMenu(self):
        username = self.UserNameInput.toPlainText()
        password = self.PasswordInput.toPlainText()
        try :
            if user_list.index(username) != ValueError:
                if password == pass_list[user_list.index(username)]:
                    self.mainmenuwindow()
                else:
                    raise Exception(self.display_error_message("Username / password incorrect"))
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
