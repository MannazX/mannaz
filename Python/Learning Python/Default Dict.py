# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:10:30 2018

@author: magge
"""

from collections import defaultdict

def polynomial_default():
    return 0.0

p3 = defaultdict(polynomial_default)
p3 = defaultdict(lambda: 0.0)
p3 = defaultdict(float)
print(p3)

p3.update(y)
print(p3)
p3[-3]
p3[-1]
p3[2]
p3[3]
p3[4]
p3[6]
p3[5]
p3 #The values looked up are added to the dictionary

k = {'keyx':{'keyxt':1}, 'keyy':2}
k['keyx']['keyxt']
for j in k:
    print(j)

for j in k:
    print(k[j])

for i in p3:
    print(p3[i])

