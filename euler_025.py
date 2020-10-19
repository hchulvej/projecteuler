from time import time

def fib_gen():
    yield 1
    yield 1
    [n_1, n] = [1, 2]
    while True:
        yield n
        [n_1, n] = [n, n_1 + n]

start = time()

fg = fib_gen()
n = 0

while True:
    fib = next(fg)
    n += 1
    if len(str(fib)) > 999:
        print("First index with at least 1000 digits is: " + str(n))
        break

stop = time()
print("Time: " + str(stop-start))