from time import time
from primePy import primes

num = 600851475143

start = time()
print("Largest prime factor: " + str(max(primes.factors(num))))
stop = time()
print("Time: " + str(stop-start))