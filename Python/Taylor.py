# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:18:23 2018

@author: magge
"""
from math import factorial

def S(x,n):
    T_sum = 0
    for i in range(0,n):
        T_sum += ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1))
    return T_sum

print(S(5, 100))