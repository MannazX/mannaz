# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:19:32 2018

@author: magge
"""

x = 1
y = 2
x1 = 1
x2 = 2
x3 = 3

v1 = [x, y]
v1

v2 = (-1, 2)
v2

def f(x):
    return x**3

n = 5
dx = 1.0/(n-1)
xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]
pairs = [[x, y] for x, y in zip(xlist, ylist)]
pairs

mylist = [2, 0.6, 'tmp.ps', [0,1]]
mylist

