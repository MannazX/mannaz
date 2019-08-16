# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:15:54 2018

@author: magge
"""

#3.8
from math import sqrt 
def roots(a, b, c):
    posr = -b + sqrt(b**2 - 4*a*c)
    negr = -b - sqrt(b**2 - 4*a*c)
    return posr, negr
print(roots(-2.0, 4.0, 5.0))
#3.4833147735478827, -11.483314773547882