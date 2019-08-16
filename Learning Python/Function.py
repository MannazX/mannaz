# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 23:42:54 2018

@author: magge
"""
from math import exp
import matplotlib.pyplot as plt

def xi(x, y, n, t):
    xlist = []
    ylist = []
    tau = 2*exp(x) - n
    omega = 2*x - t
    while x < 10000:
        y += omega*tau
        ylist.append(y)
        xlist.append(x)
    plt.plot(xlist,ylist)

xi(1, 1, 5, 3)
#xi(5, 20, 12)
