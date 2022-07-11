from PyQt5 import QtWidgets

from gui.gui_main_screen.main_screen import Ui_main_screen_frame

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_main_screen_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())