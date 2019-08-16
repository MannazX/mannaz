# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:17:10 2019

@author: Frederik
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

def fun(x,h0,rho,T):
    lam = (T/rho)
    return h0 + lam*np.cosh(x/lam)

x = np.linspace(-10,10,100)
f = fun(x,-15,1,20)

plt.plot(x,f)

