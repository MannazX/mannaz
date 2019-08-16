# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:28:27 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

Jydeseed = 90
np.random.seed(Jydeseed)
Jyder = 100
JP = np.random.randint(1,10,Jyder)
J = np.linspace(1,Jyder,Jyder)
"""
Given 100 Jyder, that have between 1 and 10 Jydepotter each
The amount of Jydepotter that each Jyde has increases by 78%
every year, the following plot and histogram shows the distribution
of Jydepotter that the Jyder will have
including the maximum number of Jydepotter.
"""

list_Jydepotter = []
def Increase_Jydepotter(i,n):
    for J in JP:
        in_JP = J*(1+i)**n
        in_JP = m.ceil(in_JP)
        list_Jydepotter.append(in_JP)
        array_Jydepotter = np.asarray(list_Jydepotter)
    print("The maximum amount of Jydepotter per Jyde is {:}".format(max(array_Jydepotter)))
    print("The average amount of Jydepotter per Jyde is {:}".format(m.floor(sum(array_Jydepotter)/len(array_Jydepotter))))
    print(array_Jydepotter)
    return array_Jydepotter
IJP = Increase_Jydepotter(0.78,10)
print(IJP)
list_Jyder = [i for i in range(len(list_Jydepotter))]

def plot1():
    plt.subplot(1,2,1)
    plt.plot(J,IJP,'g.')
    plt.title("Amount of Jydepotter per Jyde After Increase")
    plt.xlabel("Jyder"), plt.ylabel("Jydepotter")
    #plt.grid(alpha=0.5)
    plt.subplot(1,2,2)
    plt.hist(IJP,color='g')

def plot2():
    plt.plot(list_Jyder,list_Jydepotter,'o')

def plot():
    pick = str(input("Pick the following Jydepotte plot:"))
    if pick == "1":
        plot1()
    elif pick == "2":
        plot2()

plot()
        