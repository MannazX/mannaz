# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:01:18 2018

@author: magge
"""

from math import sin, cos, exp
import numpy as np

n = 5
x = np.linspace(0, 1, n)
r = np.zeros(n)

for i in range(n):
    r[i] = sin(x[i])*cos(x[i])*exp(-x[i]**2) + 2 + x[i]**2
r #array([2.        , 2.28768931, 2.57766913, 2.84667776, 3.16725591])

#vectorised
r = np.sin(x)*np.cos(x)*np.exp(-x**2) + 2 + x**2
r

#scalar argument
def sgn(x):
    if x>=0:
        return 1
    else:
        return -1

a >= 0 #array([False,  True])
a = np.array([-2, 2])
a #array([-2,  2])

def sgn(x):
    test=(x>=0)
    return 2*test-1
sgn(a) #array([-1,  1])

table = np.arange(4).reshape((2,2))
table #array([[0, 1],
       #[2, 3]])
table[1][1]
table[1,1]


A = 2*np.ones((2,2))
A #array([[2., 2.],
       #[2., 2.]])
       
B = 3*np.ones((2,2))
B #array([[3., 3.],
       #[3., 3.]])

A*B #array([[6., 6.],
       #[6., 6.]])

A.dot(B) #array([[12., 12.],
       #[12., 12.]])
       
A @ B #same as A.dot(B)

#Use array data type rather than matrix data type.


