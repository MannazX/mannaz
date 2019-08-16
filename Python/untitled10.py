# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:15:09 2018

@author: magge
"""

def flip(N):
    r = random.random()
    if r <= 0.5:
        print('head')
    else:
        print('tail')
    x = range(N)
    return[random.random() for i in x]

flip(100)
    