import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import Results
import UploadImage_Controller
from Predict import Prediction

ImagePath = ""
predes=""

class ResultsPage(QMainWindow, Results.Ui_ResultsWindow):


    ImagePath = ""

    def __init__(self, fname, parent=None):
        super(ResultsPage, self).__init__(parent)
        ImagePath = fname
        self.setupUi(self)
        self.ImagePath=fname
        self.threaclass=ThreadClass(ImagePath)
        self.threaclass.finished.connect(self.ShowButtons)
        self.threaclass.start()
        self.TwoClassButton.clicked.connect(self.Damage2class)
        self.ThreeClassButton.clicked.connect(self.Damage3class)
        self.BackButton.hide()
        self.HelpButton.hide()
        self.DamageText.hide()
        self.ThreeClassButton.hide()
        self.TwoClassButton.hide()
        pixmap = QPixmap(self.ImagePath)
        pixmap = pixmap.scaled(331, 191)
        self.DamagCarPicLabel.setPixmap(pixmap)
        movie = QMovie("Gui-pngs/LoadingGif.gif")
        self.GifLabel.setMovie(movie)
        movie.start()

    #Enable buttons after classification
    def ShowButtons(self):
        self.GifLabel.hide()
        self.Damage2class()


    #Show info for the two class classification
    def Damage2class(self):
        self.TwoClassButton.hide()
        self.ThreeClassButton.show()
        predes=ThreadClass.TwoClassPred
        if float(predes[0][0]) > 0.8:
            test=predes[0][0]
            test='{0:0.2f}'.format(100*float(test))
            self.DamageText.setText("Vehicle Damaged: " + test + "%")
        elif (float(predes[0][0]) < 0.8) and (float(predes[0][1]) <float(predes[0][0])): #damaged but not enough to pass the threshold
            self.DamageText.setText("Vehicle is damaged but doesn't pass for our detection threshold")
        elif float(predes[0][1]) > 0.8:
            self.DamageText.setText("Vehicle Whole: " + '{0:0.2f}'.format(100*float(predes[0][1])) + "%")
            self.ThreeClassButton.hide()
        elif (float(predes[0][1]) < 0.8) and (float(predes[0][0]) <float(predes[0][1])) :
            self.DamageText.setText("Vehicle is whole but doesn't pass for our detection threshold")
        self.DamageText.show()

    # Show info for the three class classification
    def Damage3class(self):
        self.TwoClassButton.show()
        self.ThreeClassButton.hide()
        Preds = ThreadClass.ThreeClassPred
        front=Preds[0][0]
        rear=Preds[0][1]
        side=Preds[0][2]
        self.DamageText.setText("Damage classification: <br>" + "Front = "+'{0:0.2f}'.format(100*float(front)) + "%<br>" + "Rear =  "+'{0:0.2f}'.format(100*float(rear)) + "%<br>" + "Side =  "+'{0:0.2f}'.format(100*float(side)) + "%<br>")
        self.DamageText.show()

    #Help info
    def show_help_info(self):
        QMessageBox.about(self,"Information", "In this window you setup the needed values the system needs in order for you to be able to train a new or an existing model")

#Thread for classification process
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

    def closeEvent(self, event):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = ResultsPage(UploadImage_Controller.ImagePath)
    menuWindow.show()
    sys.exit(app.exec_())
