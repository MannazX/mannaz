# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:18:13 2018

@author: magge
"""

string = 'Ottawa: -32.0 C at 2:00 am'
string[:8]
string[8]
string[-1]
string[:-1]
string[1:3]

yak_temp = 'Yakutsk: -57.8 C, January 4. 2:30 pm'
yak_temp[:8]
yak_temp[0:-2]

if 'C' in yak_temp:
    print('Temperature in Celsius')
else:
    print('Temperature not in Celsius')

