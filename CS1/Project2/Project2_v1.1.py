############################################## Program Explanation ##############################################
#
# The program mimic the method of long division.
# It keeps divide x by d (denominator) and uses the remainder as x in the next division
# I tried to detect repaet decimal by finding two same sequence of numbers appear next to each other.
# I observed that quotient and remainder can be used to check the repeatation of decimal point. 
# Every time the program calculate a new decimal point, it stores the new decimal point and the remainder into array logq and logr.
# Then, it searches through logq and logr array to find the first i that make logq[i] and logr[i] equal to logq[count] and logr[count].
# If it find logq[i] and logr[i] equal to logq[count] and logr[count], then the decimal starts to repeat from that point.
#
#################################################################################################################
#
# Example 1) 1/123 = 0.0                       count = 1,  quoient = 0, remainder = 10   <-- same quotient and remainder
#            1/123 = 0.00                      count = 2,  quoient = 0, remainder = 100
#            1/123 = 0.008                     count = 3,  quoient = 8, remainder = 16
#            1/123 = 0.0081                    count = 4,  quoient = 1, remainder = 37
#            1/123 = 0.00813                   count = 5,  quoient = 3, remainder = 1
#            1/123 = 0.(0)0813(0)              count = 6,  quoient = 0, remainder = 10   <-- same quotient and remainder
#
#################################################################################################################
#
# Example 2) 0.0                               count = 1,  quoient = 0, remainder = 10
#            0.00                              count = 2,  quoient = 0, remainder = 100
#            0.001                             count = 3,  quoient = 1, remainder = 300  <-- same quotient and remainder
#            0.0014                            count = 4,  quoient = 4, remainder = 200
#            0.00142                           count = 5,  quoient = 2, remainder = 600
#            0.001428                          count = 6,  quoient = 8, remainder = 400
#            0.0014285                         count = 7,  quoient = 5, remainder = 500
#            0.00142857                        count = 8,  quoient = 7, remainder = 100
#            0.00(1)42857(1)                   count = 9,  quoient = 1, remainder = 300  <-- same quotient and remainder
#
#################################################################################################################

from time import sleep     
d = int(input("Input a denominator: "))
logq = [0] * 10000
logr = [0] * 10000

def comp(i,j):
    if i < 0 or j < 0:
        return False
    return logq[i] == logq[j] and logr[i] == logr[j]

print(f"1/{d} is computed")
count = 0                           # Counter of the number of steps/decimals
done = False                        # Boolean used to detect end of computation
x = 1
digit = 0
l = 0
if d == 1:
    print("1.0")
    done = True
while not done:                     # Keep doing until termination is detected
    x = x * 10
    quotient = x // d
    remainder = x % d
    logq[count] = quotient          # An array store every quotient
    logr[count] = remainder         # An array store every remainder

    for i in range(count):
        if comp(i, count):         # compare both logq and logr
            done = True
            l = count - i

    if remainder == 0:
        l = 0
        done = True
    else:
        x = remainder
    count += 1

    ######################## Print Step by Step (For Debugging) #########################
    # print("0.", end = '')
    # for i in range(count):
    #     if i == count-1 or i == count - l - 1:
    #         print("(", end = '')
    #     print(f"{logq[i]}", end = '')
    #     if i == count -1 or i == count - l - 1:
    #         print(")", end = '')
    # print()
    # print(f"count = {count}, quoient = {quotient}, remainder = {remainder}")
    # sleep(0.1)
    #####################################################################################

n = count
if d != 1:
    print("0.", end = '')
    for i in range(n - 1):
        if i == n - l - 1:
            print("(", end = '')
        print(logq[i], end = '')
    if l > 0:
        print(")", end = '')
    if l == 0:                       # Decimal is not repeating
        print(logq[n - 1])
    print()