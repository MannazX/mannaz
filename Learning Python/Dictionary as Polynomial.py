# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:51:51 2018

@author: magge
"""

y = {0:-1, 1:0, 3:2, 4:3}

def p(data, x):
    sum = 0
    for power in data:
        sum += data[power]*x**power
    return sum

p(y,5)
p(y,2)
p(y,1)
p(y,3)

def p2(data,x):
    return sum([data[p]*x**p for p in data])
p2(y,2)
p2(y,6)
