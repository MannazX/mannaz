# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:37:23 2019

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 10
n = 100000
def MC_int(f,a,b,n):
    x = np.random.uniform(a,b,n)
    s = np.sum(f(x))
    I = s*(b-a)/n
    return I

def g(x):
    return x**3 + 2*x**2 - 5*x + 9
print("The Monte Carlo integral of the function is {:.2f}".format(MC_int(g,a,b,n)))
x = np.linspace(a,b,n)
g = g(x)
fig = plt.figure()

    
plt.plot(x,g,'g')
plt.title("Graph of g(x)")
plt.xlabel("x-values"), plt.ylabel("g(x)-values")