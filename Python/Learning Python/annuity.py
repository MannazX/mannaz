# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:09:22 2018

@author: magge
"""

"""
Calculates between
 G principle
 r interest
 n number of payments
 y payment
 
for annuity loans
"""

from math import log

def pay(G, r, n):
    return G * (r/(1-(1+r)**(-n)))

def prin(y, r, n):
    return y * ((1-(1+r)**(-n))/r)

def num_pay(G, r, y):
    return -log(1-G*r/y)/log(1+r)

def yr_to_m(r):
    (1+r)**(1.0/12) - 1

