# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame
from gui_main_screen.pop_up import Ui_pop_up
from gui_quan_li_mon_hoc.quan_li_mon_hoc import Ui_quan_ly_mon_hoc_frame
from de_thi.quan_li_de_thi import Ui_quan_li_de_thi_frame
from soan_cau_hoi.soan_cau_hoi_ver_trinh_thanh_trung import Ui_soan_cau_hoi_frame
from database.Subject.subject_access import get_subject_id


class Ui_giao_dien_chinh_frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(317, 218)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.question_manage_button = QtWidgets.QPushButton(Frame)
        self.question_manage_button.setGeometry(QtCore.QRect(10, 30, 291, 41))
        self.question_manage_button.setObjectName("question_manage_button")
        self.exam_manage_button = QtWidgets.QPushButton(Frame)
        self.exam_manage_button.setGeometry(QtCore.QRect(10, 90, 291, 41))
        self.exam_manage_button.setObjectName("exam_manage_button")
        self.subject_manage_button = QtWidgets.QPushButton(Frame)
        self.subject_manage_button.setGeometry(QtCore.QRect(10, 150, 291, 41))
        self.subject_manage_button.setObjectName("subject_manage_button")

        self.question_manage_button.clicked.connect(self.question_manage_button_click)
        self.exam_manage_button.clicked.connect(self.exam_manage_button_click)
        self.subject_manage_button.clicked.connect(self.subject_manage_button_click)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.question_manage_button.setText(_translate("Frame", "Soạn câu hỏi"))
        self.exam_manage_button.setText(_translate("Frame", "Xây dựng đề thi"))
        self.subject_manage_button.setText(_translate("Frame", "Quản lý môn học"))

    def question_manage_button_click(self):
        self.pop_up_frame = QFrame()
        self.ui_pop_up = Ui_pop_up()
        self.ui_pop_up.setupUi(self.pop_up_frame)
        self.pop_up_frame.show()
        self.ui_pop_up.ok_button.clicked.connect(self.question_manage_pop_up_ok_button_click)

    def question_manage_pop_up_ok_button_click(self):
        self.pop_up_frame.close()
        self.exam_manage_frame = QFrame()
        Ui_soan_cau_hoi_frame().setupUi(self.exam_manage_frame,
                                        get_subject_id(self.ui_pop_up.danh_sach_mon_hoc_combo_box.currentText()))
        self.exam_manage_frame.show()

    def exam_manage_button_click(self):
        self.pop_up_frame = QFrame()
        self.ui_pop_up = Ui_pop_up()
        self.ui_pop_up.setupUi(self.pop_up_frame)
        self.pop_up_frame.show()
        self.ui_pop_up.ok_button.clicked.connect(self.exam_manage_pop_up_ok_button_click)

    def exam_manage_pop_up_ok_button_click(self):
        self.exam_manage_frame = QFrame()
        Ui_quan_li_de_thi_frame().setupUi(self.exam_manage_frame,
                                          get_subject_id(self.ui_pop_up.danh_sach_mon_hoc_combo_box.currentText()))
        self.exam_manage_frame.show()
        self.pop_up_frame.close()

    def subject_manage_button_click(self):
        self.subject_manage_frame = QFrame()
        Ui_quan_ly_mon_hoc_frame().setupUi(self.subject_manage_frame)
        self.subject_manage_frame.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_giao_dien_chinh_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
