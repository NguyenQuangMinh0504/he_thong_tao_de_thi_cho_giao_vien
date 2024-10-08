# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame
from gui.gui_main_screen.pop_up import Ui_pop_up
from gui.gui_subject_manage.subject_manage import Ui_subject_manage_frame
from gui.gui_exam.exam_manage import Ui_exam_manage_frame
from gui.gui_question_manage.question_manage import Ui_question_frame
from database.Subject.subject_access import get_subject_id


class Ui_main_screen_frame(object):
    def setupUi(self, main_screen_frame):
        main_screen_frame.setObjectName("main_screen_frame")
        main_screen_frame.resize(329, 245)
        main_screen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        main_screen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_screen_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_manage_button = QtWidgets.QPushButton(main_screen_frame)
        self.question_manage_button.setObjectName("question_manage_button")
        self.verticalLayout.addWidget(self.question_manage_button)
        self.exam_manage_button = QtWidgets.QPushButton(main_screen_frame)
        self.exam_manage_button.setObjectName("exam_manage_button")
        self.verticalLayout.addWidget(self.exam_manage_button)
        self.subject_manage_button = QtWidgets.QPushButton(main_screen_frame)
        self.subject_manage_button.setObjectName("subject_manage_button")
        self.verticalLayout.addWidget(self.subject_manage_button)
        self.export_data_button = QtWidgets.QPushButton(main_screen_frame)
        self.export_data_button.setObjectName("export_data_button")
        self.verticalLayout.addWidget(self.export_data_button)
        self.import_data_button = QtWidgets.QPushButton(main_screen_frame)
        self.import_data_button.setObjectName("import_data_button")
        self.verticalLayout.addWidget(self.import_data_button)

        self.retranslateUi(main_screen_frame)
        QtCore.QMetaObject.connectSlotsByName(main_screen_frame)

        self.question_manage_button.clicked.connect(self.question_manage_button_click)
        self.exam_manage_button.clicked.connect(self.exam_manage_button_click)
        self.subject_manage_button.clicked.connect(self.subject_manage_button_click)
        self.export_data_button.clicked.connect(self.export_data_button_click)
        self.import_data_button.clicked.connect(self.import_data_button_click)

    def retranslateUi(self, main_screen_frame):
        _translate = QtCore.QCoreApplication.translate
        main_screen_frame.setWindowTitle(_translate("main_screen_frame", "Giao diện chính"))
        self.question_manage_button.setText(_translate("main_screen_frame", "Soạn câu hỏi"))
        self.exam_manage_button.setText(_translate("main_screen_frame", "Xây dựng đề thi"))
        self.subject_manage_button.setText(_translate("main_screen_frame", "Quản lý môn học"))
        self.export_data_button.setText(_translate("main_screen_frame", "Xuất dữ liệu"))
        self.import_data_button.setText(_translate("main_screen_frame", "Nhập dữ liệu"))


    def question_manage_button_click(self):
        self.pop_up_frame = QFrame()
        self.ui_pop_up = Ui_pop_up()
        self.ui_pop_up.setupUi(self.pop_up_frame)
        self.pop_up_frame.show()
        self.ui_pop_up.ok_button.clicked.connect(self.question_manage_pop_up_ok_button_click)

    def question_manage_pop_up_ok_button_click(self):
        self.pop_up_frame.close()
        self.exam_manage_frame = QFrame()
        Ui_question_frame().setupUi(self.exam_manage_frame,
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
        Ui_exam_manage_frame().setupUi(self.exam_manage_frame,
                                       get_subject_id(self.ui_pop_up.danh_sach_mon_hoc_combo_box.currentText()))
        self.exam_manage_frame.show()
        self.pop_up_frame.close()

    def subject_manage_button_click(self):
        self.subject_manage_frame = QFrame()
        self.ui_subject_manage_frame = Ui_subject_manage_frame()  # fuck garbage collector, dont remove
        self.ui_subject_manage_frame.setupUi(self.subject_manage_frame)
        self.subject_manage_frame.show()

    def export_data_button_click(self):
        path = QtWidgets.QFileDialog.getSaveFileName()
        from database.json_file_handle import export_all_to_json_file
        if path[0] != "":
            export_all_to_json_file(path[0])
        elif path[0] == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Xuất đề thi thất bại")
            msg.exec_()

    def import_data_button_click(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        from database.json_file_handle import import_all_from_json_file
        if path[0] != "":
            import_all_from_json_file(path[0])
        elif path[0] == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Nhập đề thi thất bại")
            msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_main_screen_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
