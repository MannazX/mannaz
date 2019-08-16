# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 10:49:36 2019

@author: magge
"""
import numpy as np
np.random.seed(32)

#n = 100
#a = 1
#b = 25
def median(f,a,b,n):
    np.random.seed(32)
    rand_arr = np.random.randint(a,b,n)
    med_sum = 0
#    print(rand_list)
    for i in rand_arr:
        med_sum += f(i)
    return (1/n)*med_sum
med = median(lambda x:x,1,25,10)

def variance(f,a,b,n):
    np.random.seed(32)
    var_sum = 0
    rand_arr = np.random.randint(a,b,n)
    print(rand_arr)
    for i in rand_arr:
        var_sum += f((i-med)**2)
    return (1/n)*var_sum

print("The mean value of the random array is {:}".format(median(lambda x:x,1,25,10)))
print("The variance of the random array is {:.1f}".format(variance(lambda x:x,1,25,10)))
