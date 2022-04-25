# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating a radio button
        self.button1 = QRadioButton("Button1", self)

        # setting geometry of radio button
        self.button1.setGeometry(200, 150, 100, 40)

        # creating push button
        self.push = QPushButton("Change the text ", self)

        # setting geometry of push button
        self.push.setGeometry(200, 200, 100, 40)

        # connect push button to method
        self.push.clicked.connect(self.changeName)

    # creating changeName method
    def changeName(self):
        # setting new text to radio button
        self.button1.setText("New Name")

if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())