#coding: utf-8
#Auther: wjsaya
#**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os

def dir():
    if not os.path.exists("log"):
        os.mkdir("./log")
        print ("log目录不存在，已创建")
    os.chdir("./log")

def dective():
    print (os.getcwd())
    for file in os.walk("./"):
        for i in file[2]:
            f = open(i, 'r').read()
                


if __name__ == "__main__":
    dir()
    dective()

