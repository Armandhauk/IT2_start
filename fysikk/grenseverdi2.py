def g(x):
    return (x**2 - 9) / (x - 3)

delta_x = 0.1
print("x", "\t", "\t", "g(x)")
for i in range(4): 
     x = 3 + delta_x 
     y = round(g(x), 4)