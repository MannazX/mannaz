# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:09:25 2018

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt

x = [3,4,5,8,9,10]
x = np.array(x); x
x

y = np.linspace(4,38,6)
y

plt.plot(x,y)

ar = np.arange(2, 18, 2)
ar

ar[1:-1]

br = ar[1:-1]; br[0] = -2 #Tilføjer -2 til arrayet.
ar

x = 1
y = 2
x1 = 1
x2 = 2
x3 = 3

def g(x):
    return x**3

y1 = g(x1)
y1
y2 = g(x2)
y2
y3 = g(x3)
y3

xlist = []
ylist = []

xlist.append(0)
xlist.append(x1)
xlist.append(x2)
xlist.append(x3)

ylist.append(0)
ylist.append(y1)
ylist.append(y2)
ylist.append(y3)

plt.plot(xlist,ylist)
