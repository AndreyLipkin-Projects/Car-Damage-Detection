import os
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from Hyperparameters import Ui_HyperparametersPage
from modelTraining import modelTrainer

class HyperparametersPage(QMainWindow, Ui_HyperparametersPage):

    def __init__(self, parent=None):
        super(HyperparametersPage, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.trainModelButton.clicked.connect(self.trainSystem)
        self.GifLabel.hide()
        self.HelpButton.clicked.connect(self.show_help_info)
        Path = "./Init.ini"
        THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        my_file = os.path.join(THIS_FOLDER, Path)
        self.Readparametrs(my_file)
        movie = QMovie("Gui-pngs/LoadingGif.gif")
        self.GifLabel.setMovie(movie)
        movie.start()

    #Update the init file values from the users input and start system training
    def trainSystem(self):
        self.trainModelButton.hide()
        self.BackButton.hide()
        self.GifLabel.show()
        Train_Type = ""
        Path = "./Init.ini"
        THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        my_file = os.path.join(THIS_FOLDER, Path)
        with open(my_file) as f:
            lines = f.readlines()
            counter = 0
            for x in lines:
                if "New_Model=" in x:
                    if "Yes-New model" == self.ClassTypeCombo_2.currentText():
                        lines[counter] = ("New_Model=New" + '\n')
                    elif "No-Continue training" == self.ClassTypeCombo_2.currentText():
                        lines[counter] = ("New_Model=Old" + '\n')
                if "Class_List_From_Gui=" in x:
                    if "Damage, Whole" == self.ClassTypeCombo.currentText():
                        lines[counter] = ("Class_List_From_Gui=Two_Classes" + '\n')
                        Train_Type="Two_Classes"
                    elif "Front, Rear, Side" == self.ClassTypeCombo.currentText():
                        lines[counter] = ("Class_List_From_Gui=Three_Classes" + '\n')
                        Train_Type = "Three_Classes"
                if "Epocs_from_Gui=" in x:
                    lines[counter] = ("Epocs_from_Gui=" + str(int(self.epochsSpinBox.value())) + '\n')
                if "learningRate_From_Gui" in x:
                    lines[counter] = ("learningRate_From_Gui=" + str(float(self.LearningRateSpinBox.value())) + '\n')
                if "regularizationRate_From_Gui" in x:
                    lines[counter] = ("regularizationRate_From_Gui=" + str(float(self.L1RegularizationSpinBox.value())) + '\n')
                if "Train_BatchSize_From_Gui" in x:
                    lines[counter] = ("Train_BatchSize_From_Gui=" + str(int(self.TrainBatchSizeSpinBox.value())) + '\n')
                if "Val_BatchSize_From_Gui" in x:
                    lines[counter] = ("Val_BatchSize_From_Gui=" + str(int(self.ValBatchSizeSpinBox.value())) + '\n')
                counter+=1
        f.close()
        Path = "./Init.ini"
        THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        my_file = os.path.join(THIS_FOLDER, Path)
        with open(my_file, 'w') as output:
            for row in lines:
                output.write(str(row))

        self.threaclass = ThreadClass(Train_Type)
        self.threaclass.finished.connect(self.TrainDone)
        self.threaclass.start()

    #Read values from the init file to present to the user
    def Readparametrs(self, path):

        with open(path) as f:
            lines = f.readlines()
            for x in lines:
                if "Epocs_from_Gui=" in x:
                    self.epochsSpinBox.setValue(int(x[15:]))
                if "learningRate_From_Gui" in x:
                    self.LearningRateSpinBox.setValue(float(x[22:]))
                if "regularizationRate_From_Gui" in x:
                    self.L1RegularizationSpinBox.setValue(float(x[28:]))
                if "Train_BatchSize_From_Gui" in x:
                    self.TrainBatchSizeSpinBox.setValue(int(x[25:]))
                if "Val_BatchSize_From_Gui" in x:
                    self.ValBatchSizeSpinBox.setValue(int(x[23:]))
                if "numTrain_From_Gui" in x:
                    self.TrainImagesSpin.setValue(int(x[18:]))
                if "numVal_From_Gui" in x:
                    self.ValImagesSpin.setValue(int(x[16:]))

            self.ValBatchSizeSpinBox.setMaximum(self.ValImagesSpin.value())
            self.ValBatchSizeSpinBox.setToolTip("Choose between 1 to " + str(int(self.ValImagesSpin.value())))
            self.TrainBatchSizeSpinBox.setMaximum(self.TrainImagesSpin.value())
            self.TrainBatchSizeSpinBox.setToolTip("Choose between 1 to " + str(int(self.TrainImagesSpin.value())))
            f.close()

    def closeAndReturn(self):
        self.parent().show()
        self.hide()

    #Display when the training is done.
    def TrainDone(self):
        self.GifLabel.hide()
        self.BackButton.show()

    #Help info
    def show_help_info(self):
        QMessageBox.about(self,"Information", "In this window you setup the needed values the system needs in order for you to be able to train a new or an existing model")

    def display_information_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Information")
        msg.exec()

#Thread for system training
class ThreadClass(QtCore.QThread):

    TrainStatus = False

    def __init__(self,Train_Type, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.Train_Type=Train_Type

    def run(self):
        modelTrainer(self.Train_Type)

    def closeEvent(self, event):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = HyperparametersPage()
    menuWindow.show()
    sys.exit(app.exec_())
