# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:45:02 2019

@author: magge
"""
import matplotlib.pyplot as plt
import numpy as np

def voltage(a,b,t):
    return a*np.sin(2*t + 0.4)+b*np.sin(3.5*t + 0.1)
t = np.linspace(0,10,500)
V = voltage(5.0,0.9,t)

def current(a,b,t):
    return -(a/6.7)*np.sin(2*t + 0.4)-(b/6.7)*np.sin(3.5*t + 0.1)
t = np.linspace(0,10,500)
I = current(5.0,0.9,t)

plt.plot(t,V)
plt.plot(t,I,'r')