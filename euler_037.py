from time import time
from primenumbers import isprime
from primesieve import nth_prime

def truncatable(p):
    n = len(str(p))
    for k in range(1, n + 1):
        if not isprime(int(str(p)[:k])):
            return False
    for k in range(n):
        if not isprime(int(str(p)[k:])):
            return False
    return True

start = time()

t = set()

n = 5
while True:
    p = nth_prime(n)
    if truncatable(p):
        t.add(p)
    n += 1
    if len(t) == 11:
        break

print("Sum of truncatable primes: " + str(sum(t)))


stop = time()
print("Time: " + str(stop-start))