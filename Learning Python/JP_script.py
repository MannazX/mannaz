# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:28:27 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m
"""
Given 100 Jyder, that have between 1 and 10 Jydepotter each
the amount of Jydepotter that each Jyde has increases by 130%
every year, the following plot and histogram shows the distribution
of Jydepotter that the Jyder will have
including the maximum number of Jydepotter.
"""
Jydeseed = 90
main_Jydepotte = np.random.seed(Jydeseed)
N = 100
JP = np.random.randint(1,10,N)
J = np.linspace(1,N,N)
def Increase_Jydepotter(i,n):
    list_JP = []
    for Jydeloop in JP:
        in_JP = Jydeloop*(1+i)**n
        in_JP = m.ceil(in_JP)
        list_JP.append(in_JP)
    array_JP = np.asarray(list_JP)
    print("The maximum amount of Jydepotter per Jyde is {:}".format(max(array_JP)))
    print("The total amount of Jydepotter in that year is {:}".format(sum(array_JP)))
    print(array_JP)
    return array_JP
IJP = Increase_Jydepotter(1.3,10)
plt.subplot(1,2,1)
plt.plot(J,IJP,'g.')
plt.title("Amount of Jydepotter per Jyde After Increase")
plt.xlabel("Jyder"), plt.ylabel("Jydepotter")
#plt.grid(alpha=0.5)
plt.subplot(1,2,2)
plt.hist(IJP,color='g')