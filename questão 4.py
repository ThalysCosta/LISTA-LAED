v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
#  ́Impar- ́ımpar

for i in range(len(v)):
    repetido = False
    cont = 0
    
    for m in range(i):
        if v[m] == v[i]:
            repetido = True
            
    if v[i] % 2 != 0 and not repetido:
        cont += 1
        for j in range(i + 1, len(v)):
            if v[j] == v[i]:
                cont += 1

        if cont % 2 != 0:
            print(v[i])
