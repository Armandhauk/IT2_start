liste = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]

antall_negative = 0
negative = []

for tall in liste:
    if tall < 0:
        antall_negative += 1
        negative.append(tall)
print(negative)