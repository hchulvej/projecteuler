from time import time

def det(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

start = time()

with open("p102_triangles.txt", "r") as f:
    raw = f.readlines()
    lines = []
    for r in raw:
        lines.append(list(map(int, r.replace("\n", "").split(","))))

inside = 0

for l in lines:

    [x1, y1, x2, y2, x3, y3] = l

    a = (det(0, 0, x3 - x1, y3 - y1) - det(x1, y1, x3 - x1, y3 - y1)) / det(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    b = (det(x1, y1, x2 - x1, y2 - y1) - det(0, 0, x2 - x1, y2 - y1)) / det(x2 - x1, y2 - y1, x3 - x1, y3 - y1)

    if a > 0.0 and b > 0.0 and a + b < 1.0:
        inside += 1


print("Number of triangles: ", inside)

stop = time()
print("Time: " + str(stop - start))