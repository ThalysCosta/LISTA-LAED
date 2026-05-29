#Repetidos próximos
v = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]

achei = False
k = int(input("digite k: "))
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i] == v[j] and abs(i-j) <= k:
            print(f"sim, o {v[i]}, nas posições {i} e {j}")
            achei = True

if not achei:
    print("nenhum")