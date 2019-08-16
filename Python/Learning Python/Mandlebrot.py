# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:28:39 2018

@author: magge
"""

import matplotlib.pyplot as plt
import numpy as np

def mandlebrot(h,w,maxit=20):
    y,x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    
    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2
        
    return divtime
plt.imshow(mandlebrot(200,200))
plt.show()