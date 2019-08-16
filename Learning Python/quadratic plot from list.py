# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:16:18 2018

@author: magge
"""
import matplotlib.pyplot as plt

liste = [2,3,4,5,7,8,9,11,13,15]
for i in liste:
    print("element in list:",i)
print("The list of elements has %d units" % (len(liste)))

a_list = [-2+5.2*k for k in range(0,26)]
n_list = [-2.3*t**2 + 4.1*t + 43 for t in a_list]

plt.scatter(a_list,n_list)
