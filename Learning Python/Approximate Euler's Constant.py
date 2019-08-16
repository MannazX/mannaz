# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:56:55 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

el = []
errl = []
s = 0
for n in range(0,18):
    s += 1/m.factorial(n)
    el.append(s)
    error = abs(m.exp(1)-s)
    errl.append(error)
    print("{:.15f} {:18.15f}".format(s,error))

x = [i for i in range(len(el))]
x2 = [j for j in range(len(errl))]

plt.subplot(1,2,1)
plt.plot(x,el,'go')
plt.subplot(1,2,2)
plt.plot(x2,errl,'ro')