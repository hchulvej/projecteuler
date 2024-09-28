from time import time

start = time()

fib = [0, 1]
i = 2
n = 1

while len(fib) < 125:
    fib.append(n)
    i += 1
    n = fib[i - 1] + fib[i - 2]
    


sum = 0

for n in range(2, 10 ** 9):
    if fib[120] % n == 0 and fib[121] % n == 1:
        sum += n

end = time()
print("Sum: " + str(sum))
print("Time: " + str(end - start) + " seconds")