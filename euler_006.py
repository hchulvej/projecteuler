from time import time

start = time()

n = 100
print("Difference: " + str(int(((n*(n+1))/2)**2-(n*(n+1)*(2*n+1))/6)))

stop = time()
print("Time: " + str(stop-start))