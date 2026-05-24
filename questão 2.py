v = [2,22, 42 ,21 ,14 ,28, 3 ,19, 32, 46, 6]
#encontrar segundo o maior impar
maior = None
maior2 = None

for i in range(len(v)): 
    if (maior is None or v[i] > maior) and v[i] %2 !=0:
        maior = v[i]
        posM = i

v[0],v[posM] = v[posM],v[0]


for i in range(1,len(v)): 
    if (maior2 is None or v[i] > maior2) and v[i] %2 !=0:
        maior2 = v[i]
        posM = i

if maior2 is None:
    print("não tem numero impar")
else:
    print(maior2)