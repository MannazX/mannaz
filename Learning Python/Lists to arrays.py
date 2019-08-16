# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:06:24 2018

@author: magge
"""

import numpy as np
import matplotlib.pyplot as plt

list1 = [2,3,4,8,9,11,23]
list1 = np.array(list1)
list2 = [3,5,6,9,16,23,31]
print(list1,list2)

ar1 = np.cumsum(list1)
ar2 = np.cumsum(list2)

plt.scatter(ar1,ar2, c='r', marker='o')


    

        
