# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def mean(f,a,b,n):
    np.random.seed(24)
    mean_sum = 0
    rand_arr = np.random.randint(a,b,n)
    for i in rand_arr:
        mean_sum += f(i)
    return (1/n)*mean_sum
print("The mean value of the random numbers is {:.1f}".format(mean(lambda x:x,1,10,20)))
mean = mean(lambda x:x,1,10,20)

def variance(f,a,b,n):
    np.random.seed(24)
    var_sum = 0
    rand_arr = np.random.randint(a,b,n)
    for i in rand_arr:
        var_sum += f((i-mean)**2)
    return (1/n)*var_sum
print("The variance of the random numbers is {:.1f}".format(variance(lambda x:x,1,10,20)))
var = variance(lambda x:x,1,10,20)

standard_deviation = np.sqrt(var)
print("The standard deviation of the random numbers is {:.1f}".format(standard_deviation))

def plot(a,b,n):
    np.random.seed(24)
    rand_arr = np.random.randint(a,b,n)
    len_list = []
    for i in range(1,n+1):
        len_list.append(i)
    len_arr = np.asarray(len_list)
    plt.subplot(1,2,1)
    plt.plot(len_arr,rand_arr,'gx')
    plt.subplot(1,2,2)
    plt.hist(rand_arr,color="r")
plot(1,10,20)    