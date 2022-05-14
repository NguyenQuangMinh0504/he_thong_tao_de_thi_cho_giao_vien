import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QApplication, QFrame


class StudentLogin(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.btn = QPushButton('Student Login', self)
        self.btn.move(20, 50)
        self.btn.clicked.connect(self.click)

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Student log in screen')
        self.show()

    def click(self):
        print("Foo")


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Login screen')
        btn = QPushButton('Student Login', self)
        btn.setToolTip('This will log you in as a student')
        btn.move(10, 50)
        btn.clicked.connect(self.student_log)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Log in screen')
        self.show()

    def student_log(self):
        self.widget = StudentLogin()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())