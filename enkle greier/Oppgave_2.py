import math
h=6
r=0
flaske=0
while flaske<=500 :
    r=r+0.0001
    volum_kjegle=math.pi*r**2*(h/3)
    volum_sylinder=math.pi*r**2*h
    volum_kule=((4/3)*math.pi*r**3)/2
    flaske=volum_kjegle+volum_sylinder+volum_kule
print(r)
print(volum_kjegle)
print(volum_sylinder)
print(volum_kule)
print(flaske)