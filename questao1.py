# O terceiro maior elemento
v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

maior = 0
for i in range(1, len(v)):
    if v[i] > v[maior]:
        maior = i

v[0], v[maior] = v[maior], v[0]

maior = 1
for i in range(2, len(v)):
    if v[i] > v[maior]:
        maior = i

v[1], v[maior] = v[maior], v[1]

maior = 2
for i in range(3, len(v)):
    if v[i] > v[maior]:
        maior = i

print("Terceiro maior:", v[maior])