# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Images_review.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(566, 559)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logos/output-onlinepngtools (2).png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 210, 121, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 210, 121, 111))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 350, 121, 111))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 350, 121, 111))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 500, 56, 17))
        self.pushButton.setObjectName("pushButton")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 18))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Images review"))
        self.label_3.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\":/Logos/output-onlinepngtools (2).png\"/></p></body></html>"))
        self.label_4.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.label.setText(_translate("LoginWindow", "TextLabel"))
        self.label_2.setText(_translate("LoginWindow", "TextLabel"))
        self.label_5.setText(_translate("LoginWindow", "TextLabel"))
        self.label_6.setText(_translate("LoginWindow", "TextLabel"))
        self.pushButton.setText(_translate("LoginWindow", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainApplicationWindow)
    MainApplicationWindow.show()
    sys.exit(app.exec_())
