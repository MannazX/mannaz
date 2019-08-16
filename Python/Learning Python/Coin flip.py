# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:14:36 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

np.random.seed(102)
hl = []
tl = []
xl = []
def coin_flip(n):
    head = 0
    tail = 0
    for i in range(n):
        flip = np.random.choice(['Head','Tail'])
        if flip == 'Head':
            head += 1
            print("Head")
        if flip == 'Tail':
            tail += 1
            print("Tail")
#        print("{:} {:}".format(head,tail))
    hl.append(head)
    tl.append(tail)
    return (head, tail)

for i in range(1000):
    flip = coin_flip(100)
    print(flip)
    xl.append(i+1)

plt.plot(xl,hl,'ro')
plt.plot(xl,tl,'go')
