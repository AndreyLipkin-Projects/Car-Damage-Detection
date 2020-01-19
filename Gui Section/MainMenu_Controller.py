import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from MainMenu import Ui_MainMenuWindow
from Settings_Controller import SettingsPage
from UploadImage_Controller import UploadImagePage

class MainMenuPage(QMainWindow,Ui_MainMenuWindow):

    def __init__(self,parent=None):
        super(MainMenuPage, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.TrainButton.clicked.connect(self.train)
        self.LocalizationButton.clicked.connect(self.damageclass)
        self.HelpButton.hide()

    #Go back to previuos page
    def closeAndReturn(self):
        self.parent().show()
        self.hide()

    #Move to system training page
    def train(self):
        self.settings_page = SettingsPage(self)
        self.settings_page.show()
        self.hide()

    #Move to damage classification page
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

    def closeEvent(self, event):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    menuWindow = MainMenuPage()
    menuWindow.show()
    sys.exit(app.exec_())

