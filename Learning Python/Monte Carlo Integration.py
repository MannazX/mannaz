# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:35:10 2018

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt

def MCint(f,a,b,n):
    x = np.random.uniform(a,b,n)
    s = np.sum(f(x))
    I = (b-a)/n
    return I

def funk(x):
    return x**2 - 2*x + 1

a = 10
b = 30
n = 1000000
MCint = MCint(funk,a,b,n)
print("The Monte Carlo integral is therefor {:}".format(MCint))

#values = np.empty(100)
#amount_n = np.arange(n // 100, n+1, n // 100)
#for idx, test_n in enumerate(amount_n):
#    values[idx] = MCint(funk,a,b,test_n)
#_ = plt.plot(amount_n, values - 6.5)