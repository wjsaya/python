# -*- coding: utf-8 -*-
import os
import sys
import time

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets

import img_func as img_operate
from Ui_about import Ui_MainWindow as Ui_about
from Ui_gray_enhance import Ui_MainWindow as Ui_gray_enhance
from Ui_mainWindow import Ui_MainWindow
from Ui_noisy import Ui_MainWindow as Ui_child


def set_style(in_object):
    qss_file = open('./default.qss').read()
    in_object.setStyleSheet(qss_file)

class noisy_child(QtWidgets.QMainWindow, Ui_child):
    def __init__(self, parent=None): 
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        set_style(self)
        self.setWindowIcon(QtGui.QIcon('./icons/mainWindow.jpg'))


class gray_enhance_child(QtWidgets.QMainWindow, Ui_gray_enhance):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        set_style(self)
        self.setWindowIcon(QtGui.QIcon('./icons/mainWindow.jpg'))


class about_child(QtWidgets.QMainWindow, Ui_about):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        set_style(self)
        self.setWindowIcon(QtGui.QIcon('./icons/mainWindow.jpg'))
        a = Image.open("./icons/mainWindow.jpg").convert('RGBA')
        a = QtGui.QPixmap.fromImage(ImageQt(a))
        a = a.scaled(200, 200, aspectRatioMode=QtCore.Qt.KeepAspectRatio)
        self.bgp.setPixmap(a)


