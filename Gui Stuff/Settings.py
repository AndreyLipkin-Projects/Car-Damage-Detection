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
        self.Logo.setGeometry(QtCore.QRect(60, 20, 231, 201))
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
        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(10, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.HyperparametersButton = QtWidgets.QPushButton(self.centralwidget)
        self.HyperparametersButton.setGeometry(QtCore.QRect(90, 230, 161, 41))
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
        self.ChangeClassButton.setGeometry(QtCore.QRect(120, 260, 101, 21))
        self.ChangeClassButton.setObjectName("ChangeClassButton")
        self.GraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphButton.setGeometry(QtCore.QRect(90, 280, 161, 31))
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
        self.BackButton.setGeometry(QtCore.QRect(135, 336, 61, 21))
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
        self.LogoName.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.ChangeClassButton.setText(_translate("SettingsWindow", "Change Classifier"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
