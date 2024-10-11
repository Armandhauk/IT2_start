import numpy as np

a = 0
b = 1
nøyaktighet = 0.0001
antall_iterasjoner = 0

def f(x):
    return np.log(x + 2) + x - 2

m = (a + b) / 2

while abs(b - a) >= nøyaktighet:
    antall_iterasjoner += 1
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m

    m = (a + b) / 2

print("Antall iterasjoner er", antall_iterasjoner)
print("Løsningen på likningen er x =", round(m, 5))
