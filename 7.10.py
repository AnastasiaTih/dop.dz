massiv = [2, 4, 5, 8, 7, 9]
print(massiv)
massiv_new = []
for i in range(len(massiv)):
    if massiv[i] % 2 == 0:
        massiv_new.append(massiv[i]+5)
    else:
        massiv_new.append(0)
    i += 1
print(massiv_new)