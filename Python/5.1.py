# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:10:01 2018

@author: magge
"""

#5.1
import numpy as np
from math import pi

x = np.arange(-4, 5, 1); x #creates array of values -4 to 4 in evenly spaced x-coordinates
def h(x): #defines what the function will be
    inrad = (1/np.sqrt(2*pi)) #inverse radical part of h(x)
    xp = -(0.5*x**2) #exponential function in h(x)
    return inrad*np.exp(xp) #What the function is defined as

print(x) #prints x as list of evenly spaced x-coordinates
print(h(x)) #prints the function as a list of values
