from time import time

start = time()

mult_3_and_5 = set([n for n in range(1000) if n%3 == 0 or n%5 == 0])

print("Sum is " + str(sum(mult_3_and_5)))

stop = time()

print("Time: " + str(stop-start) + " secs")