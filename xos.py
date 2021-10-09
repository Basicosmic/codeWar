#improved xo
def xo(s):
	s=s.lower()
	return s.count('x')==s.count('o')
print(xo('xxxoo'))
print(xo('xxoo'))
