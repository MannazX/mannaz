import numpy as np; import matplotlib.pyplot as plt; import math as m
    ### KODE FOR OPLADNING OG AFLADNING                                        ###

def ladning(R = 2006, C = 100*10**-9, v0 = 1):
    data = np.genfromtxt('OpOgAfladning.csv', delimiter=',', skip_header = 2081)
    """
    Simulering for opladning og afladning:
    R = Resistor, C = Kapacitator, v0 = startbetingelsen.
    
    tid            : Liste for en fuld op- eller afladning på x-aksen.
    opladning      : Liste for opladningen udregnet ved brug af den udledte formel.
    afladning      : Liste for afladningen udregnet ved brug af den udledte formel.
    w0 = 1/(R*C)   : Konstanten omega baseret på konstanterne for Resistans (R) og Kapacitans (C).
   
    Plotter simuleringen og dataene fra Analog Discovery.
    Farver:
        Kodesimulering (sim) - cyan (c)
        Firkanter (square)   - black (k)
        Data fra A.D (AD)    - magenta (m)    
    """
    w0 = 1/(R*C)
    tid = data[:1760*2,0]-data[0,0]
    opladning = []; afladning = []

    ### Udregner opladning og afladning                                        ### 
    for i in range(1760):
        y = -2 * m.exp(-w0 * tid[i]) * v0 + v0
        opladning.append(y)
    for i in range(1760):
        y =  2 * m.exp(-w0 * tid[i]) * opladning[-1] - v0
        afladning.append(y)

    ladning = opladning+afladning

    ### Plotter vores tid, ladning og firkanterne ( "," laver dem til tuples)  ###
    sim, = plt.plot(tid,ladning, label = 'simulation', 
                    color = 'c', linewidth = 1)
    
    square, = plt.plot(data[:1760*2,0],data[:1760*2,1], label = 'ladning', 
                       color = 'k', linewidth = 1)
    
    AD, = plt.plot(data[:1760*2,0],data[:1760*2,2], label = 'Analog Discovery', 
                   linestyle = ":", color = 'm', linewidth = 3)
    
    ### Navngiver akser, laver grid og navngiver de forskellige funktioner     ###
    plt.xlabel("Tid t"); plt.ylabel("Ladning V")
    plt.grid(alpha = 0.5)
    plt.legend(handles = [sim, square, AD], loc = 'upper right')

# Filtrer
def lavpas_bode(R = 2006, C = 100*10**-9):
    data_mod = np.genfromtxt('bodeplot-lavpas.csv', delimiter=',',skip_header = 1, skip_footer = 12) 
    data_arg = np.genfromtxt('bodeplot-lavpas-fase.csv', delimiter=',', skip_footer = 12)

    """
    Simulering af længden af overføringsfunktionen og fasen af overføringsfunktion for lavpasfilteret:
    R = Resistor, C = Kapacitator.
    
    mod_list        : Liste for længden af overføringsfunktionen.
    arg_list        : Liste for fasen af overføringsfunktionen.
    w = 1/(R*C*2*pi): Konstanten omega baseret på konstanterne for Resistans (R) og Kapacitans (C).
    
    knæk_mod        : Udregner knækfrekvensen for længden af overføringsfunktionen.
    knæk_arg        : Udregner knækfrekvensen for fasen af overføringsfunktionen.
    
    Plotter simuleringen og dataene fra Analog Discovery.
    Farver:
        Kodesimulering (mod) - blå (b)
        Data fra A.D (AD)    - gul (y)
        
        knækfrekvens for modulus (knæk_mod)   - rød (r)
        knækfrekvens for fasen (knæk_arg)     - rød (r)
        
    """
    mod_list = []; arg_list =[]        
    w0 = 1/(2*m.pi*R*C)
    print(w0)
    for omega in range(len(data_mod[:,0])):
        modulus  =  w0/np.sqrt(data_mod[omega,0]**2+w0**2)    
        argument = np.arctan(-data_arg[omega,0]/w0) 
        mod_list.append(20*np.log10(modulus))    #Omskrives til 20log10
        arg_list.append(argument*180/m.pi)   #Omskrives til grader fra radianer 
    knæk_mod = 20*np.log10(w0/np.sqrt(w0**2+w0**2))
    knæk_arg = 180/m.pi*np.arctan(-w0/w0)

#PLOTTER Overføringsfunktion
    plt.subplot(2,1,1)
    plt.title('Lavpasfilter')
    plt.plot(data_mod[:,0],data_mod[:,1], color = 'k')

    mod,= plt.plot(data_mod[:,0],mod_list, label = 'Overføringsfuktionen', 
                   linestyle = ":", linewidth = 4)    
    AD, = plt.plot(data_mod[:,0],data_mod[:,2], label = 'Analog Discovery', 
                   linestyle = "-", linewidth = 2, color = 'y') 
    knæk_mod, = plt.plot(w0,knæk_mod, linewidth = 0, label = 'Knækfrekvens' ,marker = 'x',
                         markersize = 8, color = 'r')
    plt.xscale('log')
    plt.ylabel("Amplituden [dB]")
    plt.legend(handles = [AD, mod, knæk_mod], loc = 'upper right')
    plt.grid(alpha = 0.5)

