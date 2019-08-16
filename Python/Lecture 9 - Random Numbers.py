# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:20:24 2018

@author: magge
"""

import random
import numpy as np

random.seed(42)

['%.2f' % random.random() for i in range(7)]

random.seed(42)
['%.2f' % random.random() for i in range(7)]


uniformt_tal = random.random()
uniformt_tal #generates random number

uniformt_tal = random.uniform(3,7)
uniformt_tal #generates random number between 3 and 7

np.random.random(size=10000)

np.random.random() #numpy has random generator function




