s = input("Input String : ")
a = list(s.encode('ascii'))

for x in a:
	if x >= 97 and x <= 122:
		print(chr(x))