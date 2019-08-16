# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:14:26 2018

@author: magge
"""

def line(x0, y0, x1, y1):
    """
    computers a, b in y=ax + b given two points.
    
    computes the coefficient a and b i  the mathematical
    expression for a straight line y=a*x + b that goes
    through the two points (x0, y0) and (x1, y1).
    
    x0,y0: point on the line (floats)
    x1,y1: another point on the line (floats)
    
    returns the coefficients a, b (floats) for the line.
    """
    
    a = (y1 - y0)/float(x1 - x0)
    b = y0 - a*x0
    return a, b

line(1, 3, 5, 7)
