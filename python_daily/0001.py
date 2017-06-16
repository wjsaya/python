#coding: utf-8
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
#Auther: wjsaya
from random import choice
import string
import os

def main():
    if os.path.exists("./activecode.code"):
        print ("已经存在activecode.code文件，已经删除")
        os.remove("./activecode.code")

    dict = string.ascii_letters[:]
    #设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
   
    for i in range(0,int(count)):
        code = get_code(dict, length)
        with open ('activecode.code', 'a+') as f:
            f.write(code+'\n')
    #通过count限制激活码个数，循环调用get_code来计算激活码 

def get_code(dict, length):
    #根据给定字典，长度来得出激活码
    code = ""
    for i in range(0,int(length)):
        code = code+str(choice(dict))
    return code
 

if __name__ == "__main__":
    main()

