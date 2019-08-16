# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:02:16 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

Q = [[20,33,42,51],[52,21,14,42],[45,75,23,68],[23,95,36,19]]
Q = np.asarray(Q)
Qt = np.transpose(Q)
Qi = np.linalg.inv(Q)
Qs = Q @ Qt
eig = np.linalg.eig(Qs)
print(eig)
eigval = np.linalg.eigvals(Qs)
eiglist = []
for i in range(len(eigval)):
    eiglist.append(i)

#plt.plot(eiglist,eigval,'md')
x = [i for i in range(len(Qs))]
plt.subplot(2,2,1)
plt.plot(x,Qs,'bo')
plt.subplot(2,2,3)
plt.plot(x,Qt,'mo')
plt.subplot(2,2,2)
plt.plot(x,Qi,'ro')