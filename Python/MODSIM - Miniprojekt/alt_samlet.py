import numpy as np
from math import ceil
from matplotlib import pyplot as plt

np.random.seed(2)

file_arrival = np.loadtxt("ankomsttider.txt", delimiter = ",", dtype = int)
file_landing = np.loadtxt("landingstider.txt", delimiter = ",", dtype = int)


def funktion_af_nye_fly(year, growth):
    New_planes = ceil(sum(file_arrival[:,2])*(1+growth)**year-
                      sum(file_landing[:,2]))
    
    place_arrival = np.zeros(len(file_arrival), dtype = int)
    place_landing = np.zeros(len(file_landing), dtype = int) 
    
    cumulated_planes_arrival = np.cumsum(file_arrival[:,2])    
    cumulated_planes_landing = np.cumsum(file_landing[:,2])    
    random_number = np.random.randint(0,cumulated_planes_arrival[-1],New_planes) 

    for i in range(New_planes):
        for j in range(len(cumulated_planes_arrival)):
            if random_number[i] < cumulated_planes_arrival[j]:
                place_arrival[j] += 1
                break
        for j in range(len(cumulated_planes_landing)):
            if random_number[i] < cumulated_planes_landing[j]:
                place_landing[j] += 1
                break
        
    
    file_arrival[:,2] += place_arrival
    file_landing[:,2] += place_landing
    
    return file_arrival, file_landing

    
def funktion_af_rndm_flytider(year, growth):

    storing_arrival_times = []
    storing_landing_times = []
    
    for row, col in enumerate(file_arrival):
        rndm_arrivaltime = np.random.randint(file_arrival[row,0]*(1-growth)**year,
                                             file_arrival[row,1]*(1-growth)**year,
                                             file_arrival[row,2])
        storing_arrival_times.append(rndm_arrivaltime)
        
    for row, col in enumerate(file_landing):
        rndm_landingtime = np.random.randint(file_landing[row,0],
                                             file_landing[row,1],
                                             file_landing[row,2])
        storing_landing_times.append(rndm_landingtime)
            
    arrival_times = np.concatenate(storing_arrival_times)
    np.random.shuffle(arrival_times)
        
    landing_times = np.concatenate(storing_landing_times)
    np.random.shuffle(landing_times)

    return arrival_times, landing_times


def funktion_for_køsystem(k, year, growth):
    """
    Denne funktion står for at lave køsystemet, samt ventetiden ved hver 
    simulation. Funktionen afhænger af sine tre variabler, henholdsvist antallet af 
    landingsbaner (k), antallet af år efter start og sin stigningsprocenten for fly.
    
    
    
    """
    arrival_times, landing_times = funktion_af_rndm_flytider(year,growth/100)    
    lanes = np.zeros(k, dtype = int)
    waittime = []
    for i in range(len(arrival_times)):
        for j in range(k):
            lanes[j] -= arrival_times[i]
            if lanes[j] < 0:
                lanes[j] = 0
        waittime.append(min(lanes))
        lanes[np.argmin(lanes)] += landing_times[i]
        last_waittime = waittime[-1]
        
        
    return sum(waittime), max(waittime), last_waittime

def funktion_for_plots(N, list_waittime, avg_waittime, list_max_waittime, list_last_waittime):


                # Plotter af summeret ventetid pr simulation 
    list_N = np.arange(0,N,1)
    plt.subplot(3,1,1)
    plt.plot(list_N,list_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_waittime)-avg_waittime/N, max(list_waittime)+avg_waittime/N)
    plt.grid(alpha = 0.2)
    plt.title("Plot af summeret ventetid pr simulation")
    plt.ylabel("Ventetider (s)")

                # Plotter af max ventetid pr simulation 
    plt.subplot(3,1,2)                
    plt.plot(list_N,list_max_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_max_waittime), max(list_max_waittime))
    plt.grid(alpha = 0.2)
    plt.title("Plot af max ventetid pr simulation")
    plt.ylabel("Max ventetider (s)")
 
                # Plotter af max ventetid pr simulation
    plt.subplot(3,1,3)                
    plt.plot(list_N,list_last_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_last_waittime), max(list_last_waittime))
    plt.grid(alpha = 0.2)
    plt.title("Plot af sidste flys ventetid pr simulation")
    plt.xlabel("Simulationer"); plt.ylabel("Sidste flys ventetider (s)")

def simuleringsantal(N, year, growth, k, plots):
    """
    Denne funktion kører hele programmet, hvortil man kan vælge 
    N-simulationer, antallet af år efter start, stigningsprocenten for fly og
    ens valgte antal (k) for landingsbaner.
    
    Funktionen udprinter den gennemsnitlige ventetid efter N simulationer for 
    de tre andre valgte variabler. 
    
    For at opgive de valgte variabler, tager den input fra ens tastatur, som 
    skal skrives i konsolen.
    """
    N += 1
    funktion_af_nye_fly(year, growth/100)  
    Planes = sum(file_arrival[:,2]) 
    
    list_waittime = [] 
    list_max_waittime = []
    list_last_waittime = []
    for i in range(N):
        funktion_af_rndm_flytider(year,growth/100)
        waittime, max_wait, last_waittime = funktion_for_køsystem(k, year, growth/100)
        list_waittime.append(waittime)
        list_max_waittime.append(max_wait)
        list_last_waittime.append(last_waittime)
    avg_waittime = sum(list_waittime)/len(list_waittime)

    if plots == str("ja"):
        funktion_for_plots(N, list_waittime, avg_waittime, list_max_waittime, list_last_waittime)
    else:
            print("Valgte ingen plots")

    return (print("Antallet af fly:", Planes),
            print("Summeret ventetid for alle fly:",avg_waittime,"sek"), 
            print("Gennemsnitlig ventetid for flyene:", avg_waittime/Planes, "sek"),
            print("Maximale ventetid:", max(list_max_waittime),"sek"))

simuleringsantal(N = int(input("Vælg antallet af simulationer: ")), 
                 year = int(input("Vælg antal år efter start (startår = 0): ")), 
                 growth = float(input("Vælg flystigningsprocenten: ")), 
                 k = int(input("Vælg antallet af landingsbaner: ")),
                 plots = input("Skal der plots med? (ja/nej): "))


print(ankomsttiderfil,"\n","\n",landingstiderfil)
print(sum(ankomsttiderfil[:,2]),"\n",sum(landingstiderfil[:,2]))
print(random_an_tid,"\n",random_land_tid)

"""
Mangler: 
   
Skal ikke bruges (tror jeg ):

"""