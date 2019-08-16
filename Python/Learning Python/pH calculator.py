# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:41:45 2018

@author: magge
"""

from math import log

print("Computes the pH of the solution, given the hydronium concentration in mol/L")
h = input("H =")
H = float(h)
pH = -log(H, 10)
print("The pH of the solution is {:.2f}".format(pH))

"""
This script computes the pH of a solution given the hydronium concentration
h is the input command for typing in the hydronium concentration
H is the hydronium concentration value in mol/L
pH is the function for computing the pH
"""