import math
import time

t1 = time.time()

# math problem!
# a/b is close to but a little bit less than 3/7
# a/b <= 3/7
# a <= 3*b/7
# a = ceiling(3b/7)-1

mimd = 1
for b in range(1,1000001):
    a = math.ceil(3*b/7)-1
    difference = 3/7-a/b
    if difference < mimd:
        mimd = difference
        ta = a

print(ta)
              
print("time:",time.time()-t1)
                
