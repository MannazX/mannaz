# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:20:15 2018

@author: magge
"""

poly_dict = {4:1, 3:2, 2:8, 1:12, 0:4}

def poly(data, x):
    sum = 0
    for pow in data:
        sum += data[pow]*x**pow
    return sum

poly(poly_dict, 5)
poly(poly_dict, 4)
poly(poly_dict, 3)
poly(poly_dict, 2)
poly(poly_dict, 1)

