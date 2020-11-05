from time import time
from math import factorial

def sum_dig(n):
    return sum([f[int(d)] for d in str(n)])

start = time()

f = {n:factorial(n) for n in range(10)}

s = [sum_dig(n) for n in range(10**6)]

s += [sum_dig(n) for n in range(10**6, max(s) + 1)]

remaining = [True] * (10**6 + 1)

sixties = 0

for i in range(len(remaining)):
    r = remaining[i]
    if r:
        chain = {i}
        n = s[i]
        while n not in chain:
            chain.add(n)
            n = s[n]
        if len(chain) == 60:
            sixties += 1
        for e in chain:
            if e < 10**6:
                remaining[e] = False

print("Number of 60-length chains: " + str(sixties))


stop = time()
print("Time: " + str(stop - start))