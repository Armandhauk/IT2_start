import random

antall_kast = 0
terningkast = random.randint(1, 6)
while terningkast != 6:
    antall_kast += 1
    print(f"Terningkast {terningkast}")

    terningkast = random.randint(1, 6)

antall_kast += 1
print(f"Terningkast {terningkast}")
print(f"Det tok {antall_kast} kast for å få 6")