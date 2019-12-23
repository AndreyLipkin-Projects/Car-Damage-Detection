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
        TrainGraphWindow.resize(466, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        TrainGraphWindow.setWindowIcon(icon)
        TrainGraphWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(TrainGraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(120, 10, 231, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
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
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(210, 450, 56, 17))
        self.BackButton.setObjectName("BackButton")
        self.GraphLabel = QtWidgets.QLabel(self.centralwidget)
        self.GraphLabel.setGeometry(QtCore.QRect(100, 200, 281, 201))
        self.GraphLabel.setObjectName("GraphLabel")
        TrainGraphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrainGraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
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
        self.Logo.setText(_translate("TrainGraphWindow", "<html><head/><body><p><img src=\"Logo.png\"/></p></body></html>"))
        self.LogoName.setText(_translate("TrainGraphWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.BackButton.setText(_translate("TrainGraphWindow", "Back"))
        self.GraphLabel.setText(_translate("TrainGraphWindow", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApplicationWindow1 = QtWidgets.QMainWindow()
    ui = Ui_TrainGraphWindow()
    ui.setupUi(MainApplicationWindow1)
    MainApplicationWindow1.show()
    sys.exit(app.exec_())
