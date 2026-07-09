from time import time
import numpy as np
from sympy import *

x = symbols('x')
n_pols = [1]
for i in range(1,11):
    n_pols.append(n_pols[i-1] * (x - i))

def pol(coeffs: list[int], x: int) -> int:
    return sum([coeffs[i] * x**i for i in range(len(coeffs))])


gen_coeffs = [1,-1,1,-1,1,-1,1,-1,1,-1,1]
#gen_coeffs = [0,0,0,1,0,0,0,0,0,0,0]

xvals = list(range(1, 11))
yvals = [pol(gen_coeffs, x) for x in xvals]

fw_diffs = {0 : yvals[0]}

def forward_differences(xvls, yvls):
    if len(xvls) == 1:
        return yvls[0]
    else:
        return (forward_differences(xvls[1:], yvls[1:]) - forward_differences(xvls[:-1], yvls[:-1])) / (xvls[-1] - xvls[0])

for j in range(1, len(xvals) + 1):
    fw_diffs[j] = int(forward_differences(xvals[:j], yvals[:j]))

print(fw_diffs)

start = time()
print("Sum of BOPs: " + str(sum([bad_OP(i) for i in range(1,11)])))
end = time()
print("Time: " + str(end - start) + " seconds")