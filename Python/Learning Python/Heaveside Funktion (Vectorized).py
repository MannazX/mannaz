# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:47:33 2018

@author: magge
"""
import matplotlib.pyplot as plt
import numpy as np

def A(x):
    return(0 if x < 0 else 2)

Av = np.vectorize(A)
x = np.linspace(-10,10,5)
a = Av(x)
plt.plot()
plt.plot(x,a)
_ = plt.axis(a[0], a[-1], -0.1, 1.1)

x2 = np.linspace(-10,10,50)
a2 = Av(x2)
plt.figure()
plt.plot(x,a,'r',x2,a2,'b',label=('step: 5','step: 0.5'))
_ = plt.axis(x[0],x[-1],-0.1,1.1)

