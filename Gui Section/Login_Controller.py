import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QLineEdit
from Login import Ui_LoginWindow

user_list = ["admin"]
pass_list = ["admin"]

class LoginPage(QMainWindow,Ui_LoginWindow):

    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.PasswordInput.setEchoMode(QLineEdit.Password)
        self.LoginButton.clicked.connect(self.openMainMenu)

    #Progams first page, check credentials
    def openMainMenu(self):
        username = self.UserNameInput.text()
        password = self.PasswordInput.text()
        try :
            if user_list.index(username) != ValueError:
                if password == pass_list[user_list.index(username)]:
                    self.mainmenuwindow()
                else:
                    self.display_error_message("Username / Password incorrect")

        except ValueError:
            self.display_error_message("No such user exist in the system")

    #Present the main menu page after login
    def mainmenuwindow(self):
        from MainMenu_Controller import MainMenuPage
        self.mainmenu_page = MainMenuPage(self)
        self.mainmenu_page.show()
        self.hide()

    #Display error function
    def display_error_message(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def closeEvent(self, event):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    LoginWindow = LoginPage()
    LoginWindow.show()
    sys.exit(app.exec_())
