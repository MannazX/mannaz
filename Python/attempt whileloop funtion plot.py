# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:04:01 2018

@author: magge
"""

import matplotlib.pyplot as plt

def f(x, n):
    ni = x**(-2)
    nu = n**(3)
    return nu/ni

def gr(y, C, t, R):
    ylist = []
    til = []
    nl = R*t - 2*C
    while t < 10:
        y += C*f(t, C)
        ylist.append(y)
        g = nl - C
        til.append(g)
        t += 1
    plt.plot(ylist, til)
    plt.plot(til, ylist)

gr(100, 20, 0.2, 25)


        
        


    
