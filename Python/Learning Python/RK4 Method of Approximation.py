# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:30:05 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

X = []
Y = []
N = 5
#N = 10
#N = 100

x_final = 4

def function(x,y):
    return np.sqrt(x)*y


def exact_function(t):
    return (2.0/3.0)*t**(3.0/2.0)

def RK4(f,x0,y0,x_final,N):
    h = (x_final - x0)/N
    x = x0 - h
    y = y0
#    X.append(x)
#    Y.append(y)
    for k in range(N+1):
        x = x + h
        k1 = f(x,y)
        k2 = f(x + 0.5*h, y + 0.5*h*k1)
        k3 = f(x + 0.5*h, y + 0.5*h*k2)
        k4 = f(x + h, y + k3*h)
        y = y + h*(k1 + 2.0*(k2 + k3) + k4)/6.0
        X.append(x)
        Y.append(y)
    
#    error = []
#    for i in range(len(Y)):
#        e = abs(Y[i] - exact[i])
#        error.append(e)
#    for n in error:
#        print(n)

t = np.linspace(1,4,N)
exact = exact_function(t)

RK4(function,1,-4,x_final,N)

plt.plot(X,Y,'c',linestyle="dashed")
