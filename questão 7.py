#Contando inversões
v = [ 2, 7, 7, 2, 2, 1, 7, 7 ,9]

cont = 0
i=0

while i < len(v):
    j = i+1
    while j < len(v):
        
        if i<j and v[i]>v[j]:
            cont +=1
      
        j+=1
    i+=1
    
print(cont)
        