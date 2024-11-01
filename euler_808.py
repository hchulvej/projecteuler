from time import time
from gmpy2 import next_prime
from math import sqrt

def is_not_palindrome(n: int) -> bool:
    s = str(n)
    return s != s[::-1]

def squares_of_primes(n: int, primes: list[int]) -> list[int]:
    inv_n = int(str(n)[::-1])
    if not ((int(sqrt(n))**2 == n) and (int(sqrt(inv_n))**2 == inv_n)):
        return False
    sn = int(sqrt(n))
    sinv_n = int(sqrt(inv_n))
    return sn in primes and sinv_n in primes
    
    
start = time()

LIMIT = 100000000
primes = []
p = 2
while p < LIMIT:
    primes.append(p)
    p = next_prime(p)

rps = []

for p in primes:
    if int(sqrt(int(str(p*p)[::-1]))) > LIMIT:
        print("Limit too low.")
        break
    if is_not_palindrome(p*p) and squares_of_primes(p*p,primes):
        rps.append(p*p)
    if len(rps) == 50:
        print("Found 50.")
        break
        


print(len(rps))
sum = sum(rps)
    

end = time()
print("Sum: " + str(sum))      
print("Time: " + str(end - start) + " seconds")