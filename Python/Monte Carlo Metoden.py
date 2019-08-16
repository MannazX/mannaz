# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:46:29 2018

@author: magge
"""
import random
import numpy as np

N = 1000000  # antal eksperimenter
udfald = np.random.randint(1, 6+1, size=(2, N))  # generér samtlige terningkast på én gang

sorte = udfald[0,:]  # viste øjne for alle kast med den sorte terning
grønne = udfald[1,:]  # viste øjne for alle kast med den grønne terning
hændelser = sorte > grønne  # hændelser[i] er sand hvis sorte[i] > grønne[i]
M = np.sum(hændelser)  # vi udnytter at alle de sande værdier tolkes som 1 og kan hermed optælle dem
M
