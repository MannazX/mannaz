# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:01:16 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

from scipy import fft


def fun(t,w):
    return np.sin(128*t)
    
t = np.linspace(0,2*np.pi,1000)

w = [1]
for k in range(len(t)-1):
    wk = 2**(k)
    w.append(wk)
w = np.array(w)

ffun = fft(fun(t,w))

plt.subplot(1,2,1)
plt.plot(t,fun(t,w),'r')
plt.subplot(1,2,2)
plt.plot(t,ffun,'b')