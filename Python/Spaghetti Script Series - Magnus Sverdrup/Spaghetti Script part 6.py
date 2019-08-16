# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x_arr = np.arange(2,20,2)
y_arr = np.arange(2,36,4)
x_slice = x_arr[1:-2]
y_slice = y_arr[1:-2]

x_table = np.arange(8).reshape((4,2))
y_table = 4*np.ones((4,2))
pr_table = x_table*y_table
val_arr = np.concatenate(pr_table)
cu_sum_arr = np.cumsum(val_arr)

n_table = np.arange(16).reshape((4,4))
p_table = 2*np.ones((4,4))
sum_table = n_table + p_table
pro_table = n_table * p_table
dotp_tables = sum_table @ pro_table
val_sum = np.concatenate(sum_table)
val_pro = np.concatenate(pro_table)
val_dp = np.concatenate(dotp_tables)
cu_sum_dp = np.cumsum(val_dp)

for length in range(len(val_sum)):
    len_arr = np.linspace(0,length+1,length+1)
#print(len_arr)

for i in pr_table:
    print(i)

for i in sum_table, pro_table, dotp_tables:
    print(i)

plt.subplot(2,2,1)
plt.plot(val_arr,cu_sum_arr, 'mo')
plt.title("Values plotted against their cumulative sum values")
plt.xlabel("Values"); plt.ylabel("Cumulative sum values")
plt.subplot(2,2,2)
plt.plot(x_slice,y_slice, 'rd')
plt.title("Plot of x and y slices")
plt.xlabel("x-slices"); plt.ylabel("y-slices")
plt.subplot(2,2,3)
Sum, = plt.plot(len_arr,val_sum,linestyle='dashed',label="Sum")
Product, = plt.plot(len_arr,val_pro,'ro',label="Product")
Dotproduct, = plt.plot(len_arr,val_dp,'md',label="Dot-product")
plt.title("Values of sum, product, and dotproduct of the tables")
plt.xlabel("Values"); plt.ylabel("Length values")
plt.legend(handles = [Sum,Product,Dotproduct], loc = "upper left")
plt.subplot(2,2,4)
plt.plot(val_dp,cu_sum_dp,'kx')
plt.title("Values of the dot-product plotted against their cumulative sum values")
plt.xlabel("Values"); plt.ylabel("Cumulative sum values")