# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_subject_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_subject_frame(object):
    def setupUi(self, add_subject_frame):
        self.add_subject_frame = add_subject_frame
        add_subject_frame.setObjectName("add_subject_frame")
        add_subject_frame.resize(385, 460)
        add_subject_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        add_subject_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(add_subject_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subject_label = QtWidgets.QLabel(add_subject_frame)
        self.subject_label.setObjectName("subject_label")
        self.horizontalLayout.addWidget(self.subject_label)
        self.subject_text_edit = QtWidgets.QTextEdit(add_subject_frame)
        self.subject_text_edit.setObjectName("subject_text_edit")
        self.horizontalLayout.addWidget(self.subject_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subject_code_label = QtWidgets.QLabel(add_subject_frame)
        self.subject_code_label.setObjectName("subject_code_label")
        self.horizontalLayout_2.addWidget(self.subject_code_label)
        self.subject_code_text_edit = QtWidgets.QTextEdit(add_subject_frame)
        self.subject_code_text_edit.setObjectName("subject_code_text_edit")
        self.horizontalLayout_2.addWidget(self.subject_code_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.num_chapter_label = QtWidgets.QLabel(add_subject_frame)
        self.num_chapter_label.setObjectName("num_chapter_label")
        self.horizontalLayout_3.addWidget(self.num_chapter_label)
        self.num_chapter_spin_box = QtWidgets.QSpinBox(add_subject_frame)
        self.num_chapter_spin_box.setObjectName("num_chapter_spin_box")
        self.horizontalLayout_3.addWidget(self.num_chapter_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.description_label = QtWidgets.QLabel(add_subject_frame)
        self.description_label.setObjectName("description_label")
        self.horizontalLayout_4.addWidget(self.description_label)
        self.description_text_edit = QtWidgets.QTextEdit(add_subject_frame)
        self.description_text_edit.setObjectName("description_text_edit")
        self.horizontalLayout_4.addWidget(self.description_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_subject_button = QtWidgets.QPushButton(add_subject_frame)
        self.add_subject_button.setObjectName("add_subject_button")
        self.horizontalLayout_5.addWidget(self.add_subject_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(add_subject_frame)
        QtCore.QMetaObject.connectSlotsByName(add_subject_frame)

    def retranslateUi(self, add_subject_frame):
        _translate = QtCore.QCoreApplication.translate
        add_subject_frame.setWindowTitle(_translate("add_subject_frame", "Thêm môn học"))
        self.subject_label.setText(_translate("add_subject_frame", "Tên môn học"))
        self.subject_code_label.setText(_translate("add_subject_frame", "Mã học phần"))
        self.num_chapter_label.setText(_translate("add_subject_frame", "Số chương"))
        self.description_label.setText(_translate("add_subject_frame", "Giới thiệu"))
        self.add_subject_button.setText(_translate("add_subject_frame", "Thêm môn học"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_subject_frame = QtWidgets.QFrame()
    ui = Ui_add_subject_frame()
    ui.setupUi(add_subject_frame)
    add_subject_frame.show()
    sys.exit(app.exec_())
