#permutação
u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]

permutacao = True

if len(u) != len(v):
    permutacao = False

for i in range(len(u)):
    cont_u = 0
    cont_v = 0

    for j in range(len(u)):
        if u[j] == u[i]:
            cont_u += 1

    for j in range(len(v)):
        if v[j] == u[i]:
            cont_v += 1

    if cont_u != cont_v:
        permutacao = False
        break

if permutacao:
    print("sim")
else:
    print("não")