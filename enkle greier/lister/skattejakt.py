import random as rd

rader = 10
kolonner = 10
tabell = []

for i in range(rader):
    rad = [False] * kolonner
    tabell.append(rad)
for i in range(5):
    rad = rd.randint(0, rader-1)
    kolonne = rd.randint(0, kolonner-1)
    tabell[rad][kolonne] = True
for i in range(rader):
    print(tabell[i])
