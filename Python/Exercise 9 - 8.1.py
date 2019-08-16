# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:15:09 2018

@author: magge
"""
import random

N = 100
head = 0
tail = 0
for i in range(N):
    r = random.randint(0,1)
    if r == 0:
        print('heads')
        head += 1
    else:
        print('tails')
        tail += 1

    