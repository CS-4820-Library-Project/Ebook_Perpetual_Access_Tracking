# Form implementation generated from reading ui file 'source/features/ui/SearchPage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Search_page(object):
    def setupUi(self, Search_page):
        Search_page.setObjectName("Search_page")
        Search_page.resize(725, 725)
        Search_page.setAutoFillBackground(False)
        Search_page.setStyleSheet("    QWidget {\n"
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
"        background-color: #ffffff;\n"
"        border: 1px solid #4d4d4d;\n"
"        color: #000000;\n"
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
        self.formLayout = QtWidgets.QFormLayout(Search_page)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 100, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Search_page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 700 60pt \"Segoe UI\";")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 100, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Search_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=Search_page)
        self.pushButton.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=Search_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=Search_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioButton = QtWidgets.QRadioButton(parent=Search_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=Search_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 200, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Search_page)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.verticalLayout)

        self.retranslateUi(Search_page)
        QtCore.QMetaObject.connectSlotsByName(Search_page)

    def retranslateUi(self, Search_page):
        _translate = QtCore.QCoreApplication.translate
        Search_page.setWindowTitle(_translate("Search_page", "Search"))
        self.label.setText(_translate("Search_page", "E-Book Search"))
        self.pushButton.setText(_translate("Search_page", "Search"))
        self.radioButton_2.setText(_translate("Search_page", "Keyword"))
        self.radioButton_2.hide()
        self.radioButton_3.setText(_translate("Search_page", "OCN"))
        self.radioButton.setText(_translate("Search_page", "Title"))
        self.radioButton_4.setText(_translate("Search_page", "eISBN"))
        self.pushButton_2.setText(_translate("Search_page", "Cancel Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search_page = QtWidgets.QWidget()
    ui = Ui_Search_page()
    ui.setupUi(Search_page)
    Search_page.show()
    sys.exit(app.exec())
