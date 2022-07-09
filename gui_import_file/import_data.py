# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_import_data_frame(object):
    def setupUi(self, import_data_frame):
        import_data_frame.setObjectName("import_data_frame")
        import_data_frame.resize(405, 134)
        import_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        import_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(import_data_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subject_label = QtWidgets.QLabel(import_data_frame)
        self.subject_label.setObjectName("subject_label")
        self.horizontalLayout.addWidget(self.subject_label)
        self.subject_combo_box = QtWidgets.QComboBox(import_data_frame)
        self.subject_combo_box.setObjectName("subject_combo_box")
        self.horizontalLayout.addWidget(self.subject_combo_box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.import_data_button = QtWidgets.QPushButton(import_data_frame)
        self.import_data_button.setObjectName("import_data_button")
        self.verticalLayout.addWidget(self.import_data_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(import_data_frame)
        self.load()

        # click handle
        self.import_data_button_click = self.import_data_button_click
        self.import_data_button.clicked.connect(self.import_data_button_click)
        QtCore.QMetaObject.connectSlotsByName(import_data_frame)

    def retranslateUi(self, import_data_frame):
        _translate = QtCore.QCoreApplication.translate
        import_data_frame.setWindowTitle(_translate("import_data_frame", "Nhập dữ liệu"))
        self.subject_label.setText(_translate("import_data_frame", "Môn học"))
        self.import_data_button.setText(_translate("import_data_frame", "Nhập dữ liệu"))

    def load(self):
        from database.Subject.subject_access import get_all_subject
        for subject in get_all_subject():
            self.subject_combo_box.addItem(subject)

    def import_data_button_click(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        from database.Question.question_access import import_json_file
        import_json_file(path[0])
        print("KEC")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    import_data_frame = QtWidgets.QFrame()
    ui = Ui_import_data_frame()
    ui.setupUi(import_data_frame)
    import_data_frame.show()
    sys.exit(app.exec_())
