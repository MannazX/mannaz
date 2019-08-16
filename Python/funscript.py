# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:52:30 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

xl = []
yl = []
for i in range(11):
    x = np.random.randint(1,10)
    def exponent_function(x):
        return np.exp(x)
    y = exponent_function(x)
    for j in xl:
        if i > 5:
            x -= 1
    xl.append(x)
    yl.append(y)
    print("{:} {:5} {:8.2f}".format(i,x,y))
    
plt.plot(xl,yl,'o')


    


