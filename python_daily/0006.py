#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya
#**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import os
import re

def dir():
#检测日志目录是否存在，不存在就创建
    if not os.path.exists("log"):
        os.mkdir("./log")
        print ("log目录不存在，已创建")
    os.chdir("./log")

def dective_words():
#检测文件内的单词,并且调用word_count来统计各个单词中出现频率最高的一个
    for file in os.walk("./"):
        print ("当前目录为："+os.getcwd())
        for i in file[2]:
            file = open(i, 'r', encoding="utf-8").read()
            word_list = re.findall('([a-zA-Z0-9]+)', file)
            word_dict = word_count(word_list)
            
            max = 0                     
            for key in word_dict.keys():
                if max < int(word_dict.get(key)):
                    max = word_dict.get(key)
                    max_key = key
            print ("在"+i+"中,最重要的词为："+max_key+"，共出现了"+str(max)+"次")    

def word_count(word_list):
#统计单词个数
    word_dict={}
    frequency = 1
    for single_word in word_list:
        try:
            number = word_dict.get(single_word)
            word_dict[single_word]=number+1
        except:
            word_dict[single_word]=frequency
    return word_dict



if __name__ == "__main__":
    dir()
    dective_words()