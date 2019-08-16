# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:29:26 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

F = np.arange(-20, 120, 1)
def C(F):
    return (5/9)*(F - 32)
C(F)

def c(F):
    return (F - 30)/2
c(F)

plt.plot(C(F), F)
plt.plot(c(F), F)
