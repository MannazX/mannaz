# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:55:43 2018

@author: magge
"""

tallet = np.random.randint(1, 100)
forsøg = 0  # tæl antal forsøg på at gætte tallet
gæt = 0  # hold styr på spillerens gæt

while gæt != tallet:
    gæt = eval(input('Gæt et tal: '))
    forsøg += 1
    if gæt == tallet: #hvis gættet er resultatet - printer tekst forneden
        print('Korrekt! Du brugte {:d} forsøg!'.format(forsøg))
        break #stopper while loop hvis man gætter rigtigt
    elif gæt < tallet: #hvis gættet er for lavt
        print('Det er for lavt!')
    else:
        print('Det er for højt!')