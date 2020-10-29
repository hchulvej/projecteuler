from time import time

def sqrt2(n):
    if n == 0:
        return 1
    else:
        return 2


start = time()

A = [1, sqrt2(0)]

B = [0, 1]

for k in range(2,1002):
    A.append(sqrt2(k) * A[k - 1] + A[k - 2])
    B.append(sqrt2(k) * B[k - 1] + B[k - 2])

special = 0

for k in range(2,1002):
    if len(str(A[k])) > len(str(B[k])):
        special += 1

print("Number of fractions: " + str(special))

stop = time()
print("Time: " + str(stop-start))