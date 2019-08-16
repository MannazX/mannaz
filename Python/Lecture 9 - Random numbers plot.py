# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:36:43 2018

@author: magge
"""
import random

random.seed(42)
N = 500  # no of samples
x = range(N)
y1 = [random.random() for i in x]

import matplotlib.pyplot as plt
#matplotlib inline
plt.plot(x, y1, '+') #plots scatter plot
plt.axis([0,N-1,-0.2,1.2])

y2 = [random.uniform(3,4) for i in x]
plt.plot(x, y2, 'r+')
plt.axis([0,N-1,2.8,4.2])

samples = np.random.uniform(-1, 10, size=10000)

plt.plot(np.arange(10000), samples, '+')
plt.axis([0,9999,-2,11])