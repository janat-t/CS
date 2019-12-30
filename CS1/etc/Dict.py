d = {}
num = [int(x) for x in input("input : ").split()]
for x in num:
	if x not in d:
		d[x] = 0
	d[x] += 1

# print(d)

for x in d:
	print(x, d[x])