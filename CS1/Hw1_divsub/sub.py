x = int(input("?x = "))  # user input
y = int(input("?y = "))  # user input
diff = 0   # difference
remain = y # remainder
while x > remain:
	diff += 1
	remain += 1
print("x-y =", diff)