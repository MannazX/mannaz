# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 09:51:49 2018

@author: magge
"""
import numpy as np

fly = [44, 34, 27, 22, 16, 13, 10, 8, 6, 5, 4, 3, 2, 2, 1, 1, 1, 0, 1, 0]
fly = np.array(fly)
cu_fly = np.cumsum(fly)
nyfly = np.random.randint(0,10,10)


for tal in range(len(nyfly)):
    r = np.random.randint(0, 200)
    for i in range(len(cu_fly)):
        r <= cu_fly[i]
        fly[i] = fly[i] + 1