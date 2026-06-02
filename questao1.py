def Troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def Particao(lista, inicio, fim):
    pivo = lista[inicio]
    esq = inicio + 1
    dir = fim

    while esq <= dir:
        if lista[esq] <= pivo:
            esq += 1
        elif lista[dir] >= pivo:
            dir -= 1
        else:
            Troca(lista, esq, dir)
            esq += 1
            dir -= 1

    Troca(lista, inicio, dir)
    return dir


def Bolha(lista, inicio, fim):
    houveTroca = False
    for idx in range(inicio, fim):
        if lista[idx] > lista[idx+1]:
            Troca(lista, idx, idx+1)
            houveTroca = True
        else:
            continue

    if houveTroca == True:
        Bolha(lista, inicio, fim)


def ParticaoBolha(lista):
    k = Particao(lista, 0, len(lista)-1)

    # Para o lado esquerdo:
    Bolha(lista, 0, k-1)

    # Para o lado direito:
    Bolha(lista, k+1, len(lista)-1)

    return lista


lista = [5, 3, 8, 1, 9, 2, 7, 4, 6]

print(f"Antes: {lista}")
ParticaoBolha(lista)
print(f"Depois: {lista}")

# a) No melhor caso, o pivô consegue dividir a lista exatamente ao meio.
# A execução da bolha possui custo (n/2)^2. Somando, teremos: (n/2)^2 + (n/2)^2 = n^2/2
# A partição ocorre em O(n). Então: T(n) = O(n) + O(n^2/2) = O(n^2).

# b) No pior caso, o pivô fica em uma das extremidades, criando uma "sublista" de tamanho n-1.
# Neste caso, a função bolha terá custo O((n-1)^2) ~ O(n^2).

# Em ambos os casos, o tempo de execução será ~O(n^2).