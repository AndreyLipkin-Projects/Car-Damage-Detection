# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hyperparameters.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HyperparametersPage(object):
    def setupUi(self, HyperparametersPage):
        HyperparametersPage.setObjectName("HyperparametersPage")
        HyperparametersPage.resize(464, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui-pngs/Logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        HyperparametersPage.setWindowIcon(icon)
        HyperparametersPage.setToolTip("")
        HyperparametersPage.setWhatsThis("")
        HyperparametersPage.setAccessibleName("")
        HyperparametersPage.setStyleSheet("background-image: url(Gui-pngs/Background.png);")
        self.centralwidget = QtWidgets.QWidget(HyperparametersPage)
        self.centralwidget.setObjectName("centralwidget")
        self.mainModelGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mainModelGroupBox.setGeometry(QtCore.QRect(10, 260, 441, 251))
        self.mainModelGroupBox.setStyleSheet("#mainModelGroupBox{\n"
"background-color: transparent;\n"
"background: none;\n"
"\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.mainModelGroupBox.setObjectName("mainModelGroupBox")
        self.LearningRateSpinBox = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.LearningRateSpinBox.setGeometry(QtCore.QRect(250, 60, 62, 22))
        self.LearningRateSpinBox.setMouseTracking(False)
        self.LearningRateSpinBox.setToolTip("")
        self.LearningRateSpinBox.setDecimals(4)
        self.LearningRateSpinBox.setMinimum(0.0001)
        self.LearningRateSpinBox.setMaximum(9999.0)
        self.LearningRateSpinBox.setSingleStep(0.0001)
        self.LearningRateSpinBox.setProperty("value", 0.0001)
        self.LearningRateSpinBox.setObjectName("LearningRateSpinBox")
        self.L1RegularizationSpinBox = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.L1RegularizationSpinBox.setGeometry(QtCore.QRect(250, 90, 62, 22))
        self.L1RegularizationSpinBox.setToolTip("")
        self.L1RegularizationSpinBox.setDecimals(2)
        self.L1RegularizationSpinBox.setMinimum(1.0)
        self.L1RegularizationSpinBox.setMaximum(9999.0)
        self.L1RegularizationSpinBox.setSingleStep(0.01)
        self.L1RegularizationSpinBox.setProperty("value", 1.0)
        self.L1RegularizationSpinBox.setObjectName("L1RegularizationSpinBox")
        self.ValBatchSizeSpinBox = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.ValBatchSizeSpinBox.setGeometry(QtCore.QRect(250, 210, 62, 22))
        self.ValBatchSizeSpinBox.setToolTip("")
        self.ValBatchSizeSpinBox.setDecimals(0)
        self.ValBatchSizeSpinBox.setMinimum(1.0)
        self.ValBatchSizeSpinBox.setMaximum(9999.0)
        self.ValBatchSizeSpinBox.setProperty("value", 1.0)
        self.ValBatchSizeSpinBox.setObjectName("ValBatchSizeSpinBox")
        self.TrainBatchSizeSpinBox = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.TrainBatchSizeSpinBox.setGeometry(QtCore.QRect(250, 180, 62, 22))
        self.TrainBatchSizeSpinBox.setToolTip("")
        self.TrainBatchSizeSpinBox.setDecimals(0)
        self.TrainBatchSizeSpinBox.setMinimum(1.0)
        self.TrainBatchSizeSpinBox.setMaximum(9999.0)
        self.TrainBatchSizeSpinBox.setProperty("value", 1.0)
        self.TrainBatchSizeSpinBox.setObjectName("TrainBatchSizeSpinBox")
        self.learningRateLabel = QtWidgets.QLabel(self.mainModelGroupBox)
        self.learningRateLabel.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.learningRateLabel.setStyleSheet("#learningRateLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.learningRateLabel.setObjectName("learningRateLabel")
        self.epochsLabel_2 = QtWidgets.QLabel(self.mainModelGroupBox)
        self.epochsLabel_2.setGeometry(QtCore.QRect(140, 180, 91, 16))
        self.epochsLabel_2.setStyleSheet("#epochsLabel_2{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.epochsLabel_2.setObjectName("epochsLabel_2")
        self.ValBatchLabel = QtWidgets.QLabel(self.mainModelGroupBox)
        self.ValBatchLabel.setGeometry(QtCore.QRect(140, 210, 101, 16))
        self.ValBatchLabel.setStyleSheet("#ValBatchLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.ValBatchLabel.setObjectName("ValBatchLabel")
        self.L1RegularizationLabel = QtWidgets.QLabel(self.mainModelGroupBox)
        self.L1RegularizationLabel.setGeometry(QtCore.QRect(140, 90, 91, 16))
        self.L1RegularizationLabel.setStyleSheet("#L1RegularizationLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.L1RegularizationLabel.setObjectName("L1RegularizationLabel")
        self.epochsSpinBox = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.epochsSpinBox.setGeometry(QtCore.QRect(250, 30, 62, 22))
        self.epochsSpinBox.setToolTip("")
        self.epochsSpinBox.setDecimals(0)
        self.epochsSpinBox.setMinimum(1.0)
        self.epochsSpinBox.setMaximum(9999.0)
        self.epochsSpinBox.setProperty("value", 12.0)
        self.epochsSpinBox.setObjectName("epochsSpinBox")
        self.epochsLabel = QtWidgets.QLabel(self.mainModelGroupBox)
        self.epochsLabel.setGeometry(QtCore.QRect(140, 30, 71, 16))
        self.epochsLabel.setStyleSheet("#epochsLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.epochsLabel.setObjectName("epochsLabel")
        self.TrainImagesSpin = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.TrainImagesSpin.setGeometry(QtCore.QRect(250, 120, 62, 22))
        self.TrainImagesSpin.setToolTip("")
        self.TrainImagesSpin.setDecimals(0)
        self.TrainImagesSpin.setMinimum(1.0)
        self.TrainImagesSpin.setMaximum(9999.0)
        self.TrainImagesSpin.setProperty("value", 12.0)
        self.TrainImagesSpin.setObjectName("TrainImagesSpin")
        self.TrainImages = QtWidgets.QLabel(self.mainModelGroupBox)
        self.TrainImages.setGeometry(QtCore.QRect(140, 120, 71, 16))
        self.TrainImages.setStyleSheet("#TrainImages{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.TrainImages.setObjectName("TrainImages")
        self.ValImagesSpin = QtWidgets.QDoubleSpinBox(self.mainModelGroupBox)
        self.ValImagesSpin.setGeometry(QtCore.QRect(250, 150, 62, 22))
        self.ValImagesSpin.setToolTip("")
        self.ValImagesSpin.setDecimals(0)
        self.ValImagesSpin.setMinimum(1.0)
        self.ValImagesSpin.setMaximum(9999.0)
        self.ValImagesSpin.setProperty("value", 12.0)
        self.ValImagesSpin.setObjectName("ValImagesSpin")
        self.ValidationImages = QtWidgets.QLabel(self.mainModelGroupBox)
        self.ValidationImages.setGeometry(QtCore.QRect(140, 150, 91, 16))
        self.ValidationImages.setStyleSheet("#ValidationImages{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.ValidationImages.setObjectName("ValidationImages")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(70, 520, 75, 31))
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
        self.LogoName = QtWidgets.QLabel(self.centralwidget)
        self.LogoName.setGeometry(QtCore.QRect(40, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setItalic(True)
        self.LogoName.setFont(font)
        self.LogoName.setObjectName("LogoName")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(120, 0, 221, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogoLabel.sizePolicy().hasHeightForWidth())
        self.LogoLabel.setSizePolicy(sizePolicy)
        self.LogoLabel.setStyleSheet("#LogoLabel{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Logo.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.LogoLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LogoLabel.setObjectName("LogoLabel")
        self.HelpButton = QtWidgets.QPushButton(self.centralwidget)
        self.HelpButton.setGeometry(QtCore.QRect(0, 520, 31, 31))
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
        self.ClassTypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ClassTypeCombo.setGeometry(QtCore.QRect(230, 240, 121, 22))
        self.ClassTypeCombo.setObjectName("ClassTypeCombo")
        self.ClassTypeCombo.addItem("")
        self.ClassTypeCombo.addItem("")
        self.ClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClassLabel.setGeometry(QtCore.QRect(150, 240, 71, 16))
        self.ClassLabel.setStyleSheet("#ClassLabel{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.ClassLabel.setObjectName("ClassLabel")
        self.ModelType = QtWidgets.QLabel(self.centralwidget)
        self.ModelType.setGeometry(QtCore.QRect(150, 210, 71, 16))
        self.ModelType.setStyleSheet("#ModelType{\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"\n"
"")
        self.ModelType.setObjectName("ModelType")
        self.ClassTypeCombo_2 = QtWidgets.QComboBox(self.centralwidget)
        self.ClassTypeCombo_2.setGeometry(QtCore.QRect(230, 210, 121, 22))
        self.ClassTypeCombo_2.setObjectName("ClassTypeCombo_2")
        self.ClassTypeCombo_2.addItem("")
        self.ClassTypeCombo_2.addItem("")
        self.trainModelButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainModelButton.setGeometry(QtCore.QRect(360, 520, 71, 31))
        self.trainModelButton.setStyleSheet("#trainModelButton{\n"
"background-color: transparent;\n"
"border-image: url(Gui-pngs/Train_up.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#trainModelButton:pressed\n"
"{\n"
"   border-image: url(Gui-pngs/Train_down.png);\n"
"}\n"
"\n"
"")
        self.trainModelButton.setText("")
        self.trainModelButton.setObjectName("trainModelButton")
        self.ClassTypeCombo.raise_()
        self.LogoLabel.raise_()
        self.BackButton.raise_()
        self.ClassLabel.raise_()
        self.ClassTypeCombo_2.raise_()
        self.HelpButton.raise_()
        self.ModelType.raise_()
        self.LogoName.raise_()
        self.mainModelGroupBox.raise_()
        self.trainModelButton.raise_()
        HyperparametersPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HyperparametersPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 26))
        self.menubar.setObjectName("menubar")
        HyperparametersPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HyperparametersPage)
        self.statusbar.setObjectName("statusbar")
        HyperparametersPage.setStatusBar(self.statusbar)

        self.retranslateUi(HyperparametersPage)
        QtCore.QMetaObject.connectSlotsByName(HyperparametersPage)

    def retranslateUi(self, HyperparametersPage):
        _translate = QtCore.QCoreApplication.translate
        HyperparametersPage.setWindowTitle(_translate("HyperparametersPage", "Hyperparameters"))
        self.mainModelGroupBox.setTitle(_translate("HyperparametersPage", "Model"))
        self.learningRateLabel.setText(_translate("HyperparametersPage", "Learning rate"))
        self.epochsLabel_2.setText(_translate("HyperparametersPage", "Training Batch size"))
        self.ValBatchLabel.setText(_translate("HyperparametersPage", "Validation Batch size"))
        self.L1RegularizationLabel.setText(_translate("HyperparametersPage", "L1 Regularization"))
        self.epochsLabel.setText(_translate("HyperparametersPage", "Epochs"))
        self.TrainImages.setText(_translate("HyperparametersPage", "#Train Images"))
        self.ValidationImages.setText(_translate("HyperparametersPage", "#Validation Images"))
        self.LogoName.setText(_translate("HyperparametersPage", "<html><head/><body><p><span style=\" font-size:24pt; color:#00009e;\">Anti Fraud Damage Detector</span></p></body></html>"))
        self.LogoLabel.setText(_translate("HyperparametersPage", "<html><head/><body><p><br/></p></body></html>"))
        self.HelpButton.setToolTip(_translate("HyperparametersPage", "<html><head/><body><p>Click here for help</p></body></html>"))
        self.ClassTypeCombo.setCurrentText(_translate("HyperparametersPage", "Damage, Whole"))
        self.ClassTypeCombo.setItemText(0, _translate("HyperparametersPage", "Damage, Whole"))
        self.ClassTypeCombo.setItemText(1, _translate("HyperparametersPage", "Front, Rear, Side"))
        self.ClassLabel.setText(_translate("HyperparametersPage", "Training Classes"))
        self.ModelType.setText(_translate("HyperparametersPage", "New model?"))
        self.ClassTypeCombo_2.setCurrentText(_translate("HyperparametersPage", "Yes-New model"))
        self.ClassTypeCombo_2.setItemText(0, _translate("HyperparametersPage", "Yes-New model"))
        self.ClassTypeCombo_2.setItemText(1, _translate("HyperparametersPage", "No-Continue training"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HyperparametersPage = QtWidgets.QMainWindow()
    ui = Ui_HyperparametersPage()
    ui.setupUi(HyperparametersPage)
    HyperparametersPage.show()
    sys.exit(app.exec_())
