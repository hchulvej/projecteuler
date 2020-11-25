from time import time

start = time()

squares = {n:n * n for n in range(600)}

sd = {n:0 for n in range(10 ** 7)}
for n in range(10):
    sd[n] = squares[n]

n = 10

while n < 10 ** 7:
    sd[n] = squares[n % 10] + sd[n // 10]
    n += 1

eighty_niners = 0

for m in range(2, 10 ** 7):
    next_num = sd[m]
    while not next_num in [1, 89]:
        next_num = sd[next_num]
    if next_num == 89:
        eighty_niners += 1
        continue

print("Number of chains ending in 89: ", eighty_niners)

stop = time()
print("Time: " + str(stop - start))