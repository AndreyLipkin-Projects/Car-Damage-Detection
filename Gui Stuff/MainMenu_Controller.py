import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from Settings_Controller import SettingsPage
from UploadImage_Controller import UploadImagePage


class MainMenuPage(QMainWindow):

    def __init__(self,parent=None):
        super(MainMenuPage, self).__init__(parent)
        loadUi('MainMenu.ui',self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.TrainButton.clicked.connect(self.train)
        self.LocalizationButton.clicked.connect(self.damageclass)

    def closeAndReturn(self):
        self.parent().show()
        self.close()


    def train(self):
        self.settings_page = SettingsPage(self)
        self.settings_page.show()
        self.hide()

    def damageclass(self):
        self.Upload_page = UploadImagePage(self)
        self.Upload_page.show()
        self.hide()

    def display_error_message(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = MainMenuPage()
    menuWindow.show()
    sys.exit(app.exec_())

