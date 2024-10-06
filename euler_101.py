from time import time

def pol(coeffs: list[int], x: int) -> int:
    return sum([coeffs[i] * x**i for i in range(len(coeffs))])

gen_coeffs = [1,-1,1,-1,1,-1,1,-1,1,-1,1]

nodes  = [(x,pol(gen_coeffs, x)) for x in range(1, 11)]

def forward_differences(nodes):
    pass

print(nodes)

start = time()

end = time()
print("Time: " + str(end - start) + " seconds")