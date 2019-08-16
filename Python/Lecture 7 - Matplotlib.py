# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:20:52 2018

@author: magge
"""

import matplotlib.pyplot as plt
#%matplotlib

def f(t):
    return t**2*np.exp(-t**2)
t = np.linspace(0, 3, 51)
y = f(t)
plt.plot(t, y)
plt.savefig('demoplot1.pdf')
plt.savefig('demoplot1.png')

def f1(t):
    return t**2*np.exp(-t**2)
def f2(t):
    return t**2*f1(t)

t = np.linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)
t3 = t[::4]
y3 = f2(t3)
y1
t3
t

import numpy as np

def H(x):
    return (0 if x < 0 else 1)
Hv = np.vectorize(H)
x = np.linspace(-10, 10, 5)
h = Hv(x)
plt.figure()
plt.plot(x, h)
_ = plt.axis([x[0], x[-1], -0.1, 1.1])

x2 = np.linspace(-10, 10, 50)
h2 = Hv(x2)
plt.figure()
plt.plot(x, h, 'r', x2, h2, 'b', label=('step: 5', 'step: 0.5'))
_ = plt.axis([x[0], x[-1], -0.1, 1.1])

plt.figure()
plt.plot([-10, 0, 0, 10], [0, 0, 1, 1])
_ = plt.axis([x[0], x[-1], -0.1, 1.1])

