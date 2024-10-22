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

x_vals = np.array(range(1,12))
y_vals = np.array([pol(gen_coeffs, x) for x in range(1,12)])


def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(order):
    coefs = divided_diff(x_vals, y_vals)[0, :]
    p = coefs[0]
    for i in range(1, order):
        p += coefs[i] * n_pols[i]
        
    return simplify(p)

def bad_OP(order):
    p = newton_poly(order)
    seq = [int(p.subs(x, x_vals[i])) for i in range(len(x_vals))]
    return seq[min([i for i in range(len(x_vals)) if seq[i] != y_vals[i]])]


start = time()
print("Sum of BOPs: " + str(sum([bad_OP(i) for i in range(1,11)])))
end = time()
print("Time: " + str(end - start) + " seconds")