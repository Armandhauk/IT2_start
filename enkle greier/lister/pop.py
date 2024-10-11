tall = [2, 4, 6, 8, 10]
n = len(tall)
tekst = ""

for i in range(n):
  if i > 0:
    tekst += " | "
  tekst = tekst + str(tall[i])

print(tekst)