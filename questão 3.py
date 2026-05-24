v = [9, 42, 21, 14, 25, 5, 3, 19,33, 45, 6]
#busca aproximada
k = int(input("digite K: "))
achei = 0

d = abs(v[0] - k)
prox = v[0]

for i in range(1,len(v)):
    if abs(v[i] - k) < d:
        d = abs(v[i] - k)
        prox = v[i]
    if prox == k:
        achei = True
        break
        
if achei:
    print("o numero esta na lista")
else:
    print(f"o mais próximo de {k} é o {prox}")

    