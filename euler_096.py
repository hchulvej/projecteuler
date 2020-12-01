from time import time
import numpy as np

def possible(grid, val, r, c):

    # Grid cell must be empty
    if grid[r, c] != 0:
        return False

    # Row or column cannot contain val already
    if np.count_nonzero(grid[r, :] == val) + np.count_nonzero(grid[:, c] == val) > 0:
        return False

    # Same 3x3 grid cannot contain val already
    if np.count_nonzero(grid[3 * (r // 3) : 3 * (r // 3) + 3, 3 * (c // 3) : 3 * (c // 3) + 3] == val) > 0:
        return False

    return True

def possibles(grid, r, c):
    return [val for val in range(1, 10) if possible(grid, val, r, c)]

def solve(n):

    global grids

    rows, cols = np.where(grids[n] == 0)

    for r in rows:
        for c in cols:
            for val in possibles(grids[n], r, c):
                grids[n][r, c] = val
                if solve(n):
                    return True
                grids[n][r, c] = 0
            return

    return True



start = time()

# Importing grids from file
# ---------------------------------------
with open("p096_sudoku.txt", "r") as f:
    raw = f.readlines()
    raw_stripped = []
    for i in range(len(raw)):
        if i % 10 > 0:
            raw_stripped.append(raw[i].replace("\n", ""))
    grids = []
    for gn in range(50):
        grid = []
        for i in range(9):
            grid.append([int(n) for n in raw_stripped[9 * gn + i]])
        grids.append(np.array(grid))
# ---------------------------------------

# Filling out the easy cells (1 possibility)
for i in range(3):
    for n in range(len(grids)):
        grid = grids[n]
        for r in range(9):
            for c in range(9):
                p_list = possibles(grid, r, c)
                if len(p_list) == 1:
                    grid[r, c] = p_list[0]

total = 0

for n in range(len(grids)):
    solve(n)
    total += grids[n][0, 0] * 100 + grids[n][0, 1] * 10 + grids[n][0, 2]

print("Sum of corners: ", total)

stop = time()
print("Time: " + str(stop - start))