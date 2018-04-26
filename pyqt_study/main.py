# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
from test1 import Ui_test
 

class Widget1(QtWidgets.QWidget, Ui_test):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self) # Ui_Form.setupUi
    
    def on_bu_1_clicked(self):
        """pbHello为点击按钮的objectName"""
        self.textArea.setText('11111111111')
        #text11111为需要修改的部分

    def on_bu_2_clicked(self):
        """pbHello为点击按钮的objectName"""
        self.textArea.setText('222222222222222')
        #text11111为需要修改的部分

    def on_bu_3_clicked(self):
        """pbHello为点击按钮的objectName"""
        self.textArea.setText('333333333333')
        #text11111为需要修改的部分

    def on_bu_4_clicked(self):
        """pbHello为点击按钮的objectName"""
        self.textArea.setText('44444')
        #text11111为需要修改的部分

        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget1()
    QtWidgets.QMessageBox.information(None, "提示",
        "这是来自wjsaya(sayawj@163.com)的测试消息\n\n"
        "支持使用\\n换行\n"
        "调用方法: QtWidgets.QMessageBox.information"
        )
    widget.show()
    sys.exit(app.exec_())
