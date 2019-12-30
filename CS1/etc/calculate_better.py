x = int(input("x = "))
y = int(input("y = "))
print(f"x+y = {x + y}")
print(f"x-y = {x - y}")
print(f"x*y = {x * y}")
if not y==0:
	print(f"x/y = {x / y}")
	print(f"x div y = {x // y}")
	print(f"x mod y = {x % y}")
else:
	print("Division by zero")
