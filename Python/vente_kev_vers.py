# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:52:11 2018

@author: Kevin Jepsen
"""

import numpy as np

#anktid = np.random.randint(0, 10, 10, dtype=int)
#lndtid = np.random.randint(0, 10, 10, dtype=int)
#enlst = []

anktid   = [1,2,1,2,1,3]
lndtid = [2,1,4,2,3,1]

c_anktid = np.cumsum(anktid)
delay = []
fordig = []

g = c_anktid[0] + lndtid[0]
fordig.append(g)
delay.append(0)

for i in range(1,len(anktid)):
    g = c_anktid[i] + lndtid[i]
    
    if c_anktid[i] < fordig[i-1]: 
        forskel = fordig[i-1]-c_anktid[i]
        delay.append(forskel)
        noet = g+delay[i]
        fordig.append(noet)
    else:
        delay.append(0)
        fordig.append(g)
    #enlst.append(sum(delay))
    #print(enlst)        
    
#print('Det sidste fly er landet ved t = {:} '.format(fordig[-1]))
#print('Den kumulerede ventetid er {:} sekunder'.format(sum(delay)))
#print('En liste over hvornår flyene lander: \n {:}'.format(fordig))
#print('En liste over hvor lang ventetid de individuelle fly har: \n {:}'.format(delay))