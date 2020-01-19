from PyQt5.QtWidgets import QFileDialog
import Upload_image
from Predict import *
from Results_Controller import *

ImagePath=""

class UploadImagePage(QMainWindow,Upload_image.Ui_UploadImagewindow):


    def __init__(self,parent=None):
        super(UploadImagePage, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.closeAndReturn)
        self.BackButton.hide()
        self.DamageclassificationButton.clicked.connect(self.getdamageclass)
        self.HelpButton.clicked.connect(self.show_help_info)
        self.UploadButton.clicked.connect(self.uploadimage)
        self.DamageclassificationButton.hide()


    def closeAndReturn(self):
        self.hide()
        self.parent().show()

    #The upload image function
    def uploadimage(self):
        #A check for the existence of a Prediction images folder
        try:
            os.makedirs("Prediction_Images")
        except FileExistsError:
            # directory already exists
            pass
        #Save the location of a selected image
        ImagePath,_filter = QFileDialog.getOpenFileName(self, 'Open file','C:/', "Image files (*.jpg *png *.jpeg)")

        #Check if no image was selected
        if ImagePath=="":
            self.display_error_message("No picture selected, Please select a picture")
        #Set path location of the selected image and enable further page buttons
        elif ImagePath!="":
            self.FilenameLabel.setText(ImagePath)
            self.DamageclassificationButton.show()

    #Move to results page
    def getdamageclass(self):
        self.mainmenu_page = ResultsPage(self.FilenameLabel.text())
        self.mainmenu_page.show()
        self.hide()

    #Help information
    def show_help_info(self):
        QMessageBox.about(self,"Information", "In this window you will get a classification result for your uploaded image, "
                                              "also, if your image passes a detection threshold ( currently at 80% ), press 'Next Classification Step' to get "
                                              "a currently incomplete model's 3-class classification")

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
    #app.setQuitOnLastWindowClosed(False)
    menuWindow = UploadImagePage()
    menuWindow.show()
    sys.exit(app.exec_())