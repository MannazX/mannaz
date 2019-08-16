# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:47:27 2018

@author: magge
"""
import numpy as np


def a_sum(f,a,b,n):
    sum1 = 0
    #sum2 = 0
    #x = np.linspace(a,b,n)
    for i in range(0, n-1):
        sum1 += f(a*i+b**i)
    return sum1

print(a_sum(lambda x:x,2,3,10))
    
    
