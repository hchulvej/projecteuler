from time import time
from gmpy2 import next_prime
from math import sqrt

def is_not_palindrome(n: int) -> bool:
    s = str(n)
    return s != s[::-1]


start = time()

LIMIT = 10000000
primes = []
p = 2
while p < LIMIT:
    primes.append(p)
    p = next_prime(p)

rps = []

for p in primes:
    ipp = int(str(p*p)[::-1])
    if p*p > LIMIT or ipp > LIMIT:
        print("Limit too low.")
        break
    if is_not_palindrome(p*p) and is_not_palindrome(ipp) and int(sqrt(ipp)) in primes:
        rps.append(p*p)
    if len(rps) > 50:
        print("Found 50.")
        print(rps)
        break
    

end = time()
       
print("Time: " + str(end - start) + " seconds")