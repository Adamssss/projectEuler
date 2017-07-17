import time

t1 = time.time()

N = 100

w = [0]*(N+1)
w[0] = 1

for i in range(1,N+1):
    # i stands for the numbers used form 1 to i
    for j in range(i,N+1):
        # w[j] is the ways make out of 1 to i-1
        # when i is added to the numbers
        # j equals i and j-i
        # so w[j-i] is added to w[j]
        w[j] += w[j-i]

def f(i):
    return w[i]-1

print(f(N))
    

print("time:",time.time()-t1)
