import numpy as np

"""
nedsætte = 1 # skal laves til K=K0*(1-r)^n hvor K0=1 r=5% og n er antal år
stigning = 1 # skal laves til K=K0*(1+r)^n hvor K0=1 r=5% og n er antal år
"""
np.random.seed(2)   #Random seed 


# Laver random ankomsttider 

an_arr = np.loadtxt("Miniprojekt - Ankomsttider.txt", delimiter = ",")
an_arr = np.asarray(an_arr,np.int)
an_multiarr = []

for row, line in enumerate(an_arr):
        h = np.random.randint(an_arr[row,0],an_arr[row,1],an_arr[row,2])
        an_multiarr.append(h)
random_an_tid = np.concatenate(an_multiarr)
np.random.shuffle(random_an_tid)
print("Tilfældige ankomsttider:","\n" ,random_an_tid)

# Laver random landingstider 

land_arr = np.loadtxt("Miniprojekt - Landingstider.txt", delimiter = ",")
land_arr = np.asarray(land_arr,np.int)
land_multiarr = []

for row, line in enumerate(land_arr):
        h = np.random.randint(land_arr[row,0],land_arr[row,1],land_arr[row,2])
        land_multiarr.append(h)
random_land_tid = np.concatenate(land_multiarr)
np.random.shuffle(random_land_tid)
print("Tilfældige landingstider:","\n" ,random_land_tid)

cu_an_tid = np.cumsum(random_an_tid)
#cu_land_tid = np.cumsum(random_land_tid)
forsinkelse = []
landet = []

g = cu_an_tid[0] + random_land_tid[0]
landet.append(g)
forsinkelse.append(0)

for i in range(1,len(random_an_tid)):
    if cu_an_tid[i] < landet[i-1]:
        forskel = landet[i-1] - cu_an_tid[i]
        forsinkelse.append(forskel)
        land_fly = g + forsinkelse[i]
        landet.append(land_fly)
    else:
        forsinkelse.append(0)
        landet.append(g)
        
print('Det sidste fly er landet ved t = {:} '.format(landet[-1]))
print('Den kumulerede ventetid er {:} sekunder'.format(sum(forsinkelse)))
#print('En liste over hvornår flyene lander: \n {:}'.format(landet))
#print('En liste over hvor lang ventetid de individuelle fly har: \n {:}'.format(forsinkelse))
#for i in range(len(random_land_tid)):
   # if i > 0:
      #  if cu_an_tid[i] < cu_land_tid[i-1]:
     #       wait_time = wait_time + cu_land_tid[i] - cu_an_tid[i-1]
    #    else:
    #        wait_time = wait_time
#print(wait_time)
            

"""
Til docstring:
    
Packages:
    Numpy pakken benyttes og omkaldes til "np".

Variabler: 
    an_arr = loader tekstfilen "ankomsttider" og konverterer "," til ny linje 
    i et array.
    
    an_multiarr = Et array, som indeholder antal fly-ankomsttider arrays.
    
    random_an_tid = Samler an_multiarr til et stort array, som bliver blandet 
    med random.shuffle funktionen..
"""