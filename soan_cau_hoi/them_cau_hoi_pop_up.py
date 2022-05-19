# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'them_cau_hoi_pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.Subject.subject_access import get_subject_chapter
from database.Question.question_access import add_question


class Ui_them_cau_hoi_frame(object):
    def setupUi(self, Frame, subject_id):
        self.subject_id = subject_id
        Frame.setObjectName("Frame")
        Frame.resize(430, 407)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cau_hoi_label = QtWidgets.QLabel(Frame)
        self.cau_hoi_label.setGeometry(QtCore.QRect(10, 120, 91, 31))
        self.cau_hoi_label.setObjectName("cau_hoi_label")
        self.cau_hoi_text_edit = QtWidgets.QTextEdit(Frame)
        self.cau_hoi_text_edit.setGeometry(QtCore.QRect(10, 160, 401, 171))
        self.cau_hoi_text_edit.setObjectName("cau_hoi_text_edit")
        self.ok_button = QtWidgets.QPushButton(Frame)
        self.ok_button.setGeometry(QtCore.QRect(290, 350, 113, 32))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dang_cau_hoi_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.dang_cau_hoi_label.setObjectName("dang_cau_hoi_label")
        self.horizontalLayout.addWidget(self.dang_cau_hoi_label)
        self.trac_nghiem_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.trac_nghiem_radio_button.setObjectName("trac_nghiem_radio_button")
        self.horizontalLayout.addWidget(self.trac_nghiem_radio_button)
        self.tu_luan_radio_button = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.tu_luan_radio_button.setObjectName("tu_luan_radio_button")
        self.horizontalLayout.addWidget(self.tu_luan_radio_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 318, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.do_kho_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.do_kho_label.setObjectName("do_kho_label")
        self.horizontalLayout_2.addWidget(self.do_kho_label)
        self.do_kho_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.do_kho_combo_box.setObjectName("do_kho_combo_box")
        self.horizontalLayout_2.addWidget(self.do_kho_combo_box)
        self.chuong_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.chuong_label.setObjectName("chuong_label")
        self.horizontalLayout_2.addWidget(self.chuong_label)
        self.chuong_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.chuong_combo_box.setObjectName("chuong_combo_box")
        self.horizontalLayout_2.addWidget(self.chuong_combo_box)

        for i in range(get_subject_chapter(self.subject_id)):
            self.chuong_combo_box.addItem(str(i + 1))
        for i in range(5):
            self.do_kho_combo_box.addItem(str(i + 1))
        self.ok_button.clicked.connect(self.ok_button_click)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.cau_hoi_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Câu hỏi</span></p></body></html>"))
        self.ok_button.setText(_translate("Frame", "OK"))
        self.dang_cau_hoi_label.setText(_translate("Frame", "Dạng câu hỏi"))
        self.trac_nghiem_radio_button.setText(_translate("Frame", "Trắc nghiệm"))
        self.tu_luan_radio_button.setText(_translate("Frame", "Tự luận"))
        self.do_kho_label.setText(_translate("Frame", "Độ khó"))
        self.chuong_label.setText(_translate("Frame", "Chương"))

    def ok_button_click(self):
        if self.trac_nghiem_radio_button.isChecked():
            add_question(self.cau_hoi_text_edit.toPlainText(),
                         self.subject_id,
                         "trac_nghiem",
                         int(self.do_kho_combo_box.currentText()),
                         int(self.chuong_combo_box.currentText())
                         )
        elif self.tu_luan_radio_button.isChecked():
            add_question(self.cau_hoi_text_edit.toPlainText(),
                         self.subject_id,
                         "tu_luan",
                         int(self.do_kho_combo_box.currentText()),
                         int(self.chuong_combo_box.currentText())
                         )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_them_cau_hoi_frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
