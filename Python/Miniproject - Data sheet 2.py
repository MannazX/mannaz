# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 12:18:01 2018

@author: magge
"""

infile = open('Landing duration.txt', 'r')
infile
landing_duration = []
number_aircraft = []
for line in infile:
    print(line)
    spl = line.split()
    landing_duration.append(spl[0])
    number_aircraft.append(spl[1])
infile.close()

landing_duration[0]
