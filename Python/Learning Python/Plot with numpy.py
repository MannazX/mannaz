# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 00:06:51 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

def xi(x):
    t = 2.7
    omega = np.sin(2*x-4)
    tau = 3*t**x
    return omega*tau
x = np.linspace(0, 40, 100)
y = xi(x)
plt.plot(x,y)
