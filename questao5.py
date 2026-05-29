v = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3]

k = int(input("Digite k: "))

for i in range(len(v)):
    repetido = False

    for j in range(i):
        if v[i] == v[j]:
            repetido = True
            break

    if not repetido:
        cont = 0

        for j in range(len(v)):
            if v[i] == v[j]:
                cont += 1

        if cont == k:
            print(f"O número {v[i]} aparece {k} vezes")