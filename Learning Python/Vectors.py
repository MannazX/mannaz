# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:47:37 2018

@author: magge
"""
from math import exp
import numpy as np

x = 3
y = 5
x1 = 2
x2 = 4

v1 = [x,y]
v1.append(7)
print(v1)

v2 = (x,y)
v3 = (x,y,x1,x2)

v_ext = [exp(-i/1.2) for i in range(200)] #200 dimensional vector

#lists used as vectors
def f(x):
    return 2*x**4

n = 10
dx = 1.0/(n-1)
listx = [i*dx for i in range(n)]
listy = [f(x) for x in listx]
vect = [[x,y] for x, y in zip(listx,listy)]

conc_vect = np.concatenate(vect)
print(vect) #prints the vector
print(conc_vect) #unpacks the vector
