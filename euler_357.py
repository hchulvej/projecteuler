from time import time
from math import sqrt

def is_prime_generating(n):
    if n % 4 == 2 and primes[n + 1]:
        lim = int(sqrt(n)) + 1
        for d in range(2, lim + 1):
            if n % d == 0 and not primes[d + n // d]:
                return False
        return True
    return False

start = time()

primes = [False, False] + [True] * (10 ** 8 - 1)

for n in range(2, 10 ** 8):
    if primes[n]:
        k = 2 * n
        while k < 10 ** 8:
            primes[k] = False
            k += n



total = 1

for n in range(2, 10 ** 8):
    if is_prime_generating(n):
        total += n


print("Sum is: ", total)

stop = time()

print("Time: ", stop - start)