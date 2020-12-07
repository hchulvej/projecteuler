from time import time

def remainder(a, n):
    if n % 2 == 0:
        return 2
    return (2 * n * a) % (a * a)

def max_remainder(a):
    lim = a * a - 1
    max_r = 2
    for n in range(1, lim + 1, 2):
        r = remainder(a, n)
        if r == lim:
            return r
        if r > max_r:
            max_r = r
    return max_r

start = time()

sum_of_remainders = 0

for a in range(3, 1001):
    sum_of_remainders += max_remainder(a)


print("Sum of remainders: ", + sum_of_remainders)

stop = time()
print("Time: " + str(stop - start))