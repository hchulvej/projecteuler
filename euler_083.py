from time import time
import numpy as np


matrix = np.empty([80, 80], int)
distance = np.full([80, 80], np.Inf)

def get_distance(i, j):
    if i < 0 or i > 79 or j < 0 or j > 79:
        return np.Inf
    else:
        return distance[i, j]

start = time()

with open("p083_matrix.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = list(map(int, lines[i].replace("\n", "").split(",")))
        for j in range(len(line)):
            matrix[i, j] = line[j]


#Bellman-Ford algorithm
#The source is (0,0)
distance[0, 0] = matrix[0, 0]

for iterations in range(6399):
    for i in range(80):
        for j in range(80):
            min_dist = min([get_distance(i + 1, j), get_distance(i - 1, j), get_distance(i, j + 1), get_distance(i, j - 1)])
            distance[i, j] = min([min_dist + matrix[i, j], distance[i, j]])


print("Minimal path sum ", distance[79, 79])

stop = time()
print("Time: " + str(stop - start))