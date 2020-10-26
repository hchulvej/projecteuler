from time import time
from math import factorial

def c(n,r):
    return facs[n] // (facs[r] * facs[n - r])

start = time()

facs = [factorial(n) for n in range(101)]

num = 0

for n in range(1,101):
    for r in range(1,101):
        if c(n, r) > 10**6:
            num += 1

print("Number of values: " + str(num))

stop = time()
print("Time: " + str(stop-start))