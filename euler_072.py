from time import time


start = time()

totients = [n for n in range(10**6 + 1)]

for n in range(2, 10**6 + 1):
    if totients[n] == n:
        j = n
        while j < 10**6 + 1:
            totients[j] -= totients[j] // n
            j += n

print("Number of proper factors: " + str(sum(totients[2:])))

stop = time()
print("Time: " + str(stop-start))