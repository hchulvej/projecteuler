from time import time
import sys


sys.set_int_max_str_digits(100000)

# Smallest integer with digit sum (m + 9j) is m999...99 (kj 9's, 0 <= m < 9).
#
# We can write m999...99 as (m+1)*10^j - 1, where j is the number of 9's.
#
# This groups the digits into groups by how many 9's are in the smallet digit sum:
# 0 9's: 0-8
# 1 9's: 9-17
# 2 9's: 18-26
# 3 9's: 27-35
# and so on.
#
# Each group consists of 9 numbers: r*10^j - 1, r = 1..9 (j is the number of 9's).
# The sum of these 9 numbers is 45*10^j-9.
# The sum of the first d groups is sum(j=0..d-1) 45*10^j-9 = 5*10^d - 9*d - 23.

def handheld(n: int) -> int:
    return ((n % 9) + 1)*10**(n // 9) - 1

def H(n: int) -> int:
    return sum([handheld(k) for k in range(1, n+1)])

def S(n: int) -> int:
    # How many whole groups are there below n?
    ng = n // 9
    #print("ng: " + str(ng))
    sum = 5*pow(10, ng, 1000000007) - 9*ng - 5
    # How many numbers are there in the last group?
    rem = (n - ng*9) % 9 + 1
    #print("rem: " + str(rem))
    # All of these numbers have ng 9's
    for r in range(1, rem + 1):
        sum += r*pow(10, ng, 1000000007) - 1
    return sum % 1000000007



start = time()

F = [0,1]
while len(F) < 91:
    F.append(F[-1] + F[-2])

thesum = 0

i = 2
while i <= 90:
    f = F[i]
    thesum += (S(f) % 1000000007)
    i += 1


end = time()
print("Sum: " + str(thesum % 1000000007))
print("Time: " + str(end - start) + " seconds")