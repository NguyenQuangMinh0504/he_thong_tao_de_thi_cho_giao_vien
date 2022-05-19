from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('', self)
        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon("../../canvas_background.jpeg"))
        self.button.setIconSize(QtCore.QSize(200,200))
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())