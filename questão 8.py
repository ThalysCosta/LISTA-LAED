#elemento repetido

u = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
v = [2 ,15 ,19 ,12 ,33, 9 ,17 ,41 ,54, 8]
 
for i in range(len(u)):
    for j in range (len(v)):
        if u[i] == v[j]:
            print(v[j])
         