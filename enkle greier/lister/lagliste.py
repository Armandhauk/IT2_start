liste = []

tall = input("Skriv inn et tall du vil ha i listen, om du er ferdig skriv 'x': ")

while tall != "x":  
    try:
        liste.append(float(tall))  
    except ValueError:
        print("Vennligst oppgi et gyldig tall.")
    
    tall = input("Skriv inn et tall du vil ha i listen, om du er ferdig skriv 'x': ")

print("Listen din er ferdig.")
print(liste)