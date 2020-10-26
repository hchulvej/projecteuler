from time import time

def sum_of_proper_factors(n):
    return sum([d for d in range(1, n // 2 + 1) if n%d == 0])

start = time()

queue = list(range(1,10000))

amicable = set()

while queue:
    a = queue[0]
    b = sum_of_proper_factors(a)
    c = sum_of_proper_factors(b)
    if a != b and a == c:
        amicable.add(a)
    queue.remove(a)

print(sum(amicable))

stop = time()
print("Time: " + str(stop-start))