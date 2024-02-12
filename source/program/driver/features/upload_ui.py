# Form implementation generated from reading ui file 'c:\Users\hp\Desktop\VSC\Cloned\Ebook-PR-Application\source\program\driver\features\upload.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1089, 681)
        Form.setMinimumSize(QtCore.QSize(1089, 650))
        Form.setStyleSheet("  QWidget {\n"
"        background-color: #333333;\n"
"        color: #ffffff;\n"
"        border: none;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        border-radius: 4px;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #5a5a5a;\n"
"        border: 1px solid #5a5a5a;\n"
"    }\n"
"    QCheckBox {\n"
"        color: #ffffff;\n"
"    }\n"
"    QLineEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QTextEdit {\n"
"        background-color: #4d4d4d;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #ffffff;\n"
"        padding: 5px;\n"
"    }\n"
"    QProgressBar {\n"
"        border: 1px solid #444444;\n"
"        border-radius: 7px;\n"
"        background-color: #2e2e2e;\n"
"        text-align: center;\n"
"        font-size: 10pt;\n"
"        color: white;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #3a3a3a;\n"
"        width: 5px;\n"
"    }\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        width: 10px;\n"
"        margin: 16px 0 16px 0;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background-color: #3a3a3a;\n"
"        height: 10px;\n"
"        margin: 0px 16px 0 16px;\n"
"    }\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: #444444;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QTabWidget {\n"
"        background-color: #2e2e2e;\n"
"        border: none;\n"
"    }\n"
"    QTabBar::tab {\n"
"        background-color: #2e2e2e;\n"
"        color: #b1b1b1;\n"
"        padding: 8px 20px;\n"
"        border-top-left-radius: 5px;\n"
"        border-top-right-radius: 5px;\n"
"        border: none;\n"
"    }\n"
" \n"
"    QTabBar::tab:selected, QTabBar::tab:hover {\n"
"        background-color: #3a3a3a;\n"
"        color: white;\n"
"    }")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1200, 200))
        self.label.setStyleSheet("font: 700 60pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(120, -1, 20, 120)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.upload_button_1 = QtWidgets.QPushButton(parent=Form)
        self.upload_button_1.setMinimumSize(QtCore.QSize(100, 60))
        self.upload_button_1.setMaximumSize(QtCore.QSize(200, 80))
        self.upload_button_1.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.upload_button_1.setObjectName("upload_button_1")
        self.horizontalLayout_2.addWidget(self.upload_button_1)
        self.file_label_1 = QtWidgets.QLabel(parent=Form)
        self.file_label_1.setMinimumSize(QtCore.QSize(600, 60))
        self.file_label_1.setMaximumSize(QtCore.QSize(700, 80))
        self.file_label_1.setStyleSheet("font: italic 12pt \"Segoe UI\";\n"
"")
        self.file_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.file_label_1.setObjectName("file_label_1")
        self.horizontalLayout_2.addWidget(self.file_label_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(19, -1, 20, 100)
        self.horizontalLayout_3.setSpacing(300)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.upload_local_file = QtWidgets.QPushButton(parent=Form)
        self.upload_local_file.setMinimumSize(QtCore.QSize(100, 60))
        self.upload_local_file.setMaximumSize(QtCore.QSize(200, 80))
        self.upload_local_file.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.upload_local_file.setObjectName("upload_local_file")
        self.horizontalLayout_3.addWidget(self.upload_local_file)
        self.cancel_process = QtWidgets.QPushButton(parent=Form)
        self.cancel_process.setMinimumSize(QtCore.QSize(100, 60))
        self.cancel_process.setMaximumSize(QtCore.QSize(200, 80))
        self.cancel_process.setStyleSheet("font: 700 18pt \"Segoe UI\";")
        self.cancel_process.setObjectName("cancel_process")
        self.horizontalLayout_3.addWidget(self.cancel_process)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Upload Local Spreadsheet"))
        self.upload_button_1.setText(_translate("Form", "Upload"))
        self.file_label_1.setText(_translate("Form", "No file selected "))
        self.upload_local_file.setText(_translate("Form", "Submit"))
        self.cancel_process.setText(_translate("Form", "Cancel"))