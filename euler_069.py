from time import time
from sympy import totient

def phi(n):
    return len(set(m for m in range(1,n) if gcd(n, m) == 1))

start = time()

max_quotient = 3.0
max_n = 6

for n in range(7,1000001):
    q = n / totient(n)
    if q > max_quotient:
        max_quotient = q
        max_n = n

print("Value of n and the quotient: " + str(max_n) + ", " + str(max_quotient))

stop = time()
print("Time: " + str(stop - start))