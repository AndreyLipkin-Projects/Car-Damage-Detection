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
        ResultsWindow.resize(507, 578)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        ResultsWindow.setWindowIcon(icon)
        ResultsWindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        ResultsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(130, 10, 231, 201))
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
        self.LogoName.setGeometry(QtCore.QRect(80, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 420, 91, 21))
        self.label.setStyleSheet("#label{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.DamagCarPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamagCarPicLabel.setGeometry(QtCore.QRect(80, 210, 331, 191))
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
        self.DamageTypeLabel.setGeometry(QtCore.QRect(230, 420, 151, 20))
        self.DamageTypeLabel.setStyleSheet("#DamageTypeLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.DamageTypeLabel.setText("")
        self.DamageTypeLabel.setObjectName("DamageTypeLabel")
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
        self.LogoName.setText(_translate("ResultsWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.label.setText(_translate("ResultsWindow", "Damage Locations: "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())
