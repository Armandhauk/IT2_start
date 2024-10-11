import random

n = int(input("Hvor mange ganger vil du trille terningen? "))

sum_terningkast = 0
sum_terningkast2=0
terningkast_liste = []
terningkast_liste2 = []

for i in range(n):
    kast = random.randint(1, 6)  
    terningkast_liste.append(kast)
    sum_terningkast += kast
for x in range(n):
    kast2 = random.randint(1, 6)  
    terningkast_liste2.append(kast2)
    sum_terningkast2 += kast2

gjennomsnitt = (sum_terningkast + sum_terningkast2) / n

print(f"Summen av terningkastene er {sum_terningkast+sum_terningkast2}.")
print(f"Gjennomsnittet av terningkastene er {gjennomsnitt:.2f}.")
print(f"Terningkastene var {terningkast_liste} og {terningkast_liste2}")
