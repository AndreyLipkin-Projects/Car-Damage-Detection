import sys
from typing import re

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.uic import loadUi

import Results
import UploadImage_Controller
from Predict import Prediction

ImagePath = ""


class ResultsPage(QMainWindow, Results.Ui_ResultsWindow):
    ImagePath = ""

    def __init__(self, fname, parent=None):
        super(ResultsPage, self).__init__(parent)
        # loadUi('Results.ui', self)
        self.ImagePath = fname
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.FurtherClassButton.clicked.connect(self.NextClass)
        self.BackButton.hide()
        self.ImagePath=fname
        pixmap = QPixmap(self.ImagePath)
        pixmap = pixmap.scaled(331, 191)
        self.DamagCarPicLabel.setPixmap(pixmap)

        #self.DamageTypeLabel.setText(str(Prediction('Two_Classes', self.ImagePath)))
        self.DamageSwitch(self.ImagePath)

    def DamageSwitch(self,ImagePath):
        Preds = Prediction('Two_Classes', ImagePath)
        predes= str(Preds).replace("[", "").replace("]", "")
        predes=str(predes).split(" ")

        if float(predes[0]) > 0.7:
            test=predes[0]
            self.DamageTypeLabel.setText("Vehicle Damaged: " + str(float(test)*100) + "%")
        elif float(predes[1]) > 0.7:
            self.DamageTypeLabel.setText("Vehicle Whole: " + str( predes[1]) + "%")
            self.FurtherClassButton.hide()
        else :
            self.DamageTypeLabel.setText("Unable to calculate")

    def NextClass(self):
        Preds = Prediction('Three_Classes', self.ImagePath)
        predes = str(Preds).replace("[", "").replace("]", "")
        predes = str(predes).split(" ")
        print(predes)

    def closeAndReturn(self):
        self.close()
        self.parent().show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = ResultsPage(UploadImage_Controller.ImagePath)
    menuWindow.show()
    sys.exit(app.exec_())
