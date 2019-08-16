# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:14:43 2018

@author: magge
"""
import matplotlib.pyplot as plt

v0 = 15
g = 9.82
n = 20
t = (2*v0/g)/n

while t <= 2*v0/g:
    yt = v0*t-(1/2)*g*t**2
    t += (2*v0/g)/n
    print(yt)
    
