from time import time

def pell():
    x1, y1 = 2, 1
    xk, yk = 2, 1
    yield (xk, yk)
    while True:
        xk, yk = x1 * xk + 3 * y1 * yk, x1 * yk + xk * y1
        yield (xk, yk)

start = time()

pg = pell()

xy = next(pg)

perims = 0

count = 0

while 2 * xy[0] + 2 < 1000000001:

    if (2 * xy[0] + 1) % 3 == 0:
        a = (2 * xy[0] + 1) // 3
        if ((a + 1) * xy[1]) % 2 == 0 and a > 1:
            perims += 3 * a + 1
            count += 1


    if (2 * xy[0] - 1) % 3 == 0:
        a = (2 * xy[0] - 1) // 3
        if ((a - 1) * xy[1]) % 2 == 0 and a > 1:
            perims += 3 * a - 1
            count += 1
            

    xy = next(pg)



print("Sum of perimeters: ", perims)


stop = time()
print("Time: " + str(stop - start))