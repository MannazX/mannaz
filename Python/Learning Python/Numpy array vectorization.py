# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:43:44 2018

@author: magge
"""

import numpy as np

n = 10
x = np.linspace(0,5,n)
r = np.zeros(n)

r = np.sin(x)*np.cos(x)*np.exp(x)
r

xtab = np.arange(4).reshape(2,2)
xtab

xtab[1,0]

R = 5 * np.ones((3,3))
R
T = 3 * np.ones((3,3))
T

R @ T
R * T
