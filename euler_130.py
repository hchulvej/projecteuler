from time import time
from primesieve import primes

def A(n):
    k = 1
    rem = 1
    while rem != 0:
        rem = (10 * rem + 1) % n
        k += 1
    return k



start = time()

prime_list = set(primes(707, 10 ** 6))

composites = [91, 259, 451, 481, 703]

n = 707
while True:
    if len(composites) == 25:
        break

    if n % 5 > 0:
        if not n in prime_list:
            if (n - 1) % A(n) == 0:
                composites.append(n)

    n += 2

print("Sum of composites:", sum(composites))

stop = time()
print("Time: " + str(stop - start))