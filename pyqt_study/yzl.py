# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
 

class MainWindow(QtWidgets.QMainWindow,  Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_button_open_clicked(self): 
        fileName = ['1', '2']
       # fileName = QtWidgets.QFileDialog.getOpenFileName(self,"打开图片","C:/Users/saya/Pictures/Screenshots","Image files(*.jpg *.png *.bmp) ;; 所有文件 * ")
        #可加 css
        self.label.setStyleSheet('''
        color:white; 
        background-color:black; 
        ''')
        self.label.setText("已打开:" + fileName[0])
        self.setWindowTitle("打开")


        scene = QtWidgets.QGraphicsScene()
        #在场景中添加文字
        im = QtGui.QPixmap.load("./lena.jpeg")
        
        self.img_origin.setPixmap(im)
       # self.img_origin.resize(im.width(), im.height())



    @pyqtSlot()
    def on_button_save_clicked(self):
        self.label.setText("保存 按钮按下")
        self.setWindowTitle("保存")

    @pyqtSlot()
    def on_button_1_clicked(self):
        self.label.setText("彩->灰 按钮按下")
        self.setWindowTitle("彩->灰")

    @pyqtSlot()
    def on_button_2_clicked(self):
        self.label.setText("灰->二 按钮按下")
        self.setWindowTitle("灰->二")

    @pyqtSlot()
    def on_button_3_clicked(self):
        self.label.setText("几何变换 按钮按下")
        self.setWindowTitle("几何变换")

    @pyqtSlot()
    def on_button_4_clicked(self):
        self.label.setText("去噪 按钮按下")
        self.setWindowTitle("去噪")

    @pyqtSlot()
    def on_button_5_clicked(self):
        self.label.setText("push 按钮按下")
        self.setWindowTitle("push")

    @pyqtSlot()
    def on_button_6_clicked(self):
        self.label.setText("边缘提取 按钮按下")
        self.setWindowTitle("边缘提取")

    @pyqtSlot()
    def on_button_7_clicked(self):
        self.label.setText("加躁 按钮按下")
        self.setWindowTitle("加躁")

    @pyqtSlot()
    def on_button_8_clicked(self):
        self.label.setText("退出 按钮按下")
        self.setWindowTitle("退出")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
   # w = MainWindow()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
