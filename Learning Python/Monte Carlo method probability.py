# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:22:27 2018

@author: magge
"""
import numpy as np
np.random.seed(48)

N = 10000
outcome = np.random.randint(1,7,size=(2,N))

black = outcome[0,:]
green = outcome[1,:]
event = black > green
M = np.sum(event)
P = M/N
print("The wanted outcome is {:}".format(M))
print("The probability of the wanted outcome is {:}".format(P))
