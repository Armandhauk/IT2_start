x=int(input("hva skal ganges:  "))
y=int(input("med? "))

for i in range(x,y):
    print(i, end="")

b=x*[i]
for b in range(x,y):
    while b<=x*y:
        b=b+1
        print(b, end="")