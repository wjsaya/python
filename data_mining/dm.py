#!/use/bin/env python
#coding:utf-8

import pandas
import numpy
import sth
import os

a=pandas.read_csv('F:/data/tianchi/fresh_comp_offline/tianchi_fresh_comp_train_item.csv')
#b=pandas.read_csv('F:/data/tianchi/fresh_comp_offline/tianchi_fresh_comp_train_user.csv')
#打开csv文件，然后传递给a数据集

test_data = pandas.DataFrame(numpy.random.rand(10,5))

#创建一个10*5的表格，内部数据为随机数据
print (a.head(15))
print (a.head(15))
#查看a的钱150和后150行
print ('#'*20)
print (a.shape)
#查看a数据集的行、列数
print (a.info())
print ('#'*20)
# 查看数据框 (DataFrame) 的索引、数据类型及内存信息c
print (a.describe())
print ('#'*20)
# 对于数据类型为数值型的列，查询其大致的统计信息，例如最大最小值等等
print ('#'*20)
print (pandas.isnull(a))
#检查数据中空值出现的情况，并返回一个由布尔值(True,Fale)组成的列
print (pandas.notnull(a))
# 检查数据中非空值出现的情况，并返回一个由布尔值(True,False)组成的列
print ("aa")


#test_data.to_csv('./1.csv')
#导出数据为1.csv
#test_data.to_excel('./1.xls')
#导出数据为1.xls
#test_data.to_html('./1.html')
#导出数据为1.html