# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:11:38 2018

@author: jakob
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def y(v0):
    global v
    v = v0
    global t
    t = np.arange(0,2*v0/g,0.1)
    return v0*t -1/2*g*t**2


plt.plot(t,y(v0))
plt.xlabel('time (s)'); plt.ylabel('height (m)')



