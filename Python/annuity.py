# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:34:05 2018

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

def payment(G, r, n):
    G*(r/(1-(1+r)**(-n)))
    
def principal(y, r, n):
    return y*(1-(1+r)**(-n))/r

def number_of_payments(G, y, r):
    return -log(1-G*r/y)/log(1+r)
    
def year_to_month(r):
    return (1+r)**(1.0/12)-1

import sys
sys.path.insert(0,'../my modules')

from annuity import payment, principal
y = payment(1e6, 0.04, 30)
