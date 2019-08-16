# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:59:09 2018

@author: magge
"""

def f(x):
    return x**2 - 3*x + 2

y = 10.0
F = f(y)
print(F)

def g(x):
    F1 = 2*x - x**2
    return F1 #F1 and x are local variables - only accessable inside function


