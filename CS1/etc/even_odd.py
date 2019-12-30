x = int(input("x = "))
if x % 2:
	print(f"x ({x}) is odd")
else:
	print(f"x ({x}) is even")

if x>0:
	print(f"x ({x}) is positive")
elif x == 0:
	print(f"x is null (zero)")
else:
	print(f"x ({x}) is negative")