import sympy as sp

pascal_triangle = [[1], [1, 1]]

def generate_pascal_triangle(n):
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        row.append(1)
        pascal_triangle.append(row)
    return pascal_triangle[:n]

# We create the unique set of coefficients from the first 51 rows of Pascal's triangle
coefficients = set()
for row in generate_pascal_triangle(51):
    coefficients.update(row)

coefficients = sorted(list(coefficients))

# We find the upper limit for prime generation based on the largest coefficient
upper_limit = int(sp.sqrt(coefficients[-1])) + 1
our_primes = list(sp.primerange(1, upper_limit))

# We find out which coefficients that don't have (prime factor)^2
def check_square_free(n):
    for prime in our_primes:
        if prime * prime > n:
            break
        if n % (prime * prime) == 0:
            return False
    return True

square_free_coefficients = [n for n in coefficients if check_square_free(n)]
print("Sum of square free numbers:", sum(square_free_coefficients))
