from time import time
from gmpy2 import is_prime

partitions = dict()
partitions[1] = [[1]]

def get_partitions(n):
    try:
        return partitions[n]
    except KeyError:
        pass
    partitions[n] = []
    for p in range(1, n + 1):
        for part in get_partitions(n - p):
            partitions[n].append(part + [p])

start = time()

print(get_partitions(13))

end = time()
print("Time: " + str(end - start) + " seconds")