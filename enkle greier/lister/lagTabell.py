rader = 4
kolonner = 4

tabell = []

for i in range(rader):
  rad = [0] * kolonner
  tabell.append(rad)

tabell[0][0] = 1
tabell[1][1] = 1
tabell[2][2] = 1
tabell[3][3] = 1

for i in range(rader):
    print(tabell[i])