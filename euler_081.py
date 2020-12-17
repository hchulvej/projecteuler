from time import time
import numpy as np

matrix = np.empty([80, 80], int)

memo = {}

def minimal_cost(c):
    global memo
    m, n = c[0], c[1]

    # Base cases
    if (m, n) in memo:
        return memo[(m, n)]
    if (m, n) == (79, 79):
        return matrix[79, 79]

    # Down the tree
    if m == 79:
        memo[(m, n)] = matrix[m, n] + minimal_cost((m, n + 1))
    if n == 79:
        memo[(m, n)] = matrix[m, n] + minimal_cost((m + 1, n))
    if max(n, m) < 79:
        memo[(m, n)] = matrix[m, n] + min(minimal_cost((m + 1, n)), minimal_cost((m, n + 1)))

    return memo[(m, n)]



start = time()

with open("p081_matrix.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = list(map(int, lines[i].replace("\n", "").split(",")))
        for j in range(len(line)):
            matrix[i, j] = line[j]


print(minimal_cost((0, 0)))

stop = time()
print("Time: " + str(stop - start))