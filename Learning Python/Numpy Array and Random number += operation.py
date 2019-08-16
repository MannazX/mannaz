# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:16:32 2018

@author: magge
"""

import numpy as np

x = np.ones((2,3), dtype=int)
y = np.random.random((2,3))
x *= 3
y += x

print(y)
print(x)
