# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import MainMenu

user_list = ["andrey"]
pass_list = ["123"]

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(317, 382)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Logo.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 220, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 260, 51, 21))
        self.label_2.setObjectName("label_2")
        self.UserNameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.UserNameInput.setGeometry(QtCore.QRect(110, 220, 121, 31))
        self.UserNameInput.setObjectName("UserNameInput")
        self.PasswordInput = QtWidgets.QTextEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(110, 260, 121, 31))
        self.PasswordInput.setObjectName("PasswordInput")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(130, 310, 61, 21))
        self.LoginButton.setObjectName("LoginButton")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(50, 20, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogoLabel.sizePolicy().hasHeightForWidth())
        self.LogoLabel.setSizePolicy(sizePolicy)
        self.LogoLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LogoLabel.setObjectName("LogoLabel")
        self.Logotext = QtWidgets.QLabel(self.centralwidget)
        self.Logotext.setGeometry(QtCore.QRect(20, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.Logotext.setFont(font)
        self.Logotext.setObjectName("Logotext")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.LoginButton.clicked.connect(self.openMainMenu)

       # self.LoginButton.clicked.connect(self.openMainMenu)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label.setText(_translate("LoginWindow", "UseName:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))
        self.LoginButton.setText(_translate("LoginWindow", "Login"))
        self.LogoLabel.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.Logotext.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))


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





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainApplicationWindow)
    MainApplicationWindow.show()
    sys.exit(app.exec_())
