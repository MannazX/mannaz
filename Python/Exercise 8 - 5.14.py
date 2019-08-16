# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:31:51 2018

@author: magge
"""

import matplotlib.pyplot as plt

infile = open('xy.txt', 'r') #opens textfile saved
infile
lines = []
x = []
y = []
for line in infile:
    print(line)
    spl = line.split()
    x.append(spl[0])
    y.append(spl[1])
    x = [float(i) for i in x]
    y = [float(i) for i in y]

#infile.seek(0)

#mean = 0
#count = 0
#for y in infile:
    #number = float(y)
    #mean += number
    #count += 1
#mean = mean/count
#print(mean)

infile.close()
plt.plot(x, y)



