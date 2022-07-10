# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exam.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QFileDialog, QFrame

from database.Exam.exam_question_access import insert_into_exam, save_exam_question_table, get_all_question, remove_question_from_exam_question_table
from database.Exam.exam_access import insert_else_update_exam_to_exam_table, save_exam_table, get_exam_info, \
    remove_exam_from_exam_table
from database.Subject.subject_access import get_subject_name
from database.Question.question_access import *
from database.Answer.mcq_answer_access import get_all_answer, get_all_correct_answer
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_exam_frame(object):
    def setupUi(self, exam_frame, subject_id, exam_id):
        self.Frame = exam_frame
        self.exam_id = exam_id
        self.subject_id = subject_id
        exam_frame.setObjectName("exam_frame")
        exam_frame.resize(801, 707)
        exam_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        exam_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.question_list_widget = QtWidgets.QListWidget(exam_frame)
        self.question_list_widget.setGeometry(QtCore.QRect(40, 60, 301, 191))
        self.question_list_widget.setObjectName("question_list_widget")
        self.question_show_text_edit = QtWidgets.QTextEdit(exam_frame)
        self.question_show_text_edit.setGeometry(QtCore.QRect(370, 60, 401, 191))
        self.question_show_text_edit.setObjectName("question_show_text_edit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(exam_frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 280, 261, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.all_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.all_radio_button.setObjectName("all_radio_button")
        self.horizontalLayout.addWidget(self.all_radio_button)
        self.mcq_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.mcq_radio_button.setObjectName("mcq_radio_button")
        self.horizontalLayout.addWidget(self.mcq_radio_button)
        self.construct_response_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.construct_response_radio_button.setObjectName("construct_response_radio_button")
        self.horizontalLayout.addWidget(self.construct_response_radio_button)
        self.question_type_label = QtWidgets.QLabel(exam_frame)
        self.question_type_label.setGeometry(QtCore.QRect(50, 260, 79, 15))
        self.question_type_label.setObjectName("question_type_label")
        self.add_question_to_exam_button = QtWidgets.QPushButton(exam_frame)
        self.add_question_to_exam_button.setGeometry(QtCore.QRect(610, 270, 161, 41))
        self.add_question_to_exam_button.setObjectName("add_question_to_exam_button")
        self.exam_question_list_widget = QtWidgets.QListWidget(exam_frame)
        self.exam_question_list_widget.setGeometry(QtCore.QRect(30, 350, 311, 111))
        self.exam_question_list_widget.setObjectName("exam_question_list_widget")
        self.exam_show_text_edit = QtWidgets.QTextEdit(exam_frame)
        self.exam_show_text_edit.setGeometry(QtCore.QRect(370, 350, 401, 251))
        self.exam_show_text_edit.setObjectName("exam_show_text_edit")
        self.list_question = QtWidgets.QLabel(exam_frame)
        self.list_question.setGeometry(QtCore.QRect(50, 20, 161, 21))
        self.list_question.setObjectName("list_question")
        self.list_exam_question_label = QtWidgets.QLabel(exam_frame)
        self.list_exam_question_label.setGeometry(QtCore.QRect(40, 300, 311, 31))
        self.list_exam_question_label.setObjectName("list_exam_question_label")
        self.question_score_spin_box = QtWidgets.QDoubleSpinBox(exam_frame)
        self.question_score_spin_box.setGeometry(QtCore.QRect(510, 280, 68, 24))
        self.question_score_spin_box.setObjectName("question_score_spin_box")
        self.question_score_label = QtWidgets.QLabel(exam_frame)
        self.question_score_label.setGeometry(QtCore.QRect(380, 280, 131, 31))
        self.question_score_label.setObjectName("question_score_label")
        self.save_exam_button = QtWidgets.QPushButton(exam_frame)
        self.save_exam_button.setGeometry(QtCore.QRect(220, 650, 161, 41))
        self.save_exam_button.setStyleSheet("background-color: green;\n"
                                             "color: white;\n"
                                             "border-radius: 5px;")
        self.save_exam_button.setObjectName("save_exam_button")
        self.delete_exam_button = QtWidgets.QPushButton(exam_frame)
        self.delete_exam_button.setGeometry(QtCore.QRect(430, 650, 161, 41))
        self.delete_exam_button.setStyleSheet("background-color: red;\n"
                                             "color: white;\n"
                                             "border-radius: 5px;")
        self.delete_exam_button.setObjectName("delete_exam_button")
        self.export_to_file_label = QtWidgets.QLabel(exam_frame)
        self.export_to_file_label.setGeometry(QtCore.QRect(660, 610, 81, 16))
        self.export_to_file_label.setStyleSheet("color: blue;\n"
                                                "text-decoration: underline;")
        self.export_to_file_label.setObjectName("export_to_file_label")
        self.up_arrow_button = QtWidgets.QToolButton(exam_frame)
        self.up_arrow_button.setGeometry(QtCore.QRect(350, 380, 16, 21))
        self.up_arrow_button.setArrowType(QtCore.Qt.UpArrow)
        self.up_arrow_button.setObjectName("up_arrow_button")
        self.down_arrow_button = QtWidgets.QToolButton(exam_frame)
        self.down_arrow_button.setGeometry(QtCore.QRect(350, 420, 16, 21))
        self.down_arrow_button.setArrowType(QtCore.Qt.DownArrow)
        self.down_arrow_button.setObjectName("down_arrow_button")
        self.shuffle_question_label = QtWidgets.QLabel(exam_frame)
        self.shuffle_question_label.setGeometry(QtCore.QRect(390, 610, 141, 16))
        self.shuffle_question_label.setStyleSheet("text-decoration: underline")
        self.shuffle_question_label.setObjectName("shuffle_question_label")
        self.delete_question_from_exam_label = QtWidgets.QLabel(exam_frame)
        self.delete_question_from_exam_label.setGeometry(QtCore.QRect(150, 470, 161, 16))
        self.delete_question_from_exam_label.setStyleSheet("text-decoration: underline;\n"
"color: red;")
        self.delete_question_from_exam_label.setObjectName("delete_question_from_exam_label")
        self.exam_info = QtWidgets.QFrame(exam_frame)
        self.exam_info.setGeometry(QtCore.QRect(30, 490, 301, 151))
        self.exam_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.exam_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exam_info.setObjectName("exam_info")
        self.exam_description_label = QtWidgets.QLabel(self.exam_info)
        self.exam_description_label.setGeometry(QtCore.QRect(0, 20, 151, 21))
        self.exam_description_label.setObjectName("exam_description_label")
        self.time_line_edit = QtWidgets.QLineEdit(self.exam_info)
        self.time_line_edit.setGeometry(QtCore.QRect(110, 50, 71, 21))
        self.time_line_edit.setObjectName("time_line_edit")
        self.time_label = QtWidgets.QLabel(self.exam_info)
        self.time_label.setGeometry(QtCore.QRect(40, 50, 101, 21))
        self.time_label.setObjectName("time_label")
        self.minute_label = QtWidgets.QLabel(self.exam_info)
        self.minute_label.setGeometry(QtCore.QRect(200, 50, 60, 16))
        self.minute_label.setObjectName("minute_label")
        self.year_line_edit = QtWidgets.QLineEdit(self.exam_info)
        self.year_line_edit.setGeometry(QtCore.QRect(110, 80, 131, 21))
        self.year_line_edit.setObjectName("year_line_edit")
        self.year_label = QtWidgets.QLabel(self.exam_info)
        self.year_label.setGeometry(QtCore.QRect(40, 80, 60, 16))
        self.year_label.setObjectName("year_label")
        self.semester_label = QtWidgets.QLabel(self.exam_info)
        self.semester_label.setGeometry(QtCore.QRect(10, 110, 60, 16))
        self.semester_label.setObjectName("semester_label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.exam_info)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 110, 181, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.semester_1_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.semester_1_radio_button.setObjectName("semester_1_radio_button")
        self.horizontalLayout_2.addWidget(self.semester_1_radio_button)
        self.semester_2_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.semester_2_radio_button.setObjectName("semester_2_radio_button")
        self.horizontalLayout_2.addWidget(self.semester_2_radio_button)
        self.summer_semester_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.summer_semester_radio_button.setObjectName("summer_semester_radio_button")
        self.horizontalLayout_2.addWidget(self.summer_semester_radio_button)

        # button click handle
        self.mcq_radio_button.clicked.connect(self.trac_nghiem_button_click)
        self.construct_response_radio_button.clicked.connect(self.tu_luan_button_click)
        self.all_radio_button.clicked.connect(self.tat_ca_button_click)
        self.add_question_to_exam_button.clicked.connect(self.them_vao_de_thi_button_click)
        self.save_exam_button.clicked.connect(self.save_exam_button_click)
        self.delete_exam_button.clicked.connect(self.delete_exam_button_click)

        # row change handle
        self.question_list_widget.currentRowChanged.connect(self.question_list_widget_row_change)
        self.exam_question_list_widget.currentRowChanged.connect(self.exam_question_list_widget_row_change)

        # clickable label handle
        self.export_to_file_label.mousePressEvent = self.export_to_file_label_click
        self.shuffle_question_label.mousePressEvent = self.shuffle_question_click
        self.delete_question_from_exam_label.mousePressEvent = self.delete_question_from_exam_click

        # tool button handle
        self.up_arrow_button.clicked.connect(self.up_arrow_button_click)
        self.down_arrow_button.clicked.connect(self.down_arrow_button_click)

        self.retranslateUi(exam_frame)
        self.all_radio_button.click()
        QtCore.QMetaObject.connectSlotsByName(exam_frame)

    def retranslateUi(self, exam_frame):
        _translate = QtCore.QCoreApplication.translate
        exam_frame.setWindowTitle(_translate("exam_frame", "Đề thi"))
        self.question_show_text_edit.setHtml(_translate("exam_frame",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.all_radio_button.setText(_translate("exam_frame", "Tất cả"))
        self.mcq_radio_button.setText(_translate("exam_frame", "Trắc nghiệm"))
        self.construct_response_radio_button.setText(_translate("exam_frame", "Tự luận"))
        self.question_type_label.setText(_translate("exam_frame", "Dạng câu hỏi"))
        self.add_question_to_exam_button.setText(_translate("exam_frame", "Thêm vào đề thi"))
        self.exam_show_text_edit.setHtml(_translate("exam_frame",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.list_question.setText(_translate("exam_frame",
                                              "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Danh sách câu hỏi</span></p></body></html>"))
        self.list_exam_question_label.setText(_translate("exam_frame",
                                                         "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Danh sách các câu trong đề</span></p></body></html>"))
        self.question_score_label.setText(_translate("exam_frame", "Điểm cho câu hỏi"))
        self.save_exam_button.setText(_translate("exam_frame", "Lưu đề thi"))
        self.delete_exam_button.setText(_translate("exam_frame", "Xóa đề thi"))
        self.export_to_file_label.setText(_translate("exam_frame", "Xuất ra file"))
        self.shuffle_question_label.setText(_translate("exam_frame", "Xáo trộn các câu hỏi"))
        self.delete_question_from_exam_label.setText(_translate("exam_frame", "Xoá câu hỏi ra khỏi đề thi"))
        self.exam_description_label.setText(_translate("exam_frame", "Thông tin về đề thi"))
        self.time_label.setText(_translate("exam_frame", "Thời gian"))
        self.minute_label.setText(_translate("exam_frame", "phút"))
        self.year_label.setText(_translate("exam_frame", "Năm học"))
        self.semester_label.setText(_translate("exam_frame", "Học kỳ"))
        self.semester_1_radio_button.setText(_translate("exam_frame", "1"))
        self.semester_2_radio_button.setText(_translate("exam_frame", "2"))
        self.summer_semester_radio_button.setText(_translate("exam_frame", "Kỳ hè"))

        # load info
        for question_id in get_all_question(self.exam_id):
            self.exam_question_list_widget.addItem(get_question(question_id))
        self.exam_question_list_widget_row_change()

        if get_exam_info(self.exam_id):
            self.time_line_edit.setText(str(get_exam_info(self.exam_id)[-2]))
            self.year_line_edit.setText(str(get_exam_info(self.exam_id)[-3]))
            semester = get_exam_info(self.exam_id)[-1]
            if semester == 1:
                self.semester_1_radio_button.click()
            elif semester == 2:
                self.semester_2_radio_button.click()
            elif semester == 3:
                self.summer_semester_radio_button.click()

    # ------------------------------------------------------------------------------------------------
    # ------------------------------- BUTTON CLICK HANDLE FUNCTION -----------------------------------
    # ------------------------------------------------------------------------------------------------

    # ---------------------------------RADIO BUTTON CLICK HANDLE -------------------------------------

    def trac_nghiem_button_click(self):
        self.question_list_widget.clear()
        for i in get_trac_nghiem_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    def tu_luan_button_click(self):
        self.question_list_widget.clear()
        for i in get_tu_luan_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    def tat_ca_button_click(self):
        self.question_list_widget.clear()
        for i in get_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    # ------------------------ CLICKABLE LABEL HANDLE ---------------------------------------

    def export_to_file_label_click(self, *args, **kwargs):
        path = QFileDialog.getSaveFileName()
        if path[0] != "":
            with open(path[0], "w") as f:
                text = self.exam_show_text_edit.toPlainText()
                f.write(text)

    def shuffle_question_click(self, *args, **kwargs):
        exam_question_num = self.exam_question_list_widget.count()
        import random
        for i in range(exam_question_num):
            random_index = random.randint(0, exam_question_num - 1)  # -1 because randint(a, b) include both a and b
            current_item = self.exam_question_list_widget.takeItem(random_index)
            self.exam_question_list_widget.insertItem(0, current_item)
        self.exam_question_list_widget_row_change()

    def delete_question_from_exam_click(self, *arg, **kwargs):
        current_row = self.exam_question_list_widget.currentRow()
        if current_row != -1:
            question = self.exam_question_list_widget.takeItem(current_row)  # delete question from gui
            question_id = get_question_id_on_question_from_question_table(question.text())
            remove_question_from_exam_question_table(question_id) # delete question from database
            self.exam_question_list_widget_row_change()
    # ---------------------------------------------------------------------------------------

    def them_vao_de_thi_button_click(self):
        question = self.question_list_widget.currentItem().text()
        question_id = get_question_id_on_question_from_question_table(question)

        # insert into database
        insert_into_exam(self.exam_id, question_id, self.question_score_spin_box.value())
        # insert into gui
        self.exam_question_list_widget.addItem(question)
        self.exam_question_list_widget_row_change()

    def delete_exam_button_click(self):
        remove_exam_from_exam_table(self.exam_id)
        save_exam_table()
        save_exam_question_table()
        self.Frame.close()
        from gui_exam.exam_manage import Ui_exam_manage_frame
        frame = QFrame()
        Ui_exam_manage_frame().setupUi(frame, self.subject_id)
        frame.show()

    def save_exam_button_click(self):
        hoc_ki = 0
        if self.semester_1_radio_button.isChecked():
            hoc_ki = 1
        elif self.semester_2_radio_button.isChecked():
            hoc_ki = 2
        elif self.summer_semester_radio_button.isChecked():
            hoc_ki = 3

        error_messages = []
        try:
            time = int(self.time_line_edit.text())
            insert_else_update_exam_to_exam_table(self.subject_id,
                                                  "Đề thi môn {}".format(get_subject_name(self.subject_id)),
                                                  self.year_line_edit.text(),
                                                  time,
                                                  hoc_ki,
                                                  exam_id=self.exam_id
                                                  )
        except ValueError:
            error_messages.append("Thời gian thi không hợp lệ")
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("\n".join(error_messages))
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            msg.exec_()
            return
        save_exam_question_table()
        save_exam_table()
        self.Frame.close()
        from gui_exam.exam_manage import Ui_exam_manage_frame
        frame = QFrame()
        Ui_exam_manage_frame().setupUi(frame, self.subject_id)
        frame.show()

    def up_arrow_button_click(self):
        current_row = self.exam_question_list_widget.currentRow()
        if current_row != -1:
            current_item = self.exam_question_list_widget.takeItem(current_row)
            self.exam_question_list_widget.insertItem(current_row - 1, current_item)
            self.exam_question_list_widget_row_change()

    def down_arrow_button_click(self):
        current_row = self.exam_question_list_widget.currentRow()
        if current_row != -1:
            current_item = self.exam_question_list_widget.takeItem(current_row)
            self.exam_question_list_widget.insertItem(current_row + 1, current_item)
            self.exam_question_list_widget_row_change()

    # ------------------------------- LIST WIDGET CHANGE HANDLE FUNCTION -----------------------------------

    def question_list_widget_row_change(self):
        try:
            self.question_show_text_edit.clear()
            question = self.question_list_widget.currentItem().text()
            question_id = get_question_id_on_question_from_question_table(question)
            list_answer = get_all_answer(question_id)
            self.question_show_text_edit.append(question)
            for number, answer in enumerate(list_answer):
                self.question_show_text_edit.append("{}.  {}".format(number, answer))
            self.question_show_text_edit.append("Thông tin chi tiết:")
            self.question_show_text_edit.append("Đáp án đúng: {}".format(get_all_correct_answer(question_id)))
            self.question_show_text_edit.append("Độ khó: {}".format(get_question_difficulty(question_id)))
            self.question_show_text_edit.append("Chương: Chương {}".format(get_question_chapter(question_id)))

        except AttributeError:
            print("Attribute Error")
            pass

    def exam_question_list_widget_row_change(self):
        questions = [self.exam_question_list_widget.item(x).text()
                     for x in range(self.exam_question_list_widget.count())]
        self.exam_show_text_edit.clear()
        alphabet = "ABCDEFGH"
        for number, question in enumerate(questions):
            question_id = get_question_id_on_question_from_question_table(question)
            self.exam_show_text_edit.append("Câu {}: {}".format(number + 1, question))
            for order, answer in enumerate(get_all_answer(question_id)):
                self.exam_show_text_edit.append("{}.   {}".format(alphabet[order], answer))
            self.exam_show_text_edit.append("")

    # ----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_exam_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
