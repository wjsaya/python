#coding: utf-8
#Auther: wjsaya
#**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
from PIL import Image

def image_small(dir1, dir2):
    list = os.listdir(dir1)
    for i in list:
        image = Image.open(dir1+'/'+i)
        while True:
            h,w = image.size
            #获取图片原始大小,然后进死循环，不停缩小图片为原来的90%，直到大小缩小为iphone5所支持的分辨率。
            if h < 1136:
            #iphone5分辨率为1136x640
                if w < 640:
                    break
            image = image.resize((int(h*0.9),int(w*0.9)))
        image.save(dir2+'/'+i)
        print (dir1+'/'+i+"已处理，保存为："+dir2+'/'+i)


if __name__ == "__main__":
    dir1 = input("缩小前图片存放目录为：")
    dir2 = input("缩小后图片存放目录为：")
    try:
        os.mkdir(dir2)
    except Exception: 
        print (Exception)
    image_small(dir1, dir2)
    