# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:17:37 2018

@author: magge
"""

from math import factorial

def binomial(x, n, p):
    Cnr = factorial(n)/(factorial(x)*(factorial(n-x)))
    return Cnr*(p**x)*p**(n-x)
print(binomial(2, 5, 0.5))
#The probability is 0.3125

