from time import time
from gmpy2 import next_prime
from itertools import permutations

def prime_generator():
    p = 2
    while True:
        yield p
        p = next_prime(p)


partitions = dict()
partitions[1] = [[1]]

def get_partitions(n):
    try:
        return partitions[n]
    except KeyError:
        pass
    partitions[n] = []
    x = [0] * (n + 1)
    for i in range(1, n + 1):
        x[i] = 1
    partitions[n].append(x[1:])
    x[0] = -1
    x[1] = 2
    h = 1
    m = n - 1
    partitions[n].append(x[1:(m + 1)])
    while x[1] != n:
        if m - h > 1:
            h += 1
            x[h] = 2
            m -= 1
        else:
            j = m - 2
            while x[j] == x[m - 1]:
                x[j] = 1
                j -= 1
            h = j + 1
            x[h] = x[m - 1] + 1
            r = x[m] + x[m - 1] * (m - h - 1)
            x[m] = 1
            m = h + r - 1
        partitions[n].append(x[1:(m + 1)])
    return partitions[n]

def partition_to_number(partition):
    digits = list(map(str, partition))
    numbers = []
    for c in permutations(digits, len(digits)):
        numbers.append(int("".join(c)))
    return list(set(numbers))

start = time()

n = 10
pg = prime_generator()
numbers = set()

primes = []
p = next(pg)
while p < 37:
    primes.append(p)
    p = next(pg)

print("Number of primes: " + str(len(primes)))

for p in primes:
    partitions_p = get_partitions(p)
    for partition in partitions_p:
        numbers.update(partition_to_number(partition))
    print("numbers added for p = " + str(p))

numbers = sorted(list(numbers))
print("Number of partitions: " + str(len(numbers)))

end = time()
print("Time: " + str(end - start) + " seconds")