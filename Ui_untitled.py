# Form implementation generated from reading ui file 'c:\Users\朱子豪\Desktop\weather\untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 551)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(690, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 50, 621, 31))
        self.textEdit.setObjectName("textEdit")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 741, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 473, 211, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.textEdit.setPlaceholderText(_translate("Form", "请输入月份"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "日期"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "天气情况"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "最低气温"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "最高气温"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "夜间风向"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "夜间风力"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "白天风力"))
        self.pushButton_2.setText(_translate("Form", "查看天气变化趋势"))
