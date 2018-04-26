# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(421, 339)
        self.textArea = QtWidgets.QLabel(test)
        self.textArea.setGeometry(QtCore.QRect(20, 60, 54, 16))
        self.textArea.setObjectName("textArea")
        self.bu_2 = QtWidgets.QPushButton(test)
        self.bu_2.setGeometry(QtCore.QRect(60, 240, 75, 23))
        self.bu_2.setObjectName("bu_2")
        self.bu_3 = QtWidgets.QPushButton(test)
        self.bu_3.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.bu_3.setObjectName("bu_3")
        self.bu_4 = QtWidgets.QPushButton(test)
        self.bu_4.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.bu_4.setObjectName("bu_4")
        self.bu_1 = QtWidgets.QPushButton(test)
        self.bu_1.setGeometry(QtCore.QRect(30, 190, 75, 23))
        self.bu_1.setObjectName("bu_1")

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "测试样例"))
        self.textArea.setText(_translate("test", "待更改"))
        self.bu_2.setText(_translate("test", "bu2"))
        self.bu_3.setText(_translate("test", "bu3"))
        self.bu_4.setText(_translate("test", "bu4"))
        self.bu_1.setText(_translate("test", "bu1"))

