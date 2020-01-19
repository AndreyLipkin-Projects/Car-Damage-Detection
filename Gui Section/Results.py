# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(507, 595)
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
"border-image: url(Gui-pngs/Logo.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.DamagCarPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamagCarPicLabel.setGeometry(QtCore.QRect(90, 210, 331, 181))
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
        self.BackButton.setGeometry(QtCore.QRect(60, 510, 61, 31))
        self.BackButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
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
        self.ThreeClassButton = QtWidgets.QPushButton(self.centralwidget)
        self.ThreeClassButton.setGeometry(QtCore.QRect(320, 500, 171, 41))
        self.ThreeClassButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ThreeClassButton.setStyleSheet("#ThreeClassButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/ThreeClass_Up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#ThreeClassButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/ThreeClass_Down.png);\n"
"}\n"
"\n"
"")
        self.ThreeClassButton.setText("")
        self.ThreeClassButton.setObjectName("ThreeClassButton")
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
        self.HelpButton.setGeometry(QtCore.QRect(0, 510, 31, 31))
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
        self.DamageText = QtWidgets.QTextEdit(self.centralwidget)
        self.DamageText.setGeometry(QtCore.QRect(150, 400, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DamageText.setFont(font)
        self.DamageText.setStyleSheet("")
        self.DamageText.setObjectName("DamageText")
        self.GifLabel = QtWidgets.QLabel(self.centralwidget)
        self.GifLabel.setGeometry(QtCore.QRect(220, 400, 211, 91))
        self.GifLabel.setStyleSheet("#GifLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.GifLabel.setText("")
        self.GifLabel.setObjectName("GifLabel")
        self.TwoClassButton = QtWidgets.QPushButton(self.centralwidget)
        self.TwoClassButton.setGeometry(QtCore.QRect(320, 500, 171, 41))
        self.TwoClassButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.TwoClassButton.setStyleSheet("#TwoClassButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/TwoClass_Up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#TwoClassButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/TwoClass_Down.png);\n"
"}\n"
"\n"
"")
        self.TwoClassButton.setText("")
        self.TwoClassButton.setObjectName("TwoClassButton")
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
        self.Logotext.setText(_translate("ResultsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Logotext_2.setText(_translate("ResultsWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.HelpButton.setToolTip(_translate("ResultsWindow", "<html><head/><body><p>Click here for help</p></body></html>"))
        self.DamageText.setHtml(_translate("ResultsWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())
