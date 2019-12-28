import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from Results_Controller import ResultsPage


class UploadImagePage(QMainWindow):

    def __init__(self,parent=None):
        super(UploadImagePage, self).__init__(parent)
        loadUi('Upload_image.ui',self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.DamageclassificationButton.clicked.connect(self.getdamageclass)

    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def getdamageclass(self):
        self.mainmenu_page = ResultsPage(self)
        self.mainmenu_page.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = UploadImagePage()
    menuWindow.show()
    sys.exit(app.exec_())