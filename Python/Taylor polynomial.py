# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:47:36 2018

@author: magge
"""
from math import factorial

def S(x, n):
    k=0
    Tsum=0
    num = ((-1)**k)*x**(2*k+1)
    den = factorial(2*k+1)
    while k < n:
        Tsum += num/den
        k += 1
    return Tsum
print(S(0, 1))
