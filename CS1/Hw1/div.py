x  = int(input("?x = "))    # user input
y  = int(input("?y = "))    # user input
quotient = 0   # quotient
remainder = x  # remainder
while remainder >= y:
    quotient += 1
    remainder -= y
print("x div y =", quotient)
print("x mod y =", remainder)