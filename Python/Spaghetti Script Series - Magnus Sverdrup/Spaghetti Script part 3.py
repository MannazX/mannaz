# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def Diff_eq1(t):
    v0 = 2
    w = 20
    return -v0*np.exp(-w*t)
t = np.linspace(1,2,100)
y = Diff_eq1(t)

def Diff_eq2(t):
    v0 = 2
    w = 20
    return v0*np.exp(-w*t)+v0
g = Diff_eq2(t)

def Derivative1(t):
    v0 = 2
    w = 20
    return w*v0*np.exp(-w*t)
dy = Derivative1(t)

def Derivative2(t):
    v0 = 2
    w = 20
    return -w*v0*np.exp(-w*t)
dg = Derivative2(t)

plt.subplot(2,2,1)
plt.plot(t,y)
plt.subplot(2,2,2)
plt.plot(t,g)
plt.subplot(2,2,3)
plt.plot(t,dy,'r')
plt.subplot(2,2,4)
plt.plot(t,dg,'r')
