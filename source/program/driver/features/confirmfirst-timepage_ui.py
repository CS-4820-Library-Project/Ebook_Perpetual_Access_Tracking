# Form implementation generated from reading ui file 'c:\Users\hp\Desktop\VSC\Cloned\Ebook-PR-Application\source\program\driver\features\confirmfirst-timepage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 280)
        Form.setStyleSheet("    QWidget {\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 481, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 700 20pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 481, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confirm_update_first_time = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.confirm_update_first_time.setMinimumSize(QtCore.QSize(0, 0))
        self.confirm_update_first_time.setMaximumSize(QtCore.QSize(120, 16777215))
        self.confirm_update_first_time.setStyleSheet("font: 700 18pt \"Segoe UI\";\n"
"")
        self.confirm_update_first_time.setObjectName("confirm_update_first_time")
        self.horizontalLayout.addWidget(self.confirm_update_first_time)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Your CRKN data is now up to date!"))
        self.confirm_update_first_time.setText(_translate("Form", "Ok"))