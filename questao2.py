#O k- ́esimo maior elemento
v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

k = int(input("Digite k: "))

for pos in range(k):
    maior = pos

    for i in range(pos + 1, len(v)):
        if v[i] > v[maior]:
            maior = i

    v[pos], v[maior] = v[maior], v[pos]

print(f"{k}º maior elemento:", v[k - 1])