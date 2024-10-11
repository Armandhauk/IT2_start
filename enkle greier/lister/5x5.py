rader = 8
kolonner = 8

tabell = []

for i in range(rader):
  rad = [0] * kolonner
  tabell.append(rad)

for i in range(rader):
   for j in range(kolonner):
    if (i+j)%2==0:
         tabell[i][j] = "H"
    else :
      tabell[i][j] = "S"

for i in range(rader):
    print(tabell[i])