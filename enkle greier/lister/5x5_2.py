rader = 5
kolonner = 5

tabell = []

for i in range(rader):
  rad = [0] * kolonner
  tabell.append(rad)

for i in range(rader):
    for j in range(kolonner):
      if (j == 0) or (j == rader-1):
        tabell[i][j] = 1


for i in range(rader):
    print(tabell[i])