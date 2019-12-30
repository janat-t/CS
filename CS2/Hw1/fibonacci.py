def fibo_iter(n):
	a = 0
	b = 1
	c = 1
	for i in range(n):
		a = b
		b = c
		c = a + b
	return a  # Change here


def fibo_rec(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibo_rec(n - 1) + fibo_rec(n - 2)


# Main program to check your functions
n = int(input("Choose a value for n: "))
print("According to your functions:")
print(f"F({n}) = {fibo_iter(n)} = {fibo_rec(n)}")
