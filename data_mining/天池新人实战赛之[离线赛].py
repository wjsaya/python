#!/usr/bin/env python
#coding:utf-8
#source:https://tianchi.aliyun.com/getStart/introduction.htm?spm=5176.100066.0.0.74bb9bc7wQUGC4&raceId=231522


import numpy as np

D1 = open('F:/data/tianchi/fresh_comp_offline/tianchi_fresh_comp_train_item.csv')
D2 = open('F:/data/tianchi/fresh_comp_offline/tianchi_fresh_comp_train_user.csv')
item_data = D1.readlines()
user_data = D2.readlines()
    print (len(item_data))
    print (len(user_data))

