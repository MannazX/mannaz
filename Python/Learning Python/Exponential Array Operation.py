# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:29:12 2018

@author: magge
"""

import numpy as np
a = np.arange(10)**3
print(a)
a[2:5]
for i in a:
   # print(i*2*a)
    print(i**(1/3))

#little extra thing
t = np.floor(10*np.random.random((2,12)))
t
yt = np.hsplit(t,3)
y = np.hsplit(t,(3,4))

