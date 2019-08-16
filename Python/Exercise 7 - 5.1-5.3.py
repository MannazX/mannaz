# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:29:53 2018

@author: magge
"""

import numpy as np
from math import pi
#5.1
x = np.arange(-4, 4, 1); x
def h(x):
    inrad = (1/np.sqrt(2*pi))
    xp = -(0.5*x**2)
    return inrad*np.exp(xp)

h(x)
#array([1.33830226e-04, 4.43184841e-03, 5.39909665e-02
#2.41970725e-01,
# 3.98942280e-01, 2.41970725e-01, 5.39909665e-02,
#4.43184841e-03])

#5.2
x2 = np.empty(8)
for i in range(8):
    x2[i] = x[i]
    x2

y = np.empty(8)
for i in range(8):
    y[i] = h(x[i])
    y

#5.3
x2 = np.linspace(-4,4,8); x2
    #array([-4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])

y = np.array(h(x))
y #array([1.33830226e-04, 4.43184841e-03, 5.39909665e-02,
# 2.41970725e-01,
     #  3.98942280e-01, 2.41970725e-01, 5.39909665e-02,
       #4.43184841e-03])

