from time import time
from libnum import invmod

start = time()

M = 1504170715041707
N = 4503599627370517

eulercoins = [(1,1504170715041707)]
smallest_eulercoin = 1504170715041707

n = 1

# We find the first few Eulercoins by brute force
while len(eulercoins) < 16:
    n += 1
    e = (M * n) % N
    if e < smallest_eulercoin:
        eulercoins.append((n,e))
        smallest_eulercoin = e


# Eulercoin no. 16 is 15806432 corresponding to n = 42298633
# If Mn mod N is another Eulercoin, then Mn mod N < 15806432
# and n > 42298633.
# If Mn = k mod N, then n = (M^-1)k mod N.


invM = invmod(M, N)
candidates = {(invM * k) % N : k for k in range(1, 15806432)}

# løb over n'erne i voksende rækkefølge (næste ...)
for n in sorted(candidates.keys()):
    if candidates[n] < eulercoins[-1][1] and n > eulercoins[-1][0]:
        eulercoins.append((n, candidates[n]))
        # print(str(eulercoins[-2]) + " -> " + str(eulercoins[-1]))

#for i,e in enumerate(eulercoins):
#    print(str(i) + ": " + str(e))

end = time()
print("Sum of all Eulercoins: " + str(sum([e[1] for e in eulercoins])))
print("Time: " + str(end - start) + " seconds")