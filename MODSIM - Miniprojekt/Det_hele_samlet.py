# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:33:08 2018

@author: magge
"""

                            # Det hele samlet
import numpy as np
np.random.seed(2)
stigning = 0.05
år = 10
antal_sim = 25
liste = []



#def stiging_i_år(stigning,aar):
 #   al = [] #list med værdier steget
 #   a  = 0 #stigning
 #      a = (1+stigning)**(aar)
 #      al.append(a) 
       #a = 0
  #     aar+=1 #inkrementere år med 1
  #  return print(al)
#stiging_i_år(0.05,1)


        
        
ankomsttider_og_fly = np.loadtxt("ankomsttider.txt", delimiter = ",")
ankomsttider_og_fly = np.asarray(ankomsttider_og_fly,np.int) # Liste med antallet af fly i hvert interval

landingstider_og_fly = np.loadtxt("landingstider.txt", delimiter = ",")
landingstider_og_fly = np.asarray(landingstider_og_fly,np.int) # Liste med antallet af fly i hvert interval

antal_nye_fly = int(sum(landingstider_og_fly[:,2])*((1+stigning)**år)-sum(landingstider_og_fly[:,2]))

flyplads_i_ankomst = np.zeros(len(ankomsttider_og_fly), dtype = int)
flyplads_i_landing = np.zeros(len(landingstider_og_fly), dtype = int) # dtype = datatype som er heltal (int)
    
cum_fly_ankomsttider = np.cumsum(ankomsttider_og_fly[:,2])    # Kummuleret sum af fly
cum_fly_landingstider = np.cumsum(landingstider_og_fly[:,2])    # Kummuleret sum af fly
randomtal = np.random.randint(0,cum_fly_ankomsttider[-1],antal_nye_fly) # laver n nye tal (check n varablen) 

for i in range(antal_nye_fly):
    for j in range(len(cum_fly_ankomsttider)):
        if randomtal[i] < cum_fly_ankomsttider[j]:
            flyplads_i_ankomst[j] = flyplads_i_ankomst[j] + 1
            break
    
for i in range(antal_nye_fly):
    for j in range(len(cum_fly_landingstider)):
        if randomtal[i] < cum_fly_landingstider[j]:
            flyplads_i_landing[j] = flyplads_i_landing[j] + 1
            break
    
ankomsttider_og_fly[:,2] = ankomsttider_og_fly[:,2] + flyplads_i_ankomst 
landingstider_og_fly[:,2] = landingstider_og_fly[:,2] + flyplads_i_landing


an_multiarr = []
land_multiarr = []

for row, line in enumerate(ankomsttider_og_fly):
    h = np.random.randint(ankomsttider_og_fly[row,0]*(1-stigning)**år,
                          ankomsttider_og_fly[row,1]*(1-stigning)**år,
                          ankomsttider_og_fly[row,2])
    an_multiarr.append(h)
    
for row, line in enumerate(landingstider_og_fly):
    h = np.random.randint(landingstider_og_fly[row,0]*(1-stigning)**år,
                          landingstider_og_fly[row,1]*(1-stigning)**år,
                          landingstider_og_fly[row,2])
    land_multiarr.append(h)
    
random_an_tid = np.concatenate(an_multiarr)
np.random.shuffle(random_an_tid)
    
random_land_tid = np.concatenate(land_multiarr)
np.random.shuffle(random_land_tid)

c_anktid = np.cumsum(random_an_tid)
delay = []
fordig = []

g = c_anktid[0] + random_land_tid[0]
fordig.append(g)
delay.append(0)
for i in range(1,len(random_an_tid)):
    g = c_anktid[i] + random_land_tid[i]
    if c_anktid[i] < fordig[i-1]: 
        forskel = fordig[i-1]-c_anktid[i]
        delay.append(forskel)
        noet = g+delay[i]
        fordig.append(noet)
    else:
        delay.append(0)
        fordig.append(g)

print(antal_nye_fly)
print('Det sidste fly er landet ved t = {:} '.format(fordig[-1]))
#print('Den kumulerede ventetid er {:} sekunder'.format(sum(delay)))
#print('En liste over hvornår flyene lander: \n {:}'.format(fordig))
print('En liste over hvor lang ventetid de individuelle fly har: \n {:}'.format(delay))
