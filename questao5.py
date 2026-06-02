def tem_linhas_iguais(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i] == matriz[j]:
                return True, i + 1, j + 1
    return False, None, None


M = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [5, 8, 2, 3, 9, 8, 4, 1, 7],
    [8, 3, 4, 2, 3, 1, 3, 9, 4],
    [3, 7, 2, 9, 4, 2, 1, 2, 3],
    [7, 5, 3, 1, 2, 4, 5, 8, 2],
    [4, 7, 3, 6, 5, 1, 9, 3, 2],
    [1, 5, 3, 2, 9, 8, 7, 6, 5],
    [3, 9, 4, 2, 4, 1, 8, 5, 1],  
]

resultado, linha_a, linha_b = tem_linhas_iguais(M)

if resultado:
    print(f"Sim, as linhas {linha_a} e {linha_b} são exatamente iguais.")
else:
    print("Não há linhas iguais.")