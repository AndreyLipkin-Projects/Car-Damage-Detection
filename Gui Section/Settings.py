# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(334, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        SettingsWindow.setWindowIcon(icon)
        SettingsWindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        SettingsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(50, 40, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setStyleSheet("#Logo{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.HyperparametersButton = QtWidgets.QPushButton(self.centralwidget)
        self.HyperparametersButton.setGeometry(QtCore.QRect(85, 234, 161, 41))
        self.HyperparametersButton.setStyleSheet("#HyperparametersButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Hyperparameters_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#HyperparametersButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Hyperparameters_down.png);\n"
"}\n"
"\n"
"")
        self.HyperparametersButton.setText("")
        self.HyperparametersButton.setObjectName("HyperparametersButton")
        self.ChangeClassButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeClassButton.setGeometry(QtCore.QRect(115, 264, 101, 21))
        self.ChangeClassButton.setObjectName("ChangeClassButton")
        self.GraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphButton.setGeometry(QtCore.QRect(85, 284, 161, 31))
        self.GraphButton.setStyleSheet("#GraphButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/TrainGraph_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#GraphButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/TrainGraph_down.png);\n"
"}\n"
"\n"
"")
        self.GraphButton.setText("")
        self.GraphButton.setObjectName("GraphButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(130, 340, 61, 21))
        self.BackButton.setStyleSheet("#BackButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Back_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#BackButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Back_down.png);\n"
"}\n"
"\n"
"")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        self.HelpButton = QtWidgets.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(0, 340, 31, 31))
        self.HelpButton.setStyleSheet("#HelpButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Help_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#HelpButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Help_down.png);\n"
"}\n"
"\n"
"")
        self.HelpButton.setText("")
        self.HelpButton.setObjectName("HelpButton")
        self.Logotext_2 = QtWidgets.QLabel(self.centralwidget)
        self.Logotext_2.setGeometry(QtCore.QRect(80, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.Logotext_2.setFont(font)
        self.Logotext_2.setStyleSheet("#Logotext_2{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo2.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.Logotext_2.setObjectName("Logotext_2")
        self.Logotext = QtWidgets.QLabel(self.centralwidget)
        self.Logotext.setGeometry(QtCore.QRect(100, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.Logotext.setFont(font)
        self.Logotext.setStyleSheet("#Logotext{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo1.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.Logotext.setObjectName("Logotext")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.Logo.setText(_translate("SettingsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ChangeClassButton.setText(_translate("SettingsWindow", "Change Classifier"))
        self.HelpButton.setToolTip(_translate("SettingsWindow", "<html><head/><body><p>Click here for help</p></body></html>"))
        self.Logotext_2.setText(_translate("SettingsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext.setText(_translate("SettingsWindow", "<html><head/><body><p><br/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
