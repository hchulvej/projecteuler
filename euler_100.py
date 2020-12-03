from time import time

start = time()

xn, yn = 3, 4

while yn < 10 ** 12:
    xn, yn = 3 * xn + 2 * yn - 2, 4 * xn + 3 * yn - 3


print("Number of blue discs: ", xn)

stop = time()
print("Time: " + str(stop - start))