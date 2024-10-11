navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"]

unike_navn = []
for n in navn:
    if n not in unike_navn:
        unike_navn.append(n)

print(unike_navn)
