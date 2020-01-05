import os
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from Hyperparameters import Ui_HyperparametersPage
from modelTraining import modelTrainer


class HyperparametersPage(QMainWindow, Ui_HyperparametersPage):


    def __init__(self, parent=None):
        super(HyperparametersPage, self).__init__(parent)
        # loadUi('Hyperparameters.ui',self)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.trainModelButton.clicked.connect(self.trainSystem)
        self.HelpButton.clicked.connect(self.show_help_info)
        Path = ".\PycharmProjects\Test\Init.ini"
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, Path)

        self.Readparametrs("C:/Users/alipkine/PycharmProjects/Test/Init.ini")

    def trainSystem(self):
        Train_Type = ""

        with open("C:/Users/alipkine/PycharmProjects/Test/Init.ini") as f:
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

        with open("C:/Users/alipkine/PycharmProjects/Test/Init.ini", 'w') as output:
            for row in lines:
                output.write(str(row))


        modelTrainer(Train_Type)

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
            f.close()

    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def slider_callback(self):
        percentage = self.trainingValidationSlider.value()
        percentage_text = str(percentage) + "%"
        self.trainingPercentageLineEdit.setText(percentage_text)
        percentage = 100 - percentage
        percentage_text = str(percentage) + "%"
        self.validationPercentageLineEdit.setText(percentage_text)

    def show_help_info(self):
        QMessageBox.about(self,"Information", "In this window you setup the needed values the system needs in order for you to be able to train a new or an existing model")
      #  self.display_information_message("In this window you setup the needed values the system needs in order for you to be able to train a new or an existing model")

    def display_information_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Information")
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = HyperparametersPage()
    menuWindow.show()
    sys.exit(app.exec_())
