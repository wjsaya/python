#!/usr/bin/env python  
#-*- coding: utf-8 -*-  

import cv2
import numpy
import random
from PIL import Image, ImageChops
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
import scipy.signal as signal
from matplotlib import pyplot


def __init__(self, parent=None):
    pass
def otsu_im(imgin):
    '''
    in:     Qpixmap
    大津法(OTSU)求T并二值化
    out:    Qpixmap
    '''
    img = numpy.asarray(imgin)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    img = Image.fromarray(dst)  #二值图转回PIL格式
    imgout = QtGui.QPixmap.fromImage(ImageQt(img))
    return imgout

def JX(imgin, type):
    '''
    in:    Qpixmap
    镜像
    out:   Qpixmap
    '''
    if type == 's':
        out = imgin.transpose(Image.FLIP_TOP_BOTTOM) 
    elif type == 'v':
        out = imgin.transpose(Image.FLIP_LEFT_RIGHT)
    imgout = out.convert('RGBA')  #转PIL的RGB为RGBA
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))
    return imgout
    
def add_salt_noise(imgin, percetage):
    '''
    in:    Qpixmap
    加椒盐噪声
    out:   Qpixmap
    '''
    imgin = numpy.asarray(imgin).copy()
    NoiseNum = int(percetage * imgin.shape[0] * imgin.shape[1])
    for i in range(NoiseNum):
        randX = random.randint(0,imgin.shape[0]-1)
        randY = random.randint(0,imgin.shape[1]-1)
        if random.randint(0,1) <= 0.5:
            imgin[randX,randY] = 0
        else:
            imgin[randX,randY] = 255
    imgin = Image.fromarray(imgin).convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
    return imgout
    
def add_gaussian_noise(imgin, avg, b):
    '''
    in:    Qpixmap
    加高斯噪声
    out:   Qpixmap
    '''
    imgin = numpy.asarray(imgin).copy()  
    s_dsplit = []
    for d in range(imgin.shape[2]):
        img = imgin[:, :, d]
        # 添加均值为 avg, 标准差为 b 的加性高斯白噪声
        img = img + numpy.random.normal(avg, b, img.shape)        #参数意思? 
        if numpy.min(img) >= 0 and numpy.max(img) <= 255:
            imgout = img
        # 对比拉伸
        else:
            img = img - numpy.full(img.shape, numpy.min(img))
            img = img * 255 / numpy.max(img)
            img = img.astype(numpy.uint8)
            imgout = img
        s_dsplit.append(imgout)
    imgout = numpy.dstack(s_dsplit)
    imgout = Image.fromarray(imgout).convert('RGBA') 
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))    
    return imgout

def mean_filter(imgin, m=1, n=3):
    '''
    in:    Qpixmap
    均值滤波
    out:   Qpixmap
    '''
    imgin = numpy.asarray(imgin).copy()
    imgin = cv2.blur(imgin,(m, n))                  #m,n为滤波器大小
    imgin = Image.fromarray(imgin).convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
    return imgout


def median_filter(imgin, a=3):
    '''
    in:    Qpixmap
    中值滤波
    out:   Qpixmap
    '''
    imgin = numpy.asarray(imgin).copy()
    imgin = cv2.medianBlur(imgin, a)                 #图片, 孔径的尺寸，一个大于1的奇数。
    imgin = Image.fromarray(imgin).convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
    return imgout


def gauss_fliter(imgin, a=7, b=7, c=0):
    '''
    in:    Qpixmap
    高斯滤波
    out:   Qpixmap
    '''
    imgin = numpy.asarray(imgin).copy()
    imgin = cv2.GaussianBlur(imgin, (a, b), c)                   #参数意思?
    imgin = Image.fromarray(imgin).convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
    return imgout
def SaltAndPepper(src, percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255          
    cv2.imshow('PepperandSalt', NoiseImg)


def Laplace(self, imgin):
    '''
    in:    Qpixmap
    Laplace的扩展算子,边缘检测
    out:   Qpixmap
    '''
    suanzi2 = numpy.array([[1, 1, 1],
                        [1,-8, 1],
                        [1, 1, 1]])
    imgin = numpy.asarray(imgin).copy()
    print(imgin.size)
    image2 = signal.convolve2d(imgin, suanzi2, mode="same")
    image2 = (image2/float(image2.max()))*255
    image2[image2>image2.mean()] = 255
    imgin = Image.fromarray(image2) #二值图转回PIL格式,转PIL的RGB为RGBA
    return imgin


def ImgOfffSet(imgin, xoff, yoff):
    width, height = imgin.size
    imgout = ImageChops.offset(imgin, xoff, yoff)
    imgout.paste((0,0,0),(0,0, xoff, height))
    imgout.paste((0,0,0),(0,0, width, yoff))
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout.convert('RGBA')))
    return imgout


def linearTransformation(imgin, a=125, b=225):
    # 线性变换
    result = imgin.convert('L').crop()
    table = []
    for x in range(0, 256):
        if x < a:
            table.append(int(0.56 * x))
        elif x < b:
            table.append(int(1.1 * x - 67.5))
        else:
            table.append(int(2.5 * x - 382.5))
    imgout = result.point(table, 'L').convert('RGBA')
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))
    return imgout
   

def powerTransformation(imgin, a=256, b=0.5):
    # 幂变换
    result = imgin.convert('L').crop()
    table = []
    for x in range(0, 256):
            table.append(int(((x/a)**b)*a))
    imgout = result.point(table, 'L').convert('RGBA')
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))
    return imgout
   
# 一阶差分
def firstDifference(imgin):
    image_gray = imgin.convert('L').crop()
    suanzi_x = numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    suanzi_y = numpy.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    image_x = signal.convolve2d(image_gray, suanzi_x, mode="same")
    image_y = signal.convolve2d(image_gray, suanzi_y, mode="same")
    image_xy = numpy.sqrt(image_x ** 2 + image_y ** 2)
    image_xy = (image_xy / float(image_xy.max())) * 255
    # image_xy[image_xy > image_xy.mean()] = 255
    image_xy = 255 - image_xy
    imgout = Image.fromarray(image_xy).convert("RGBA")
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))
    return imgout

# 二阶差分
def secondDifference(imgin):
    image_gray = imgin.convert('L').crop()
    suanzi = numpy.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    image_suanzi = signal.convolve2d(image_gray, suanzi, mode="same")
    image_suanzi = (image_suanzi / float(image_suanzi.max())) * 255
    # image_suanzi[image_suanzi > image_suanzi.mean()] = 255
    image_suanzi = 255 - image_suanzi
    imgout = Image.fromarray(image_suanzi).convert("RGBA")
    imgout = QtGui.QPixmap.fromImage(ImageQt(imgout))
    return imgout

#灰度直方图
def getHistogramList(imgin):
    imgin = numpy.array(imgin)
    pyplot.hist(imgin.ravel(), 256, [0, 256])
    pyplot.show()



if __name__ == '__main__':
    img = Image.open('./123.jpeg').convert('L')
    getHistogramList(img)
    