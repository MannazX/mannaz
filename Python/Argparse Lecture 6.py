# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:02:47 2018

@author: magge
"""

import argparse
parser = argparse.ArgumentParser()

#Arguments that argparse is going to interpret (parse).
parser.add_argument('--v0', type=float, default=1.0,
                    help='initial velocity', metavar='v0')

parser.add_argument('--s0', type=float, default=15.0,
                    help='initial position', metavar='s0')

parser.add_argument('--a', type=float, default=9.81,
                    help='acceleration', metavar='a')

parser.add_argument('--t', type=float, default=8.0,
                    help='time', metavar='t')

args = parser.parse_args()
#Extracts parameters from above argument.

v0 = args.v0
s0 = args.s0
a = args.a
t = args.t

st = s0 + v0*t + 0.5*a*t**2

print("s({:.2f}) = {:.2f}".format(t, st))
