# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:57:13 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

def some_function(a,b,i,n):
    some_list = []
    while True:
        i += 1
        some_list.append(i)
        if i > n+1:
            break
    some_list = np.asarray(some_list)
    random_array = np.random.uniform(a,b,n)
    for k in range(len(random_array)):
        if some_list > random_array:
            random_array[k] *= k
        else:
            random_array[k] += k
    plt.plot(some_list,random_array,'o')
    return some_list, random_array


    
        
