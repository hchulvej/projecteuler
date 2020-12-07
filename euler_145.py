from time import time

def reverse(n):
    return int(str(n)[::-1])

def odd_digits(n):
    s = str(n)
    for d in "02468":
        if d in s:
            return 0
    return 1


start = time()

revs = {n : odd_digits(n + reverse(n)) for n in range(1, 10 ** 9, 2) if n % 10 > 0}

print("Number of reversible numbers: ", 2 * sum(revs.values()))


stop = time()
print("Time: " + str(stop - start))