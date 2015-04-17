import time

t1 = time.time()


N = 2000000

n = (N+1)//2

p = [True]*(n)

i = 1
total = 2

while i < n:
    if p[i]:
        t = 2*i+1
        total += t
        j = i
        while j < n:
            p[j] = False
            j += t
    i += 1

print (total)

print("time:",time.time()-t1)
                
