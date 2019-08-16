# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:39:07 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

"""
The following script is about the Fibonacci sequence and the
Golden ratio, the first part of the script approximates
the golden ratio to 15 decimal places (40 iterations). 
The second part of the script computes the Fibonacci sequence 
and appends the numbers in a list (39 terms). The last part of 
the script plots the Fibonacci numbers, their square values, the
approximation of the Golden ratio, and the error decrease.
"""

al = []
fl = []
el = []
a0 = 0
a1 = 1
al.append(a1)

phi = (1+np.sqrt(5))/2

for i in range(2,40):
    a = a0 + a1
    al.append(a)
    f = a/a1
    err = abs(f-phi)
    fl.append(f)
    el.append(err)
    print("{:.15f} {:15.15f}".format(f,err))
    a0 = a1
    a1 = a
print(48*'-')
print(al)
print(48*'-')

al2 = [i**2 for i in al]

x1 = [i for i in range(len(al))]
x2 = [j for j in range(len(fl))]
x3 = [k for k in range(len(el))]

def plot():
    plot = str(input("Choose one of the plots (1, 2, 3, or 4):"))
    if plot == "1":
        plt.plot(x1,al,'g.')
        plt.title("Fibbonacci Numbers Generated")
    elif plot == "2":
        plt.plot(x1,al2,'m.')
        plt.title("Squares of Fibbonacci Numbers")
    elif plot == "3":
        plt.plot(x2,fl,'k.')
        plt.title("Approksimation of the Golden Ratio")
    elif plot == "4":
        plt.plot(x3,el,'b.')
        plt.title("Erorr of the Golden Ratio Approksimation")
    else:
        print(plot, "is not one of the plot options, there are four, please choose one of them.")

plot()
        
