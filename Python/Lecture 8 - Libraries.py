# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:17:48 2018

@author: magge
"""

pollen = [10.1, 3.7, 4.7]
træer = ['el', 'hassel', 'elm']
pollen = {'el': 10.1, 'hassel': 3.7, 'elm': 4.7}
pollen

for træ in pollen:
    print(træ)
    print(pollen[træ])
    
if 'el' in pollen:
    print("Vi har et pollental for el.")
    
'bøg' in pollen #not in list

pollen.keys() #order is not always properly defined
pollen.values()


