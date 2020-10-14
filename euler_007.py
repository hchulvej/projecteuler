from primesieve import nth_prime
from time import time

start = time()

print("10001st prime is: " + str(nth_prime(10001)))

stop = time()
print("Time: " + str(stop-start))