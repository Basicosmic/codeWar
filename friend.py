def fr(x):
    length = len(x)
    nx =[]
    for i in range(length):
        
        if len(x[i]) == 4:
            nx.append(x[i])
            
            
    return nx
        
friend1=["Ryan", "Kieran", "Mark",]

friend2=["Ryan", "Jimmy", "123", "4", "Cool Man"]
friend3=["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]

print(fr(friend1))
print(fr(friend2))
print(fr(friend3))

