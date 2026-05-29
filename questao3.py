#O mais pr ́oximo da m ́edia
v = [5, 3, 1 ,10, 2, 13, 9, 12, 4, 7]

soma = 0
for i in range(len(v)):
    soma += v[i]

media = soma/len(v)
achei = False
prox = None
for i in range(len(v)):
    if v[i] == media:
        achei = True
        break
    elif prox is None or abs(media-v[i]) < abs(media-prox):
        prox = v[i]

if achei:
    print("a media esta na lista")
else:
    print(f"o mais proximo da media é o {prox}")



