# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 12:01:16 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

def A(x):
    return(0 if x < 0 else 1)
    
V = np.vectorize(A)
x = np.linspace(-10,10,100)
Av = V(x)
plt.plot(x,Av)

def B(x):
    return(0 if x < 2 else 1)

V2 = np.vectorize(B)
Bv = V2(x)
plt.plot(x,Bv)