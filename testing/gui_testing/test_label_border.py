# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Label")

        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        # by default label will display at top left corner
        self.label_1 = QLabel('It is Label 1', self)

        # moving position
        self.label_1.move(100, 100)

        # setting up border
        self.label_1.setStyleSheet("border: 1px solid black;")

        # creating a label widget
        # by default label will display at top left corner
        self.label_2 = QLabel('It is Label 2', self)

        # moving position
        self.label_2.move(100, 200)

        # setting up border
        self.label_2.setStyleSheet("border: 3px solid blue;")

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())