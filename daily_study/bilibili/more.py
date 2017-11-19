#!/use/bin/env python3
#encoding: utf-8

import multiprocessing
import time

def process(num):
    print ("process%d" % num)

if __name__ == '__main__':
    for i in range(1,100)
        p = mulyiprocessing.Process(target=process, args=(i,))
        p.start()
