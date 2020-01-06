# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(507, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        ResultsWindow.setWindowIcon(icon)
        ResultsWindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        ResultsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(140, 50, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setStyleSheet("#Logo{\n"
"background-color: transparent;\n"
"border-image: url(:/Logo/Logo.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 420, 141, 21))
        self.label.setStyleSheet("#label{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("MS Shell Dlg 2",12,QtGui.QFont.Bold))
        self.DamagCarPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamagCarPicLabel.setGeometry(QtCore.QRect(90, 210, 331, 191))
        self.DamagCarPicLabel.setStyleSheet("#DamagCarPicLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.DamagCarPicLabel.setText("")
        self.DamagCarPicLabel.setObjectName("DamagCarPicLabel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(60, 500, 51, 21))
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
        self.DamageTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamageTypeLabel.setGeometry(QtCore.QRect(190, 420, 251, 20))
        self.DamageTypeLabel.setStyleSheet("#DamageTypeLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.DamageTypeLabel.setObjectName("DamageTypeLabel")
        self.DamageTypeLabel.setFont(QtGui.QFont("MS Shell Dlg 2", 12, QtGui.QFont.Bold))
        self.FurtherClassButton = QtWidgets.QPushButton(self.centralwidget)
        self.FurtherClassButton.setGeometry(QtCore.QRect(320, 490, 171, 41))
        self.FurtherClassButton.setStyleSheet("#FurtherClassButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Nextstep_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#FurtherClassButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Nextstep_down.png);\n"
"}\n"
"\n"
"")
        self.FurtherClassButton.setText("")
        self.FurtherClassButton.setObjectName("FurtherClassButton")
        self.Logotext = QtWidgets.QLabel(self.centralwidget)
        self.Logotext.setGeometry(QtCore.QRect(180, 10, 151, 31))
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
        self.Logotext_2 = QtWidgets.QLabel(self.centralwidget)
        self.Logotext_2.setGeometry(QtCore.QRect(160, 40, 191, 51))
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
        self.HelpButton = QtWidgets.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(0, 500, 31, 31))
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
        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        ResultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "Results"))
        self.Logo.setText(_translate("ResultsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("ResultsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Damage Locations: </span></p></body></html>"))
        self.DamageTypeLabel.setText(_translate("ResultsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">PlaceHolder</span></p></body></html>"))
        self.Logotext.setText(_translate("ResultsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext_2.setText(_translate("ResultsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.HelpButton.setToolTip(_translate("ResultsWindow", "<html><head/><body><p>Click here for help</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())
