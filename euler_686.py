from time import time

def check():
    j = 12710
    n = 45
    num = int(str(2 ** j)[:15])
    while True:
        if str(num)[:3] == "123":
            yield (n, j)
            n += 1
        j += 1
        num = int(str(2 * num)[:15])

start = time()

checker = check()

while True:
    c = next(checker)

    if c[0] == 678910:
        print("L(123, 678910) = ", c[0])
        break

stop = time()
print("Time: " + str(stop - start))