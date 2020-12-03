from time import time

def check_number(n):

    s = str(n)

    if len(s) != 19:
        return False

    for i in range(1, 10):
        if int(s[2 * i - 2]) != i:
            return False

    return int(s[-1]) == 0

start = time()

n = 1058921220
while n < 1389026624:
    if check_number(n * n):
        print("Number is: ", n)
        break
    n += 10


stop = time()

print("Time: ", stop - start)