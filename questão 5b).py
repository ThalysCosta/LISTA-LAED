#alguem é o dobro (lista ordenada)
v = [1,2,3,4,5,6,7,8,9,10]
i =0
j=1
while j <= len(v)-1:
    
    if 2*v[i] == v[j]:
        print(f"o {v[i]} e o {v[j]}")
        i +=1
        j +=1
        
    elif v[j] > 2*v[i]:
        i +=1
        if i ==j:
            j+=1
        
    else:
        j+=1    
    