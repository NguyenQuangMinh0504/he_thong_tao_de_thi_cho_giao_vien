from PyQt5 import QtWidgets

from gui_main_screen.main_screen import Ui_giao_dien_chinh_frame

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_giao_dien_chinh_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())