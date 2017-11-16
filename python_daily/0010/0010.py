#!/usr/bin/env python
#coding:utf-8


from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string

def get_code(leng):
    code = ''
    for i in range(0,int(leng)):
        code = code + str(random.choice(string.ascii_letters[:]))
    return(code)


def put_image(code):
    print (code)





if __name__ == '__main__':
    ver_code = get_code(4)
    put_image(ver_code)


