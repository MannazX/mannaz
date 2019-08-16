# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 13:49:21 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    omega = 2**t*np.pi
    return np.sin(omega*t**2)
t = np.linspace(0, np.pi, 1000)
y = f(t)
plt.plot(t, y)

