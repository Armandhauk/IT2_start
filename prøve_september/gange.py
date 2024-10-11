tallord = {'null': 0, 'en': 1, 'to': 2, 'tre': 3, 'fire': 4, 'fem': 5, 'seks': 6, 'sju': 7, 'åtte': 8, 'ni': 9, 'ti': 10, 
           'elleve': 11, 'tolv': 12, 'tretten': 13, 'fjorten': 14, 'femten': 15, 'seksten': 16, 'sytten': 17, 'atten': 18, 'nitten': 19, 
           'tjue': 20, 'tjueen': 21, 'tjueto': 22, 'tjuetre': 23, 'tjuefire': 24, 'tjuefem': 25, 'tjueseks': 26, 'tjuesju': 27, 'tjueåtte': 28, 'tjueni': 29, 
           'tretti': 30, 'trettien': 31, 'trettito': 32, 'trettitre': 33, 'trettifire': 34, 'trettifem': 35, 'trettiseks': 36, 'trettisju': 37, 'trettiåtte': 38, 'trettini': 39, 
           'førti': 40, 'førtien': 41, 'førtito': 42, 'førtitre': 43, 'førtifire': 44, 'førtifem': 45, 'førtiseks': 46, 'førtisju': 47, 'førtiåtte': 48, 'førtini': 49, 
           'femti': 50, 'femtien': 51, 'femtito': 52, 'femtitre': 53, 'femtifire': 54, 'femtifem': 55, 'femtiseks': 56, 'femtisju': 57, 'femtiåtte': 58, 'femtini': 59, 
           'seksti': 60, 'sekstien': 61, 'sekstito': 62, 'sekstitre': 63, 'sekstifire': 64, 'sekstifem': 65, 'sekstiseks': 66, 'sekstisju': 67, 'sekstiåtte': 68, 'sekstini': 69, 
           'sytti': 70, 'syttien': 71, 'syttito': 72, 'syttitre': 73, 'syttifire': 74, 'syttifem': 75, 'syttiseks': 76, 'syttisju': 77, 'syttiåtte': 78, 'syttini': 79, 
           'åtti': 80, 'åttien': 81, 'åttito': 82, 'åttitre': 83, 'åttifire': 84, 'åttifem': 85, 'åttiseks': 86, 'åttisju': 87, 'åttiåtte': 88, 'åttini': 89, 
           'nitti': 90, 'nittien': 91, 'nittito': 92, 'nittitre': 93, 'nittifire': 94, 'nittifem': 95, 'nittiseks': 96, 'nittisju': 97, 'nittiåtte': 98, 'nittini': 99, 'hundre': 100} 

a=int(input("hva skal ganges?"))
b=int(input("hva skal ganges?"))

if a and b == int:
    print(f"a * b = {a*b}")
elif a == int and b ==str:
    print(f"{a}*tallord[b]")
elif a== str and b==int:
    print(f"tallord[a]*{b}")
elif a== str and b== str:
    print(f"{tallord[a]*tallord[b]}")
