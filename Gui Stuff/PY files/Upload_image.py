# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Upload_image.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Results


class Ui_Classificationswindow(object):
    def setupUi(self, Classificationswindow):
        Classificationswindow.setObjectName("Classificationswindow")
        Classificationswindow.resize(336, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Classificationswindow.setWindowIcon(icon)
        Classificationswindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Classificationswindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(70, 20, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.UploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.UploadButton.setGeometry(QtCore.QRect(140, 230, 91, 21))
        self.UploadButton.setObjectName("UploadButton")
        self.DamageclassificationButton = QtWidgets.QPushButton(self.centralwidget)
        self.DamageclassificationButton.setGeometry(QtCore.QRect(120, 290, 131, 21))
        self.DamageclassificationButton.setObjectName("DamageclassificationButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(160, 330, 51, 21))
        self.BackButton.setObjectName("BackButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 260, 61, 20))
        self.label.setObjectName("label")
        self.FilenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.FilenameLabel.setGeometry(QtCore.QRect(120, 260, 131, 21))
        self.FilenameLabel.setObjectName("FilenameLabel")
        Classificationswindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Classificationswindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        Classificationswindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Classificationswindow)
        self.statusbar.setObjectName("statusbar")
        Classificationswindow.setStatusBar(self.statusbar)

        self.DamageclassificationButton.clicked.connect(self.Resultwindow)

        self.retranslateUi(Classificationswindow)
        QtCore.QMetaObject.connectSlotsByName(Classificationswindow)

    def retranslateUi(self, Classificationswindow):
        _translate = QtCore.QCoreApplication.translate
        Classificationswindow.setWindowTitle(_translate("Classificationswindow", "Upload Image"))
        self.Logo.setText(_translate("Classificationswindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("Classificationswindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.UploadButton.setText(_translate("Classificationswindow", "Upload car image"))
        self.DamageclassificationButton.setText(_translate("Classificationswindow", "Get damage localization"))
        self.BackButton.setText(_translate("Classificationswindow", "Back"))
        self.label.setText(_translate("Classificationswindow", "File Name:"))
        self.FilenameLabel.setText(_translate("Classificationswindow", "TextLabel"))

    def Resultwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Results.Ui_ResultsWindow()
        self.ui.setupUi(self.window)
        # self.hide()
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_Classificationswindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())
