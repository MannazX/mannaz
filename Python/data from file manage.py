# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:26:44 2018

@author: magge
"""

infile = open('data.txt', 'r')
infile

while True:
    line = infile.readline()
    print(line)
    if not line:
        break
    
lines = infile.readlines
lines

infile.seek(0)

mean = 0
count = 0
for line in infile:
    number = float(line)
    mean += number
    count += 1
    mean = mean/count
    print(mean)
