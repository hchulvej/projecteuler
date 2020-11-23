from time import time
from itertools import product, combinations


def check(s, t):
    # 01
    one = (0 in s and 1 in t) or (1 in s and 0 in t)

    # 04
    four = (0 in s and 4 in t) or (4 in s and 0 in t)

    # 09
    nine = (0 in s and 9 in t) or (9 in s and 0 in t) or (0 in s and 6 in t) or (6 in s and 0 in t)

    # 16
    sixteen = (1 in s and 9 in t) or (9 in s and 1 in t) or (1 in s and 6 in t) or (6 in s and 1 in t)

    # 25
    twenty_five = (2 in s and 5 in t) or (5 in s and 2 in t)

    # 36
    thirty_six = (3 in s and 9 in t) or (9 in s and 3 in t) or (3 in s and 6 in t) or (6 in s and 3 in t)

    # 49 and 64
    forty_nine = (4 in s and 9 in t) or (9 in s and 4 in t) or (4 in s and 6 in t) or (6 in s and 4 in t)

    # 81
    eighty_one = (8 in s and 1 in t) or (1 in s and 8 in t)

    return one and four and nine and sixteen and twenty_five and thirty_six and forty_nine and eighty_one

start = time()

dice = combinations([d for d in range(10)], 6)

valid = 0

for c in product(dice, repeat=2):
    if check(c[0], c[1]):
        valid += 1

print("Number of combinations: ", valid // 2)

stop = time()

print("Time: ", stop - start)