import time

t1 = time.time()

N = 60000

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
        # %1000000
        if w[j] >= 1000000:
            w[j] -= 1000000
            
    if w[i] == 0:
        print(i)
        break 
    

print("time:",time.time()-t1)
# time:1240.589958190918
