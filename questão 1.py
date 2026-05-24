v = [2,22, 42 ,21 ,14 ,28, 3 ,19, 32, 46, 6]
#encontrar o maior impar
maior = None
for i in range(len(v)): 
    if (maior is None or v[i] > maior) and v[i] %2 !=0:
        maior = v[i]

if maior is None:
    print("não tem numero impar")
else:
    print(maior)