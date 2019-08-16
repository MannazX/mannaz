# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:05:22 2018

@author: magge
"""

x = 32.0 #Global variable

def f(x):
    return 2*x**3 - 3*x**2 # x - local variable

print(f(x))

def g(x):
    return 2*x**3 - 3*x**2

print("f(10.0) = %.2f, g(x) = %.2f" % (f(10.0),g(10.0)))

n = 10
def p(x):
    n = 23
    return n*x - 3


def h(x):
    global n
    n = 12 # another function may depend on previous global variable - careful
    return n*x - 3

print(p(4),n)
print(h(4),n)
