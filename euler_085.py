from time import time

def number_of_rectangles(n, m):
    return (n * (n + 1) * m  * (m + 1)) // 4

def boundaries(n):
    m = 1
    while number_of_rectangles(n, m) < 2000000:
        m += 1
    return [m - 1, m]

start = time()

optimal_area = 0
e = 2000000

for n in range(1, 2000):
    b = boundaries(n)
    if min(b) <= n:

        low = number_of_rectangles(n, b[0])

        high = number_of_rectangles(n, b[1])

        if abs(low - 2000000) < e:
            e = abs(low - 2000000)
            optimal_area = n * b[0]

        if abs(high - 2000000) < e:
            e = abs(high - 2000000)
            optimal_area = n * b[1]


print("Optimal area: ", optimal_area)






stop = time()
print("Time: " + str(stop - start))