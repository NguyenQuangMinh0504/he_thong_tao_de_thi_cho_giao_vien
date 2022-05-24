# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soan_cau_hoi_ver_trinh_thanh_trung.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QMessageBox

from database.MCQS_Answer.written_exam_answer_access import save_written_exam_answer_table, get_written_answer, \
    insert_answer
from database.Question.question_access import *
from database.MCQS_Answer.mcq_answer_access import *
from database.Subject.subject_access import get_subject_chapter
from database.Exam.exam_question_access import get_exam_id
from database.Exam.exam_access import get_exam_info_string
from soan_cau_hoi.chinh_sua_dap_an_pop_up import Ui_chinh_sua_dap_an_pop_up
from soan_cau_hoi.them_dap_an_pop_up import Ui_them_dap_an_pop_up
from soan_cau_hoi.add_question_pop_up import Ui_them_cau_hoi_frame


class Ui_soan_cau_hoi_frame(object):
    def setupUi(self, Frame, subject_id):
        # set up subject_id
        self.subject_id = subject_id
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
        self.question_list_widget = QtWidgets.QListWidget(Frame)
        self.question_list_widget.setGeometry(QtCore.QRect(10, 80, 151, 181))
        self.question_list_widget.setObjectName("question_list_widget")
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
        self.save_button = QtWidgets.QPushButton(Frame)
        self.save_button.setGeometry(QtCore.QRect(270, 500, 113, 32))
        self.save_button.setObjectName("save_button")
        self.them_cau_hoi_label = QtWidgets.QLabel(Frame)
        self.them_cau_hoi_label.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.them_cau_hoi_label.setObjectName("them_cau_hoi_label")
        self.cac_lua_chon_dap_an_container = QtWidgets.QWidget(Frame)
        self.cac_lua_chon_dap_an_container.setGeometry(QtCore.QRect(250, 220, 271, 161))
        self.cac_lua_chon_dap_an_container.setObjectName("cac_lua_chon_dap_an_container")
        self.cac_lua_chon_dap_an_label = QtWidgets.QLabel(self.cac_lua_chon_dap_an_container)
        self.cac_lua_chon_dap_an_label.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.cac_lua_chon_dap_an_label.setObjectName("cac_lua_chon_dap_an_label")
        self.multiple_choice_answer_list_widget = QtWidgets.QListWidget(self.cac_lua_chon_dap_an_container)
        self.multiple_choice_answer_list_widget.setGeometry(QtCore.QRect(20, 20, 201, 81))
        self.multiple_choice_answer_list_widget.setObjectName("multiple_choice_question_list_widget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.cac_lua_chon_dap_an_container)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 110, 201, 41))
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
        self.written_exam_answer_container = QtWidgets.QWidget(Frame)
        self.written_exam_answer_container.setGeometry(QtCore.QRect(250, 220, 271, 161))
        self.written_exam_answer_container.setObjectName("written_exam_answer_container")
        self.dap_an_hoac_goi_y_tra_loi_label = QtWidgets.QLabel(self.written_exam_answer_container)
        self.dap_an_hoac_goi_y_tra_loi_label.setGeometry(QtCore.QRect(10, 0, 161, 16))
        self.dap_an_hoac_goi_y_tra_loi_label.setObjectName("dap_an_hoac_goi_y_tra_loi_label")
        self.dap_an_hoac_goi_y_tra_loi_text_edit = QtWidgets.QTextEdit(self.written_exam_answer_container)
        self.dap_an_hoac_goi_y_tra_loi_text_edit.setGeometry(QtCore.QRect(20, 20, 201, 81))
        self.dap_an_hoac_goi_y_tra_loi_text_edit.setObjectName("dap_an_hoac_goi_y_tra_loi_text_edit")
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        # handle click
        self.handle_click()
        self.trac_nghiem_radio_button.click()

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.danh_sach_cau_hoi_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:24pt;\">Danh sách câu hỏi</span></p></body></html>"))
        self.dang_cau_hoi_label.setText(_translate("Frame", "Dạng câu hỏi"))
        self.trac_nghiem_radio_button.setText(_translate("Frame", "Trắc nghiệm"))
        self.tu_luan_radio_button.setText(_translate("Frame", "Tự luận"))
        self.de_bai_label.setText(_translate("Frame", "Đề bài"))
        self.chuong_label.setText(_translate("Frame", "Chương"))
        self.do_kho_label.setText(_translate("Frame", "Độ khó"))
        self.xoa_cau_hoi_button.setText(_translate("Frame", "Xóa câu hỏi"))
        self.save_button.setText(_translate("Frame", "Lưu"))
        self.them_cau_hoi_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Thêm câu hỏi</span></p></body></html>"))
        self.cac_lua_chon_dap_an_label.setText(_translate("Frame", "Các lựa chọn đáp án"))
        self.them_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Thêm</span></p></body></html>"))
        self.chinh_sua_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Chỉnh sửa</span></p></body></html>"))
        self.xoa_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#fc0107;\">Xóa</span></p></body></html>"))
        self.dap_an_hoac_goi_y_tra_loi_label.setText(_translate("Frame", "Đáp án hoặc gợi ý trả lời"))

        for i in range(get_subject_chapter(self.subject_id)):
            self.chuong_combo_box.addItem(str(i + 1))

    def handle_click(self):
        # handle click
        self.question_list_widget.currentRowChanged.connect(self.question_list_widget_row_change)
        self.trac_nghiem_radio_button.clicked.connect(self.trac_nghiem_radio_button_click)
        self.tu_luan_radio_button.clicked.connect(self.tu_luan_radio_button_click)
        self.save_button.clicked.connect(self.save_button_click)
        self.xoa_cau_hoi_button.clicked.connect(self.delete_question_click)

        # clickable label
        self.them_label.mousePressEvent = self.them_dap_an_click
        self.chinh_sua_label.mousePressEvent = self.chinh_sua_click
        self.xoa_label.mousePressEvent = self.delete_mcq_answer_click
        self.them_cau_hoi_label.mousePressEvent = self.them_cau_hoi_click
    # ------------------------------------------------------------------------------------------
    # Handle when changing question from question list

    def question_list_widget_row_change(self):

        try:
            question = self.question_list_widget.currentItem().text()
            question_id = get_question_id_on_question_from_question_table(question)

            self.de_bai_text_edit.setPlainText(question)

            self.dap_an_hoac_goi_y_tra_loi_text_edit.clear()
            written_answer = get_written_answer(question_id)
            if written_answer:
                self.dap_an_hoac_goi_y_tra_loi_text_edit.setPlainText(written_answer)

            self.multiple_choice_answer_list_widget.clear()
            for answer in get_answer(question_id):
                self.multiple_choice_answer_list_widget.addItem(QtWidgets.QListWidgetItem(answer))
            self.chuong_combo_box.setCurrentText(str(get_question_chapter(question_id)))

            self.do_kho_combo_box.clear()
            self.do_kho_combo_box.addItem(get_question_difficulty(question_id))

        except AttributeError:
            print("Attribute Error")
            pass

    # ------------------------------------------------------------------------------------------
    # Radio button click handle

    def trac_nghiem_radio_button_click(self):
        self.cac_lua_chon_dap_an_container.show()
        self.written_exam_answer_container.hide()
        self.question_list_widget.clear()
        self.de_bai_text_edit.clear()
        for i in get_trac_nghiem_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    def tu_luan_radio_button_click(self):
        self.cac_lua_chon_dap_an_container.hide()
        self.written_exam_answer_container.show()
        self.question_list_widget.clear()
        self.de_bai_text_edit.clear()
        for i in get_tu_luan_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    # ------------------------------------------------------------------------------------------

    def them_dap_an_click(self, *args, **kwargs):
        self.them_dap_an_pop_up = QFrame()
        self.ui_them_dap_an_pop_up = Ui_them_dap_an_pop_up()
        self.ui_them_dap_an_pop_up.setupUi(self.them_dap_an_pop_up)
        # clear the check box of them dap an pop up
        self.ui_them_dap_an_pop_up.dap_an_check_box.setChecked(False)
        # clear the text edit of them dap an pop up
        self.ui_them_dap_an_pop_up.dap_an_dung_text_edit.clear()
        # show the text edit pop up
        self.them_dap_an_pop_up.show()
        self.ui_them_dap_an_pop_up.ok_button.clicked.connect(self.them_dap_an_pop_up_ok_button_click)

    def chinh_sua_click(self, *args, **kwargs):
        self.chinh_sua_dap_an_pop_up = QFrame()
        self.ui_chinh_sua_dap_an_pop_up = Ui_chinh_sua_dap_an_pop_up()
        self.ui_chinh_sua_dap_an_pop_up.setupUi(self.chinh_sua_dap_an_pop_up)
        if self.multiple_choice_answer_list_widget.currentItem() is not None:  # in case the user don't click any answer
            # set text of pop up text edit to current clicked answer
            current_answer = self.multiple_choice_answer_list_widget.currentItem().text()
            self.ui_chinh_sua_dap_an_pop_up.dap_an_dung_text_edit.setText(current_answer)
            # set correct answer check box
            self.ui_chinh_sua_dap_an_pop_up.dap_an_check_box.setChecked(get_answer_correct(current_answer))
            # show pop up
            self.chinh_sua_dap_an_pop_up.show()
            self.ui_chinh_sua_dap_an_pop_up.ok_button.clicked.connect(self.chinh_sua_dap_an_pop_up_ok_button_click)

    def delete_mcq_answer_click(self, *args, **kwargs):
        answer = self.multiple_choice_answer_list_widget.currentItem().text()
        # remove answer from database
        remove_answer(answer)
        # remove data from ui
        self.multiple_choice_answer_list_widget.takeItem(self.multiple_choice_answer_list_widget.currentRow())

    def save_button_click(self):
        answer = self.dap_an_hoac_goi_y_tra_loi_text_edit.toPlainText()
        if self.question_list_widget.currentItem() is not None:
            question_id = get_question_id_on_question_from_question_table(self.question_list_widget.currentItem().text())
            insert_answer(question_id, answer)
        save_mcq_answer_table()
        save_question_table()
        save_written_exam_answer_table()

    def delete_question_click(self):
        # get text from the question to delete
        if self.question_list_widget.currentItem() is not None:
            question = self.question_list_widget.currentItem().text()
            # get question id from question text
            question_id = get_question_id_on_question_from_question_table(question)
            exam_list = [get_exam_info_string(exam_id) for exam_id in get_exam_id(question_id)]

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText( "Những đề thi sau đây sẽ bị ảnh hưởng: \n" + "\n".join(exam_list))
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec_() == QMessageBox.Ok:
                from database.Question.question_access import remove_question_from_question_table
                remove_question_from_question_table(question_id)
                print("xoa thanh cong")
            else:
                print("bruh 2")
            self.question_list_widget.takeItem(self.question_list_widget.currentRow())


    def them_cau_hoi_click(self, *args, **kwargs):
        self.them_cau_hoi_pop_up = QFrame()
        self.ui_them_cau_hoi_pop_up = Ui_them_cau_hoi_frame()
        self.ui_them_cau_hoi_pop_up.setupUi(self.them_cau_hoi_pop_up, self.subject_id)
        self.them_cau_hoi_pop_up.show()
        self.ui_them_cau_hoi_pop_up.ok_button.clicked.connect(self.them_cau_hoi_pop_up_ok_button_click)

    # ------------------------------------------------------------------------------------------
    # Pop up event handler

    def chinh_sua_dap_an_pop_up_ok_button_click(self):
        answer = self.multiple_choice_answer_list_widget.currentItem().text()
        new_answer = self.ui_chinh_sua_dap_an_pop_up.dap_an_dung_text_edit.toPlainText()
        # update data
        mcq_answer_table.replace(answer, new_answer, inplace=True)
        modify_correct(new_answer, self.ui_chinh_sua_dap_an_pop_up.dap_an_check_box.isChecked())
        # update ui
        self.multiple_choice_answer_list_widget.currentItem().setText(new_answer)
        # close pop up window
        self.chinh_sua_dap_an_pop_up.close()

    def them_dap_an_pop_up_ok_button_click(self):
        # add question to database
        mcq_answer = self.ui_them_dap_an_pop_up.dap_an_dung_text_edit.toPlainText()
        question = self.question_list_widget.currentItem().text()
        insert_row(int(get_question_id_on_question_from_question_table(question)), mcq_answer, self.ui_them_dap_an_pop_up.dap_an_check_box.isChecked())
        # update gui
        self.multiple_choice_answer_list_widget.addItem(mcq_answer)
        # close pop up window
        self.them_dap_an_pop_up.close()

    def them_cau_hoi_pop_up_ok_button_click(self):
        question = self.ui_them_cau_hoi_pop_up.cau_hoi_text_edit.toPlainText()
        # close pop up
        self.them_cau_hoi_pop_up.close()
        # add widget to gui
        self.question_list_widget.addItem(question)

    # ----------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_soan_cau_hoi_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
