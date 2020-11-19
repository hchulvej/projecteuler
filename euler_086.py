from time import time
from math import ceil, floor, sqrt

def is_square(n):
    return int(sqrt(n))**2 == n

def number_of_int_sols(M):
    count = 0
    for z in range(3, M + 1):
        for xy in range(1, 2 * z + 1):
            if is_square(z ** 2 + xy ** 2):
                if xy <= z:
                    count += floor(xy / 2)
                else:
                    count += 1 + z - ceil(xy / 2)
    return count

start = time()

M = 1000
while number_of_int_sols(M) < 1000000:
    M += 100

print(M, number_of_int_sols(M), M - 100, number_of_int_sols(M - 100))

M = 1800
while number_of_int_sols(M) < 1000000:
    M += 10

print(M, number_of_int_sols(M), M - 10, number_of_int_sols(M - 10))

M = 1810
while number_of_int_sols(M) < 1000000:
    M += 1

print(M, number_of_int_sols(M), M - 1, number_of_int_sols(M - 1))

stop = time()
print("Time: " + str(stop - start))