#PLOTTER Faseforskydning
    plt.subplot(2,1,2)
    arg, = plt.plot(data_arg[:,0],arg_list, label = 'Faseforskydning', 
                    linestyle = ':', linewidth = 4)
    AD,  = plt.plot(data_arg[:,0],data_arg[:,1], label = 'Analog Discovery',
                    linewidth = 2, color = 'y')
    knæk_arg, = plt.plot(w0,knæk_arg, linewidth = 0, label = 'Knækfrekvens' ,marker = 'x', 
                         markersize = 8, color = 'r')
     
    plt.xscale('log')
    plt.xlabel("frekvens [Hz]"); plt.ylabel("Fasen $\Theta$ i grader")
    plt.legend(handles = [AD, arg, knæk_arg], loc = 'upper right')
    plt.grid(alpha = 0.5)

def hojpas_bode(R = 2006, C = 100*10**-9):
    data_mod = np.genfromtxt('bodeplot-højpas.csv', delimiter=',', skip_footer = 40) 
    data_arg = np.genfromtxt('bodeplot-højpas-fase.csv', delimiter=',', skip_footer = 40) 
    """
    Simulering af længden af overføringsfunktionen og fasen af overføringsfunktion for højpasfilteret.
    R = Resistor, C = Kapacitator.
    
    mod_list        : Liste for længden af overføringsfunktionen.
    arg_list        : Liste for fasen af overføringsfunktionen.
    w = 1/(R*C*2*pi): Konstanten omega baseret på konstanterne for Resistans (R) og Kapacitans (C).
    
    knæk_mod        : Udregner knækfrekvensen for længden af overføringsfunktionen.
    knæk_arg        : Udregner knækfrekvensen for fasen af overføringsfunktionen.
    
    Plotter simuleringen og dataene fra Analog Discovery.
    Farver:
        Kodesimulering (mod) - blå (b)
        Data fra A.D (AD)    - gul (y)
        
        knækfrekvens for modulus (knæk_mod)   - rød (r)
        knækfrekvens for fasen (knæk_arg)     - rød (r)
    
    """
    mod_list = []; arg_list =[]        
    w0 = 1/(2*m.pi*R*C)
    print(w0)
    for omega in range(len(data_mod[:,0])):
        modulus =  (np.sqrt(data_mod[omega,0]**2/w0**2)/
                    np.sqrt(data_mod[omega,0]**2/w0**2+1))
        
        argument  = np.arctan(w0/data_arg[omega,0])
        mod_list.append(20*np.log10(modulus))    #Omskrives til 20log10
        arg_list.append(180/m.pi*argument)   #Omskrives til grader fra radianer 
    knæk_mod = 20*np.log10(np.sqrt(w0**2/w0**2)/np.sqrt(w0**2/w0**2+1))
    knæk_arg = 180/m.pi*np.arctan(w0/w0)
    
#PLOTTER Overføringsfunktion
    
    plt.subplot(2,1,1)
    plt.title('Højpasfilter')
    plt.plot(data_mod[:,0],data_mod[:,1], color = 'k')

    mod,= plt.plot(data_mod[:,0],mod_list, label = 'Overføringsfuktionen', 
                   linestyle = ":", linewidth = 4)    
    AD, = plt.plot(data_mod[:,0],data_mod[:,2], label = 'Analog Discovery', 
                   linestyle = "-", linewidth = 2, color = 'y') 
    knæk_mod, = plt.plot(w0,knæk_mod, linewidth = 0, label = 'Knækfrekvens' ,marker = 'x',
                         markersize = 8, color = 'r')
    plt.xscale('log')
    plt.ylabel("Amplituden [dB]")
    plt.legend(handles = [AD, mod, knæk_mod], loc = 'upper right')
    plt.grid(alpha = 0.5)

#PLOTTER Faseforskydning
    plt.subplot(2,1,2)
    arg, = plt.plot(data_arg[:,0],arg_list, label = 'Faseforskydning', 
                    linestyle = ':', linewidth = 4)
    AD,  = plt.plot(data_arg[:,0],data_arg[:,1], label = 'Analog Discovery',
                    linewidth = 2, color = 'y')
    knæk_arg, = plt.plot(w0,knæk_arg, linewidth = 0, label = 'Knækfrekvens' ,marker = 'x', 
                         markersize = 8, color = 'r')
    plt.xscale('log')
    plt.xlabel("frekvens [Hz]"); plt.ylabel("Fasen  $\Theta$ i grader")
    plt.legend(handles = [AD,arg,knæk_arg], loc = 'upper right')
    plt.grid(alpha = 0.5)
    

