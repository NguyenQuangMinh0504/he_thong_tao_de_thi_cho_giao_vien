# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject_manage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QMessageBox

from database.Subject.subject_access import get_all_subject, get_subject_info, change_subject_info, save_subject_table, \
    get_subject_id, add_subject


class Ui_subject_manage_frame(object):
    def setupUi(self, subject_manage_frame):
        subject_manage_frame.setObjectName("subject_manage_frame")
        subject_manage_frame.resize(378, 407)
        subject_manage_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        subject_manage_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayoutWidget = QtWidgets.QWidget(subject_manage_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 346, 379))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.subject_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.subject_label.setObjectName("subject_label")
        self.horizontalLayout_6.addWidget(self.subject_label)
        self.subject_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.subject_combo_box.setObjectName("subject_combo_box")
        self.horizontalLayout_6.addWidget(self.subject_combo_box)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subject_name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.subject_name_label.setObjectName("subject_name_label")
        self.horizontalLayout.addWidget(self.subject_name_label)
        self.subject_name_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.subject_name_text_edit.setObjectName("subject_name_text_edit")
        self.horizontalLayout.addWidget(self.subject_name_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subject_code_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.subject_code_label.setObjectName("subject_code_label")
        self.horizontalLayout_2.addWidget(self.subject_code_label)
        self.subject_code_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.subject_code_text_edit.setObjectName("subject_code_text_edit")
        self.horizontalLayout_2.addWidget(self.subject_code_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.num_chapter_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.num_chapter_label.setObjectName("num_chapter_label")
        self.horizontalLayout_3.addWidget(self.num_chapter_label)
        self.num_chapter_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.num_chapter_spin_box.setObjectName("num_chapter_spin_box")
        self.horizontalLayout_3.addWidget(self.num_chapter_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.description_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.description_label.setObjectName("description_label")
        self.horizontalLayout_4.addWidget(self.description_label)
        self.description_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.description_text_edit.setObjectName("description_text_edit")
        self.horizontalLayout_4.addWidget(self.description_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_5.addWidget(self.save_button)
        self.add_subject_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_subject_button.setObjectName("add_subject_button")
        self.horizontalLayout_5.addWidget(self.add_subject_button)
        self.delete_subject_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_subject_button.setObjectName("delete_subject_button")
        self.horizontalLayout_5.addWidget(self.delete_subject_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.subject_combo_box.currentTextChanged.connect(self.ten_mon_hoc_combo_box_change)
        self.save_button.clicked.connect(self.luu_button_click)
        self.add_subject_button.clicked.connect(self.add_subject_button_click)
        self.delete_subject_button.clicked.connect(self.delete_subject_button_click)

        for subject in get_all_subject():
            self.subject_combo_box.addItem(subject)

        self.ten_mon_hoc_combo_box_change()

        self.retranslateUi(subject_manage_frame)
        QtCore.QMetaObject.connectSlotsByName(subject_manage_frame)

    def retranslateUi(self, subject_manage_frame):
        _translate = QtCore.QCoreApplication.translate
        subject_manage_frame.setWindowTitle(_translate("subject_manage_frame", "Quản lý môn học"))
        self.subject_label.setText(_translate("subject_manage_frame", "Môn học"))
        self.subject_name_label.setText(_translate("subject_manage_frame", "Tên môn học"))
        self.subject_code_label.setText(_translate("subject_manage_frame", "Mã học phần"))
        self.num_chapter_label.setText(_translate("subject_manage_frame", "Số chương"))
        self.description_label.setText(_translate("subject_manage_frame", "Giới thiệu"))
        self.save_button.setText(_translate("subject_manage_frame", "Lưu"))
        self.add_subject_button.setText(_translate("subject_manage_frame", "Thêm môn học"))
        self.delete_subject_button.setText(_translate("subject_manage_frame", "Xóa môn học"))

    def ten_mon_hoc_combo_box_change(self):
        info = get_subject_info(self.subject_combo_box.currentText())
        if info:
            self.subject_name_text_edit.setText(self.subject_combo_box.currentText())
            self.subject_code_text_edit.setPlainText(info[0])
            self.description_text_edit.setText(info[2])
            self.num_chapter_spin_box.setValue(info[1])

    def luu_button_click(self):
        change_subject_info(
            get_subject_id(self.subject_combo_box.currentText()),
            self.subject_name_text_edit.toPlainText(),
            self.subject_code_text_edit.toPlainText(),
            self.num_chapter_spin_box.value(),
            self.description_text_edit.toPlainText()
        )
        save_subject_table()

    def add_subject_button_click(self):
        self.add_subject_frame = QFrame()
        from gui.gui_subject_manage.add_subject_frame import Ui_add_subject_frame
        self.ui_add_subject_frame = Ui_add_subject_frame()
        self.ui_add_subject_frame.setupUi(self.add_subject_frame)

        def pop_up_add_subject_button_click():
            add_subject(
                self.ui_add_subject_frame.subject_text_edit.toPlainText(),
                self.ui_add_subject_frame.subject_code_text_edit.toPlainText(),
                self.ui_add_subject_frame.num_chapter_spin_box.value(),
                self.ui_add_subject_frame.description_text_edit.toPlainText()
            )
            self.subject_combo_box.addItem(self.ui_add_subject_frame.subject_text_edit.toPlainText())
            self.ui_add_subject_frame.add_subject_frame.close()
            print("kec")


        self.ui_add_subject_frame.add_subject_button.clicked.connect(pop_up_add_subject_button_click)
        self.add_subject_frame.show()

    def delete_subject_button_click(self):
        from database.Subject.subject_access import remove_subject_from_subject_table
        if not remove_subject_from_subject_table(get_subject_id(self.subject_combo_box.currentText())):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Vui lòng xoá hết câu hỏi và đề thi của môn học trước khi xoá môn học")
            self.msg.setStandardButtons(QMessageBox.Close)
            self.msg.exec_()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Bạn đã xoá môn học thành công")
            self.msg.setStandardButtons(QMessageBox.Close)
            self.msg.exec_()
            self.subject_combo_box.removeItem(self.subject_combo_box.currentIndex())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quan_ly_mon_hoc_frame = QtWidgets.QFrame()
    ui = Ui_subject_manage_frame()
    ui.setupUi(quan_ly_mon_hoc_frame)
    quan_ly_mon_hoc_frame.show()
    sys.exit(app.exec_())
