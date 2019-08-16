# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:51:58 2018

@author: magge
"""

import random
import numpy as np

def r(N):
     r = np.random.randint(0, 2, size=N)
     n_tails = np.sum(np.logical_not(r))
     return r

r(20)
n_tails
