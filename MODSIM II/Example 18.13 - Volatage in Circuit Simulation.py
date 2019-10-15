# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:00:23 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m



v1 = 0.238
v2 = 5.83
v3 = -6.07

def Vc(t):
    """returns the voltage over the capacitor formula."""
    return v1 + v2*np.exp(-t/(434*10**-6)) + v3*np.exp(-t/(43.9*10**-6))

t = np.linspace(0,3E-3,1000) #time interval between 0 and 3 milliseconds.

plt.plot(t,Vc(t))