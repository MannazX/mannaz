# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:01:43 2018

@author: magge
"""

infile = open('data.txt', 'r')

infile.seek(0)
count = 0
mean = 0
for line in infile:
    number = float(line)
    mean += number
    count += 1
mean = mean/count
print(mean)

infile.seek(0)  # genstart læsning af filen

lines = infile.readlines()
mean = sum([float(line) for line in lines])/len(lines)
mean

infile = open('data1.txt', 'r')
numbers = [float(line) for line in infile.readlines()]
infile.close()
mean = sum(numbers)/len(numbers)
mean

infile.seek(0)  # genstart læsning af filen

numbers = [float(w) for w in infile.read().split()]
mean = sum(numbers)/len(numbers)
infile.close()
mean
