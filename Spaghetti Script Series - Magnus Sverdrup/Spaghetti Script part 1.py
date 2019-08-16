# -*- coding: utf-8 -*-
"""
Welcome to the "Spaghetti Script series".
These scripts serve as a collection of conglomorates of everything that Magnus
has learned about coding over the last 3 months of going to university.
The purpose of these scripts is to be creative and self-educating, 
since coding in python 3.6 is a fundamental part of his education.
This script will include various attempts to simulate and model with this
amazing tool and shall be extended as new knowledge is gained. 
So brace yourself, it's going to be a deep rabbithole!
"""
#First import the desired modules for the script
import numpy as np
import matplotlib.pyplot as plt

#A foundation is needed to start a script, this will be in the form of
#data, pick any file to load down data from, and make your own set!
spa_file = open('spa_data1.txt', 'r')
spa_file

x_list = []
y_list = []

for line in spa_file:
    spl = line.split()
    x_list.append(spl[0])
    y_list.append(spl[1])
x_list = np.asarray(x_list)
y_list = np.asarray(y_list)
spa_shuffle = np.random.shuffle(y_list)
rndm_chaos = []
for ran in range(len(y_list)):
    rnd_int = np.random.randint(1,98,ran)
    rndm_chaos.append(rnd_int)
#print(rndm_chaos)
rndm_chaos = np.concatenate(rndm_chaos)
rndm_chaos_len = []
for rlen in range(len(rndm_chaos)):
    rndm_chaos_len.append(rlen)

spa_file.close()

plt.subplot(2,2,1)
plt.plot(rndm_chaos_len,rndm_chaos,'r+')
plt.plot(rndm_chaos_len,rndm_chaos)
plt.xlabel('Random value number'); plt.ylabel('Random value')
plt.subplot(2,2,2)
_ = plt.hist(rndm_chaos)
plt.xlabel('Random distribution intervals'); plt.ylabel('Frequency of distribution')
plt.subplot(2,2,3)
plt.plot(x_list,y_list, 'r+')
plt.plot(x_list,y_list)
plt.axis([0,20,0,20])
plt.subplot(2,2,4)
_ = plt.hist(y_list)
#As you can see, this is an aweful mess of randomly generated values
#Plotting these reveals how chaotic the results can become
#This can be done through numpy arrays aswell, lets dig further into that in
#The next spaghetti script
#Docstring will come below

"""
"""





    