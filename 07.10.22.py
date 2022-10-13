a = int(input('Введите размерность массива (нечетное число): '))
if a % 2 != 0:
    massiv = []
    for i in range(a):
        massiv.append(int(input('Введите число: ')))
        i += 1
    print(massiv)
    ind = a // 2 + 1
    count = 0
    for j in range(ind, a):
        if massiv[j] > ind:
            count += 1
        j += 1
    print(count)
else:
    print("Ошибка: введите нечетное число")