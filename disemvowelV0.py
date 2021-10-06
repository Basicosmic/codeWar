def disemvowel(n):
    vowel = 'aeiou'
    for i in vowel:
	n = n.replace(i,"")
    return n
n = 'hello everyone'
print(disemvowel(n))
