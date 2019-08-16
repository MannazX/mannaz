# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:34:03 2018

@author: magge
"""
import math

def g(x):
    if 0 <= x <= math.pi:
        return math.cos(x)
    else:
        return 0.0
    
print(g(math.pi))
print(g(-1))
