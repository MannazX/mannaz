# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:28:15 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

infile = open('pos.txt', 'r')
infile
lines = []
x = []
y = []
s = 15.0
t = np.linspace(0, 360, 25)
for line in infile:
    print(line)
    spl = line.split()
    x.append(spl[0])
    y.append(spl[1])
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    
infile.close()
plt.plot(x, y)

plt.plot(t,x)
plt.plot(t,y)
