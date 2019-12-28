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
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.LoginWindow.setWindowIcon(icon)
        self.LoginWindow.setDocumentMode(False)
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
        self.LogoLabel.setGeometry(QtCore.QRect(50, 30, 231, 201))
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

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label.setText(_translate("LoginWindow", "UseName:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))
        self.LoginButton.setText(_translate("LoginWindow", "Login"))
        self.LogoLabel.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.Logotext.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))


