# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:19:28 2018

@author: magge
"""

def num_diff(f,x,h=1E-4):
    return (f(x+h)-f(x-h)/2*h)

def g(x):
    return x**-4

x = 1.8
print("Numerical approximation of g'(%.2f) is %.2f" % (x, num_diff(g,x)))

dg = num_diff(lambda x: x**(-4), 1.8)
print(dg) # more precise approximation

