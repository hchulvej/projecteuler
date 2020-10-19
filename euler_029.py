from time import time
from itertools import product

start = time()

powers = set()
for ab in product(range(2,101),repeat=2):
    powers.add(ab[0]**ab[1])

print("Number of distinct powers: " + str(len(powers)))

stop = time()
print("Time: " + str(stop-start))