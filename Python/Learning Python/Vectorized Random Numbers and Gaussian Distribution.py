# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:14:14 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.random()
np.random.random(size=1000)

samp = np.random.uniform(0,10,size=2000)

plt.plot(np.arange(2000), samp, '+')
plt.axis([0,2000,-2,12])

N = 1000

sample = np.random.randn(N)

m = 2
s = 5


sample = np.random.normal(m, s, size=N)
_ = plt.plot(np.arange(N), sample, '+')
_ = plt.hist(sample, normed=True)

