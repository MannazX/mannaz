#2.8
v0 = 15
g = 9.82
n = 20
t = (2*v0/g)/n

while t <= 2*v0/g:
    yt = v0*t-(1/2)*g*t**2
    t += (2*v0/g)/n
    print(yt)

