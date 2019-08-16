# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:59:25 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

def timedialation(t0,v,c):
    t = t0/(np.sqrt(1-(v**2/c**2)))
    return t
print("The time observed from the observers inertial reference frame is {:.2f} s".format(timedialation(10,2.9*10**8,3*10**8)))
