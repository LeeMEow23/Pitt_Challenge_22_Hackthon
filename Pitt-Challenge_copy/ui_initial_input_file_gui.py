# Form implementation generated from reading ui file '/Users/juliusarolovitch/Desktop/Pitt_Challenge2/initial_input_file_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 330)
        Form.setStyleSheet("background-color: rgb(255, 216, 89)")
        self.file_input_header = QtWidgets.QLabel(Form)
        self.file_input_header.setGeometry(QtCore.QRect(170, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.file_input_header.setFont(font)
        self.file_input_header.setStyleSheet("")
        self.file_input_header.setObjectName("file_input_header")
        self.file_input_box = QtWidgets.QGroupBox(Form)
        self.file_input_box.setGeometry(QtCore.QRect(20, 60, 371, 51))
        self.file_input_box.setStyleSheet("background-color : yellow;\n"
"border-radius: 5px;")
        self.file_input_box.setTitle("")
        self.file_input_box.setObjectName("file_input_box")
        self.image_text_input = QtWidgets.QPlainTextEdit(self.file_input_box)
        self.image_text_input.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.image_text_input.setStyleSheet("background-color : white;\n"
"border: 1px solid black;\n"
"color: black;\n"
"")
        self.image_text_input.setObjectName("image_text_input")
        self.send_image_button = QtWidgets.QPushButton(self.file_input_box)
        self.send_image_button.setGeometry(QtCore.QRect(300, 10, 61, 32))
        self.send_image_button.setStyleSheet("background-color : rgb(255, 174, 0);\n"
"border: 1px solid black;\n"
"")
        self.send_image_button.setObjectName("send_image_button")
        self.dose_select_header = QtWidgets.QLabel(Form)
        self.dose_select_header.setGeometry(QtCore.QRect(30, 280, 60, 16))
        self.dose_select_header.setText("")
        self.dose_select_header.setObjectName("dose_select_header")
        self.file_input_subheader = QtWidgets.QLabel(Form)
        self.file_input_subheader.setGeometry(QtCore.QRect(110, 30, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.file_input_subheader.setFont(font)
        self.file_input_subheader.setObjectName("file_input_subheader")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.file_input_header.setText(_translate("Form", "AccessRx"))
        self.image_text_input.setPlainText(_translate("Form", "Enter image file name"))
        self.send_image_button.setText(_translate("Form", "Send"))
        self.file_input_subheader.setText(_translate("Form", "Prototype GUI For Pitt Challenge 2022"))
