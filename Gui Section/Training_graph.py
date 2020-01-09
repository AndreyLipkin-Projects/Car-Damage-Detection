# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Training_graph.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainGraphWindow(object):
    def setupUi(self, TrainGraphWindow):
        TrainGraphWindow.setObjectName("TrainGraphWindow")
        TrainGraphWindow.resize(1244, 770)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo_2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        TrainGraphWindow.setWindowIcon(icon)
        TrainGraphWindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        TrainGraphWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(TrainGraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(510, 50, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setStyleSheet("#Logo{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo_2.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(590, 690, 61, 31))
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
        self.AccGraphLabel = QtWidgets.QLabel(self.centralwidget)
        self.AccGraphLabel.setGeometry(QtCore.QRect(630, 260, 611, 401))
        self.AccGraphLabel.setStyleSheet("#GraphLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.AccGraphLabel.setText("")
        self.AccGraphLabel.setObjectName("AccGraphLabel")
        self.Logotext_2 = QtWidgets.QLabel(self.centralwidget)
        self.Logotext_2.setGeometry(QtCore.QRect(530, 40, 191, 51))
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
        self.Logotext.setGeometry(QtCore.QRect(550, 10, 151, 31))
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 210, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.LossGraphLabel = QtWidgets.QLabel(self.centralwidget)
        self.LossGraphLabel.setGeometry(QtCore.QRect(0, 260, 611, 401))
        self.LossGraphLabel.setStyleSheet("#GraphLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.LossGraphLabel.setText("")
        self.LossGraphLabel.setObjectName("LossGraphLabel")
        self.HelpButton = QtWidgets.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(10, 690, 31, 31))
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
        TrainGraphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrainGraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 21))
        self.menubar.setObjectName("menubar")
        TrainGraphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TrainGraphWindow)
        self.statusbar.setObjectName("statusbar")
        TrainGraphWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrainGraphWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainGraphWindow)

    def retranslateUi(self, TrainGraphWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainGraphWindow.setWindowTitle(_translate("TrainGraphWindow", "Training graph preview"))
        self.Logo.setText(_translate("TrainGraphWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext_2.setText(_translate("TrainGraphWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext.setText(_translate("TrainGraphWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("TrainGraphWindow", "Two Class Model"))
        self.comboBox.setItemText(1, _translate("TrainGraphWindow", "Three Class Model"))
        self.HelpButton.setToolTip(_translate("TrainGraphWindow", "<html><head/><body><p>Click here for help</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainGraphWindow = QtWidgets.QMainWindow()
    ui = Ui_TrainGraphWindow()
    ui.setupUi(TrainGraphWindow)
    TrainGraphWindow.show()
    sys.exit(app.exec_())
