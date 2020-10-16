from time import time

start = time()

sd = sum([int(d) for d in str(2**1000)])
print("Sum of digits: " + str(sd))

stop = time()
print("Time: " + str(stop-start))