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
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        UploadImagewindow.setWindowIcon(icon)
        UploadImagewindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(UploadImagewindow)
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
        self.label.setGeometry(QtCore.QRect(0, 260, 61, 20))
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
        self.Logo.setText(_translate("UploadImagewindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("UploadImagewindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.UploadButton.setText(_translate("UploadImagewindow", "Upload car image"))
        self.DamageclassificationButton.setText(_translate("UploadImagewindow", "Get damage localization"))
        self.BackButton.setText(_translate("UploadImagewindow", "Back"))
        self.label.setText(_translate("UploadImagewindow", "File Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UploadImagewindow = QtWidgets.QMainWindow()
    ui = Ui_UploadImagewindow()
    ui.setupUi(UploadImagewindow)
    UploadImagewindow.show()
    sys.exit(app.exec_())
