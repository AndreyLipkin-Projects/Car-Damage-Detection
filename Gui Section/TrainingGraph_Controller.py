import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from Training_graph import Ui_TrainGraphWindow


class TrainGraphPage(QMainWindow,Ui_TrainGraphWindow):

    def __init__(self,parent=None):
        super(TrainGraphPage, self).__init__(parent)
        #loadUi('Training_graph.ui',self)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.HelpButton.clicked.connect(self.show_help_info)
        self.comboBox.currentIndexChanged.connect(self.ModelGraphSwitcher)

        self.Fill2classGraphs()

    def ModelGraphSwitcher(self):
        if 0==self.comboBox.currentIndex():
            self.Fill2classGraphs()
        elif 1==self.comboBox.currentIndex():
            self.Fill3classGraphs()

    def show_help_info(self):
        QMessageBox.about(self,"Information", "In this window, according to the model chosen, the coresponding graphs of Accuracy and Loss will be presented.<br> "
                                              "If you place a new model to be a default for the system, the changed images will be presented.")

    def Fill3classGraphs(self):

        AccPath = "checkpoints/Three_Classes/Three_Classes_Accuracy.jpeg"
        LssPath = "checkpoints/Three_Classes/THree_Classes_Loss.jpeg"
        THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        AccuracyPath = os.path.join(THIS_FOLDER, AccPath)
        LossPath = os.path.join(THIS_FOLDER, LssPath)
        pixmap = QPixmap(AccuracyPath)
        pixmap = pixmap.scaled(611, 401)
        self.LossGraphLabel.setPixmap(pixmap)
        pixmap = QPixmap(LossPath)
        pixmap = pixmap.scaled(611, 401)
        self.AccGraphLabel.setPixmap(pixmap)

    def Fill2classGraphs(self):

        AccPath = "checkpoints/Two_Classes/Two_Classes_Accuracy.jpeg"
        LssPath = "checkpoints/Two_Classes/Two_Classes_Loss.jpeg"
        THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        AccuracyPath = os.path.join(THIS_FOLDER, AccPath)
        LossPath = os.path.join(THIS_FOLDER, LssPath)
        pixmap = QPixmap(AccuracyPath)
        pixmap = pixmap.scaled(611, 401)
        self.LossGraphLabel.setPixmap(pixmap)
        pixmap = QPixmap(LossPath)
        pixmap = pixmap.scaled(611, 401)
        self.AccGraphLabel.setPixmap(pixmap)


    def closeAndReturn(self):
        self.close()
        self.parent().show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = TrainGraphPage()
    menuWindow.show()
    sys.exit(app.exec_())