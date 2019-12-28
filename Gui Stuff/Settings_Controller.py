import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from ChangeClassifier_Controller import ChangeClassPage
from Hyperparameters_Controller import HyperparametersPage
from TrainingGraph_Controller import TrainGraphPage


class SettingsPage(QMainWindow):

    def __init__(self,parent=None):
        super(SettingsPage, self).__init__(parent)
        loadUi('Settings.ui',self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.HyperparametersButton.clicked.connect(self.hyper)
        self.ChangeClassButton.clicked.connect(self.changeClass)
        self.GraphButton.clicked.connect(self.trainGraph)

    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def trainGraph(self):
        self.mainmenu_page = TrainGraphPage(self)
        self.mainmenu_page.show()
        self.hide()

    def changeClass(self):
        self.mainmenu_page = ChangeClassPage(self)
        self.mainmenu_page.show()
        self.hide()

    def hyper(self):
        self.mainmenu_page = HyperparametersPage(self)
        self.mainmenu_page.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = SettingsPage()
    menuWindow.show()
    sys.exit(app.exec_())