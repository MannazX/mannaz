# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:54:46 2018

@author: magge
"""

import random
import matplotlib.pyplot as plt

random.seed(32)
['%.2f' % random.random() for i in range(12)]

uni_number = random.random()
some_n = random.uniform(3,8)
print(some_n)

#sequence of random numbers
N = 600
x = range(N)
y1 = [random.uniform(3,9) for i in x]

#%matplotlib inline
plt.plot(x, y1, 'r+')
plt.axis(0,N-1,3.2,5.0)

_ = plt.hist(y1, normed=True)
