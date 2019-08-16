# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:24:53 2018

@author: magge
"""

import numpy as np

narr = [1, 2, 3, 4, 5]
narr = np.array(narr)
cu_narr = np.cumsum(narr)

marr = [2, 4, 5, 6, 9, 11]
marr = np.array(marr)
cu_marr = np.cumsum(marr)

for i in range(len(cu_narr)):
    if i <= 0:
        if cu_narr[i] >= 0:
            vt = 0
    if i > 0:
        cu_narr[i] >= cu_marr[i-1]
        vt = 0
    else:
        vt = vt + cu_marr[i-1]-cu_narr[i]
        break
    print(vt)




    

