#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya


#类的定义，调用方法练习


class Score(object):
#定义类
    def __init__(self, name, score):
#传入参数名字和分数
        self.name = name
        self.score = score
#连续定义两个方法，即为函数吧？
    def print_score(self):
        print ('%s:%s' % (self.name, self.score))

    def print_grade(self):
        if self.score >= 300:
            print ('%s，你好呀，你的分数是%s，你的等级为A，真棒！' % (self.name, self.score))
        elif self.score >= 200:
            print ('%s，你好呀，你的分数是%s，你的等级为B，还不错！' % (self.name, self.score))
        elif self.score <= 200:
            print ('%s，你好呀，你的分数是%s，你的等级为C，请继续加油！' % (self.name, self.score))

#生成三个实例
saya1 = Score('saya1', 666)
saya2 = Score('saya2', 233)
saya3 = Score('saya3', 100)

#调用实例下的方法。
saya1.print_grade()
saya2.print_grade()
saya3.print_grade()



class test(Score):
#生成一个新类，集成score的方法。
    def __init__(self, name, score):
        self.name = name
        self.score = score

test2 = test('a', 23333)
test2.print_grade()
test2.print_score()
