# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quan_li_mon_hoc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.Subject.subject_access import get_subject_name,\
    get_subject_info, change_subject_info, save_subject_table, get_subject_id


class Ui_quan_ly_mon_hoc_frame(object):
    def setupUi(self, quan_ly_mon_hoc_frame):
        quan_ly_mon_hoc_frame.setObjectName("quan_ly_mon_hoc_frame")
        quan_ly_mon_hoc_frame.resize(385, 428)
        quan_ly_mon_hoc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        quan_ly_mon_hoc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayoutWidget = QtWidgets.QWidget(quan_ly_mon_hoc_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 346, 379))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mon_hoc_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mon_hoc_label.setObjectName("mon_hoc_label")
        self.horizontalLayout_6.addWidget(self.mon_hoc_label)
        self.mon_hoc_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.mon_hoc_combo_box.setObjectName("mon_hoc_combo_box")
        self.horizontalLayout_6.addWidget(self.mon_hoc_combo_box)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ten_mon_hoc_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ten_mon_hoc_label.setObjectName("ten_mon_hoc_label")
        self.horizontalLayout.addWidget(self.ten_mon_hoc_label)
        self.ten_mon_hoc_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.ten_mon_hoc_text_edit.setObjectName("ten_mon_hoc_text_edit")
        self.horizontalLayout.addWidget(self.ten_mon_hoc_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ma_hoc_phan_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ma_hoc_phan_label.setObjectName("ma_hoc_phan_label")
        self.horizontalLayout_2.addWidget(self.ma_hoc_phan_label)
        self.ma_hoc_phan_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.ma_hoc_phan_text_edit.setObjectName("ma_hoc_phan_text_edit")
        self.horizontalLayout_2.addWidget(self.ma_hoc_phan_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.so_chuong_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.so_chuong_label.setObjectName("so_chuong_label")
        self.horizontalLayout_3.addWidget(self.so_chuong_label)
        self.so_chuong_spin_box = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.so_chuong_spin_box.setObjectName("so_chuong_spin_box")
        self.horizontalLayout_3.addWidget(self.so_chuong_spin_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gioi_thieu_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gioi_thieu_label.setObjectName("gioi_thieu_label")
        self.horizontalLayout_4.addWidget(self.gioi_thieu_label)
        self.gioi_thieu_text_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.gioi_thieu_text_edit.setObjectName("gioi_thieu_text_edit")
        self.horizontalLayout_4.addWidget(self.gioi_thieu_text_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.luu_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.luu_button.setObjectName("luu_button")
        self.horizontalLayout_5.addWidget(self.luu_button)
        self.huy_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.huy_button.setObjectName("huy_button")
        self.horizontalLayout_5.addWidget(self.huy_button)
        self.xoa_mon_hoc_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.xoa_mon_hoc_button.setObjectName("xoa_mon_hoc_button")
        self.horizontalLayout_5.addWidget(self.xoa_mon_hoc_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.mon_hoc_combo_box.currentTextChanged.connect(self.ten_mon_hoc_combo_box_change)
        self.luu_button.clicked.connect(self.luu_button_click)


        for subject in get_subject_name():
            self.mon_hoc_combo_box.addItem(subject)

        self.ten_mon_hoc_combo_box_change()

        self.retranslateUi(quan_ly_mon_hoc_frame)
        QtCore.QMetaObject.connectSlotsByName(quan_ly_mon_hoc_frame)

    def retranslateUi(self, quan_ly_mon_hoc_frame):
        _translate = QtCore.QCoreApplication.translate
        quan_ly_mon_hoc_frame.setWindowTitle(_translate("quan_ly_mon_hoc_frame", "Frame"))
        self.mon_hoc_label.setText(_translate("quan_ly_mon_hoc_frame", "Môn học"))
        self.ten_mon_hoc_label.setText(_translate("quan_ly_mon_hoc_frame", "Tên môn học"))
        self.ma_hoc_phan_label.setText(_translate("quan_ly_mon_hoc_frame", "Mã học phần"))
        self.so_chuong_label.setText(_translate("quan_ly_mon_hoc_frame", "Số chương"))
        self.gioi_thieu_label.setText(_translate("quan_ly_mon_hoc_frame", "Giới thiệu"))
        self.luu_button.setText(_translate("quan_ly_mon_hoc_frame", "Lưu"))
        self.huy_button.setText(_translate("quan_ly_mon_hoc_frame", "Thêm môn học"))
        self.xoa_mon_hoc_button.setText(_translate("quan_ly_mon_hoc_frame", "Xóa môn học"))

    def ten_mon_hoc_combo_box_change(self):
        info = get_subject_info(self.mon_hoc_combo_box.currentText())
        self.ten_mon_hoc_text_edit.setText(self.mon_hoc_combo_box.currentText())
        self.ma_hoc_phan_text_edit.setPlainText(info[0])
        self.gioi_thieu_text_edit.setText(info[2])
        self.so_chuong_spin_box.setValue(info[1])

    def luu_button_click(self):
        change_subject_info(
            get_subject_id(self.mon_hoc_combo_box.currentText()),
            self.ten_mon_hoc_text_edit.toPlainText(),
            self.ma_hoc_phan_text_edit.toPlainText(),
            self.so_chuong_spin_box.value(),
            self.gioi_thieu_text_edit.toPlainText()
        )
        save_subject_table()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quan_ly_mon_hoc_frame = QtWidgets.QFrame()
    ui = Ui_quan_ly_mon_hoc_frame()
    ui.setupUi(quan_ly_mon_hoc_frame)
    quan_ly_mon_hoc_frame.show()
    sys.exit(app.exec_())
