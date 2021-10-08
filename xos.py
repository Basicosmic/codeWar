def xo(s):
	counter_x = 0
	counter_o = 0
	length = len(str(s))
	for i in range(length):
		if 'x' == s[i].lower():
			counter_x += 1
		elif 'o' == s[i].lower():
			counter_o += 1
	if counter_x == counter_o:
		return True
	else:
		return False 

print('The number of x and o is equal')
print(xo('xxoo'))
print(xo('xoxoo'))
print(xo('xXoo'))
print(xo('zpzp'))
print(xo('xoaaaaa'))