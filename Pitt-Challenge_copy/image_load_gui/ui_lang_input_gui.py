# Form implementation generated from reading ui file '/Users/juliusarolovitch/Desktop/Pitt_Challenge2/image_load_gui/lang_input_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 131)
        Form.setStyleSheet("background-color: rgb(255, 216, 89)")
        self.lang_gui_header = QtWidgets.QLabel(Form)
        self.lang_gui_header.setGeometry(QtCore.QRect(160, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lang_gui_header.setFont(font)
        self.lang_gui_header.setStyleSheet("")
        self.lang_gui_header.setObjectName("lang_gui_header")
        self.lang_input_subheader = QtWidgets.QLabel(Form)
        self.lang_input_subheader.setGeometry(QtCore.QRect(100, 30, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lang_input_subheader.setFont(font)
        self.lang_input_subheader.setObjectName("lang_input_subheader")
        self.lang_input_box = QtWidgets.QGroupBox(Form)
        self.lang_input_box.setGeometry(QtCore.QRect(20, 60, 371, 51))
        self.lang_input_box.setStyleSheet("background-color : yellow;\n"
"border-radius: 5px;")
        self.lang_input_box.setTitle("")
        self.lang_input_box.setObjectName("lang_input_box")
        self.send_lang_button = QtWidgets.QPushButton(self.lang_input_box)
        self.send_lang_button.setGeometry(QtCore.QRect(300, 10, 61, 32))
        self.send_lang_button.setStyleSheet("background-color : rgb(255, 174, 0);\n"
"border: 1px solid black;\n"
"")
        self.send_lang_button.setObjectName("send_lang_button")
        self.lang_select_box = QtWidgets.QComboBox(self.lang_input_box)
        self.lang_select_box.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.lang_select_box.setStyleSheet("background-color: white; color: black; border: 1px solid black; border-left-radius: 5px;")
        self.lang_select_box.setObjectName("lang_select_box")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lang_gui_header.setText(_translate("Form", "AccessRx"))
        self.lang_input_subheader.setText(_translate("Form", "Prototype GUI For Pitt Challenge 2022"))
        self.send_lang_button.setText(_translate("Form", "Send"))
