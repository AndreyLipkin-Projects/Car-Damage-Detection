# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import Hyperparameters
import Login
import Settings
import Upload_image


class Ui_MainMenuWindow(object):

    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(332, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Logo.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainMenuWindow.setWindowIcon(icon)
        MainMenuWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setPixmap(QPixmap('Logo.png'))
        self.Logo.setGeometry(QtCore.QRect(50, 20, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")

        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(10, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.LocalizationButton = QtWidgets.QPushButton(self.centralwidget)
        self.LocalizationButton.setGeometry(QtCore.QRect(110, 230, 101, 21))
        self.LocalizationButton.setObjectName("LocalizationButton")
        self.TrainButton = QtWidgets.QPushButton(self.centralwidget)
        self.TrainButton.setGeometry(QtCore.QRect(110, 260, 101, 21))
        self.TrainButton.setObjectName("TrainButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(130, 310, 51, 21))
        self.BackButton.setObjectName("BackButton")
        MainMenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        MainMenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenuWindow)
        self.statusbar.setObjectName("statusbar")
        MainMenuWindow.setStatusBar(self.statusbar)

        self.TrainButton.clicked.connect(self.Settingswindow)
        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

        self.BackButton.clicked.connect(self.backfunc)
        self.TrainButton.clicked.connect(self.Settingswindow)
        self.LocalizationButton.clicked.connect(self.Classificationswindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "MainMenu"))
        self.Logo.setText(_translate("MainMenuWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("MainMenuWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.LocalizationButton.setText(_translate("MainMenuWindow", "Get Classification"))
        self.TrainButton.setText(_translate("MainMenuWindow", "Train System"))
        self.BackButton.setText(_translate("MainMenuWindow", "Back"))

    def backfunc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        #self.MainApplicationWindow1.hide()
        self.window.show()

    def Settingswindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Settings.Ui_SettingsWindow()
        self.ui.setupUi(self.window)
        #self.hide()
        self.window.show()

    def Classificationswindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Upload_image.Ui_Classificationswindow()
        self.ui.setupUi(self.window)
        #self.hide()
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())