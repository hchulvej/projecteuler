from time import time

def unit_fraction(n):
    num = 10**(len(str(n)))
    while True:
        rem = num//n
        yield (num,rem)
        num = (num - rem*n)
        num *= 10

def recurring_length(n):
    uf = unit_fraction(n)
    nums = []
    while True:
        u_step = next(uf)
        if u_step[0] == 0:
            return 0
        if u_step[0] in nums:
            return len(nums)
        else:
            nums.append(u_step[0])

start = time()

max_length = 0
max_d = 0

for d in range(1,1000):
    l = recurring_length(d)
    if l > max_length:
        [max_length, max_d] = [l, d]

print("d with the longest recurring cycle: " + str(max_d) + " (length = " + str(max_length) + ")")

stop = time()
print("Time: " + str(stop-start))