tall_liste = []
sum = 0
antall = 0

tall = float(input("Skriv inn et tall (stopp hvis tallet er større enn 10): "))

while tall <= 10:
    tall_liste.append(tall)
    sum = sum + tall
    antall += 1
    tall = float(input("Skriv inn et til tall (stopp hvis tallet er større enn 10): "))

sum+=1
antall+=1
tall_liste.append(tall)
if antall > 0:
    største = max(tall_liste)
    minste = min(tall_liste)
    gjennomsnitt = sum / antall

    print(f"Det største tallet du skrev er {største}, og det minste er {minste}.")
    print(f"Summen av tallene er {sum}.")
    print(f"Gjennomsnittet er {gjennomsnitt}")
else:
    print("Ingen tall ble skrevet inn som var mindre enn eller lik 10.")
