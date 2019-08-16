# -*- coding: utf-8 -*-
# new part of the script comes here.
import numpy as np
import matplotlib.pyplot as plt

    spa_file2 = np.loadtxt('spa_data2.txt', delimiter = ',', dtype = int)
    spa_arr1 = spa_file2[:,0]
    spa_arr2 = spa_file2[:,1]
for i in range(len(spa_arr1)):
    arr_ran = np.random.random(i)
    arr_zeros = np.zeros(i, dtype=float)
    arr_zeros += arr_ran
#print(arr_zeros)
for j in range(len(spa_arr1)):
    arr_ran_int = np.random.randint(0,10,j)
    arr_zeros2 = np.zeros(j, dtype=int)
#print(arr_ran_int)
for i in range(len(arr_ran)):
    if arr_ran_int[i] > arr_ran[i]:
        arr_zeros2 += arr_ran_int
    else:
        break
#print(arr_zeros2)
minarg = np.argmin(arr_ran_int)
maxarg = np.argmax(arr_ran_int)
for i in range(len(arr_ran_int)):
    if minarg < arr_ran_int[i] < maxarg:
        arr_zeros2 -= minarg
        arr_zeros2 += maxarg
    else:
        break

plt.subplot(2,2,1)
plt.plot(spa_arr1,spa_arr2)
plt.plot(spa_arr1,spa_arr2,'r+')
plt.xlabel('Data length value'); plt.ylabel('Data frequency values')
plt.title('Plot of the data values')
plt.subplot(2,2,2)
_ = plt.hist(spa_arr2)
plt.title('Histogram of the data frequency values')
plt.subplot(2,2,3)
#plt.plot(arr_zeros,arr_zeros2)
plt.plot(arr_zeros,arr_zeros2,'o')
plt.xlabel('x-value data'); plt.ylabel('y-value data')
plt.title('Scatter plot of data values in zeros lists')
plt.subplot(2,2,4)
_ = plt.hist(arr_zeros2)
plt.title('Histogram of the y-value data')
#Similar chaotic messes can be made in similar ways with numpy arrays instead
#of lists to generate random values.
#Docstring below
"""
spa_arr1 and 2 are arrays of the first and second data columns respektively
arr_ran = array with randomly generated float values
arr_zeros = array with zero values of float type, that is incremented with the
arr_ran array
arr_ran_int = array with randomly generated integers in the length of spa_arr1
arr_zeros2 = second array with zeros, but of integer type, that is incremented
with the arr_ran_int array.
minarg = The minimum index value of arr_ran_int
maxarg = The maximum index value of arr_ran_int
The first plot shows the values of spa_arr1 and spa_arr2 plotted together
The second plot shows a histogram of the spa_arr2 values
The third plot shows the plotted values of arr_zeros and arr_zeros2 values.
The fourth plot shows a histogram of the arr_zeros2 values
The third and the fourth plot will vary when plotted multiple times, unless if
a numpy seed function is added.
"""
