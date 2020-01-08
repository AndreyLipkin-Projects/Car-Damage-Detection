import os
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import Upload_image
from Predict import *
from Results_Controller import *

ImagePath=""

class UploadImagePage(QMainWindow,Upload_image.Ui_UploadImagewindow):


    def __init__(self,parent=None):
        super(UploadImagePage, self).__init__(parent)
        #loadUi('Upload_image.ui',self)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.DamageclassificationButton.clicked.connect(self.getdamageclass)
        self.UploadButton.clicked.connect(self.uploadimage)

    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def uploadimage(self):
        try:
            os.makedirs("Prediction_Images")
        except FileExistsError:
            # directory already exists
            pass

        ImagePath,_filter = QFileDialog.getOpenFileName(self, 'Open file',
                                            'C:/', "Image files (*.jpg *png *.jpeg)")
        self.FilenameLabel.setText(ImagePath)
        #print(Prediction('Two_Classes', fname ))

    def getPath(self):
        return self.FilenameLabel.text()

    def getdamageclass(self):
        self.mainmenu_page = ResultsPage(self.FilenameLabel.text())
        self.mainmenu_page.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = UploadImagePage()
    menuWindow.show()
    sys.exit(app.exec_())