from time import time

start = time()

s = str(sum(set(n**n for n in range(1,1001))))

print("Last 10 digits: " + s[-10:])

stop = time()
print("Time: " + str(stop-start))