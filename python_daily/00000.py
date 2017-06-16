#coding: utf-8
#Auther: wjsaya
#**第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from PIL import Image,ImageFont,ImageDraw
def main():
    image = Image.open('./cat.jpg')
    wight, hight = image.size
    text = "233"
    color = (255,0,0)
    fontsize = wight//8
    font = ImageFont.truetype("/usr/share/fonts/wps-office/arial.ttf",fontsize)

    draw = ImageDraw.Draw(image)
    draw.text((fontsize*6,0), text, color, font)
    image.save('./c.jpg', 'jpeg')


if __name__ == "__main__":
    main()

