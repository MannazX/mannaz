# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:58:49 2018

@author: magge
"""

students = ['Erin', 'James', 'Marco', 'Vera', 'Vladislav', 'Jane', 'Annie', 'Derek', 'Chris']
years_at_uni = [3,2,3,1,4,2,4,3,2]

years_dict = {'Erin':3, 'James':2, 'Marco':3, 'Vera':1, 'Vladislav':4, 'Jane':2, 'Annie':4, 'Derek':3, 'Chris':2}
print(years_dict['James'])

l = []
for year in years_dict:
    print(year)
    l.append(years_dict[year])
    print(years_dict[year])
print(l)

if 'Marco' in years_dict:
    print('There is a student from Italy')

'Jared' in years_dict #answers false - Boolean response to answer in dictionary
years_dict.keys() #Finds keys - Students

years_dict.update({'Carlos':1, 'Jordan':4, 'Valery':2}) #Adds three new keys and values two dictionary
years_dict

if 'Vladislav' or 'Vera' in years_dict:
    print('There are two students from Ukraine')

dict_copy = years_dict.copy()
dict_copy.update({'Xenia':4, 'Jan':2})
dict_copy
del dict_copy['Carlos']
print(dict_copy)

if 'Xenia' or 'Jan' in years_dict:
    print('There are two new Polish students')
else:
    print('They are not in this list, they have been added to the copy')
    
if 'Xenia' or 'Jan' in dict_copy:
    print('The two polish students are in this list')
