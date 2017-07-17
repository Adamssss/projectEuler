import time

t1 = time.time()

count = 0
for i in range(0,1000):
    if (i%3 == 0) or (i%5 == 0):
        count += i

print (count)

print("time:",time.time()-t1)
