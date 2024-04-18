import sys
import sqlite3
from PyQt6.QtWidgets import (

       QMainWindow, QApplication, QDialog, QMessageBox,

       QFileDialog,QTableWidgetItem) #列出的项目除了QApplication，其余可根据界面增删

from PyQt6.QtGui import QImage, QPixmap

from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtMultimedia import QMediaPlayer 
from PyQt6.QtCore import QUrl 

import pandas as pd  
from datetime import datetime  
from Ui_untitled import Ui_Form
from draw_graph import DrawGraph,ScatterGraph
from Ui_weather import Ui_weather

class showlinewindow(QDialog,Ui_weather):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_7)
        self.pushButton_2.clicked.connect(self.draw_30)
        self.pushButton_3.clicked.connect(self.quit)

    def draw_7(self):
        try:
            print(end_data)
            draw_win = ScatterGraph()
            draw_win.draw_scatter([i for i in range(1,8)],[int(j[3].replace("℃",'')) for j in end_data[:7]])
            self.line1 = QGridLayout(self.groupBox)
            self.line1.addWidget(draw_win)

        except:
            reply = QMessageBox.warning(self, "确认", "存在错误")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()
    def draw_30(self):
        try:
            print(end_data)
            draw_win = DrawGraph()
            draw_win.draw_plot([i for i in range(1,31)],[int(j[3].replace("℃",'')) for j in end_data[:30]])


            self.line1 = QGridLayout(self.groupBox_2)
            self.line1.addWidget(draw_win)

        except:
            reply = QMessageBox.warning(self, "确认", "存在错误")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()
    def quit(self):
        self.hide()
        log_win.show()



class LogWindow(QDialog, Ui_Form):
    def __init__(self,df):
        super().__init__()
        self.setupUi(self)
        self.df = df
        self.pushButton.clicked.connect(self.find)
        self.pushButton_2.clicked.connect(self.draw)
    
    def draw(self):
        try:
            if end_data: 
                global draw_win
                draw_win = showlinewindow()
                draw_win.show() 
                self.hide()
        except:
            reply = QMessageBox.warning(self, "确认", "没有输入月份")
            if reply == QMessageBox.StandardButton.Yes:
                app = QApplication.instance()
                app.quit()

         

    def find(self):
        global end_data
        end_data = []
        try:
            for index, row in self.df.iterrows(): 
                format_str = "%Y年%m月%d日"  
                date_obj = datetime.strptime(row["日期"], format_str)
                if int(date_obj.month) == int(self.textEdit.toPlainText()):
                    data = [] 
                    data.extend([row["日期"], row["天气状况"]])
                    parts = row["最低气温/最高气温"].split(" / ")
                    data.extend(parts)
                    parts = row["风力风向(夜间/白天)"].split("/")
                    data.extend(parts[0].split())
                    data.extend(parts[1].split())
                    end_data.append(data)
        except:
                reply = QMessageBox.warning(self, "确认", "输入应为月份")
                if reply == QMessageBox.StandardButton.Yes:
                    app = QApplication.instance()
                    app.quit()

            
        title = "日期,天气情况,最低气温,最高气温,夜间风向,夜间风力,白天风向,白天风力"  
        self.tableWidget.setColumnCount(len(title.split(',')))  
        self.tableWidget.setHorizontalHeaderLabels(title.split(','))  
 
        self.tableWidget.setRowCount(0)  
          
        for i, item in enumerate(end_data):    
            if i >= self.tableWidget.rowCount():  
                self.tableWidget.insertRow(self.tableWidget.rowCount())  
              
            for j, row in enumerate(item):  
                new_cell = QTableWidgetItem(str(row))  
                new_cell.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
                self.tableWidget.setItem(i, j, new_cell)  
          
        self.tableWidget.resizeRowsToContents()  
        self.tableWidget.resizeColumnsToContents()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    df = pd.read_csv('Beijing.csv') 
    log_win = LogWindow(df)
    log_win.show()
    sys.exit(app.exec())
