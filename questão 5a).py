#alguem é o dobro (lista não ordenada)
v = [9, 42 ,21, 14, 25, 3 ,19, 33, 45, 6]

for i in range(len(v)):
    for j in range (1,len(v)):
        if v[i] == 2* v[j]:
            print(f"o {v[i]} e o {v[j]}")
            