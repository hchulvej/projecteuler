from time import time
from sympy import isprime, lcm, factorint, primerange
from functools import reduce

def basic_pisano(n: int) -> int:
    if n < 2:
        return 1
    else:
        a, b = 1, 1
        i = 1
        while a != 0 or b != 1:
            a, b = b, (a + b) % n
            i += 1
        return i

def prime_power_pisano(p:int, k: int) -> int:
    return p**(k-1)*basic_pisano(p)

print(prime_power_pisano(7,4))      

start = time()

end = time()
print("Time: " + str(end - start) + " seconds")