class MainWindow(QtWidgets.QMainWindow,  Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        set_style(self)
        self.__init_slot()
        self.__init_noisy_child()
        self.__init_gray_enhance()
        self.__init_about()
        self.setWindowIcon(QtGui.QIcon('./icons/mainWindow.jpg'))

    def __init_slot(self):
        self.action_quit.triggered.connect(self.close)
        self.action_salt_noise.triggered.connect(lambda: self.salt_noise(0.001))
        self.action_gaussian_noise.triggered.connect(lambda: self.gaussian_noise(avg=1, b=20))
        self.action_mean_filter.triggered.connect(lambda: self.mean_filter(a=1, b=3))
        self.action_median_filter.triggered.connect(lambda: self.median_filter(a=3))
        self.action_gauss_fliter.triggered.connect(lambda: self.gauss_fliter(a=7, b=7, c=0))
        self.action_linear.triggered.connect(lambda: self.linear_enhance(a=125, b=225))
        self.action_power.triggered.connect(lambda: self.power_enhance(a=256, b=0.5))
        

    def __init_noisy_child(self):
        self.noisy_child = noisy_child()
        self.noisy_child.submit_jyzs.clicked.connect\
            (lambda:self.salt_noise(self.noisy_child.jyzs_value.value()))
        self.noisy_child.submit_gszs.clicked.connect\
            (lambda:self.gaussian_noise(avg=self.noisy_child.gszs_value1.value(), b=self.noisy_child.gszs_value2.value()))
        self.noisy_child.submit_jzlb.clicked.connect\
            (lambda:self.mean_filter(a=self.noisy_child.value_jzlb1.value(), b=self.noisy_child.value_jzlb2.value()))
        self.noisy_child.submit_zzlb.clicked.connect\
            (lambda:self.median_filter(a=self.noisy_child.value_zzlb.value()))
        self.noisy_child.submit_gslb.clicked.connect\
            (lambda: self.gauss_fliter(a=self.noisy_child.value_gslb_ab.value(), b=self.noisy_child.value_gslb_ab.value(), c=self.noisy_child.value_gslb_c.value()))
            

    def __init_gray_enhance(self):
        self.gray_enhance_child = gray_enhance_child()
        self.gray_enhance_child.submit_linear.clicked.connect\
            (lambda: self.linear_enhance(a=self.gray_enhance_child.value_linear_a.value(), b=self.gray_enhance_child.value_linear_b.value()))
        self.gray_enhance_child.submit_power.clicked.connect\
            (lambda: self.power_enhance(a=self.gray_enhance_child.value_power_a.value(), b=self.gray_enhance_child.value_power_b.value()))

    def __init_about(self):
        self.about_child = about_child()

    def on_action_about_triggered(self):
        self.about_child.show()

    def on_action_noisy_menu_triggered(self):
        self.noisy_child.show()


    def on_action_gray_enhance_menu_triggered(self):
        self.gray_enhance_child.show()


    def alert(self):
        print(self.noisy_child.doubleSpinBox.value())


    def mousePressEvent(self, event):
        if self.thumb_origin.underMouse():   #big_prev是否在鼠标下面
            if self.thumb_origin.pixmap():
                self.label_big_prev.setText("原图")
                self.big_prev.setPixmap(self.__no_scaled_origin_pixmap)

        if self.thumb_prev.underMouse():   #big_prev是否在鼠标下面
            if self.thumb_prev.pixmap():
                self.label_big_prev.setText("当前修改")
                self.big_prev.setPixmap(self.__no_scaled_big_prev_pixmap)


    def wheelEvent(self, event):
        if self.big_prev.pixmap() is None:  #big_prev无内容，无视滚轮
            #print("鼠标不在big_prev上")
            return

        if self.big_prev.underMouse():   #big_prev是否在鼠标下面
            self.delta = event.angleDelta().y()
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers != QtCore.Qt.ControlModifier:  #未按ctrl滚轮，无视
            #    #print('Ctrl 未按下')
                return

            big_prev_height = self.big_prev.height()
            big_prev_width = self.big_prev.width()
            self.big_prev_pixmap = self.__no_scaled_big_prev_pixmap.copy()
            if(self.delta > 0):
                self.big_prev_scaled = self.big_prev_pixmap.scaled(big_prev_width*1.1, big_prev_height*1.1, aspectRatioMode=QtCore.Qt.KeepAspectRatio) 
                self.big_prev.setPixmap(self.big_prev_scaled)
                self.statusBar().showMessage("当前图片尺寸：" + str(big_prev_width) + ' X ' + str(big_prev_height))
            else:
                self.big_prev_scaled = self.big_prev_pixmap.scaled(big_prev_width*0.9, big_prev_height*0.9, aspectRatioMode=QtCore.Qt.KeepAspectRatio) 
                self.big_prev.setPixmap(self.big_prev_scaled)
                self.statusBar().showMessage("当前图片尺寸：" + str(big_prev_width) + ' X ' + str(big_prev_height))


    def closeEvent(self, event): 
        #重写closeEvent,添加确认弹框
        if (isinstance(self.thumb_prev.pixmap(), QtGui.QPixmap)) is False:
            #sys.exit() 
            # 如果不用if嵌套,直接sys.exit()也可,但是if嵌套逻辑更清晰.
            # 如果self.img_prev.pixmap()不是Qpixmap,那么img_prev标签则没有图片,那么直接同意closeEvent退出即可.
            event.accept()
        else:
            checkMsgBox = QtWidgets.QMessageBox(self)
            checkMsgBox.setWindowTitle("退出?")
            checkMsgBox.setWindowIcon(QtGui.QIcon('./icons/quit.ico'))
            savequitButton = checkMsgBox.addButton(self.tr("保存&退出"), QtWidgets.QMessageBox.ActionRole)
            justquitButton = checkMsgBox.addButton(self.tr("直接退出"), QtWidgets.QMessageBox.ActionRole)
            cancelButton = checkMsgBox.addButton("手滑了,取消",QtWidgets.QMessageBox.ActionRole)
            checkMsgBox.setText(self.tr("对图片的修改还未保存,直接退出?"))
            checkMsgBox.exec_()
        
            button = checkMsgBox.clickedButton()
            if button == savequitButton:
                self.on_button_save_clicked()
                event.accept()
            elif button == justquitButton:
                event.accept()
            elif button == cancelButton:
                event.ignore()


    def put_thumb_prev(self, label_name):
        if label_name == 'thumb_origin':
            self.thumb_temp_pixmap = self.__no_scaled_origin_pixmap.copy()
            self.thumb_origin.setPixmap(self.thumb_temp_pixmap.scaled(self.thumb_origin.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
            #print("origin已更改")
        elif label_name == 'thumb_prev':
            self.thumb_temp_pixmap = self.__no_scaled_big_prev_pixmap.copy()
            self.thumb_prev.setPixmap(self.thumb_temp_pixmap.scaled(self.thumb_prev.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
            #print("prev已更改")



    def dd(self):
        self.statusBar().showMessage('关于我们')   
        QtWidgets.QMessageBox.information(None, "关于我们",
            "第5组\n"+
            "组长:杨宗霖\n"+
            "组员:王啸宇,仇喆,胡博")
    

    @QtCore.pyqtSlot()
    def on_action_open_triggered(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self,
		    "选择想要编辑的图片--wjsaya.top",
		    "./",
		    "常见图片格式(*.jpeg *.jpg *.png *.bmp) ;; 所有文件 (*)")
        if self.fileName[0] == '' and self.fileName[1] == '':   #如果未选择图片,不做操作
            return

        self.statusBar().showMessage("已打开:" + self.fileName[0])
        #self.__no_scaled_origin_pixmap = QtGui.QPixmap(self.fileName[0])
        img = Image.open(self.fileName[0]).convert('RGBA')
        self.__no_scaled_origin_pixmap = QtGui.QPixmap.fromImage(ImageQt(img))
        self.__no_scaled_big_prev_pixmap = self.__no_scaled_origin_pixmap.copy()   
        self.big_prev.setPixmap(self.__no_scaled_origin_pixmap)
        self.put_thumb_prev(label_name='thumb_origin')

    
    @QtCore.pyqtSlot()
    def on_action_save_triggered(self):     
        QtWidgets.QMessageBox.information(None, "提示",
            "此操作会将右边预览窗口的图片保存到本地\n"
            "如果需要更改图片大小,请将其缩放到所需大小"
            "然后再保存\n")
        self.saveimg_name, self.saveimg_type = QtWidgets.QFileDialog.getSaveFileName(self,  
            "文件保存",
            "./",
            "Image files(*.jpeg *.jpg *.png *.bmp) ;; 所有文件 (*)")

        if self.saveimg_name != '':
            try:
                self.big_prev.pixmap().save(self.saveimg_name)
                self.statusBar().showMessage("已保存为:" + self.saveimg_name)
            except:
                self.statusBar().showMessage("保存失败")

    @QtCore.pyqtSlot()
    def on_action_2gray_triggered(self):
        img = Image.fromqpixmap(self.big_prev.pixmap()).convert('L')
        img = QtGui.QPixmap.fromImage(ImageQt(img))
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("灰度图转换完毕")


    @QtCore.pyqtSlot()
    def on_action_2binary_triggered(self):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.otsu_im(img)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("二值图转换完毕")


    @QtCore.pyqtSlot()
    def on_JX_v_clicked(self):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.JX(img, type='v')
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("水平镜像")


    @QtCore.pyqtSlot()
    def on_JX_s_clicked(self):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.JX(img, type='s')
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("垂直镜像")

    @QtCore.pyqtSlot(float)
    def salt_noise(self, percetage=0):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.add_salt_noise(img, percetage)  #0.2参数改为可更改,参数越小,噪点越少
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("加->椒盐噪声")


    @QtCore.pyqtSlot(int, int)
    def gaussian_noise(self, avg=0, b=0):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.add_gaussian_noise(img, avg, b)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("加->高斯噪声")


    @QtCore.pyqtSlot(int, int)
    def mean_filter(self, a=0, b=0):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.mean_filter(img, a, b)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("均值滤波")
        

    @QtCore.pyqtSlot(int)
    def median_filter(self, a=3):
        if a % 2 == 0:    #a不能为偶数,遇到偶数+1
            a = a + 1
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.median_filter(img)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("中值滤波")
        

    @QtCore.pyqtSlot(int, int, int)
    def gauss_fliter(self, a=7, b=7, c=0):
        if a % 2 == 0:    #ab不能为偶数,遇到偶数+1
            a = a + 1
            b = b + 1
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.gauss_fliter(img, a, b, c)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("高斯滤波")


    @QtCore.pyqtSlot(int, int)
    def linear_enhance(self, a, b):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.linearTransformation(img, a, b)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("线性变换")

    @QtCore.pyqtSlot(int, float)
    def power_enhance(self, a=256, b=0.5):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.powerTransformation(img, a, b)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("幂变换")


    @QtCore.pyqtSlot()
    def on_action_6_triggered(self):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.firstDifference(img)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("一阶差分")


    @QtCore.pyqtSlot()
    def on_action_7_triggered(self):
        img = Image.fromqpixmap(self.big_prev.pixmap())
        img = img_operate.secondDifference(img)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("二阶差分")


    def on_slider_PY_V_valueChanged(self):
        if '_MainWindow__no_PY_V_img' not in dir(self):
            self.__no_PY_V_img = self.big_prev.pixmap().copy()
            self.PY_unit_H = int(self.big_prev.pixmap().height() / 80)
        value = self.slider_PY_V.value() * self.PY_unit_H
        img = Image.fromqpixmap(self.__no_PY_V_img)
        img = img_operate.ImgOfffSet(img, 0, value)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("垂直平移")


    def on_slider_PY_S_valueChanged(self):
        if '_MainWindow__no_PY_S_img' not in dir(self):
            self.__no_PY_S_img = self.big_prev.pixmap().copy()
            self.PY_unit_W = int(self.big_prev.pixmap().width() / 80)
        value = self.slider_PY_S.value() * self.PY_unit_W
        img = Image.fromqpixmap(self.__no_PY_S_img)
        img = img_operate.ImgOfffSet(img, value, 0)
        self.big_prev.setPixmap(img)
        self.__no_scaled_big_prev_pixmap = img.copy()
        self.put_thumb_prev(label_name='thumb_prev')
        self.statusBar().showMessage("水平平移")


    @QtCore.pyqtSlot()
    def on_action_hdzft_triggered(self):
        a = Image.fromqpixmap(self.__no_scaled_big_prev_pixmap)
        img_operate.getHistogramList(a)


#################################下方为自制以及未作要求部分##############################################################################
    @QtCore.pyqtSlot()
    def on_action_own_2gray_triggered(self):
        self.statusBar().showMessage("灰度转换中...")
        import own_made as f
        a = Image.fromqpixmap(self.__no_scaled_big_prev_pixmap)
        aa = f.toGray(a)
        self.big_prev.setPixmap(aa)
        self.__no_scaled_big_prev_pixmap = aa.copy()
        self.statusBar().showMessage("灰度转换完毕")


    @QtCore.pyqtSlot()
    def on_action_own_2binary_triggered(self):
        self.statusBar().showMessage("灰度转换二值图中...")
        import own_made as f
        a = Image.fromqpixmap(self.__no_scaled_big_prev_pixmap)
        aa = f.do2(a)
        self.big_prev.setPixmap(aa)
        self.__no_scaled_big_prev_pixmap = aa.copy()
        self.statusBar().showMessage("灰度转换二值图完毕")

        
    def on_slider_XZ_valueChanged(self):
    #未做要求，不再继续完善
        if 'originXZOrigin' not in dir(self):
            self.originXZOrigin = self.big_prev.pixmap().copy()    #保存预览图最初样貌,scaled会调用
            self.prevXZ2Origin = self.originXZOrigin.copy()
        else:
            self.originXZOrigin = self.prevXZ2Origin.copy()

        value_now = self.slider_XZ.value() * 3.6
        pixmap = Image.fromqpixmap(self.originXZOrigin)
        pixmap = pixmap.rotate(value_now) #两
        QtImage1 = ImageQt(pixmap.convert('RGBA'))
        pixmap = QtGui.QPixmap.fromImage(QtImage1)
        self.big_prev.setPixmap(pixmap)
        self.__no_scaled_big_prev_pixmap = pixmap.copy()
        self.put_thumb_prev(label_name='thumb_prev')
       ##有问题部分


        

if __name__ == "__main__":
    app=0
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
