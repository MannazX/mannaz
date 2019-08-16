# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:13:33 2018

@author: magge
"""

def MCint_area(f, a, b, m, n):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    below = y[y < f(x)].size
    area = below/n*m*(b-a)
    return area

def circle_f(x, y):
    return (x**2)+(y**2)

a = -1
b = 1
m = 1000
n = 1000000
MCint_area(circle_f, a, b, m, n)
