# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from ui_widget import Ui_Form
 
class Widget1(QtGui.QWidget, Ui_Form):
    """QtGui.QWidget和界面设计时选择的类型一致"""
    def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.setupUi(self) # Ui_Form.setupUi
    
 
class Widget2(QtGui.QWidget, Ui_Form):
    """QtGui.QWidget和界面设计时选择的类型一致"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self) # Ui_Form.setupUi
    
    @QtCore.pyqtSignature("")
    def on_pbHello_clicked(self):
        """pbHello和界面设计时的objectName一致"""
        self.lHello.setText('Hello PyQt4') # lHello和界面设计的objectName一致
        
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
