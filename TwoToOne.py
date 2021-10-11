# add a1 in new list
# add letter from str2 to list if diff letter
# sort the list
# join list into string 

def longest(a1, a2):
    L = []

    for i in a1:
        if not (i in L):
            L.append(i)

    for i in a2:
        if not (i in L):
            L.append(i)

    a1 = ''.join(sorted(L))

    return a1

a1 = "inmanylanguages"
a2 = "theresapairoffunctions"

print(longest(a1, a2))
