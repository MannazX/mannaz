# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:30:25 2019

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

def MCint_area(f,a,b,m,n):
    np.random.seed(82)
    t = np.linspace(a,b,n)
    x = np.random.uniform(a,b,n)
    y = np.random.uniform(0,m,n)
    n_under = y[y<f(x)].size
    area = n_under/n*m*(b-a)
    plt.plot(t,y,'g+',alpha=0.1)
    return area

def exp(x):
    return np.exp(x)
    
print("The area under the curve exp is {:.2f}".format(MCint_area(exp,1,5,148.4,100000)))
    
x = np.linspace(1,5,100)
exp = exp(x)

plt.plot(x,exp,'m')
plt.title("Monte Carlo integral approximation of exponential graph")
plt.xlabel("x-values"), plt.ylabel("y-values")