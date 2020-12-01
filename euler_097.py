from time import time

start = time()

N = 10 ** 10

npm = 1
for i in range(7830457):
    npm = (2 * npm) % N

npm = (28433 * npm + 1) % N

print("The last 10 digits are: ", npm)

stop = time()
print("Time: " + str(stop - start))