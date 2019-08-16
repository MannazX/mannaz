# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:22:21 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    tau = 2*x**3
    xi = 2/(5*x**2)
    return tau*xi - np.sin(x)
x = np.linspace(0, 5, 40)
y = f(x)
plt.scatter(x, y)

#failed so far, return!!