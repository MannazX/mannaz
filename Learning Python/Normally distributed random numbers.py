# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:10:06 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

N = 900

sample = np.random.randn(N)
n = 5
s = 12

sample = np.random.normal(n,s,size=N)

_ = plt.plot(np.arange(N), sample, '+')
