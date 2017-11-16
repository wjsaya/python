#!/usr/bin/env python3
#coding: utf-8
#Auther: wjsaya


#类的继承相关练习

class me(object):
    def print(self):
        print ('i\'m jay1')

    def print_child(self):
        print ('i\'m may2')

class child(me):
    def print_child(self):
        print ('i\'m may2\'s son')

test = me()
test.print()
test.print_child()

test2 = child()
test2.print()
#print方法仍旧为me里面的。
test2.print_child()
#可以看到，此处的print_child方法是child类里面的，child从me那里继承了过来，但是如果自己有的话，那么就以自己的为优先。


def children(a):
    print ('-----------------------')
    a.print_child()

children(child())
#调用函数时就可以看出这样的优势了，如果传入子类child的内容，那么输出的就是child里的方法。
children(me())
#传入父类me，那么就是调用父类里面的方法。