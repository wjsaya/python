#!/usr/bin/env python
#coding:utf-8
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_code(leng):
    code = ''
    for i in range(0,int(leng)):
        code = code + str(random.choice(string.ascii_letters[:]))
    return(code)
 
def put_image(code):
    width = 100 * 4
    height = 100
    image = Image.new('RGB', (width, height), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    draw =ImageDraw.Draw(image)
    draw.line((0,0) +image.size, fill=128)

    Font4 = ImageFont.truetype("C:\Windows\Fonts\SHOWG.TTF",50)  
    draw.text([40, 10], code, font = Font4)  
    image.show()

if __name__ == '__main__':
    ver_code = get_code(4)
    put_image(ver_code)


