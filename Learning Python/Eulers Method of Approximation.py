# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:09:14 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

X = []
Y = []
error = []
N = 100
h = 1

def function(x,y):
    """Returns the slope of the differential equation for approximation."""
    return 6*x

def exact_function(t):
    """Returns the exact solution to the differential equation that is to be approximated."""
    return 3*t**2

def euler(f,x0,y0,h,N,r):
    """Computes Eulers method and the error between the approximation and the exact solution."""
    x = x0 - h
    y = y0
    for k in range(m.ceil(N/h)+1):
        x = x + h
        y = y + h*f(x,y)
        X.append(x)
        Y.append(y)
    for i in range(len(Y[:-1])):
        e = abs(Y[i] - exact[i])
        error.append(e)
    k = 0
    for n in error:
        k += 1
        if r == 1:
            print("Error {:} is: {:.2f}".format(k,n))

t = np.linspace(0,N,m.ceil(N/h))
exact = exact_function(t)

euler(function,0,0,h,N,1)

def plot_euler():
    """Plots Eulers method."""
    plt.plot(t,exact,'m',label="Exact Soultion")
    plt.plot(X,Y,'c',linestyle="dashed",label="Euler Approximation")
    plt.title("Eulers Method Approximation of the Differential Equation")
    plt.legend()

def plot_error():
    """Plots the error points."""
    plt.plot(t,error,'g.',label="Error")
    plt.title("Error of Eulers Method")
    plt.legend()
    
pick_plot = str(input("Choose either euler or error:"))
if pick_plot == "euler":
    plot_euler()
elif pick_plot == "error":
    plot_error()
