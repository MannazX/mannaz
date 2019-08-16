# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:00:02 2018

@author: magge
"""

import numpy as np

w = np.arange(0, 3.1, 0.1); n
w[:] #whole array
w[:-2] #array minus two last values
w[::5] #array shortened to list of 5
w[2:-2:6]

import matplotlib.pyplot as plt
def y(t):
    v0 = 10
    g = 9.81
    d = 2*v0/g
    t = np.linspace(0, d, 10)
    return v0*t - 0.5*g*t**2
y(t)
plt.plot(t, y(t))


