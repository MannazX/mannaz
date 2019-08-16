# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:34:22 2018

@author: Andreas
"""
import numpy as np
from matplotlib import pyplot as plt

# Defines constants
g = 9.81
N = 10 # Is the number of points in the interval

# Takes user input as string
v0_str = input("Input an array of values for v0 seperated by comma ")

# Converts user input from string to float and reshapes it to a vector
v0_array = np.fromstring(v0_str,dtype=float,sep=",").reshape(-1,1)

# Creates an empty matrix with the dimentions corresponding to the length of v0_array times the lenght of N
t = np.empty((len(v0_array),N))

# Inserts t-values into the empty matrix, so that the matrix has all values of t for each v0
for idx, v0 in enumerate(v0_array):
    t[idx,:] = np.linspace(0,2*v0/g,N)

# Calculates y as a matrix with the same dimentions as t
y = v0_array * t - 1/2*g*t**2

# Plots the curves
plt.plot(t.T,y.T)
