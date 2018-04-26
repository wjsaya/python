#!/usr/bin/env python3
# coding: utf-8
'''
每次创建文件太麻烦，干脆直接参照模板创建，然后修改。
'''
import os

file_list = []
for i in os.walk('./'):
    file_list.append(i[2])
for file_name in [str(i)+'-'+str(j)+'.py' for i in range(3, 10) for j in range(1, 10)]:
    try:
        file_list.index(file_name)
    except ValueError:
        os.system('copy template.py ' + file_name)
