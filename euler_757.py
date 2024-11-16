from time import time


# Some math:
#
# Assume ab = cd = N, and a+b = c+d+1
#
# Let x = c - a and y = d - a
#
# Then:
# (1) x + y = c + d - 2a = a + b - 1 - 2a = b - a - 1
# (2) x * y = (c - a) * (d - a) = c*d - a(c + d) + a^2 = a*b - a(a + b - 1) + a^2 = a
# (3) x*(y + 1) = x*y + x = a + c - a = c
# (4) (x + 1)*y = x*y + y = a + d - a = d
# (5) (x + 1)*(y + 1) = x*y + x + y + 1 = a + b - a - 1 + 1 = b
#
# Therefore:
# N = a*b = c*d = x*(x + 1)*y*(y + 1)
#
#
# If y >= x >= L^(1/4), then N > L


start = time()

limit_on_N = 10**14
limit_on_x = int(limit_on_N ** (1/4)) + 1

products_x = [x * (x + 1) for x in range(1, limit_on_x)]
products_xy = set()

for p in products_x:
    limit_y = int(p ** (1/2))
    for y in range(limit_y, limit_on_N):
        if p * y * (y + 1) <= limit_on_N:
            products_xy.add(p * y * (y + 1))
        else:
            break

res = len(products_xy)


end = time()
print("Number of stealthy numbers: " + str(res))
print("Time: " + str(end - start) + " seconds")