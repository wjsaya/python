#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-10 00:01:32 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-10 00:46:47 

import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

def get_str():
    '''获取单个随机字符
    string.digits + string.ascii_letters = 
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    '''
    return random.choice(string.digits + string.ascii_letters)

def get_color():
    '''返回颜色元组
    '''
    return (random.randint(64,200),random.randint(64,200),random.randint(64,200))

def get_pic(num=4):
    '''生成指定验证码个数的验证码图片，默认为4个，每个的大小均为60*60
    '''
    heigh = 60
    width = heigh * num
    image = Image.new('RGB', (width, heigh), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('ariblk.ttf',44)
    # 创建图片，画布，以及字体对象

    for  x in range(width):
        for y in range(heigh):
            draw.point((x,y),fill=get_color())
            # 画布随机加噪点
    for t in range(num):
        draw.text((60 * t + 10, 0), get_str(), font=font, fill=get_color())
        # 随机获取num个字符，使用指定字体，使用随机颜色
    image = image.filter(ImageFilter.SMOOTH)
    # 模糊处理图片
    image.save('vercode.png')

if __name__ == '__main__':
    num = 4
    get_pic(num)