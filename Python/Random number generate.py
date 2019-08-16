# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:31:37 2018

@author: magge
"""
import random
import numpy as np

a = np.arange(10)
indeks = np.random.randint(0,10, size=5)
a[indeks]

udvalg = np.random.choice(a, size=5, replace=False) #generere tal med tilbagelægning
udvalg

np.random.shuffle(a)
udvalg = a[:5]
udvalg

værdier = np.array(['plat', 'krone'])
udfald = np.random.choice(værdier, size=100, replace=True)
np.sum(udfald == 'plat') #gives boolean array of true and false
#replace giver resultater med tilbagelægning
