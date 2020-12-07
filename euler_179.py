from time import time


start = time()

divisors = {n : 2 for n in range(2, 10 ** 7)}

for d in range(2, 5 * 10 ** 6):
    k = 2 * d
    while k < 10 ** 7:
        divisors[k] += 1
        k += d

number = 0

for i in range(2, 10 ** 7 - 1):
    if divisors[i] == divisors[i + 1]:
        number += 1


print("Number of integers:", number)

stop = time()
print("Time: " + str(stop - start))