# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:36:11 2018

@author: magge
"""

s1 = 'Hej, med'
s2 = 'Dig, der'
s3 = s2.lower()
s3 = s3.replace(',', '')
s4 = s1.replace(',', '')
('{:s} {:s}'.center(50, '*').format(s4, s3))