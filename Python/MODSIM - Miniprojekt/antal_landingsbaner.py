# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:15:03 2018

@author: magge
"""

import numpy as np
np.random.seed(234)
liste = []
anktid = [1,0,1,1,2]
#anktid = np.random.randint(0,5,5, dtype = int)
anktid = np.asarray(anktid, dtype = int)
c_ank = np.cumsum(anktid)
lndtid = [3,2,3,4,1]
lndtid = np.asarray(lndtid, dtype = int)
#lndtid = np.random.randint(1,5,5, dtype = int)
#print(anktid, "\n", lndtid)
k = 2
landingsbaner = np.zeros(k, dtype = int)
ventetid = 0


for i in range(len(anktid)):
    for j in range(len(landingsbaner)):
        if landingsbaner[j] == 0:
            landingsbaner[j] += lndtid[i]
            print(landingsbaner)
            break
        else:
             if anktid[i] < landingsbaner[np.argmin(landingsbaner)]:
                 ventetid += landingsbaner[np.argmin(landingsbaner)]-anktid[i]
             landingsbaner[np.argmin(landingsbaner)] += lndtid[i]
             print(landingsbaner)
             print(ventetid)
             break


#print(landingsbaner)
print(np.argmin(landingsbaner))
