from time import time

def sum_of_5th_powers(n):
    return sum([int(d)**5 for d in str(n)])

start = time()

hits = [n for n in range(2,10**6) if sum_of_5th_powers(n) == n]
print("Sum of all the numbers: " + str(sum(hits)))

stop = time()
print("Time: " + str(stop-start))