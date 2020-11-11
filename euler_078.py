from time import time
from math import sqrt

def gen_pen(n):
    if n%2 == 0:
        k = (-1) * n // 2
    else:
        k = (n + 1) // 2
    return k * (3 * k - 1) // 2

def add_m(m):
    for n in range(len(p), len(p) + m):
        pn = 0
        i = 0
        k = 1
        while gen_pen(k) <= n:
            pn += signum[i % 4] * p[n - gen_pen(k)]
            i += 1
            k += 1
        p.append(pn)


start = time()

signum = [1, 1, -1, -1]

p = [1]

while p[-1]%1000000 != 0:
    add_m(1)

print("Number: " + str(len(p) - 1))

stop = time()
print("Time: " + str(stop - start))