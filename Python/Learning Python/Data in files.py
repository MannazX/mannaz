# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:05:35 2018

@author: magge
"""

infile = open('Data for learning python.txt', 'r')
infile

lin = []
for line in infile:
    print(line)
    lin.append(line)

#Compute an average
infile.seek(0)

mean = 0
count = 0
for line in infile:
    number = float(line)
    mean += number
    count += 1
mean = mean/count
print(mean)



#while True:
#    line = infile.readline()
#    print(line)
#    if not line:
#        break

#infile.seek(0)
#lines = infile.readlines
#
#infile.close()