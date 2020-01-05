# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Upload_image.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UploadImagewindow(object):
    def setupUi(self, UploadImagewindow):
        UploadImagewindow.setObjectName("UploadImagewindow")
        UploadImagewindow.resize(336, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        UploadImagewindow.setWindowIcon(icon)
        UploadImagewindow.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        UploadImagewindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(UploadImagewindow)
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
        self.LogoName.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.UploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.UploadButton.setGeometry(QtCore.QRect(100, 220, 151, 31))
        self.UploadButton.setStyleSheet("#UploadButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/UploadCar_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#UploadButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/UploadCarn_down.png);\n"
"}\n"
"\n"
"")
        self.UploadButton.setText("")
        self.UploadButton.setObjectName("UploadButton")
        self.DamageclassificationButton = QtWidgets.QPushButton(self.centralwidget)
        self.DamageclassificationButton.setGeometry(QtCore.QRect(80, 290, 191, 31))
        self.DamageclassificationButton.setStyleSheet("#DamageclassificationButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/GetDmgClass_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#DamageclassificationButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/GetDmgClassn_down.png);\n"
"}\n"
"\n"
"")
        self.DamageclassificationButton.setText("")
        self.DamageclassificationButton.setObjectName("DamageclassificationButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(150, 330, 51, 21))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 260, 61, 20))
        self.label.setStyleSheet("#label{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.label.setObjectName("label")
        self.FilenameLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.FilenameLabel.setGeometry(QtCore.QRect(50, 260, 281, 20))
        self.FilenameLabel.setText("")
        self.FilenameLabel.setObjectName("FilenameLabel")
        UploadImagewindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UploadImagewindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        UploadImagewindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UploadImagewindow)
        self.statusbar.setObjectName("statusbar")
        UploadImagewindow.setStatusBar(self.statusbar)

        self.retranslateUi(UploadImagewindow)
        QtCore.QMetaObject.connectSlotsByName(UploadImagewindow)

    def retranslateUi(self, UploadImagewindow):
        _translate = QtCore.QCoreApplication.translate
        UploadImagewindow.setWindowTitle(_translate("UploadImagewindow", "Upload Image"))
        self.Logo.setText(_translate("UploadImagewindow", "<html><head/><body><p><br/></p></body></html>"))
        self.LogoName.setText(_translate("UploadImagewindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.label.setText(_translate("UploadImagewindow", "File Name:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UploadImagewindow = QtWidgets.QMainWindow()
    ui = Ui_UploadImagewindow()
    ui.setupUi(UploadImagewindow)
    UploadImagewindow.show()
    sys.exit(app.exec_())
