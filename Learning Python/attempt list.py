# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:25:34 2018

@author: magge
"""
from math import exp
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in x:
    i += 1
x = list(range(0, 11, 1))
y = [exp(i)-2 for i in x]
#print(y)
#for Y in y:
   # print(Y)
#for X in x:
    #print(X)
    
plt.plot(x, y)
