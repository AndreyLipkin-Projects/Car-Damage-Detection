import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from ChangeClassifier_Controller import ChangeClassPage
from Hyperparameters_Controller import HyperparametersPage
from Settings import Ui_SettingsWindow
from TrainingGraph_Controller import TrainGraphPage


class SettingsPage(QMainWindow,Ui_SettingsWindow):

    def __init__(self,parent=None):
        super(SettingsPage, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.HyperparametersButton.clicked.connect(self.hyper)
        self.ChangeClassButton.hide()
        self.GraphButton.clicked.connect(self.trainGraph)
        self.HelpButton.hide()

    def closeAndReturn(self):
        self.hide()
        self.parent().show()

    #Move to training graphs page
    def trainGraph(self):
        self.mainmenu_page = TrainGraphPage(self)
        self.mainmenu_page.show()
        self.hide()

    #Move to hyperparameters page
    def hyper(self):
        self.mainmenu_page = HyperparametersPage(self)
        self.mainmenu_page.show()
        self.hide()

    def closeEvent(self, event):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    menuWindow = SettingsPage()
    menuWindow.show()
    sys.exit(app.exec_())