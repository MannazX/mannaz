# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:02:36 2018

@author: magge
"""
import matplotlib.pyplot as plt
import  numpy as np

def f(x):
    return x**2*np.exp(-x)

def g(x):
    return -x**2*np.exp(-x)

x = np.linspace(0, 5, 50)
y1 = f(x)
y2 = g(x)
x3 = x[::4]
y3 = g(x3)

plt.figure(figsize=(15,9))
plt.subplot(2,1,1)
plt.plot(x, y1, 'ro', label='$x^2 \exp(-x))$')
plt.plot(x, y2, 'bo', label='$-x^2 \exp(-x))$')
plt.xlabel('x'); plt.ylabel('y')
plt.axis([x[0], x[-1], min(y2)-0.05, max(y2)+1])
plt.legend(); plt.title('Plot of f(x) and g(x)')
plt.subplot(2,1,2)
plt.plot(x, y1, 'r-', x3, y3, 'bs')
plt.xlabel('x'); plt.ylabel('y')
plt.axis([0, 5, -2, 2])
plt.legend(['$x^2 \exp(-x)$', '$-x^2 \exp(-x)$'])
plt.title('Bottom figure')
plt.savefig('plotted graphs.pdf')