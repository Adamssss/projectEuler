import math
import time

t1 = time.time()

# n dig number is a to the nth
# a must be less than 10
# a will be 1-9
# there is a maxium n for each a as a to the nth is fewer dig than n
# since a is less than 10 no more n should exist

possibility = []
for i in range(1,10):
    for j in range(1,100):
        n = math.pow(i,j)
        dig = math.floor(math.log10(n)+1)
        if dig == j:
            possibility.append([i,j])
        elif dig+1 < j:
            break

print(len(possibility))

print("time:",time.time()-t1)
