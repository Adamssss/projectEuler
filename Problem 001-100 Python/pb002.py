import time

t1 = time.time()

fib = [1,2]
total = 2
while fib[-1] < 4000000:
    newfib = fib[-1]+fib[-2]
    fib.append(newfib)
    if newfib%2 == 0:
        total += newfib

print (total)

print("time:",time.time()-t1)
