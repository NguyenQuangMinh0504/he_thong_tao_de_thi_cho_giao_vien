# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_export_data_frame(object):
    def setupUi(self, export_data_frame):
        export_data_frame.setObjectName("export_data_frame")
        export_data_frame.resize(405, 134)
        export_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        export_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(export_data_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subject_label = QtWidgets.QLabel(export_data_frame)
        self.subject_label.setObjectName("subject_label")
        self.horizontalLayout.addWidget(self.subject_label)
        self.subject_combo_box = QtWidgets.QComboBox(export_data_frame)
        self.subject_combo_box.setObjectName("subject_combo_box")
        self.horizontalLayout.addWidget(self.subject_combo_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.export_exam_button = QtWidgets.QPushButton(export_data_frame)
        self.export_exam_button.setObjectName("export_exam_button")
        self.verticalLayout.addWidget(self.export_exam_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(export_data_frame)
        QtCore.QMetaObject.connectSlotsByName(export_data_frame)

        self.load()
        # click handle
        self.export_data_button_click = self.export_data_button_click
        self.export_exam_button.clicked.connect(self.export_data_button_click)

    def retranslateUi(self, export_data_frame):
        _translate = QtCore.QCoreApplication.translate
        export_data_frame.setWindowTitle(_translate("export_data_frame", "Xuất dữ liệu"))
        self.subject_label.setText(_translate("export_data_frame", "Môn học"))
        self.export_exam_button.setText(_translate("export_data_frame", "Xuất dữ liệu"))

    def load(self):
        from database.Subject.subject_access import get_all_subject
        for subject in get_all_subject():
            self.subject_combo_box.addItem(subject)

    def export_data_button_click(self):
        path = QtWidgets.QFileDialog.getSaveFileName()
        print(path)
        from database.Question.question_access import export_to_json
        export_to_json(path[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    export_data_frame = QtWidgets.QFrame()
    ui = Ui_export_data_frame()
    ui.setupUi(export_data_frame)
    export_data_frame.show()
    sys.exit(app.exec_())
