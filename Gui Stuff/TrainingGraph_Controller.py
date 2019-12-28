import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

class TrainGraphPage(QMainWindow):

    def __init__(self,parent=None):
        super(TrainGraphPage, self).__init__(parent)
        loadUi('Training_graph.ui',self)
        self.BackButton.clicked.connect(self.closeAndReturn)

    def closeAndReturn(self):
        self.close()
        self.parent().show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = TrainGraphPage()
    menuWindow.show()
    sys.exit(app.exec_())