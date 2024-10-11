x=int(input("hva er det du skal fakultere? "))
def fakultet(x):
    if x==1 or x==0:
        return 1
    elif x<0:
        return x*fakultet(x+1) 
    else:
        return x*fakultet(x-1)

print(fakultet(x))
