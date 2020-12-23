from time import time

def A(n):
    if n % 5 == 0:
        return 0
    k = 1
    rem = 1
    while rem != 0:
        rem = (10 * rem + 1) % n
        k += 1
    return k



start = time()

n = 10 ** 6 + 1
while A(n) <= 10 ** 6:
    n += 2

print("Least value of n:", n)

stop = time()
print("Time: " + str(stop - start))