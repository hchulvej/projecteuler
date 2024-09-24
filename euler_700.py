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
# If Mn mod N is another Eulercoin, then Mn mod N < 15806432
# and n > 42298633.
# If Mn = k mod N, then n = (M^-1)k mod N.
# We check k < 15806432 and note each corresponding n

invM = invmod(M, N)
candidates = {(invM * k) % N : k for k in range(1, 15806432)}

# løb over n'erne i voksende rækkefølge (næste ...)
for k in range(15806431,1,-1):
    if k < eulercoins[-1][0] and candidates[k] > eulercoins[-1][1]:
        eulercoins.append((k, candidates[k]))
        print(str(eulercoins[-2]) + " -> " + str(eulercoins[-1]))


end = time()
print("Time: " + str(end - start) + " seconds")