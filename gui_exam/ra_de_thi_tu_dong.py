# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ra_de_thi_tu_dong.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QPushButton, QSpinBox

from database.Exam.exam_access import get_last_exam_id
from database.Exam.exam_question_access import auto_generate_exam_on_difficulty, auto_generate_exam_on_coverage
from database.Subject.subject_access import get_subject_chapter
from gui_exam.exam import Ui_exam_frame


class Ui_ra_de_thi_tu_dong_frame(object):
    def setupUi(self, Frame, subject_id):
        self.Frame = Frame
        self.subject_id = subject_id
        Frame.setObjectName("main_screen_frame")
        Frame.resize(424, 664)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thiet_lap_theo_do_kho = QtWidgets.QWidget(Frame)
        self.thiet_lap_theo_do_kho.setGeometry(QtCore.QRect(30, 170, 271, 421))
        self.thiet_lap_theo_do_kho.setObjectName("thiet_lap_theo_do_kho")
        self.thiet_lap_do_kho_label = QtWidgets.QLabel(self.thiet_lap_theo_do_kho)
        self.thiet_lap_do_kho_label.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.thiet_lap_do_kho_label.setObjectName("thiet_lap_do_kho_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.thiet_lap_theo_do_kho)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 160, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.so_cau_de_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.so_cau_de_label.setObjectName("so_cau_de_label")
        self.horizontalLayout_3.addWidget(self.so_cau_de_label)
        self.so_cau_de_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.so_cau_de_spin_box.setObjectName("so_cau_de_spin_box")
        self.horizontalLayout_3.addWidget(self.so_cau_de_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.so_cau_vua_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.so_cau_vua_label.setObjectName("so_cau_vua_label")
        self.horizontalLayout_5.addWidget(self.so_cau_vua_label)
        self.so_cau_vua_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.so_cau_vua_spin_box.setObjectName("so_cau_vua_spin_box")
        self.horizontalLayout_5.addWidget(self.so_cau_vua_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.so_cau_kho_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.so_cau_kho_label.setObjectName("so_cau_kho_label")
        self.horizontalLayout_4.addWidget(self.so_cau_kho_label)
        self.so_cau_kho_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.so_cau_kho_spin_box.setObjectName("so_cau_kho_spin_box")
        self.horizontalLayout_4.addWidget(self.so_cau_kho_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 20, 361, 136))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dang_de_thi_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.dang_de_thi_label.setObjectName("dang_de_thi_label")
        self.horizontalLayout.addWidget(self.dang_de_thi_label)
        self.dang_de_thi_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.dang_de_thi_combo_box.setObjectName("dang_de_thi_combo_box")
        self.dang_de_thi_combo_box.addItem("")
        self.dang_de_thi_combo_box.addItem("")
        self.dang_de_thi_combo_box.addItem("")
        self.horizontalLayout.addWidget(self.dang_de_thi_combo_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hinh_thuc_thi_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.hinh_thuc_thi_label.setObjectName("hinh_thuc_thi_label")
        self.horizontalLayout_6.addWidget(self.hinh_thuc_thi_label)
        self.hinh_thuc_thi_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.hinh_thuc_thi_combo_box.setObjectName("hinh_thuc_thi_combo_box")
        self.hinh_thuc_thi_combo_box.addItem("")
        self.hinh_thuc_thi_combo_box.addItem("")
        self.horizontalLayout_6.addWidget(self.hinh_thuc_thi_combo_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.so_cau_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.so_cau_label.setObjectName("so_cau_label")
        self.horizontalLayout_2.addWidget(self.so_cau_label)
        self.so_cau_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.so_cau_spin_box.setObjectName("so_cau_spin_box")
        self.horizontalLayout_2.addWidget(self.so_cau_spin_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ra_de_thi_theo_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.ra_de_thi_theo_label.setObjectName("ra_de_thi_theo_label")
        self.horizontalLayout_7.addWidget(self.ra_de_thi_theo_label)
        self.ra_de_thi_theo_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.ra_de_thi_theo_combo_box.setObjectName("ra_de_thi_theo_combo_box")
        self.ra_de_thi_theo_combo_box.addItem("")
        self.ra_de_thi_theo_combo_box.addItem("")
        self.horizontalLayout_7.addWidget(self.ra_de_thi_theo_combo_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.tao_de_thi_button = QtWidgets.QPushButton(Frame)
        self.tao_de_thi_button.setGeometry(QtCore.QRect(140, 610, 141, 41))
        self.tao_de_thi_button.setObjectName("tao_de_thi_button")
        self.thiet_lap_tho_do_bao_phu = QtWidgets.QFrame(Frame)
        self.thiet_lap_tho_do_bao_phu.setGeometry(QtCore.QRect(30, 170, 271, 421))
        self.thiet_lap_tho_do_bao_phu.setObjectName("thiet_lap_tho_do_bao_phu")
        self.thiet_lap_do_bao_phu_label = QtWidgets.QLabel(self.thiet_lap_tho_do_bao_phu)
        self.thiet_lap_do_bao_phu_label.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.thiet_lap_do_bao_phu_label.setObjectName("thiet_lap_do_bao_phu_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.thiet_lap_tho_do_bao_phu)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 60, 164, 280))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        for i in range(get_subject_chapter(self.subject_id)):
            horizontal_layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel("Câu hỏi chương {}".format(i + 1), self.verticalLayoutWidget_3)
            horizontal_layout.addWidget(label)
            spinbox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
            spinbox.setObjectName("chuong_{}_spin_box".format(i + 1))
            horizontal_layout.addWidget(spinbox)
            self.verticalLayout_3.addLayout(horizontal_layout)

        self.ra_de_thi_theo_combo_box.currentTextChanged.connect(self.ra_de_thi_theo_combo_box_index_change)
        self.tao_de_thi_button.clicked.connect(self.tao_de_thi_button_click)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("main_screen_frame", "main_screen_frame"))
        self.thiet_lap_do_kho_label.setText(_translate("main_screen_frame", "Thiết lập độ khó"))
        self.so_cau_de_label.setText(_translate("main_screen_frame", "Số câu dễ"))
        self.so_cau_vua_label.setText(_translate("main_screen_frame", "Số câu vừa"))
        self.so_cau_kho_label.setText(_translate("main_screen_frame", "Số câu khó"))
        self.dang_de_thi_label.setText(_translate("main_screen_frame", "Dạng đề thi"))
        self.dang_de_thi_combo_box.setItemText(0, _translate("main_screen_frame", "Trắc nghiệm"))
        self.dang_de_thi_combo_box.setItemText(1, _translate("main_screen_frame", "Tự luận"))
        self.dang_de_thi_combo_box.setItemText(2, _translate("main_screen_frame", "Trắc nghiệm và tự luận"))
        self.hinh_thuc_thi_label.setText(_translate("main_screen_frame", "Hình thức"))
        self.hinh_thuc_thi_combo_box.setItemText(0,
                                                 _translate("main_screen_frame", "Trắc nghiệm và tự luận riêng biệt"))
        self.hinh_thuc_thi_combo_box.setItemText(1, _translate("main_screen_frame", "Trộn lẫn trắc nghiệm và tự luận"))
        self.so_cau_label.setText(_translate("main_screen_frame", "Số câu"))
        self.ra_de_thi_theo_label.setText(_translate("main_screen_frame", "Ra đề thi theo"))
        self.ra_de_thi_theo_combo_box.setItemText(0, _translate("main_screen_frame", "Độ khó"))
        self.ra_de_thi_theo_combo_box.setItemText(1, _translate("main_screen_frame", "Độ bao phủ"))
        self.tao_de_thi_button.setText(_translate("main_screen_frame", "Tạo đề thi"))
        self.thiet_lap_do_bao_phu_label.setText(_translate("main_screen_frame", "Thiết lập độ bao phủ"))

    def ra_de_thi_theo_combo_box_index_change(self):
        current_text = self.ra_de_thi_theo_combo_box.currentText()
        if current_text == "Độ khó":
            self.thiet_lap_theo_do_kho.show()
            self.thiet_lap_tho_do_bao_phu.hide()
        else:
            self.thiet_lap_theo_do_kho.hide()
            self.thiet_lap_tho_do_bao_phu.show()

    def tao_de_thi_button_click(self):
        self.Frame.close()
        if self.ra_de_thi_theo_combo_box.currentText() == "Độ khó":
            status = auto_generate_exam_on_difficulty(self.subject_id,
                                                      self.so_cau_de_spin_box.value(),
                                                      self.so_cau_vua_spin_box.value(),
                                                      self.so_cau_kho_spin_box.value()
                                                      )
            if not status:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("\n".join(status[1]))
                msg.setStandardButtons(QtWidgets.QMessageBox.Close)
                msg.exec_()
                self.Frame.show()
                return

        elif self.ra_de_thi_theo_combo_box.currentText() == "Độ bao phủ":
            coverage = []
            for i in range(get_subject_chapter(self.subject_id)):
                coverage.append(
                    self.verticalLayoutWidget_3.findChild(QSpinBox, "chuong_{}_spin_box".format(i + 1)).value())
            status = auto_generate_exam_on_coverage(self.subject_id, coverage)
            if not status:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("\n".join(status[1]))
                msg.setStandardButtons(QtWidgets.QMessageBox.Close)
                msg.exec_()
                self.Frame.show()
                return
        self.ui_chon_cau_hoi_de_dua_vao_de_thi = Ui_exam_frame()
        self.chon_cau_hoi_de_dua_vao_de_thi_frame = QFrame()
        self.ui_chon_cau_hoi_de_dua_vao_de_thi.setupUi(self.chon_cau_hoi_de_dua_vao_de_thi_frame,
                                                       self.subject_id,
                                                       get_last_exam_id()
                                                       )
        self.chon_cau_hoi_de_dua_vao_de_thi_frame.show()
