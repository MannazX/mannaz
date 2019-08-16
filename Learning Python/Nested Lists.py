# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 22:57:43 2018

@author: magge
"""
import matplotlib.pyplot as plt

Cdeg = range(-30, 60, 5)
Fdeg = [(9.0/5.0)*C + 32 for C in Cdeg]
tab1 = [Cdeg, Fdeg]
tab2 = [[C,F] for C,F in zip(Cdeg,Fdeg)]
tab3 = zip(Cdeg,Fdeg)
plt.scatter(Cdeg,Fdeg)

#Traversing both lists at the same time.
for i in range(len(Cdeg)):
    print("%5.1f %5.1f" \
          % (Cdeg[i], Fdeg[i]))

#Prefer this one.
for C,F in zip(Cdeg,Fdeg):
    print("%5.1f %5.1f" % (C,F))

scores = []
scores.append([3, 4, 8, 19])
scores.append([9])
scores.append([6, 9, 11, 14, 17, 15])
for player in scores:
    for game in player:
        print("%4d" % game),
    print("")
