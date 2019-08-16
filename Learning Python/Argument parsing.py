# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:28:31 2018

@author: magge
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--y', type = float, default = 0.5,
                      help ='vertical movement', metavar ='y')

args = parser.parse_args()

y = args.y

