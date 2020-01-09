# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Change_classifier.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ClassifierWindow(object):
    def setupUi(self, ClassifierWindow):
        ClassifierWindow.setObjectName("ClassifierWindow")
        ClassifierWindow.resize(366, 362)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Gui-pngs/Logo.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        ClassifierWindow.setWindowIcon(icon)
        ClassifierWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(ClassifierWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(60, 10, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(30, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(250, 300, 61, 21))
        self.SaveButton.setObjectName("SaveButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(40, 300, 61, 21))
        self.BackButton.setObjectName("BackButton")
        self.SelectClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectClassLabel.setGeometry(QtCore.QRect(50, 250, 81, 20))
        self.SelectClassLabel.setObjectName("SelectClassLabel")
        self.ClassCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ClassCombo.setGeometry(QtCore.QRect(140, 250, 131, 22))
        self.ClassCombo.setObjectName("ClassCombo")
        ClassifierWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClassifierWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        ClassifierWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClassifierWindow)
        self.statusbar.setObjectName("statusbar")
        ClassifierWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClassifierWindow)
        QtCore.QMetaObject.connectSlotsByName(ClassifierWindow)

    def retranslateUi(self, ClassifierWindow):
        _translate = QtCore.QCoreApplication.translate
        ClassifierWindow.setWindowTitle(_translate("ClassifierWindow", "Change classifier"))
        self.Logo.setText(_translate("ClassifierWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("ClassifierWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.SaveButton.setText(_translate("ClassifierWindow", "Save"))
        self.BackButton.setText(_translate("ClassifierWindow", "Back"))
        self.SelectClassLabel.setText(_translate("ClassifierWindow", "Select classifier:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_ClassifierWindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())