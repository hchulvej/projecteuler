from time import time
from math import sqrt

limitx = 1000
searching = True

start = time()

squares =set([n ** 2 for n in range(1, limitx)])
hits = []

for a in range(1, limitx):
    if a % 2 == 0:
        for b in range(2, a, 2):
            x = (a ** 2 + b ** 2) // 2
            y = a ** 2 - x
            for c in range(int(sqrt(x)), a):
                z = c ** 2 - x
                if x + y in squares and x - y in squares:
                    if x + z in squares and x - z in squares:
                        if y + z in squares and y - z in squares:
                            hits.append((x, y, z))
    else:
        for b in range(1, a, 2):
            x = (a ** 2 + b ** 2) // 2
            y = a ** 2 - x
            for c in range(int(sqrt(x)), a):
                z = c ** 2 - x
                if x + y in squares and x - y in squares:
                    if x + z in squares and x - z in squares:
                        if y + z in squares and y - z in squares:
                            hits.append((x, y, z))



print(hits, sum(hits[0]))



stop = time()
print("Time: " + str(stop - start))