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
        Path = ".\PycharmProjects\Test\Init.ini"
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, Path)

        self.Readparametrs("C:/Users/alipkine/PycharmProjects/Test/Init.ini")

    def trainSystem(self):

        with open("C:/Users/alipkine/PycharmProjects/Test/Init.ini") as f:
            lines = f.readlines()
            counter = 0
            for x in lines:
                if "Class_List_From_Gui=" in x:
                    lines[counter] = ("Class_List_From_Gui=" + str(self.ClassTypeCombo.currentText()) + '\n')
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


        modelTrainer(self.ClassTypeCombo.currentText())

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuWindow = HyperparametersPage()
    menuWindow.show()
    sys.exit(app.exec_())
