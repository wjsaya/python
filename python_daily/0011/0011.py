#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-10 12:33:32 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-10 12:33:32 
 
def get_dirty(fileName=''):
    '''解析文件获取敏感词
    '''
    with open (fileName, 'r', encoding='utf-8') as f:
        re = f.readlines()

    for i in range(len(re)):
        re[i] = re[i].strip('\n')

    return(re)

def fliter(dirty_dict):
    '''过滤敏感词
    '''
    instr = input("不要输入敏感词哦：")
    for i in dirty_dict:
        if (instr == i):
            print('Freedom')
            return 1

    print('Human Rights')
    return 0


if __name__ == '__main__':
    file = 'filtered_words.txt'
    dirty_dict = get_dirty(fileName=file)
    while(1):
        fliter(dirty_dict)

