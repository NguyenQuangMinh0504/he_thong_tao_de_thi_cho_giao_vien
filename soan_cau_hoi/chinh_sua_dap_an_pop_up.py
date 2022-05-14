from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chinh_sua_dap_an_pop_up(object):
    def setupUi(self, Frame):
        self.Frame = Frame
        Frame.setObjectName("Frame")
        Frame.resize(244, 166)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dap_an_label = QtWidgets.QLabel(Frame)
        self.dap_an_label.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.dap_an_label.setObjectName("dap_an_label")
        self.dap_an_dung_text_edit = QtWidgets.QTextEdit(Frame)
        self.dap_an_dung_text_edit.setGeometry(QtCore.QRect(30, 40, 171, 31))
        self.dap_an_dung_text_edit.setObjectName("dap_an_dung_text_edit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 70, 111, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.dap_an_check_box_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.dap_an_check_box_layout.setContentsMargins(0, 0, 0, 0)
        self.dap_an_check_box_layout.setObjectName("dap_an_check_box_layout")
        self.dap_an_check_box = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.dap_an_check_box.setText("")
        self.dap_an_check_box.setObjectName("dap_an_check_box")
        self.dap_an_check_box_layout.addWidget(self.dap_an_check_box)
        self.dap_an_dung_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.dap_an_dung_label.setObjectName("dap_an_dung_label")
        self.dap_an_check_box_layout.addWidget(self.dap_an_dung_label)

        self.ok_button = QtWidgets.QPushButton(Frame)
        self.ok_button.setGeometry(QtCore.QRect(70, 110, 113, 32))
        self.ok_button.setObjectName("ok_button")
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.dap_an_label.setText(_translate("Frame", "Đáp án"))
        self.dap_an_dung_label.setText(_translate("Frame", "Đáp án đúng"))
        self.ok_button.setText(_translate("Frame", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_chinh_sua_dap_an_pop_up()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
