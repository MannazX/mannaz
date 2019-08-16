# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:57:55 2018

@author: magge
"""

import random
import numpy as np

N = 500

samples = np.random.randn(N)

m = 2.3
s = 2

samples = np.random.normal(m, s, size=N)

_ = plt.plot(np.arange(N), samples, '+')

_ = plt.hist(samples, normed=True) #plots histogram
