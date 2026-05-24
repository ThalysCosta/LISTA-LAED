#Os dois elementos mais proximos
v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

d = abs(v[0]-v[1])

for i in range(len(v)):
    for j in range(2,len(v)): 
          
        if abs(v[i]-v[j]) < d:
            d = abs(v[i]-v[j])
            a = i
            b = j
        
print(f"o {v[a]} e o {v[b]}")