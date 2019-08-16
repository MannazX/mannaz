import numpy as np
import matplotlib.pyplot as plt
import math as m

# =============================================================================
#                       OPLAD- OG AFLADNING
# =============================================================================
def setup(R, C, v0, tidsfirkant, repeat):

    ### Udregner konstanterne ###    
    w = 1/(R*C)
    end = 2*tidsfirkant                  
    punkter = 5000
    
    ### Nødvendige lister ###
    tid = np.linspace(0, end*repeat, punkter, dtype = float)
    firkant1 = np.full(int(len(tid)/2),v0, dtype = int)
    firkant2 = np.zeros(int(len(tid)/2), dtype = int)

    sumfirkant = np.append(firkant1,firkant2)
    sumtid = np.empty(0,dtype = int)

    opladning = []; afladning = []; done_ladning = []; temp = 0

    ### Udregner opladning og afladning ### 
    for i in range(int(len(tid)/2)):
        y = -m.exp(-w*tid[i])*v0+v0
        opladning.append(y)
        
    for i in range(int(len(tid)/2)):
        y = m.exp(-w*tid[i])*opladning[-1]  
        afladning.append(y)

    ### Gentager processen alt efter hvad repeat er ###    
    done_ladning = (opladning+afladning)
    temp = done_ladning[-1]
    done_ladning = np.array(done_ladning)
    done_ladning = np.tile(done_ladning,(repeat,1))

    ### Forskyder de nye punkter op ad y aksen ###
    for i in range(1,len(done_ladning)):
        for j in range(punkter):
            done_ladning[i,j] += i*temp 
            if done_ladning[i,j] > v0:
               done_ladning[i,j] = v0 
    done_ladning= np.concatenate(done_ladning)
    sumtid = np.repeat(tid,repeat)
    sumfirkant = np.tile(sumfirkant,repeat)
    
    return sumtid, sumfirkant, done_ladning
 
### Plotter vores tid, ladning og firkanterne ###
for i in range(1,5):
    sumtid, sumfirkant, done_ladning = setup(5000,100*10**-9,1, 0.00025*i, 3)
    plt.subplot(2,2,i)
    plt.plot(sumtid,sumfirkant)
    plt.plot(sumtid,done_ladning)
    plt.xlabel("Tid t (s)")
    plt.ylabel("Spænding S (V)")
    t=0.00025*i
    plt.title('Input ændres ved = {:} ms'.format(t*1000))
    plt.grid(alpha = 0.5)

"""
Benyttes ikke 
    ### Plotter vores tid, ladning og firkanterne ###
    plt.plot(sumtid,sumfirkant)
    plt.plot(sumtid,done_ladning)
    plt.xlabel("Tid t")
    plt.ylabel("Ladning V")
    plt.grid(alpha = 0.5)
""" 
