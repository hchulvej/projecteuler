from time import time
import numpy as np

start = time()

partitions = np.empty([101, 101], int)
partitions.fill(0)

for n in range(101):
    partitions[n, 0] = 1

for n in range(1,101):
    partitions[n, 1] = 1

for n in range(2, 101):
    for k in range(2, n + 1):
        partitions[n, k] = partitions[n - 1, k - 1] + partitions[n - k, k]


print(sum([partitions[100, k] for k in range(1,101)]))


stop = time()
print("Time: " + str(stop - start))