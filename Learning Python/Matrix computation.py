# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:47:28 2019

@author: magge
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

A = np.ones((2,2), dtype=int)
B = np.ones((2,3), dtype=int)

C = [[1,2,3],[4,5,6],[7,8,9]]
D = np.transpose(C)
T = C*D
u1 = [1,1,1]
u1 = np.asarray(u1)
v1 = u1 @ T

print(np.linalg.eig(T))

I = [[2,0,0],[0,2,0],[0,0,2]]
R = T-I
J = np.linalg.det(R)
lambda_T = np.linalg.eigvals(T)

conC = np.concatenate(C)
conD = np.concatenate(D)

cuC = np.cumsum(conC)
cuD = np.cumsum(conD)

for i in range(len(cuC)):
    if cuC[i] > cuD[i]:
        cuD[i] += 10
    else:
        cuC[i] += 10
#    print(cuC)
#    print(cuD)

print(cuC)
print(cuD)
plt.subplot(1,2,1)
plt.plot(conC,conD,'go')
plt.subplot(1,2,2)
plt.plot(cuC,cuD,'mo-')