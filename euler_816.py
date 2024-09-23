from time import time

start = time()

s = []
def number_generator():
    s_n = 290797
    while True:
        yield s_n
        s_n = (s_n * s_n) % 50515093
        

ng = number_generator()

for _ in range(50515093):
    s.append(next(ng))

def P(n:int) -> list[int]:
    return [s[2*n], s[2*n+1]]

print(len(set(s)))

## NOT DONE


end = time()
print("Time: " + str(end - start) + " seconds")