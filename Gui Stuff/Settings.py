# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Change_classifier
import Hyperparameters
import Training_graph


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(334, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Logo.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        SettingsWindow.setWindowIcon(icon)
        SettingsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(50, 20, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
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
        self.HyperparametersButton.setGeometry(QtCore.QRect(120, 230, 101, 21))
        self.HyperparametersButton.setObjectName("HyperparametersButton")
        self.ChangeClassButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeClassButton.setGeometry(QtCore.QRect(120, 250, 101, 21))
        self.ChangeClassButton.setObjectName("ChangeClassButton")
        self.GraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphButton.setGeometry(QtCore.QRect(120, 270, 101, 21))
        self.GraphButton.setObjectName("GraphButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(140, 340, 56, 17))
        self.BackButton.setObjectName("BackButton")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)


        self.ChangeClassButton.clicked.connect(self.ChangeClasswindow)
        self.HyperparametersButton.clicked.connect(self.Hyperparameterswindow)
        self.GraphButton.clicked.connect(self.Traingraphwindow)

        self.BackButton.clicked.connect(self.closeAndReturn)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.Logo.setText(_translate("SettingsWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("SettingsWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.HyperparametersButton.setText(_translate("SettingsWindow", "Hyperparameters"))
        self.ChangeClassButton.setText(_translate("SettingsWindow", "Change Classifier"))
        self.GraphButton.setText(_translate("SettingsWindow", "Training graph"))
        self.BackButton.setText(_translate("SettingsWindow", "Back"))

    def ChangeClasswindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Change_classifier.Ui_ClassifierWindow()
        self.ui.setupUi(self.window)
        #self.hide()
        self.window.show()

    def closeAndReturn(self):
        self.close()
        self.parent().show()


    def Hyperparameterswindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Hyperparameters.Ui_HyperparametersWindow()
        self.ui.setupUi(self.window)
        # self.hide()
        self.window.show()

    def Traingraphwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Training_graph.Ui_TrainGraphWindow()
        self.ui.setupUi(self.window)
        # self.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())
