# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:07:23 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

special_list = []
special_number = 30
for loop in range(-special_number,special_number+1,1):
    special_list.append(loop)
s = special_list
print(s)
# Now it is time to do something special with this specific list!
print(57*'-')
special_list2 = []
for x in s:
    t = -x**2 - 20*x + 200
#    t = 5*x**3 + 20*x**2 - 50*x + 200
    special_list2.append(t)
sp = special_list2
s = np.asarray(s)
sp = np.asarray(sp)
cs = np.cumsum(sp)
for S,SP,CS in zip(s,sp,cs):
    print("%d %5d %5d" % (S,SP,CS))

print(57*'-')
arg_list = []
bit_list = []
for i in range(len(sp)):
    if sp[i] > cs[i]:
        bit_list.append(1)
    else:
        bit_list.append(0)

signal_list = []
for j in range(len(bit_list)):
    if bit_list[j] == bit_list[np.argmax(bit_list)]:
        signal_list.append(sp[j])
    else:
        signal_list.append(0)

print(bit_list)
print(57*'-')
print(signal_list)
    
def plot1():
    plt.subplot(1,2,1)
    plt.plot(s,sp,'m.',scalex=True,scaley=True)
    plt.title("Plot of the special list function")
    plt.subplot(1,2,2)
    plt.plot(s,cs,'k.',scalex=True,scaley=True)
    plt.title("Plot of the cumulative sum of the special list function")

def plot2():
    plt.subplot(1,2,1)
    plt.plot(s,bit_list,'k')
    plt.title("Heaveside plot of the binary sample")
    plt.subplot(1,2,2)
    plt.plot(s,signal_list,'b')
    plt.plot(s,sp,'g')
    plt.title("Signal plot filtered by binary sample")


def plots():
    pick = str(input("Choose the desired plot 1 or 2:"))
    if pick == "1":
        plot1()
    elif pick == "2":
        plot2()
"""
The plots() function chooses the plots that are desired by
the user. The options are plots of the special function and
its cumulative sum in one plot and the unit step of the binary
signal in the other plot.
"""
        
plots()
    