############################################## Program Explanation ##############################################
#
# The program mimic the method of long division.
# It keeps divide x by d (denominator) and uses the remainder as x in the next division
# I tried to detect repaet decimal by finding two same sequence of numbers appear next to each other.
# I observed that quotient and remainder can be used to check the repeatation of decimal point. 
# Every time the program calculate a new decimal point, it stores the new decimal point and the remainder into array logq and logr.
# Then, it loops back into logq and logr array to find the same sequence as the most recent decimal.
# If it found a sequence with a length of idx that same as the last idx decimal in log and they are sitting next to each other, it is the answer
#
#################################################################################################################
#
# Example 1) 1/123 = 0.(0)                     count = 1,  quoient = 0, remainder = 10
#            1/123 = 0.(00)                    count = 2,  quoient = 0, remainder = 100
#            1/123 = 0.(008)                   count = 3,  quoient = 8, remainder = 16
#            1/123 = 0.(0081)                  count = 4,  quoient = 1, remainder = 37
#            1/123 = 0.(00813)                 count = 5,  quoient = 3, remainder = 1
#            1/123 = 0.(0)0813(0)              count = 6,  quoient = 0, remainder = 10
#            1/123 = 0.(00)813(00)             count = 7,  quoient = 0, remainder = 100
#            1/123 = 0.(008)13(008)            count = 8,  quoient = 8, remainder = 16
#            1/123 = 0.(0081)3(0081)           count = 9,  quoient = 1, remainder = 37
#            1/123 = 0.(00813)(00813)          count = 10, quoient = 3, remainder = 1
#
#################################################################################################################
#
# Example 2) 0.(0)                             count = 1, quoient = 0, remainder = 10
#            0.(00)                            count = 2, quoient = 0, remainder = 100
#            0.(001)                           count = 3, quoient = 1, remainder = 300
#            0.(0014)                          count = 4, quoient = 4, remainder = 200
#            0.(00142)                         count = 5, quoient = 2, remainder = 600
#            0.(001428)                        count = 6, quoient = 8, remainder = 400
#            0.(0014285)                       count = 7, quoient = 5, remainder = 500
#            0.(00142857)                      count = 8, quoient = 7, remainder = 100
#            0.00(1)42857(1)                   count = 9, quoient = 1, remainder = 300
#            0.00(14)2857(14)                  count = 10, quoient = 4, remainder = 200
#            0.00(142)857(142)                 count = 11, quoient = 2, remainder = 600
#            0.00(1428)57(1428)                count = 12, quoient = 8, remainder = 400
#            0.00(14285)7(14285)               count = 13, quoient = 5, remainder = 500
#            0.00(142857)(142857)              count = 14, quoient = 7, remainder = 100

#################################################################################################################

from time import sleep     
d = int(input("Input a denominator: "))
logq = [0] * 10000
logr = [0] * 10000

def comp(i,j):
    if logq[i] == logq[j] and logr[i] == logr[j]:
        return True
    else:
        return False

print(f"1/{d} is computed")
count = 0                           # Counter of the number of steps/decimals
done = False                        # Boolean used to detect end of computation
x = 1
digit = 0
if d == 1:
    print("1.0")
    done = True
while not done:                     # Keep doing until termination is detected
    x = x * 10
    quotient = x // d
    remainder = x % d
    logq[count] = quotient          # An array store every quotient
    logr[count] = remainder         # An array store every remainder
    for i in range(count, -1, -1):
        idx = 0
        while 0 <= count - idx and 0 <= i - idx and comp(count-idx, i-idx):
            idx += 1
            # k = idx                        # Part of Print Step by Step
            if count - idx == i:
                done = True                  # log[count - 2*idx +1] to log[count - idx] are the same as log[count - idx + 1] to log[count]
                digit = idx
    if remainder == 0:
        done = True
    else:
        x = remainder
    count += 1
    ################################ Print Step by Step ################################
    # print("0.", end = '')
    # for i in range(count):
    #     if i == count-k:
    #         print("(", end = '')
    #     print(f"{logq[i]}", end = '')
    # if k > 0:
    #     print(")", end = '')
    # print()
    # print(f"count = {count}, quoient = {quotient}, remainder = {remainder}")
    # sleep(0.1)
    ####################################################################################


n = count
# ------- Uncomment the line below to print the repeated decimals only once ------- #
# n = count - digit
if d != 1:
    print("0.", end = '')
    for i in range(n):
        if i == n-digit:
            print("(", end = '')
        print(f"{logq[i]}", end = '')
    if digit > 0:
        print(")", end = '')
    print()