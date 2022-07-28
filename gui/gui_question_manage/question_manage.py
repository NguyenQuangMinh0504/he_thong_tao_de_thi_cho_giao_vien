# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question_manage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from database.Exam.exam_access import get_exam_info_string
from database.Exam.exam_question_access import get_exam_id
from database.Answer.mcq_answer_access import save_mcq_answer_table, mcq_answer_table, modify_correct, insert_row
from database.Answer.written_exam_answer_access import \
    insert_answer_or_modify_current_answer_to_written_exam_answer_table, save_written_exam_answer_table
from database.Question.question_access import save_question_table, get_question_id_on_question_from_question_table
from gui.gui_question_manage.add_question_pop_up import Ui_them_cau_hoi_frame


class Ui_question_frame(object):
    def setupUi(self, question_frame, subject_id):
        self.subject_id = subject_id
        question_frame.setObjectName("question_frame")
        question_frame.resize(1137, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(question_frame.sizePolicy().hasHeightForWidth())
        question_frame.setSizePolicy(sizePolicy)
        question_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        question_frame.setAutoFillBackground(False)
        question_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        question_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(question_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self._3 = QtWidgets.QHBoxLayout()
        self._3.setObjectName("_3")
        self._4 = QtWidgets.QVBoxLayout()
        self._4.setObjectName("_4")
        self.list_question_label = QtWidgets.QLabel(question_frame)
        self.list_question_label.setObjectName("list_question_label")
        self._4.addWidget(self.list_question_label)
        self.question_list_widget = QtWidgets.QListWidget(question_frame)
        self.question_list_widget.setObjectName("question_list_widget")
        self._4.addWidget(self.question_list_widget)
        self.add_question_label = QtWidgets.QLabel(question_frame)
        self.add_question_label.setObjectName("add_question_label")
        self._4.addWidget(self.add_question_label)
        self._3.addLayout(self._4)
        self._5 = QtWidgets.QVBoxLayout()
        self._5.setObjectName("_5")
        self._10 = QtWidgets.QHBoxLayout()
        self._10.setObjectName("_10")
        self.question_type_label = QtWidgets.QLabel(question_frame)
        self.question_type_label.setObjectName("question_type_label")
        self._10.addWidget(self.question_type_label)
        self.mcq_radio_button = QtWidgets.QRadioButton(question_frame)
        self.mcq_radio_button.setObjectName("mcq_radio_button")
        self._10.addWidget(self.mcq_radio_button)
        self.construct_response_radio_button = QtWidgets.QRadioButton(question_frame)
        self.construct_response_radio_button.setObjectName("construct_response_radio_button")
        self._10.addWidget(self.construct_response_radio_button)
        self._5.addLayout(self._10)
        self._8 = QtWidgets.QHBoxLayout()
        self._8.setObjectName("_8")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.chapter_label = QtWidgets.QLabel(question_frame)
        self.chapter_label.setObjectName("chapter_label")
        self._2.addWidget(self.chapter_label)
        self.chapter_combo_box = QtWidgets.QComboBox(question_frame)
        self.chapter_combo_box.setObjectName("chapter_combo_box")
        self._2.addWidget(self.chapter_combo_box)
        self._8.addLayout(self._2)
        self._7 = QtWidgets.QHBoxLayout()
        self._7.setObjectName("_7")
        self.difficulty_label = QtWidgets.QLabel(question_frame)
        self.difficulty_label.setObjectName("difficulty_label")
        self._7.addWidget(self.difficulty_label)
        self.difficulty_combo_box = QtWidgets.QComboBox(question_frame)
        self.difficulty_combo_box.setObjectName("difficulty_combo_box")
        self._7.addWidget(self.difficulty_combo_box)
        self._8.addLayout(self._7)
        self._5.addLayout(self._8)
        self.problem_label = QtWidgets.QLabel(question_frame)
        self.problem_label.setObjectName("problem_label")
        self._5.addWidget(self.problem_label)
        self.probelem_text_edit = QtWidgets.QTextEdit(question_frame)
        self.probelem_text_edit.setObjectName("probelem_text_edit")
        self._5.addWidget(self.probelem_text_edit)
        self.mcq_answer_label = QtWidgets.QLabel(question_frame)
        self.mcq_answer_label.setObjectName("mcq_answer_label")
        self._5.addWidget(self.mcq_answer_label)
        self.multiple_choice_answer_list_widget = QtWidgets.QListWidget(question_frame)
        self.multiple_choice_answer_list_widget.setObjectName("multiple_choice_answer_list_widget")
        self._5.addWidget(self.multiple_choice_answer_list_widget)
        self._9 = QtWidgets.QHBoxLayout()
        self._9.setObjectName("_9")
        self.add_mcq_answer_label = QtWidgets.QLabel(question_frame)
        self.add_mcq_answer_label.setObjectName("add_mcq_answer_label")
        self._9.addWidget(self.add_mcq_answer_label)
        self.edit_mcq_answer_label = QtWidgets.QLabel(question_frame)
        self.edit_mcq_answer_label.setObjectName("edit_mcq_answer_label")
        self._9.addWidget(self.edit_mcq_answer_label)
        self.delete_mcq_answer_label = QtWidgets.QLabel(question_frame)
        self.delete_mcq_answer_label.setObjectName("delete_mcq_answer_label")
        self._9.addWidget(self.delete_mcq_answer_label)
        self._5.addLayout(self._9)
        self.answer_or_suggest_answer_label = QtWidgets.QLabel(question_frame)
        self.answer_or_suggest_answer_label.setObjectName("answer_or_suggest_answer_label")
        self._5.addWidget(self.answer_or_suggest_answer_label)
        self.answer_or_suggest_answer_text_edit = QtWidgets.QTextEdit(question_frame)
        self.answer_or_suggest_answer_text_edit.setObjectName("answer_or_suggest_answer_text_edit")
        self._5.addWidget(self.answer_or_suggest_answer_text_edit)
        self._6 = QtWidgets.QHBoxLayout()
        self._6.setObjectName("_6")
        self.delete_question_button = QtWidgets.QPushButton(question_frame)
        self.delete_question_button.setObjectName("delete_question_button")
        self._6.addWidget(self.delete_question_button)
        self.save_button = QtWidgets.QPushButton(question_frame)
        self.save_button.setObjectName("save_button")
        self._6.addWidget(self.save_button)
        self._5.addLayout(self._6)
        self._3.addLayout(self._5)
        self.verticalLayout.addLayout(self._3)

        self.retranslateUi(question_frame)
        QtCore.QMetaObject.connectSlotsByName(question_frame)
        # handle click
        self.handle_click()
        self.mcq_radio_button.click()


    def retranslateUi(self, question_frame):
        _translate = QtCore.QCoreApplication.translate
        question_frame.setWindowTitle(_translate("question_frame", "Quản lý câu hỏi"))
        self.list_question_label.setText(_translate("question_frame", "<html><head/><body><p><span style=\" font-size:24pt;\">Danh sách câu hỏi</span></p></body></html>"))
        self.add_question_label.setText(_translate("question_frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Thêm câu hỏi</span></p></body></html>"))
        self.question_type_label.setText(_translate("question_frame", "Dạng câu hỏi"))
        self.mcq_radio_button.setText(_translate("question_frame", "Trắc nghiệm"))
        self.construct_response_radio_button.setText(_translate("question_frame", "Tự luận"))
        self.chapter_label.setText(_translate("question_frame", "Chương"))
        self.difficulty_label.setText(_translate("question_frame", "Độ khó"))
        self.problem_label.setText(_translate("question_frame", "Đề bài"))
        self.mcq_answer_label.setText(_translate("question_frame", "Các lựa chọn đáp án"))
        self.add_mcq_answer_label.setText(_translate("question_frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Thêm</span></p></body></html>"))
        self.edit_mcq_answer_label.setText(_translate("question_frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0000ff;\">Chỉnh sửa</span></p></body></html>"))
        self.delete_mcq_answer_label.setText(_translate("question_frame", "<html><head/><body><p><span style=\" text-decoration: underline; color:#fc0107;\">Xóa</span></p></body></html>"))
        self.answer_or_suggest_answer_label.setText(_translate("question_frame", "Đáp án hoặc gợi ý trả lời"))
        self.delete_question_button.setText(_translate("question_frame", "Xóa câu hỏi"))
        self.save_button.setText(_translate("question_frame", "Lưu"))

        from database.Subject.subject_access import get_subject_chapter
        for i in range(get_subject_chapter(self.subject_id)):
            self.chapter_combo_box.addItem(str(i + 1))

    def handle_click(self):
        # handle click
        self.question_list_widget.currentRowChanged.connect(self.question_list_widget_row_change)
        self.mcq_radio_button.clicked.connect(self.trac_nghiem_radio_button_click)
        self.construct_response_radio_button.clicked.connect(self.tu_luan_radio_button_click)
        self.save_button.clicked.connect(self.save_button_click)
        self.delete_question_button.clicked.connect(self.delete_question_click)

        # clickable label
        self.add_mcq_answer_label.mousePressEvent = self.add_answer_click
        self.edit_mcq_answer_label.mousePressEvent = self.modify_answer_click
        self.delete_mcq_answer_label.mousePressEvent = self.delete_mcq_answer_click
        self.add_question_label.mousePressEvent = self.them_cau_hoi_click
    # ------------------------------------------------------------------------------------------
    # Handle when changing question from question list

    def question_list_widget_row_change(self):

        try:
            # First, clear all widgets ( text_edit, list_widget)
            self.answer_or_suggest_answer_text_edit.clear()
            self.multiple_choice_answer_list_widget.clear()


            question = self.question_list_widget.currentItem().text()
            from database.Question.question_access import get_question_id_on_question_from_question_table
            # Get question id
            question_id = get_question_id_on_question_from_question_table(question)


            # Then, set  question, question chapter and question difficulty

            self.probelem_text_edit.setPlainText(question)

            from database.Question.question_access import get_question_chapter
            self.chapter_combo_box.setCurrentText(str(get_question_chapter(question_id)))

            self.difficulty_combo_box.clear()
            from database.Question.question_access import get_question_difficulty
            self.difficulty_combo_box.addItem(get_question_difficulty(question_id))


            if self.mcq_radio_button.isChecked():
                from database.Answer.mcq_answer_access import get_all_answer

                for answer in get_all_answer(question_id):
                    self.multiple_choice_answer_list_widget.addItem(QtWidgets.QListWidgetItem(answer))

                from database.Answer.mcq_answer_access import get_all_correct_answer
                self.answer_or_suggest_answer_text_edit.setPlainText("\n".join(get_all_correct_answer(question_id)))


            elif self.construct_response_radio_button.isChecked():
                from database.Answer.written_exam_answer_access import get_written_answer
                written_answer = get_written_answer(question_id)
                if written_answer == False:
                    self.answer_or_suggest_answer_text_edit.setPlainText("")
                else:
                    self.answer_or_suggest_answer_text_edit.setPlainText(str(written_answer))

        except AttributeError:
            # This happens because of question list widget item
            print("Attribute Error")
            pass

    # ------------------------------------------------------------------------------------------
    # Radio button click handle

    def trac_nghiem_radio_button_click(self):
        self.question_list_widget.clear()
        self.probelem_text_edit.clear()
        from database.Question.question_access import get_trac_nghiem_info
        for i in get_trac_nghiem_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    def tu_luan_radio_button_click(self):
        self.question_list_widget.clear()
        self.probelem_text_edit.clear()
        self.answer_or_suggest_answer_text_edit.clear()
        from database.Question.question_access import get_tu_luan_info
        for i in get_tu_luan_info(self.subject_id):
            self.question_list_widget.addItem(QtWidgets.QListWidgetItem(i))

    # ------------------------------------------------------------------------------------------

    def add_answer_click(self, *args, **kwargs):

        if self.question_list_widget.currentItem() is not None:  # in case the user don't click any answer
            self.add_answer_pop_up_frame = QtWidgets.QFrame()
            from gui.gui_question_manage.add_answer_pop_up import Ui_add_answer_pop_up
            self.ui_add_answer_pop_up = Ui_add_answer_pop_up()
            self.ui_add_answer_pop_up.setupUi(self.add_answer_pop_up_frame)
            # clear right answer check box
            self.ui_add_answer_pop_up.right_answer_check_box.setChecked(False)
            # clear answer text edit
            self.ui_add_answer_pop_up.answer_text_edit.clear()
            # show the text edit pop up
            self.add_answer_pop_up_frame.show()

            def add_answer_pop_up_ok_button_click():
                # add question to database
                mcq_answer = self.ui_add_answer_pop_up.answer_text_edit.toPlainText()
                question = self.question_list_widget.currentItem().text()
                insert_row(int(get_question_id_on_question_from_question_table(question)), mcq_answer,
                           self.ui_add_answer_pop_up.right_answer_check_box.isChecked())
                # update gui
                self.multiple_choice_answer_list_widget.addItem(mcq_answer)
                # close pop up window
                self.add_answer_pop_up_frame.close()

            self.ui_add_answer_pop_up.ok_button.clicked.connect(add_answer_pop_up_ok_button_click)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Bạn chưa chọn câu hỏi để thêm")
            msg.exec_()


    def modify_answer_click(self, *args, **kwargs):
        self.modify_answer_pop_up = QtWidgets.QFrame()
        from gui.gui_question_manage.modify_answer_pop_up import Ui_modify_answer_pop_up
        self.ui_modify_answer_pop_up = Ui_modify_answer_pop_up()
        self.ui_modify_answer_pop_up.setupUi(self.modify_answer_pop_up)
        if self.multiple_choice_answer_list_widget.currentItem() is not None:  # in case the user don't click any answer
            # set text of pop up text edit to current clicked answer
            current_answer = self.multiple_choice_answer_list_widget.currentItem().text()
            self.ui_modify_answer_pop_up.answer_text_edit.setText(current_answer)
            # set correct answer check box
            from database.Answer.mcq_answer_access import get_answer_correct
            self.ui_modify_answer_pop_up.right_answer_check_box.setChecked(get_answer_correct(current_answer))
            # show pop up
            self.modify_answer_pop_up.show()

            def modify_answer_pop_up_ok_button_click():
                answer = self.multiple_choice_answer_list_widget.currentItem().text()
                new_answer = self.ui_modify_answer_pop_up.answer_text_edit.toPlainText()
                # update data
                mcq_answer_table.replace(answer, new_answer, inplace=True)
                modify_correct(new_answer, self.ui_modify_answer_pop_up.right_answer_check_box.isChecked())
                # update ui
                self.multiple_choice_answer_list_widget.currentItem().setText(new_answer)
                # close pop up window
                self.modify_answer_pop_up.close()

            self.ui_modify_answer_pop_up.ok_button.clicked.connect(modify_answer_pop_up_ok_button_click)

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Bạn chưa chọn câu hỏi để chỉnh sửa")
            msg.exec_()

    def delete_mcq_answer_click(self, *args, **kwargs):
        if self.multiple_choice_answer_list_widget.currentItem() is not None:  # in case the user don't click any answer
            answer = self.multiple_choice_answer_list_widget.currentItem().text()
            # remove answer from database
            from database.Answer.mcq_answer_access import remove_answer
            remove_answer(answer)
            # remove data from ui
            self.multiple_choice_answer_list_widget.takeItem(self.multiple_choice_answer_list_widget.currentRow())
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Bạn chưa chọn câu hỏi để xoá")
            msg.exec_()


    def save_button_click(self):
        if self.construct_response_radio_button.isChecked():
            answer = self.answer_or_suggest_answer_text_edit.toPlainText()
            if self.question_list_widget.currentItem() is not None:
                from database.Question.question_access import get_question_id_on_question_from_question_table
                question_id = get_question_id_on_question_from_question_table(self.question_list_widget.currentItem().text())
                insert_answer_or_modify_current_answer_to_written_exam_answer_table(question_id, answer)
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

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText( "Những đề thi sau đây sẽ bị ảnh hưởng: \n" + "\n".join(exam_list))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if msg.exec_() == QtWidgets.QMessageBox.Ok:
                from database.Question.question_access import remove_question_from_question_table
                self.question_list_widget.takeItem(self.question_list_widget.currentRow())
                remove_question_from_question_table(question_id)
            else:
                pass

    def them_cau_hoi_click(self, *args, **kwargs):
        self.them_cau_hoi_pop_up = QtWidgets.QFrame()
        self.ui_them_cau_hoi_pop_up = Ui_them_cau_hoi_frame()
        self.ui_them_cau_hoi_pop_up.setupUi(self.them_cau_hoi_pop_up, self.subject_id)
        self.them_cau_hoi_pop_up.show()

    # ------------------------------------------------------------------------------------------



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    question_frame = QtWidgets.QFrame()
    ui = Ui_question_frame()
    ui.setupUi(question_frame)
    question_frame.show()
    sys.exit(app.exec_())
