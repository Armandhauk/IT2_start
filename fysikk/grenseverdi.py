def f(x):
    return (x**2 - 9) / (x - 3)

delta_x = 0.1

print("x", "\t", "\t", "g(x)")

for i in range(4):	 	 	 	
    x = 3 + delta_x	 	 	 	 
    y = round(f(x), 4)	 	 	 
    print(x, "\t", "\t", y)
    delta_x = delta_x * 0.1	

delta_x2=0.1

print("x", "\t", "\t", "g(x)")

for b in range(4):
    x = 3 - delta_x2
    y=round(f(x), 4)
    print(x, "\t", "\t", y)
    delta_x2 = delta_x2 * 0.1