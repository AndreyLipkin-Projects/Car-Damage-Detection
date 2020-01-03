import os
import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from Hyperparameters import Ui_HyperparametersPage


class HyperparametersPage(QMainWindow,Ui_HyperparametersPage):

    def __init__(self,parent=None):
        super(HyperparametersPage, self).__init__(parent)
        #loadUi('Hyperparameters.ui',self)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.trainingValidationSlider.valueChanged.connect(self.slider_callback)

        Path = ".\PycharmProjects\Test\Init.ini"
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, Path)


        f = open("C:/Users/alipkine/PycharmProjects/Test/Init.ini", "r")
        for x in f:
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