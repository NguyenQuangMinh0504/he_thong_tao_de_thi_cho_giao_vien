# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soan_cau_hoi_ver_trinh_thanh_trung.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.Question.question_access import *
from database.MCQS_Answer.mcqs_access import get_answer


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(590, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        Frame.setAutoFillBackground(False)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.danh_sach_cau_hoi_label = QtWidgets.QLabel(Frame)
        self.danh_sach_cau_hoi_label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.danh_sach_cau_hoi_label.setObjectName("danh_sach_cau_hoi_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 20, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.dang_cau_hoi_horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.dang_cau_hoi_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.dang_cau_hoi_horizontal_layout.setObjectName("dang_cau_hoi_horizontal_layout")
        self.dang_cau_hoi_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.dang_cau_hoi_label.setObjectName("dang_cau_hoi_label")
        self.dang_cau_hoi_horizontal_layout.addWidget(self.dang_cau_hoi_label)
        self.trac_nghiem_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.trac_nghiem_radio_button.setObjectName("trac_nghiem_radio_button")
        self.dang_cau_hoi_horizontal_layout.addWidget(self.trac_nghiem_radio_button)
        self.tu_luan_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.tu_luan_radio_button.setObjectName("tu_luan_radio_button")
        self.dang_cau_hoi_horizontal_layout.addWidget(self.tu_luan_radio_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 80, 251, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.de_bai_horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.de_bai_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.de_bai_horizontal_layout.setObjectName("de_bai_horizontal_layout")
        self.de_bai_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.de_bai_label.setObjectName("de_bai_label")
        self.de_bai_horizontal_layout.addWidget(self.de_bai_label)
        self.de_bai_text_edit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.de_bai_text_edit.setObjectName("de_bai_text_edit")
        self.de_bai_horizontal_layout.addWidget(self.de_bai_text_edit)
        self.cac_lua_chon_dap_an_label = QtWidgets.QLabel(Frame)
        self.cac_lua_chon_dap_an_label.setGeometry(QtCore.QRect(260, 230, 131, 16))
        self.cac_lua_chon_dap_an_label.setObjectName("cac_lua_chon_dap_an_label")
        self.question_list_widget = QtWidgets.QListWidget(Frame)
        self.question_list_widget.setGeometry(QtCore.QRect(10, 80, 151, 181))
        self.question_list_widget.setObjectName("question_list_widget")
        self.multiple_choice_question_list_widget = QtWidgets.QListWidget(Frame)
        self.multiple_choice_question_list_widget.setGeometry(QtCore.QRect(280, 260, 201, 81))
        self.multiple_choice_question_list_widget.setObjectName("multiple_choice_question_list_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 400, 211, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chuong_doi_kho_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chuong_doi_kho_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.chuong_doi_kho_vertical_layout.setObjectName("chuong_doi_kho_vertical_layout")
        self.chuong_horizontal_layout = QtWidgets.QHBoxLayout()
        self.chuong_horizontal_layout.setObjectName("chuong_horizontal_layout")
        self.chuong_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.chuong_label.setObjectName("chuong_label")
        self.chuong_horizontal_layout.addWidget(self.chuong_label)
        self.chuong_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.chuong_combo_box.setObjectName("chuong_combo_box")
        self.chuong_horizontal_layout.addWidget(self.chuong_combo_box)
        self.chuong_doi_kho_vertical_layout.addLayout(self.chuong_horizontal_layout)
        self.do_kho_horizontal_layout = QtWidgets.QHBoxLayout()
        self.do_kho_horizontal_layout.setObjectName("do_kho_horizontal_layout")
        self.do_kho_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.do_kho_label.setObjectName("do_kho_label")
        self.do_kho_horizontal_layout.addWidget(self.do_kho_label)
        self.do_kho_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.do_kho_combo_box.setObjectName("do_kho_combo_box")
        self.do_kho_horizontal_layout.addWidget(self.do_kho_combo_box)
        self.chuong_doi_kho_vertical_layout.addLayout(self.do_kho_horizontal_layout)
        self.xoa_cau_hoi_button = QtWidgets.QPushButton(Frame)
        self.xoa_cau_hoi_button.setGeometry(QtCore.QRect(420, 500, 113, 32))
        self.xoa_cau_hoi_button.setObjectName("xoa_cau_hoi_button")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(280, 350, 201, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.them_chinh_su_xoa_horizontal_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.them_chinh_su_xoa_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.them_chinh_su_xoa_horizontal_layout.setObjectName("them_chinh_su_xoa_horizontal_layout")
        self.them_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.them_label.setObjectName("them_label")
        self.them_chinh_su_xoa_horizontal_layout.addWidget(self.them_label)
        self.chinh_sua_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.chinh_sua_label.setObjectName("chinh_sua_label")
        self.them_chinh_su_xoa_horizontal_layout.addWidget(self.chinh_sua_label)
        self.xoa_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.xoa_label.setObjectName("xoa_label")
        self.them_chinh_su_xoa_horizontal_layout.addWidget(self.xoa_label)
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.danh_sach_cau_hoi_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:24pt;\">Danh sách câu hỏi</span></p></body></html>"))
        self.dang_cau_hoi_label.setText(_translate("Frame", "Dạng câu hỏi"))
        self.trac_nghiem_radio_button.setText(_translate("Frame", "Trắc nghiệm"))
        self.tu_luan_radio_button.setText(_translate("Frame", "Tự luận"))
        self.de_bai_label.setText(_translate("Frame", "Đề bài"))
        self.cac_lua_chon_dap_an_label.setText(_translate("Frame", "Các lựa chọn đáp án"))
        self.chuong_label.setText(_translate("Frame", "Chương"))
        self.do_kho_label.setText(_translate("Frame", "Độ khó"))
        self.xoa_cau_hoi_button.setText(_translate("Frame", "Xóa câu hỏi"))
        self.them_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Thêm</span></p></body></html>"))
        self.chinh_sua_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Chỉnh sửa</span></p></body></html>"))
        self.xoa_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#fc0107;\">Xóa</span></p></body></html>"))
        self.question_list_widget.currentRowChanged.connect(self.change_row)
        self.trac_nghiem_radio_button.clicked.connect(self.trac_nghiem_radio_button_click)
        self.tu_luan_radio_button.clicked.connect(self.tu_luan_radio_button_click)

    def change_row(self):
        try:
            question = self.question_list_widget.currentItem().text()
            self.de_bai_text_edit.setPlainText(question)
            self.multiple_choice_question_list_widget.clear()
            for i in get_answer(question):
                item = QtWidgets.QListWidgetItem(i)
                self.multiple_choice_question_list_widget.addItem(item)
            self.chuong_combo_box.clear()
            #currently not working
            print("Chapter: ", get_question_chapter(question))
            self.chuong_combo_box.addItem(get_question_chapter(question))
            self.do_kho_combo_box.clear()
            print("Difficulty: ", get_question_difficulty(question))
            self.do_kho_combo_box.addItem(get_question_difficulty(question))
        except AttributeError:
            pass
        except TypeError:
            pass

    def trac_nghiem_radio_button_click(self):
        self.question_list_widget.clear()
        self.de_bai_text_edit.clear()
        for i in get_trac_nghiem_info():
            item = QtWidgets.QListWidgetItem(i)
            self.question_list_widget.addItem(item)

    def tu_luan_radio_button_click(self):
        self.question_list_widget.clear()
        self.de_bai_text_edit.clear()
        for i in get_tu_luan_info():
            item = QtWidgets.QListWidgetItem(i)
            self.question_list_widget.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
