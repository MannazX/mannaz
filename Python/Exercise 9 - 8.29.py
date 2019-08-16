# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:32:32 2018

@author: magge
"""
import numpy as np
import math


def F(n, b, a): #Defines function, that approximates pi
    x = np.random.uniform(a, b, n) #Generates an 'n' amount of x-values between a and b
    y = np.random.uniform(a, b, n) #Generates an 'n' amount of y-values between a and b
    m = np.sum(np.square(x)+np.square(y) < b) #Checks x and y points that are within the circle x^2 + y^2 < 1
    area = m/n*(2*b)**2 #Formula for the area to approximate
    approx_pi = area/b #Formula for the approximation of pi
    return approx_pi #Returns the approximation
print("Den approximerede pi", F(n = 10000000, a = -1, b = 1)) #Prints the approximated value for pi within given interval
print("Den rigtige pi", math.pi) #Prints the real value for pi