def midpointint(f,a,b,n):
    h=((b-a)/n)             #the width of each rectangle
    højdesum=0              #a er det første punkt i integralet og b er andet n er antal endelinger
    i=0                     #første indelingspunkt
    while i<n:              #Summen er fra i til n-1
        højdesum += f(a+i*h+(1/2)*h) #Hver funktion bliver lagt til højdesummen
        i+=1                        #Næste loop går til næste indelingspunkt
    return højdesum * h             #Finder arealet under funktionen
print("Det approximerede areal under grafen er {}".format(midpointint(lambda x:x,0,10,100)))

