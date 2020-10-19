from time import time

def sum_ring(n):
    return 4*n**2-6*(n-1)

def diagonal_sum(n):
    if n == 1:
        return 1
    else:
        return sum_ring(n) + diagonal_sum(n-2)

start = time()

print(diagonal_sum(1001))

stop = time()
print("Time: " + str(stop-start))