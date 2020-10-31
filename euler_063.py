from time import time
from itertools import count

start = time()

solutions = set()

for n in count(1):
    added = 0
    for k in count(1):
        p = k**n
        if len(str(p)) < n:
            k += 1
        if len(str(p)) == n:
            solutions.add(p)
            added += 1
        if len(str(p)) > n:
            break
    if added == 0:
        break

print("Number of solutions: " + str(len(solutions)))


stop = time()
print("Time: " + str(stop - start))