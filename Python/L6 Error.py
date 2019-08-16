# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:44:56 2018

@author: magge
"""

import sys

try:
    C = float(sys.argv[1])
except:
    print("Please provide Celcius degree as input on the command line".)
    sys.exit(1)