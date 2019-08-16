# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:07:02 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

rand = np.random.randint(1,10,20)
uni = np.random.uniform(2,5,10)
random_numb = np.random.random(20)


def rand_x(a,b,n):
    randr = np.random.uniform(a,b,n)
    rands = np.random.random(n)
    for i in range(len(randr)):
        randr[i] += rands[i]
    return randr

def rand_y(a,b,n):
    randp = np.random.uniform(a,b,n)
    randq = np.random.random(n)
    for i in range(len(randp)):
        randp[i] += randq[i]
    return randp

valx = rand_x(2,7,1000)
valy = rand_y(5,12,1000)

plt.plot(valx,valy, 'r+')
#_ = plt.hist(valx)
#_ = plt.hist(valy)
