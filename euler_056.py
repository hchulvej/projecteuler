from time import time
from itertools import product

def dig_sum(n):
    s = str(n).replace("0", "")
    return sum([int(d) for d in s])

start = time()

max_dig_sum = 0

for xy in product(range(1,100), repeat=2):
    ds = dig_sum(xy[0]**xy[1])
    if ds > max_dig_sum:
        max_dig_sum = ds

print("Maximum digital sum: " + str(max_dig_sum))

stop = time()
print("Time: " + str(stop-start))