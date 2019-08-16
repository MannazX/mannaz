# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def A(x):
    return(0 if x <= 0 else 1)

def B(x):
    return(1 if x <= 0 else 0)

A = np.vectorize(A)
x = np.linspace(-20,20,50)
y = 0.5*np.sin(0.08*x)+0.5
Av = A(x)
B = np.vectorize(B)
Bv = B(x)
g = 0.5*np.cos(0.08*x-4.8)+0.5

plt.subplot(1,2,1)
plt.plot(x,Av,'k',linestyle="dashed")
plt.plot(x,y,'mo')
plt.subplot(1,2,2)
plt.plot(x,Bv,'r',linestyle="dashed")
plt.plot(x,g,'go')