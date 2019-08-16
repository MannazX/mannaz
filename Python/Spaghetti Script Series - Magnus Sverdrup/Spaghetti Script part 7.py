# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

data_file = np.loadtxt('spa_data2.txt', delimiter = ',', dtype = int)
xdata = data_file[:,0]
ydata = data_file[:,1]
def median(f):
    med_sum = 0
    n = len(ydata)
    for i in ydata:
        med_sum += f(i)
    return (1/n)*med_sum
print("The median value for the y-data is {:.1f}".format(median(lambda x:x)))
med = median(lambda x:x)
def variance(f):
    var_sum = 0
    n = len(ydata)
    for i in ydata:
        var_sum += f((i-med)**2)
    return (1/n)*var_sum
print("The variance of the y-data is {:.1f}".format(variance(lambda x:x)))
var = variance(lambda x:x)
standard_deviation = np.sqrt(var)
print("The standard deviation of the y-data is {:.1f}".format(standard_deviation))

plt.subplot(1,2,1)
plt.plot(xdata,ydata,"g")
plt.title("x-data plotted against y-data")
plt.xlabel("x-data"); plt.ylabel("y-data")
plt.subplot(1,2,2)
plt.hist(ydata)
plt.title("Histogram of ydata values")
plt.xlabel("Value intervals of y-data"); plt.ylabel("Frequency of the values in the intervals")

