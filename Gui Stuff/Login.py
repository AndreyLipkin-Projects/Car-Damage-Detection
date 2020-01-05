# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(317, 382)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        LoginWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 220, 61, 31))
        self.label.setStyleSheet("#label{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 260, 51, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("#label_2{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(120, 300, 81, 31))
        self.LoginButton.setStyleSheet("#LoginButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Login_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#LoginButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Login_down.png);\n"
"}\n"
"\n"
"")
        self.LoginButton.setText("")
        self.LoginButton.setObjectName("LoginButton")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(60, 10, 211, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogoLabel.sizePolicy().hasHeightForWidth())
        self.LogoLabel.setSizePolicy(sizePolicy)
        self.LogoLabel.setStyleSheet("#LogoLabel{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
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
        self.UserNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.UserNameInput.setGeometry(QtCore.QRect(110, 230, 113, 20))
        self.UserNameInput.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"\n"
"")
        self.UserNameInput.setObjectName("UserNameInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(110, 260, 113, 20))
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.label.raise_()
        self.label_2.raise_()
        self.LoginButton.raise_()
        self.UserNameInput.raise_()
        self.PasswordInput.raise_()
        self.LogoLabel.raise_()
        self.Logotext.raise_()
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

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label.setText(_translate("LoginWindow", "UseName:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))
        self.LogoLabel.setText(_translate("LoginWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
