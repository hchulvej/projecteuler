from time import time
from primesieve import primes

start = time()

prime_list = primes(100000)
factor = {p : False for p in prime_list}

wild_shot = 10 ** 20

for p in prime_list:

    if pow(10, wild_shot, 9 * p) == 1:
        factor[p] = True


print("Sum of nonfactors:", sum([p for p in prime_list if not factor[p]]))

stop = time()
print("Time: " + str(stop - start))