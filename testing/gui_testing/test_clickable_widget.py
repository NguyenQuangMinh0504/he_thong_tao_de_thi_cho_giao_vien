import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame, QLabel


def foo(*arg, **kwargs):
    print("Bar")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Frame = QFrame()
    label = QLabel(Frame)
    label.mousePressEvent = foo
    label.setText("Label")
    Frame.show()
    sys.exit(app.exec_())
