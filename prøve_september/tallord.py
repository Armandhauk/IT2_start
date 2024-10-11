
liten = ["null", "en", "to", "tre", "fire", "fem", "seks", "sju", "åtte", "ni", "ti"] 
middels = ["elleve", "tolv", "tretten", "fjorten", "femten", "seksten", "sytten", "atten", "nitten"] 
stor = ["tjue", "tretti", "førti", "femti", "seksti", "sytti", "åtti", "nitti", "hundre"]

liste = []

for i in range(101):
    if i <= 10:
       
        liste.append(liten[i])
    elif i <= 19:
      
        liste.append(middels[i - 11])  
    elif i <= 99:
       
        ti_tall = stor[(i // 10) - 2] 
        en_tall = liten[i % 10] if i % 10 != 0 else ""
        if en_tall:
            liste.append(ti_tall + "-" + en_tall) 
        else:
            liste.append(ti_tall)  
    else:
        liste.append(stor[-1])  

for ord in liste:
    print(ord)


        
