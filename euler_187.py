from time import time
from primesieve import primes


start = time()

p_plist = primes(10 ** 8)

semiprimes = 0

for i in range(len(p_plist) - 1):
    j = i
    while p_plist[i] * p_plist[j] < 10 ** 8:
        semiprimes += 1
        j += 1

print("number og semiprimes:", semiprimes)

stop = time()
print("Time: " + str(stop - start))