import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Login import Ui_LoginWindow
from test2 import Ui_Form


class LoginConfig(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(LoginConfig, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # go on setting up your handlers like:
        # self.ui.okButton.clicked.connect(function_name)
        # etc...

def main():
    app = QtGui.QApplication(sys.argv)
    w = LoginConfig()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()