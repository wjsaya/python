#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya


#类的私有属性练习



class Score(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score
#定义name为私有变量，score仍旧为常规变量，具体的看下面调取结果。
    def print_score(self):
        print ('%s:%s' % (self.__name, self.score))


saya1 = Score('saya1', 666)


try:
    print ("saya1.name为" + saya1.name)
except:
    print ("saya.name调取失败")

try:
    print ("saya1._name为" + saya1._name)
except:
    print ("saya._name调取失败")
#name目前为私有属性，所以会调用失败。如果想读取或修改，那么可以通过在Score里定义类来实现。

try:
    print ("修改前的saya1.score为" + str(saya1.score))
    saya1.score=66
    print ("修改后的saya1.score为" + str(saya1.score))
except:
    print ("saya.score调取失败")
#但是score变量仍旧为普通属性，所以仍旧可修改与读取。
