from PIL import Image
from PyQt5 import QtGui
from PIL.ImageQt import ImageQt
import numpy as np


def toGray(imgin, sw=''):
    gray_im = Image.new("RGB",(imgin.size[0], imgin.size[1]))
    gray_list = []
    im = imgin.load()
    for i in range(0, imgin.size[0]):
        for j in range(0, imgin.size[1]):
            r, g, b = im[i, j]
            gray_list.append((r*19595 + g*38469 + b*7472) >> 16)
    NO = 0
    for i in range(0, imgin.size[0]):
        for j in range(0, imgin.size[1]):
            gray_im.putpixel((i, j), (gray_list[NO], gray_list[NO], gray_list[NO]))    #将rgb转化为像素
            NO += 1

    if sw == 'inside':
        return gray_im

    else:
        imgin = gray_im.convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
        imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
        return imgout


def otsu(im_gray=""):
        '''
        类判别分析法（otsu）求二值化的阈值T
        假设我们使用阈值T将灰度图像分割为前景和背景
        size：图像总像素个数
        u：图像的平均灰度
        w0：前景像素点占整幅图像大小的比例
        u0：前景像素点的平均值
        w1：背景像素点占整幅图像大小的比例
        u0：背景像素点的平均值
        g：类间方差
        u = w0 * u0 + w1 * u1  (1)
        g = w0*(u - u0)^2 + w1*(u - u1)^2 (2)
        将(1)代入(2)得：
        g = w0 * w1 * (u0 - u1)^2
        采用遍历的方法，遍历所有阈值，当g最大时，该阈值就是我们所求的认为最合适的阈值了。 
        '''
        max_g = 0
        suitable_T = 0
        im_gray = np.array(im_gray)     #图像转numpy中ndarray
        for loop_T in range(0, 255):
                fore_pix_list = (im_gray > loop_T)
                back_pix_list = (im_gray <= loop_T)
                #大于和小于等于给定临时T，通过比较获取两个大于或者小于等于临时T的nparray，两个数组的组成元素为True和False
                fore_pix = np.sum(fore_pix_list)
                back_pix = np.sum(back_pix_list)
                #统计True个数，即当前大于或者小于等于T的像素点个数
                if 0 is fore_pix:
                #如果前景中的像素点统计为0，由于T从0-255递增，如果没有大于T最大值，即255的像素点时，即代表遍历完毕。
                        break
                if 0 is back_pix:
                #如果背景像素点为0个，即没有小于临时T的像素点，跳过本轮，让T自增1继续进行统计
                        continue
                w0 = float(fore_pix) / im_gray.size
                #求前景所有像素点个数/所有像素点的比例
                u0 = float(np.sum(im_gray * fore_pix_list)) / fore_pix
                #im_gray * fore_pix_list，[true, false]*[1,2]=[1, 0],false对应转化为0，其余不变.
                #np.sum的axis默认为0，所以统计本行统计非0的累计和，np.sum([1,2,3,0])结果为6
                w1 = float(back_pix) / im_gray.size
                u1 = float(np.sum(im_gray * back_pix_list)) / back_pix
                g = w0 * w1 * (u0 - u1) * (u0 - u1)
                #套用公式，求出类间方差g
                if g > max_g:
                #过滤出最大的类间方差，并提取对应的T
                        max_g = g
                        suitable_T = loop_T
        return suitable_T
        #返回最大的T，即为OTSU法求出的最合适T


def do2(imgin):
        '''
        imgin为PIL格式图片
        '''
        binary_im = Image.new("L",(imgin.size[0], imgin.size[1]))
        imgin = imgin.convert('L')
        T = otsu(imgin)
        print(T)
        img = np.array(imgin)
        binary_im = np.array(binary_im)
        print(img.shape)
        rows = img.shape[0]
        cols = img.shape[1]
        for i in range(rows):
                for j in range(cols):
                        if (img[i, j] <= T):
                                binary_im[i, j] = 0
                        else:
                                binary_im[i, j] = 255
        imgin = Image.fromarray(binary_im).convert('RGBA')  #二值图转回PIL格式,转PIL的RGB为RGBA
        imgout = QtGui.QPixmap.fromImage(ImageQt(imgin))
        return imgout
