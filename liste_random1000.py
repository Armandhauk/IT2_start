import random as rd
liste=[]
for i in range(1000):
    tilfeldig= rd.randint(1,100)
    liste.append(tilfeldig)
    mest_repeterte_tall = max(liste, key=liste.count)

print(sorted(liste))
print("----------------------------------------------------------------")
print(mest_repeterte_tall, "ble repetert", liste.count(mest_repeterte_tall),"ganger")
print(max(liste))
print(min(liste))

