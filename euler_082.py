from time import time
import numpy as np

matrix = np.empty([80, 80], int)

start = time()

with open("p082_matrix.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = list(map(int, lines[i].replace("\n", "").split(",")))
        for j in range(len(line)):
            matrix[i, j] = line[j]

minimal = 300000

#If the optimal route ends in (i0, 79)
for i0 in range(80):
    path_sums = np.empty([80, 80], int)

    #Last column is initialised
    path_sums[i0, 79] = matrix[i0, 79]

    for i in range(1, i0 + 1):
        path_sums[i0 - i, 79] = matrix[i0 - i, 79] + path_sums[i0 - i + 1, 79]

    for i in range(i0 + 1, 80):
        path_sums[i, 79] = matrix[i, 79] + path_sums[i - 1, 79]

    #The penultimate row is populated
    path_sums[i0, 78] = matrix[i0, 78] + path_sums[i0, 79]

    for i in [k for k in range(80) if k != i0]:
        if i < i0:
            path_sums[i, 78] = matrix[i, 78] + min(path_sums[i, 79], path_sums[i + 1, 78])
        if i > i0:
            path_sums[i, 78] = matrix[i, 78] + min(path_sums[i - 1, 78], path_sums[i, 79])


    #The rest of the rows are populated
    for j in reversed(range(78)):
        for i in range(80):
            #go right
            optimal = matrix[i, j] + path_sums[i, j + 1]
            #go up
            if i > 0:
                k = 1
                while i - k > -1:
                    test = sum([matrix[i - d, j] for d in range(k + 1)]) + path_sums[i - k, j + 1]
                    if test < optimal:
                        optimal = test
                    k += 1
            #go down
            if i < 79:
                k = 1
                while i + k < 80:
                    test = sum([matrix[i + d, j] for d in range(k + 1)]) + path_sums[i + k, j + 1]
                    if test < optimal:
                        optimal = test
                    k += 1

            path_sums[i, j] = optimal

    minimal = min(minimal, min(path_sums[:, 0]))


print("Minimal path sum: " + str(minimal))

stop = time()
print("Time: " + str(stop - start))