from time import time
from libnum import invmod

start = time()

M = 1504170715041707
N = 4503599627370517

eulercoins = [(1504170715041707, 1)]
smallest_eulercoin = 1504170715041707

n = 1

# We find the first few Eulercoins by brute force
while len(eulercoins) < 16:
    n += 1
    e = (M * n) % N
    if e < smallest_eulercoin:
        eulercoins.append((e,n))
        smallest_eulercoin = e

print(eulercoins[-1])
# Eulercoin no. 16 is 15806432 corresponding to n = 42298633

## NOT DONE - TOO INEFFICIENT

end = time()
print("Time: " + str(end - start) + " seconds")