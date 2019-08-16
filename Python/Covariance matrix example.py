# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:31:45 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

C = [[1.5625,0.2656,0.8281,1.8438],[0.2656,0.8281,1.5938,-0.6250],[0.8281,1.5938,8.4219,0.2188],[1.8438,-0.6250,0.2188,4.4375]]
C = np.asarray(C)
print("This is the covariance matrix C")
print(C)
eig_val, eig_vec = np.linalg.eig(C)
print("This is the eigen vector of C")
print(eig_val)
print("These are the eigenvectors of C contained in one matrix")
print(eig_vec)

u1 = eig_vec[:,0]
u2 = eig_vec[:,1]
u3 = eig_vec[:,2]
u4 = eig_vec[:,3]

x = [i for i in range(len(eig_val))]
plt.plot(x,eig_val,'o-')
