from time import time

def reduction(row1,row2):
    #row2 has n element and row1 has n-1 elements
    #output row3 has n-1 elements
    row3 = []
    for i in range(len(row1)):
        row3.append(max(row1[i]+row2[i],row1[i]+row2[i+1]))
    return row3

start = time()

with open("p067_triangle.txt", "r") as f:
    raw = f.readlines()

triangle = []
for l in raw:
    l = l.replace("\n", "")
    triangle.append(list(map(int,l.split(" "))))

while len(triangle) > 1:
    new_last_row = reduction(triangle[len(triangle)-2],triangle[len(triangle)-1])
    triangle.remove(triangle[-1])
    triangle.remove(triangle[-1])
    triangle.append(new_last_row)

print("Max path sum: " + str(triangle[0][0]))

stop = time()
print("Time: " + str(stop - start))