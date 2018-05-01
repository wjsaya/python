# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)

    def on_button_open_clicked(self):
        self.img_Origin.setText('222222222222222')
        #text11111为需要修改的部分


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()  
    sys.exit(app.exec_())