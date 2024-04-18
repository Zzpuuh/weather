from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PyQt6.QtWidgets import (

       QMainWindow, QApplication, QDialog, QMessageBox,

       QFileDialog,QTableWidgetItem) #列出的项目除了QApplication，其余可根据界面增删

import sys

class DrawGraph(FigureCanvas):
    def __init__ (self,parent=None,width=5,height=5,dpi=100):
    #Figure相当于画板、FigureCanvas相当于一张画纸
        self.board=Figure(figsize=(width,height),dpi=dpi)
        FigureCanvas.__init__(self,self.board)
        self.setParent(parent)


    def draw_plot(self,x,y):
        self.axes =self.board.add_subplot(111)
        self.axes.plot(x,y)

class ScatterGraph(DrawGraph):  
    def __init__(self, parent=None, width=5, height=5, dpi=100):  
        super().__init__(parent, width, height, dpi)  
  
    def draw_scatter(self, x, y): 
        self.axes =self.board.add_subplot(111) 
        self.axes.scatter(x, y) 
if __name__ == '__main__':

    app = QApplication(sys.argv)
    log_win = DrawGraph()
    log_win.show()
    sys.exit(app.exec())