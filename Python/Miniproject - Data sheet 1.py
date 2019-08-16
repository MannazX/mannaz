# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:01:46 2018

@author: magge
"""

import random

infile = open('Inter-arrival time.txt', 'r')
infile
lines = []
arrive_time = []
number_aircraft = []
for line in infile:
    print(line)
    spl = line.split()
    arrive_time.append(spl[0])
    number_aircraft.append(spl[1])
infile.close()

arrive_time[0] # 0-59
number_aircraft[0] # 44
t1 = random.sample(range(0, 59), 44)
t1

