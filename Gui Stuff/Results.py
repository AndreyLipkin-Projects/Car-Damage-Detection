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
        ResultsWindow.resize(704, 578)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logos/output-onlinepngtools (2).png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        ResultsWindow.setWindowIcon(icon)
        ResultsWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(230, 20, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(180, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 450, 91, 21))
        self.label.setObjectName("label")
        self.DamagCarPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamagCarPicLabel.setGeometry(QtCore.QRect(180, 230, 331, 191))
        self.DamagCarPicLabel.setObjectName("DamagCarPicLabel")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(310, 500, 51, 21))
        self.BackButton.setObjectName("BackButton")
        self.DamageTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.DamageTypeLabel.setGeometry(QtCore.QRect(300, 450, 151, 20))
        self.DamageTypeLabel.setObjectName("DamageTypeLabel")
        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
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
        self.Logo.setText(_translate("ResultsWindow", "<html><head/><body><p><img src=\":/Logos/output-onlinepngtools (2).png\"/></p></body></html>"))
        self.LogoName.setText(_translate("ResultsWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.label.setText(_translate("ResultsWindow", "Damage Locations: "))
        self.DamagCarPicLabel.setText(_translate("ResultsWindow", "TextLabel"))
        self.BackButton.setText(_translate("ResultsWindow", "Back"))
        self.DamageTypeLabel.setText(_translate("ResultsWindow", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())
