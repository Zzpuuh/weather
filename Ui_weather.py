# Form implementation generated from reading ui file 'c:\Users\朱子豪\Desktop\weather\weather.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_weather(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 523)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(70, 39, 541, 181))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 220, 541, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 410, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 410, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 410, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "温度变化情况"))
        self.groupBox.setTitle(_translate("Form", "7日温度变化"))
        self.groupBox_2.setTitle(_translate("Form", "30日温度变化"))
        self.pushButton.setText(_translate("Form", "显示7天温度"))
        self.pushButton_2.setText(_translate("Form", "显示30天温度"))
        self.pushButton_3.setText(_translate("Form", "退出"))