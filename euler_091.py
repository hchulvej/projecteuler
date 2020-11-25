from time import time
import numpy as np

start = time()

cuboid = np.full([51, 51, 51, 51], 0)

for a in range(1, 51):
    for b in range(1, 51):
        for c in range(a + 1, 51):
            for d in range(b):
                if a * (c - a) + b * (d - b) == 0:
                    cuboid[a, b, c, d] = 1
        for c in range(a):
            for d in range(b + 1, 51):
                if a * (c - a) + b * (d - b) == 0:
                    cuboid[a, b, c, d] = 1

print("Number of rectangles: ", cuboid.sum() + 7500)

stop = time()
print("Time: " + str(stop-start))