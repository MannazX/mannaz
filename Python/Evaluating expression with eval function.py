# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:49:43 2018

@author: magge
"""

r = eval('3+4')
print(r,type(r))

s = eval('"strings are amazing"')
type(s)
print(s)
print(type(s),s)

from math import sin
x = eval('sin(2/3)')
print(type(x),x)

print("sum these numbers")
i1 = eval(input("Input 1: "))
i2 = eval(input("Input 2: "))
g = i1 + i2
print("sum = {0}, type = {1}".format(g,type(g)))