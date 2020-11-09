from time import time
from primePy import primes

start = time()

p_list = primes.upto(100)

limit = 100

ways = [1] + [0] * limit

for p in p_list:
    for j in range(p, limit + 1):
        ways[j] += ways[j - p]

print("Number: " + str(min([n for n in range(len(ways)) if ways[n] > 5000])))


stop = time()
print("Time: " + str(stop - start))