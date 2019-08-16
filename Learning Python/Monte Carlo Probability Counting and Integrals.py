# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:44:22 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(45)

N = 1000
outcome = np.random.randint(0,10,size=(2,N))
a = outcome[0,:]
b = outcome[1,:]
event = a > b
M = sum(event)

P = N/M
print(P)

def MCInt(f,a,b,n):
    x = np.random.uniform(a,b,n)
    MCsum = np.sum(f(x))
    I = (b-a)/n*MCsum
    return I

def fun(x):
    return 2*x**2 - 3*x

print(MCInt(fun,2,4,10000))

def MCInt_Area(f,a,b,m,n):
    x = np.random.uniform(a,b,n)
    y = np.random.uniform(0,m,n)
    M = y[y<f(x)].size #Amount under curve
    area = (M/n)*m*(b-a)
    return area

print(MCInt_Area(fun,2,4,5.5,10000))

