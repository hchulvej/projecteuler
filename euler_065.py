from time import time


def a(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if (n - 2)%3 == 0:
        return (2 * n + 2) // 3
    else:
        return 1


start = time()

a_list = [a(n) for n in range(100)]

p_list = [a_list[0], a_list[1]*a_list[0] + 1]
for n in range(2,100):
    p_list.append(a_list[n] * p_list[n - 1] + p_list[n - 2])

num = p_list[-1]
s = sum([int(d) for d in str(num)])

print("Sum of the digits of the numerator: " + str(s))

stop = time()
print("Time: " + str(stop-start))