from time import time
from math import sqrt


def is_integer(f):
    return f-int(f) == 0.0

def is_pentagonal(i):
    return is_integer((1 + sqrt(1 + 24*i))/6)

start = time()

pentagonals = [n for n in range(1,10000000) if is_pentagonal(n)]

difference = set()

for i in range(len(pentagonals)):
    for j in range(i, len(pentagonals)):
        if is_pentagonal(pentagonals[j]-pentagonals[i]):
            difference.add((pentagonals[i], pentagonals[j]))

sums = []

for d in difference:
    if is_pentagonal(d[0] + d[1]):
        sums.append(d)

print("Pair: " + str(sums) + ", D: " + str(sums[0][1]-sums[0][0]))

stop = time()
print("Time: " + str(stop-start))