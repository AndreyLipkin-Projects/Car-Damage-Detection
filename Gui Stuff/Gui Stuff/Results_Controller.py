import sys
import threading
from typing import re

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.uic import loadUi

import Results
import UploadImage_Controller
from Predict import Prediction

ImagePath = ""
predes=""

class ResultsPage(QMainWindow, Results.Ui_ResultsWindow):
    ImagePath = ""

    def __init__(self, fname, parent=None):
        super(ResultsPage, self).__init__(parent)
        # loadUi('Results.ui', self)

        ImagePath = fname
        self.setupUi(self)
        self.ImagePath=fname
        self.threaclass=ThreadClass(ImagePath)
        self.threaclass.finished.connect(self.Damage2class)
        self.threaclass.start()
        self.FurtherClassButton.clicked.connect(self.Damage3class)
        self.BackButton.clicked.connect(self.back)
        #self.connect(self.threaclass,QtCore.PYQT_SIGNAL('test'),self.DamageSwitch())
        self.DamageText.hide()
        self.FurtherClassButton.hide()
        pixmap = QPixmap(self.ImagePath)
        pixmap = pixmap.scaled(331, 191)
        self.DamagCarPicLabel.setPixmap(pixmap)
        movie = QMovie("Gui-pngs/LoadingGif.gif")
        self.GifLabel.setMovie(movie)
        movie.start()
        #self.DamageTypeLabel.setText(str(Prediction('Two_Classes', self.ImagePath)))
        #self.DamageSwitch()


    def Damage2class(self):
        self.threaclass.terminate()
        self.GifLabel.hide()
        self.DamageText.show()
        predes=ThreadClass.TwoClassPred
        if float(predes[0][0]) > 0.7:
            test=predes[0][0]
            test='{0:0.2f}'.format(100*float(test))
            self.DamageText.setText("Vehicle Damaged: " + test + "%")
            self.FurtherClassButton.show()
        elif float(predes[0][1]) > 0.7:
            self.DamageText.setText("Vehicle Whole: " + str( predes[0][1]) + "%")
        else :
            self.DamageText.setText("Unable to calculate")

    def Damage3class(self):
        self.DamageText.hide()
        self.FurtherClassButton.hide()
        self.GifLabel.show()
        Preds = ThreadClass.ThreeClassPred
        self.GifLabel.hide()
        front=Preds[0][0]
        rear=Preds[0][1]
        side=Preds[0][2]
        self.DamageText.setText("Damage classification: <br>" + "Front = "+'{0:0.2f}'.format(100*float(front)) + "%<br>" + "Rear = "+'{0:0.2f}'.format(100*float(rear)) + "%<br>" + "Side = "+'{0:0.2f}'.format(100*float(side)) + "%<br>")
        self.FurtherClassButton.hide()
        self.DamageText.show()


    def back(self):
        self.close()
        from MainMenu_Controller import MainMenuPage
        self.mainmenu_page = MainMenuPage(self)
        self.mainmenu_page.show()


    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def damageclass(self):
        self.Upload_page = UploadImage_Controller.UploadImagePage(self)
        self.Upload_page.show()
        self.hide()

class ThreadClass(QtCore.QThread):

    global ImagePath
    PredesResult=QtCore.pyqtSignal(list)
    TwoClassPred=""
    ThreeClassPred = ""
    def __init__(self,ImagePath, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.ImagePath=ImagePath

    def run(self):
        Preds2 = Prediction('Two_Classes', self.ImagePath)
        Preds3 = Prediction('Three_Classes', self.ImagePath)
        ThreadClass.TwoClassPred=Preds2
        ThreadClass.ThreeClassPred=Preds3

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = ResultsPage(UploadImage_Controller.ImagePath)
    menuWindow.show()
    sys.exit(app.exec_())
