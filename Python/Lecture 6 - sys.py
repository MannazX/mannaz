# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 08:50:05 2018

@author: magge
"""

import sys

C = float(sys.argv[1])
F = (9.0/5)*C + 32
print("{:.2f} degree Celcius is {:.2f} degrees Fahrenheit". format(
        C, F))
#type run "Lecture 6 - sys.py" 45 in console.
#Result is 
#45.00 degree Celcius is 113.00 degrees Fahrenheit

C = float(sys.argv[1])
F = (9.0/5)*C + 32
for C in Cdegrees:
    Cdegrees = range(10, 25, 5)
    
print("{:.2f} and {:.2f} degree Celcius is {:.2f} and {:.2f} degrees Fahrenheit".format(
        C, F))