# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:30:09 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

N = 2000
a = 2
b = 10
sample = np.random.randint(a,b,N)

_ = plt.plot(np.arange(N), sample, '+')
toss = np.random.randint(0,2,size=50)
toss_tail = np.sum(np.logical_not(toss))
print(toss_tail)

p = np.arange(20)
indx = np.random.randint(0,20,size=12)
p[indx]

choice = np.random.choice(p, size=12)
print(choice)

np.random.shuffle(p)
choice = p[8:]
print(choice)
