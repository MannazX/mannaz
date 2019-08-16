# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:11:45 2018

@author: magge
"""

y = {2:3, 1:3, 0:5}

def f(data, x):
    sum = 0
    for p in data:
        sum += data[p]*x**p
    return sum

f(y,3)
f(y,2)
f(y,5)
