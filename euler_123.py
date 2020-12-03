from time import time
from primesieve import nth_prime

def primgen():
    n = 1
    while True:
        yield (n, nth_prime(n))
        n += 1

def remainder(gen):
    n = gen[0]
    p = gen[1]
    a = pow(p - 1, n, p ** 2)
    b = pow(p + 1, n, p ** 2)
    return (a + b) % (p ** 2)

start = time()

pg = primgen()
n = 1
r = remainder(next(pg))

while r < 10 ** 10:
    r = remainder(next(pg))
    n += 1

print("The smallest n is: ", n)

stop = time()
print("Time: " + str(stop - start))