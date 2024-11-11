from time import time
from math import log, exp, comb
from gmpy2 import next_prime

def prime_gen():
    n = 5
    while True:
        yield n
        n = next_prime(n)

def log_power(a,b):
    return log(a) * b + a * log(b)

def binary_search(p, upper_limit):
    low = p + 1
    high = int(upper_limit) + 1
    mid = low
    print(low, high, mid)
    
    while low <= high:
        mid = (low + high) // 2
        if log_power(p, mid) > upper_limit:
            high = mid - 1
        elif log_power(p, mid) < upper_limit:
            low = mid + 1
        else:
            return mid
    
    return -1


start = time()

primes = [2, 3]
pg = prime_gen()

limit = 800
n = limit * log(limit)

prime_limit = log_power(primes[-1], primes[-2])

while prime_limit < n:
    primes.append(next(pg))
    prime_limit = log_power(primes[-1], primes[-2])


print(binary_search(2, 8000000))

end = time()
print("Time: " + str(end - start) + " seconds")