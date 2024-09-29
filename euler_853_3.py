from time import time
from sympy import factorint, sieve

def Fibonacci() -> list[int]:
    fib = [0, 1]
    while len(fib) < 122:
        fib.append((fib[-1] + fib[-2]))
    return fib

# If n > 2 and L_t <= n, then pi(n) >= 2t
# L_60 = 29075380
# L_61 = 38516678
# I.e. if n >= 38516678, then pi(n) >= 122
# We limit n to be < 38516678
start = time()
sum = 0
primes = [p for p in sieve.primerange(38516678)]
print(primes[-1])

end = time()
print("Sum: " + str(sum))
print("Time: " + str(end - start) + " seconds")