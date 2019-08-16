# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:15:53 2018

@author: magge
"""

import sys

try:
    C = float(sys.argv[1]) #sys.argv[1] is the error - index error
except IndexError:
    print("Celcius degrees must be provided on the command\
          line.")
    sys.exit(1)
except ValueError:
    print("Celcius degree should be a number, not\
          '{}'".format(sys.argv[1]))
    sys.exit(1)