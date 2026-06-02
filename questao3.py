def mediana_menor(A, B):
    n = len(A)

    if n == 1:
        return min(A[0], B[0])

    if n == 2:
        return sorted(A + B)[1]

    m = n // 2

    if n % 2 == 1:  # n ímpar
        if A[m] == B[m]:
            return A[m]

        elif A[m] < B[m]:
            return mediana_menor(A[m:], B[:m+1])

        else:
            return mediana_menor(A[:m+1], B[m:])

    else:  # n par
        if A[m] == B[m]:
            return A[m]

        elif A[m] < B[m]:
            return mediana_menor(A[m-1:], B[:m+1])

        else:
            return mediana_menor(A[:m+1], B[m-1:])


def teste():
    casos = [
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3, 4], [5, 6, 7, 8]),
        ([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]),
        ([5, 6, 7, 8], [1, 2, 3, 4])
    ]

    for A, B in casos:
        print(f"A={A}, B={B} -> mediana menor = {mediana_menor(A, B)}")


teste()