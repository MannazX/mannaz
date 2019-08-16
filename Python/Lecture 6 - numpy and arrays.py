# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:31:05 2018

@author: magge
"""

import numpy as np

r = [1, 2, 3]
n = 3
c = int(1)
p = 1; q = 3

a = np.array(r); a #List converted to array.
#array([1, 2, 3])

a = np.zeros(n); a
#array([0., 0., 0.])

a = np.zeros((n, n)); a
#array as matrix form

a = np.zeros_like(c)
a.dtype #dtype('int32') #windows standard.

a = np.linspace(1/3, 23.9, 12); a
#uniformly spaced values

a = np.arange(2, 18, 2.1); a
#create range of integers

a[2]#6.199999999999999 index from list

a[1:-1] #slice of the list
#array([ 4.1,  6.2,  8.3, 10.4, 12.5, 14.6])

b = a[1:-1]; b[0] = 0 #different views on array
a #array([ 2. ,  0. ,  6.2,  8.3, 10.4, 12.5, 14.6, 16.7])
# b is a variable that only points to a part of the array
# changing in b also changes in a.

x2 = np.linspace(0,1,n); x2 #array([0. , 0.5, 1. ])

y2 = np.empty(n)
for i in range(n):
    y2[i] = f(x2[i])
y2 #operations on lists in python is slow.
#array([0.   , 0.125, 1.   ])

#instead numpy arrays
y2 = f(x2)
y2 #wasn't that just simple! 
#array([0.   , 0.125, 1.   ])

