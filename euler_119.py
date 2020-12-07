from time import time
from itertools import count

def sum_dig(n):
    return sum([int(c) for c in str(n)])

def is_integer(f):
    return float.is_integer(f)

start = time()


dig_power_sums = set()


for n in count(2):

    # n = number of digits

    digit_sums = [k for k in range(2, 9 * n)]

    for sd in digit_sums:

        m = 1
        while sd ** m < 10 ** 20:
            t = sd ** m
            if sum_dig(t) == sd and t > 9:
                dig_power_sums.add(t)
            m += 1

    if len(dig_power_sums) > 29:
        break


print("a_30 is", sorted(dig_power_sums)[29])

stop = time()
print("Time: " + str(stop - start))