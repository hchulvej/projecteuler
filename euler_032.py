from time import time

def is_pandigital(n1,n2,n3):
    return "".join(sorted(str(n1) + str(n2) + str(n3))) == "123456789"

start = time()

pandigitals = set()

for i in range(1,10000):
    j = i + 1
    while len(str(i) + str(j) + str(i * j)) < 10:
        if is_pandigital(i, j, i*j):
            pandigitals.add(i*j)
        j += 1

print("Sum of pandigital products: " + str(sum(pandigitals)))

stop = time()
print("Time: " + str(stop-start))