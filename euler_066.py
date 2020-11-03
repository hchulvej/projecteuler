from time import time
from math import sqrt


def CF_sqrt(n):
    if sqrt(n) == int(sqrt(n)):
        return ([int(sqrt(n))], 0)
    a = [int(sqrt(n))]
    b = [0, a[0]]
    c = [0, n - a[0] ** 2]
    i = 1
    while a[-1] != 2 * a[0]:
        i += 1
        a.append(int((a[0] + b[i - 1]) / c[i - 1]))
        b.append(a[i - 1] * c[i - 1] - b[i - 1])
        c.append((n - b[i] ** 2) / c[i - 1])
    return (a, len(a) - 1)

def a(cf, m):
    if cf[1] == 0:
        return 0
    r = cf[1]
    p = cf[0]
    if m == 0:
        return p[0]
    return p[(m - 1)%r + 1]

def p_list(a_list):
    ps = [a_list[0], a_list[1] * a_list[0] + 1]
    for n in range(2, len(a_list)):
        ps.append(a_list[n] * ps[n - 1] + ps[n - 2])
    return ps

def q_list(a_list):
    qs = [1, a_list[1]]
    for n in range(2, len(a_list)):
        qs.append(a_list[n] * qs[n - 1] + qs[n - 2])
    return qs


start = time()

maximal_x = 9
D_val = 5

for D in range(8,1001):
    if int(sqrt(D))**2 == D:
        continue
    else:
        cf = CF_sqrt(D)
        r = cf[1] - 1
        a_list = [a(cf, m) for m in range(2 * r + 2)]
        p = p_list(a_list)
        q = q_list(a_list)

    if r%2 == 0:
        sol = (p[2 * r + 1], q[2 * r + 1])
    else:
        sol = (p[r], q[r])

    if sol[0] > maximal_x:
        maximal_x = sol[0]
        D_val = D





print("D: " + str(D_val))

stop = time()
print("Time: " + str(stop - start))