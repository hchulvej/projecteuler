from time import time


start = time()

print("Last ten digits: ", (28433 * pow(2, 7830457, 10 ** 10) + 1) % (10 ** 10))

stop = time()

print("Time: ", stop - start)