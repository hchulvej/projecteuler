from time import time
import primesieve

pgen = primesieve.Iterator()
psum = 0

start = time()
p = pgen.next_prime()
while p < 2000000:
    psum += p
    p = pgen.next_prime()

print("The sum of primes: " + str(psum))

stop = time()
print("Time: " + str(stop-start))