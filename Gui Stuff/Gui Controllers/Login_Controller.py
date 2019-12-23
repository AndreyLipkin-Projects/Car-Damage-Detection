from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import MainMenu
from Gui.Login import Ui_LoginWindow

user_list = ["andrey"]
pass_list = ["123"]

class LoginConfig(QtWidgets.QMainWindow, Ui_LoginWindow):


    def __init__(self, parent=None):
        super(LoginConfig, self).__init__(parent)
        self.setupUi(self)
        username = self.UserNameInput.toPlainText()
        password = self.PasswordInput.toPlainText()

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


        #self.display_error_message("the username is:" + username + "the password is:" + password)


    def mainmenuwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MainMenu.Ui_MainMenuWindow()
        self.ui.setupUi(self.window)
        #MainApplicationWindow.hide()
        self.window.show()


    def display_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()