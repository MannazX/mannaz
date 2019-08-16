import numpy as np
from math import ceil
from matplotlib import pyplot as plt

# =============================================================================
#                               Loader filerne
# =============================================================================

#np.random.seed(213129)

file_arrival = np.loadtxt("ankomsttider.txt", delimiter = ",", dtype = int)
file_landing = np.loadtxt("landingstider.txt", delimiter = ",", dtype = int)


def funktion_af_nye_fly(year, growth):
    """
    Returnerer de originale variablerne for ankomsttider.txt og landingstider.txt,
    samt de nye fly i de intervaller, som passer med sandsynlighedsfordelingen.
    
    New_planes : Antallet af nye fly.
    place_arrival : liste som pladsholder fyldt med nuller i længden af antallet linjer i ankomsttider.txt.
    place_landing : liste som pladsholder fyldt med nuller i længden af antallet linjer i landingstider.txt.
    cumulated_planes_arrival : Liste med kummulerede summer af fly fra ankomsttider.txt.
    cumulated_planes_landing : Liste med kummulerede summer af fly fra landingstider.txt.
    random_number : Liste med tilfældige tal som er New_planes lang.
    """
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
    """
    Returnerer de tilfældige ankomst- og landingstider for alle flyene
    
    storing_arrival_times : Liste som gemmer alle de nye ankomsttider som lister.
    storing_landing_times : Liste som gemmer alle de nye landingstider som lister.
    rndm_arrivaltime : Laver tilfældige ankomsttider for flyene alt efter deres intervaller.
    rndm_landingtime : Laver tilfældige landingstider for flyene alt efter deres intervaller.
    arrival_times : Liste over alle de tilfældige ankomsttider, som er blevet shufflet forinden.
    landing_times : Liste over alle de tilfældige landingstider, som er blevet shufflet forinden.
    """

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


def funktion_for_køsystem(k, year, growth, arrival_times, landing_times):
    """
    Returnerer liste af ventetider, summen af alle ventetider, 
    den maximale ventetid og ventetiden for det sidste fly.
    
    k : Antal landingsbaner.
    lanes : Laver antallet (k) af valgte landingsbaner. 
    list_waittime : Laver tom liste til ventetiderne for hvert fly.
    """   
    
    lanes = np.zeros(k, dtype = int)
    list_waittime = []
    for i in range(len(arrival_times)):
        for j in range(k):
            lanes[j] -= arrival_times[i]
            if lanes[j] < 0:
                lanes[j] = 0
        list_waittime.append(min(lanes))
        lanes[np.argmin(lanes)] += landing_times[i]
    last_waittime = list_waittime[-1]
            
    return list_waittime, sum(list_waittime), max(list_waittime), last_waittime

def funktion_for_plots(N, list_sum_waittime, avg_waittime, 
                       list_max_waittime, list_last_waittime, 
                       list_waittime, Planes):
                # Plotter summeret ventetid pr simulation 
    list_N = np.arange(0,N,1)
    plt.subplot(2,2,1)
    plt.plot(list_N,list_sum_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_sum_waittime)-avg_waittime/N, max(list_sum_waittime)+avg_waittime/N)
    plt.grid(alpha = 0.2)
    plt.title("Plot af summeret ventetid pr simulation")
    plt.xlabel("Simulationer"); plt.ylabel("Ventetider (s)")

                # Plotter max ventetid pr simulation 
    plt.subplot(2,2,2)                
    plt.plot(list_N,list_max_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_max_waittime), max(list_max_waittime))
    plt.grid(alpha = 0.2)
    plt.title("Plot af max ventetid pr simulation")
    plt.xlabel("Simulationer"); plt.ylabel("Max ventetider (s)")
 
                # Plotter ventetiden for sidste fly pr simulation
    plt.subplot(2,2,3)                
    plt.plot(list_N,list_last_waittime, marker="o", alpha = 0.5)  
    plt.ylim(min(list_last_waittime), max(list_last_waittime))
    plt.grid(alpha = 0.2)
    plt.title("Plot af sidste flys ventetid pr simulation")
    plt.xlabel("Simulationer"); plt.ylabel("Sidste flys ventetider (s)")

                # Plotter ventetiderne for hvert fly.
    planes_list = np.arange(0,Planes,1)
    plt.subplot(2,2,4)                
    plt.plot(planes_list,list_waittime, marker="d", linestyle = '', alpha = 0.8)  
    plt.xlim(0, max(planes_list))
    plt.ylim(min(list_waittime), max(list_waittime))
    plt.grid(alpha = 0.2)
    plt.title("Plot af flyenes individuelle ventetider")
    plt.xlabel("Fly"); plt.ylabel("ventetider (s)")
    
def simuleringsantal(N, year, growth, k, plots):
    """
    Denne funktion kører hele programmet, hvortil man kan vælge 
    N-simulationer, antallet af år efter start, stigningsprocenten for fly og
    ens valgte antal (k) for landingsbaner.
    
    Returnerer den antallet af fly, samt den summeret-, gennemsnitlige- 
    og maximale ventetid.
    
    list_sum_waittime = liste som indeholder ventetiderne for hver simulation. 
    list_max_waittime = liste som indeholder de maximale ventetider for hver simulation.
    list_last_waittime = liste som indeholder det sidste flys ventetid for hver simulation.
    avg_waittime = den gennemsnitlige ventetid for hvert fly.
    """
    N += 1
    funktion_af_nye_fly(year, growth/100)  
    Planes = sum(file_arrival[:,2]) 
    
    list_sum_waittime = [] 
    list_max_waittime = []
    list_last_waittime = []
    for i in range(N):
        arrival_times, landing_times = funktion_af_rndm_flytider(year,growth/100)
        list_waittime, waittime, max_wait, last_waittime = funktion_for_køsystem(k, year, growth/100,
                                                                                 arrival_times, landing_times)
        list_sum_waittime.append(waittime)
        list_max_waittime.append(max_wait)
        list_last_waittime.append(last_waittime)
    avg_waittime = sum(list_sum_waittime)/len(list_sum_waittime)

    if plots == str("ja"):
        funktion_for_plots(N, list_sum_waittime, avg_waittime, list_max_waittime, 
                           list_last_waittime, list_waittime, Planes)
    else:
            print("\n","Du valgte ingen plots")
    if avg_waittime > 86400:
        print("\n","Flyene kommer ikke længere kun over en dag.","\n")
    if max(list_max_waittime) >= 1200: # 15 minutter i sekunder
        print("\n","Der anbefales flere landingsbaner.")
        if max(list_max_waittime) >= 2400: # 30 minutter i sekunder
            print("Den maksimale ventetid for et fly er nu over 30 minutter")
        else:
            print("Den maksimale ventetid for et fly er nu over 15 minutter","\n")

    return (print('Antallet af fly er {:}:'.format(Planes)),
            print('Summeret ventetid for alle fly er {:.2f} sek'.format(avg_waittime)), 
            print('Gennemsnitlig ventetid for flyene er {:.2f} sek'.format(avg_waittime/Planes)),
            print('Maximale ventetid er {:.2f} sek:'.format(max(list_max_waittime))))

simuleringsantal(N = int(input("Vælg antallet af simulationer: ")), 
                 year = int(input("Vælg antal år efter start (startår = 0): ")), 
                 growth = float(input("Vælg flystigningsprocenten: ")), 
                 k = int(input("Vælg antallet af landingsbaner: ")),
                 plots = input("Skal der grafer med? (ja/nej): "))