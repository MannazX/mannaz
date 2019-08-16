# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:59:01 2018

@author: magge
"""

import matplotlib.pyplot as plt
import numpy as np

def g(t):
    return t**(4)*np.exp(-3*t**2)

t = np.linspace(0, 2, 100)
y = g(t)

plt.plot(t,y)


