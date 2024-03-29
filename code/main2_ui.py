# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sarak\02_new_code\01_Practice\PyQt5\taskmanager\main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 528)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 40, 661, 211))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 250, 661, 171))
        self.listWidget.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"background-color: rgb(217, 233, 255);")
        self.listWidget.setObjectName("listWidget")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(580, 425, 81, 31))
        self.saveButton.setStyleSheet("QPushButton#saveButton {\n"
"    background-color: rgb(24, 11, 170);\n"
"    font: 700 8pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgb(24, 11, 170); \n"
"}\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"    background-color: #3498db; \n"
"}\n"
"")
        self.saveButton.setCheckable(True)
        self.saveButton.setDefault(False)
        self.saveButton.setObjectName("saveButton")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(370, 425, 61, 31))
        self.addButton.setStyleSheet("QPushButton#addButton {\n"
"    background-color: rgb(24, 11, 170);\n"
"    font: 700 8pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgb(24, 11, 170); \n"
"}\n"
"\n"
"QPushButton#addButton:pressed {\n"
"    background-color: #3498db; \n"
"}\n"
"")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 41))
        self.label.setStyleSheet("background-color: rgb(69, 2, 127);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Segoe UI\";\n"
"border-radius:8px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.taskLineEdit = QtWidgets.QLineEdit(Form)
        self.taskLineEdit.setGeometry(QtCore.QRect(0, 420, 361, 41))
        self.taskLineEdit.setStyleSheet("\n"
"border-top-color: rgb(0, 0, 0);")
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.removeButton = QtWidgets.QPushButton(Form)
        self.removeButton.setGeometry(QtCore.QRect(448, 425, 121, 31))
        self.removeButton.setStyleSheet("QPushButton#removeButton {\n"
"    background-color: rgb(24, 11, 170);\n"
"    font: 700 8pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgb(24, 11, 170); \n"
"}\n"
"\n"
"QPushButton#removeButton:pressed {\n"
"    background-color: #3498db; \n"
"}\n"
"")
        self.removeButton.setObjectName("removeButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 460, 661, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\sarak\\02_new_code\\01_Practice\\PyQt5\\taskmanager\\../../../../Downloads/bbbb.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Save changes"))
        self.addButton.setText(_translate("Form", "Add Task"))
        self.label.setText(_translate("Form", "Task Manager"))
        self.removeButton.setText(_translate("Form", "Remove Selected Task"))
