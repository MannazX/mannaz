# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:19:14 2018

@author: magge
"""

import numpy as np

np.random.seed(32)

Ar = np.arange(20)
Ind = np.random.randint(0,20,size=10)
Ar[Ind]

selection = np.random.choice(Ar, size=10)
selection

np.random.shuffle(Ar)

selection = Ar[:5]
print(selection) #prints selection of 5 elements from array.
